import re
from typing import Any, Dict, List, Tuple


# Matches any Java IO/NIO stream or reader/writer variable declaration.
# Covers standard library types ending in InputStream, OutputStream, Reader, Writer.
_RESOURCE_VAR_RE = re.compile(
    r"\b([A-Za-z][A-Za-z0-9]*(?:InputStream|OutputStream|Reader|Writer))"
    r"\s+([A-Za-z_][A-Za-z0-9_]*)\s*="
)


class JavaMutator:
    def __init__(self, profile: Dict[str, Any]) -> None:
        self.profile = profile

    def _find_resource_vars(self, code: str) -> List[Tuple[str, str]]:
        """Return [(class_name, var_name), ...] for all resource-like variable declarations."""
        seen: set = set()
        results = []
        for m in _RESOURCE_VAR_RE.finditer(code):
            key = (m.group(1), m.group(2))
            if key not in seen:
                seen.add(key)
                results.append(key)
        return results

    def generate_mutations(
        self,
        code: str,
        budget: int = 2,
        operator_offset: int = 0,
    ) -> List[Dict[str, Any]]:
        operators = list(self.profile.get("priority_operators", []))
        if operators:
            normalized_offset = operator_offset % len(operators)
            operators = operators[normalized_offset:] + operators[:normalized_offset]
        candidates_by_operator = []
        for operator in operators:
            handler = getattr(self, operator, None)
            if handler is None:
                continue
            operator_candidates = []
            for mutated_code in handler(code):
                cleaned = mutated_code.strip()
                if cleaned and cleaned != code.strip():
                    operator_candidates.append(
                        {
                            "code": cleaned,
                            "operator": operator,
                            "profile": self.profile.get("mutation_profile", "generic_java"),
                        }
                    )
            if operator_candidates:
                candidates_by_operator.append(operator_candidates)

        unique = []
        seen = set()
        round_index = 0
        while len(unique) < max(budget, 0):
            progress = False
            for operator_candidates in candidates_by_operator:
                if round_index >= len(operator_candidates):
                    continue
                candidate = operator_candidates[round_index]
                marker = candidate["code"]
                progress = True
                if marker in seen:
                    continue
                seen.add(marker)
                unique.append(candidate)
                if len(unique) >= max(budget, 0):
                    break
            if not progress:
                break
            round_index += 1
        return unique

    def _rewrite_first(self, pattern: str, replacement_fn, code: str) -> List[str]:
        compiled = re.compile(pattern)
        mutated = []
        replacements = replacement_fn() if callable(replacement_fn) else replacement_fn
        for replacement in replacements:
            replaced, count = compiled.subn(replacement, code, count=1)
            if count:
                mutated.append(replaced)
        return mutated

    def _replace_first_string_literal(
        self, code: str, replacements: List[str]
    ) -> List[str]:
        pattern = re.compile(r'"(?:\\.|[^"\\])*"')
        mutated = []
        for replacement in replacements:
            replaced, count = pattern.subn(replacement, code, count=1)
            if count:
                mutated.append(replaced)
        return mutated

    def _replace_first_numeric_literal(
        self, code: str, replacements: List[str]
    ) -> List[str]:
        pattern = re.compile(r"\b\d+(?:L)?\b")
        mutated = []
        for replacement in replacements:
            replaced, count = pattern.subn(replacement, code, count=1)
            if count:
                mutated.append(replaced)
        return mutated

    def _insert_after_main_open(self, code: str, snippets: List[str]) -> List[str]:
        pattern = re.compile(
            r"(public\s+static\s+void\s+main\s*\(\s*String\[\]\s+\w+\s*\)\s*(?:throws\s+[^{]+)?\{\s*)"
        )
        mutated = []
        for snippet in snippets:
            replaced, count = pattern.subn(rf"\1{snippet}\n        ", code, count=1)
            if count:
                mutated.append(replaced)
        return mutated

    def _insert_after_first_match(
        self, code: str, pattern: str, snippets: List[str]
    ) -> List[str]:
        compiled = re.compile(pattern)
        mutated = []
        for snippet in snippets:
            replaced, count = compiled.subn(
                lambda m: f"{m.group(1)}\n        {snippet}",
                code,
                count=1,
            )
            if count:
                mutated.append(replaced)
        return mutated

    # RESOURCE operators
    def resource_constructor_edge(self, code: str) -> List[str]:
        """Mutate buffer-size arguments in any resource (InputStream/OutputStream/Reader/Writer) constructor."""
        mutated = []
        processed_types: set = set()
        for class_name, _ in self._find_resource_vars(code):
            if class_name in processed_types:
                continue
            processed_types.add(class_name)
            # Mutate existing size argument: new Foo(arg, size) → new Foo(arg, N)
            sized_pattern = re.compile(
                rf"new\s+{re.escape(class_name)}\((.+?),\s*(-?\d+)\)"
            )
            for size in ["1", "8", "8192", "0", "-1"]:
                replaced, count = sized_pattern.subn(
                    lambda m, rt=class_name, s=size: f"new {rt}({m.group(1)}, {s})",
                    code,
                    count=1,
                )
                if count:
                    mutated.append(replaced)
            # Inject size argument into single-arg constructor: new Foo(arg) → new Foo(arg, N)
            unsized_pattern = re.compile(rf"new\s+{re.escape(class_name)}\(([^,\n)]+)\)")
            for size in ["1", "8", "8192"]:
                replaced, count = unsized_pattern.subn(
                    lambda m, rt=class_name, s=size: f"new {rt}({m.group(1)}, {s})",
                    code,
                    count=1,
                )
                if count:
                    mutated.append(replaced)
        return mutated

    def resource_lifecycle_sequence(self, code: str) -> List[str]:
        """Insert lifecycle calls (flush/close/mark/reset/skip) after resource creation for any stream type."""
        mutated = []
        for class_name, var_name in self._find_resource_vars(code):
            is_output = "OutputStream" in class_name or "Writer" in class_name
            is_input = "InputStream" in class_name or "Reader" in class_name

            if is_output:
                insert_after_write = re.compile(
                    rf"({re.escape(var_name)}\s*\.\s*write\([^\n;]*\);\s*)"
                )
                for snippet in [
                    f"\\1\n        {var_name}.flush();",
                    f"\\1\n        {var_name}.flush();\n        {var_name}.write(255);",
                    f"\\1\n        {var_name}.close();\n        {var_name}.flush();",
                ]:
                    replaced, count = insert_after_write.subn(snippet, code, count=1)
                    if count:
                        mutated.append(replaced)

            if is_input:
                if "InputStream" in class_name:
                    snippets = [
                        f"{var_name}.mark(8);",
                        f"try {{ {var_name}.read(); {var_name}.reset(); }} catch (Exception ignored) {{ }}",
                        f"try {{ {var_name}.available(); {var_name}.skip(1L); }} catch (Exception ignored) {{ }}",
                    ]
                else:  # Reader
                    snippets = [
                        f"{var_name}.mark(16);",
                        f"try {{ {var_name}.read(); {var_name}.reset(); }} catch (Exception ignored) {{ }}",
                        f"try {{ {var_name}.skip(1L); }} catch (Exception ignored) {{ }}",
                    ]
                mutated.extend(
                    self._insert_after_first_match(
                        code,
                        rf"(\b{re.escape(class_name)}\s+{re.escape(var_name)}\s*=\s*[^\n;]+;\s*)",
                        snippets,
                    )
                )
        return mutated

    def resource_wrapper_depth(self, code: str) -> List[str]:
        """Wrap a resource constructor inside another compatible wrapper to stress nesting."""
        mutated = []
        processed_types: set = set()
        for class_name, _ in self._find_resource_vars(code):
            if class_name in processed_types:
                continue
            processed_types.add(class_name)
            pattern = re.compile(rf"new\s+{re.escape(class_name)}\(([^,\n]+)\)")
            is_output = "OutputStream" in class_name or "Writer" in class_name
            is_input = "InputStream" in class_name or "Reader" in class_name

            if is_output:
                replacements = [
                    lambda m, rt=class_name: f"new {rt}(new {rt}({m.group(1)}))",
                    lambda m: "new java.io.BufferedOutputStream(new java.io.ByteArrayOutputStream())",
                ]
            elif is_input:
                replacements = [
                    lambda m, rt=class_name: f"new {rt}(new {rt}({m.group(1)}))",
                    lambda m: "new java.io.BufferedInputStream(new java.io.ByteArrayInputStream(new byte[]{1,2,3}))",
                ]
            else:
                continue

            for replacement in replacements:
                replaced, count = pattern.subn(replacement, code, count=1)
                if count:
                    mutated.append(replaced)
        return mutated

    def resource_exception_shell(self, code: str) -> List[str]:
        if "throws IOException" in code:
            return [
                code.replace(
                    "throws IOException",
                    "",
                    1,
                )
            ]
        if "public static void main(String[] args)" in code:
            return [
                code.replace(
                    "public static void main(String[] args)",
                    "public static void main(String[] args) throws IOException",
                    1,
                )
            ]
        return []

    # BUFFER operators
    def buffer_write_single_edge(self, code: str) -> List[str]:
        pattern = re.compile(r"(\.\s*write\()\s*(-?\d+)\s*(\))")
        mutated = []
        for value in ["0", "1", "127", "128", "255", "256", "-1"]:
            replaced, count = pattern.subn(
                lambda m: f"{m.group(1)}{value}{m.group(3)}",
                code,
                count=1,
            )
            if count:
                mutated.append(replaced)
        if mutated:
            return mutated
        for pattern in [
            re.compile(r"(\.\s*skip\()\s*(-?\d+L?)\s*(\))"),
            re.compile(r"(\.\s*mark\()\s*(-?\d+)\s*(\))"),
        ]:
            for value in ["0", "1", "8", "-1"]:
                replaced, count = pattern.subn(
                    lambda m: f"{m.group(1)}{value}{m.group(3)}",
                    code,
                    count=1,
                )
                if count:
                    mutated.append(replaced)
        return mutated

    def buffer_write_bulk_edge(self, code: str) -> List[str]:
        pattern = re.compile(
            r"(\.\s*(?:write|read)\(\s*[^,\n]+,\s*)([^,\n]+)(\s*,\s*)([^)\n]+)(\s*\))"
        )
        mutated = []
        combos = [
            ("0", "0"),
            ("0", "1"),
            ("1", "1"),
            ("-1", "1"),
            ("0", "-1"),
            ("0", "8"),
        ]
        for off, length in combos:
            replaced, count = pattern.subn(
                lambda m: f"{m.group(1)}{off}{m.group(3)}{length}{m.group(5)}",
                code,
                count=1,
            )
            if count:
                mutated.append(replaced)
        return mutated

    def buffer_array_alias_mutation(self, code: str) -> List[str]:
        array_match = re.search(r"byte\[\]\s+([A-Za-z_][A-Za-z0-9_]*)\s*=\s*new\s+byte\[(.+?)\];", code)
        if not array_match:
            return []
        array_name = array_match.group(1)
        insertion_pattern = re.compile(rf"({re.escape(array_name)}\s*\[[^\]]+\]\s*=\s*[^\n;]+;\s*)")
        mutated = []
        for snippet in [
            f"\\1\n        {array_name}[0] = (byte) 255;",
            f"\\1\n        byte[] alias_{array_name} = {array_name};\n        alias_{array_name}[0] = (byte) 128;",
        ]:
            replaced, count = insertion_pattern.subn(snippet, code, count=1)
            if count:
                mutated.append(replaced)
        if not mutated and array_match:
            declaration = array_match.group(0)
            mutated.append(
                code.replace(
                    declaration,
                    declaration + f"\n        {array_name}[0] = (byte) 255;",
                    1,
                )
            )
        return mutated

    def buffer_length_constant_mutation(self, code: str) -> List[str]:
        mutated = []
        patterns = [
            (r"\b4096\b", ["1", "8", "8192"]),
            (r"\b1024\b", ["0", "1", "2048"]),
        ]
        for pattern, replacements in patterns:
            for replacement in replacements:
                replaced, count = re.subn(pattern, replacement, code, count=1)
                if count:
                    mutated.append(replaced)
        return mutated

    # FILE operators
    def file_path_traversal_mutation(self, code: str) -> List[str]:
        mutated = self._replace_first_string_literal(
            code,
            [
                '"../tmp/../fuzz4all"',
                '"/tmp/./../tmp/fuzz4all"',
                '"././nested/../../target.txt"',
                '""',
            ],
        )
        if mutated:
            return mutated
        return self._rewrite_first(
            r"(Paths\.get\()\s*([^)]+)(\))",
            lambda: [
                r'\1"../tmp/../fuzz4all"\3',
                r'\1"/tmp/./../tmp/fuzz4all"\3',
            ],
            code,
        )

    def file_state_transition_mutation(self, code: str) -> List[str]:
        mutated = []
        path_match = re.search(r"\bPath\s+([A-Za-z_][A-Za-z0-9_]*)\s*=", code)
        if path_match:
            path_var = path_match.group(1)
            mutated.extend(
                self._insert_after_first_match(
                    code,
                    rf"(\bPath\s+{re.escape(path_var)}\s*=\s*[^\n;]+;\s*)",
                    [
                        f"java.nio.file.Files.deleteIfExists({path_var});",
                        f"if (java.nio.file.Files.exists({path_var})) {{ java.nio.file.Files.deleteIfExists({path_var}); }}",
                    ],
                )
            )
        file_match = re.search(r"\bFile\s+([A-Za-z_][A-Za-z0-9_]*)\s*=", code)
        if file_match:
            file_var = file_match.group(1)
            mutated.extend(
                self._insert_after_first_match(
                    code,
                    rf"(\bFile\s+{re.escape(file_var)}\s*=\s*[^\n;]+;\s*)",
                    [
                        f"{file_var}.delete();",
                        f"if ({file_var}.exists()) {{ {file_var}.delete(); }}",
                    ],
                )
            )
        return mutated

    def file_permission_toggle_mutation(self, code: str) -> List[str]:
        file_match = re.search(r"\bFile\s+([A-Za-z_][A-Za-z0-9_]*)\s*=", code)
        if file_match:
            file_var = file_match.group(1)
            return self._insert_after_first_match(
                code,
                rf"(\bFile\s+{re.escape(file_var)}\s*=\s*[^\n;]+;\s*)",
                [
                    f"{file_var}.setReadable(false);",
                    f"{file_var}.setWritable(false);",
                ],
            )
        path_match = re.search(r"\bPath\s+([A-Za-z_][A-Za-z0-9_]*)\s*=", code)
        if path_match:
            path_var = path_match.group(1)
            return self._insert_after_first_match(
                code,
                rf"(\bPath\s+{re.escape(path_var)}\s*=\s*[^\n;]+;\s*)",
                [
                    f"{path_var}.toFile().setReadable(false);",
                    f"{path_var}.toFile().setWritable(false);",
                ],
            )
        return []

    # CONCURRENT operators
    def concurrent_yield_injection(self, code: str) -> List[str]:
        return self._insert_after_main_open(
            code,
            [
                "Thread.yield();",
                "try { Thread.sleep(1L); } catch (InterruptedException ignored) { Thread.currentThread().interrupt(); }",
            ],
        )

    def concurrent_thread_wrapper_mutation(self, code: str) -> List[str]:
        return self._insert_after_main_open(
            code,
            [
                "Thread helper = new Thread(() -> { Thread.yield(); }); helper.start(); try { helper.join(); } catch (InterruptedException ignored) { Thread.currentThread().interrupt(); }",
                "Thread helper = new Thread(() -> { try { Thread.sleep(1L); } catch (InterruptedException ignored) { Thread.currentThread().interrupt(); } }); helper.start();",
            ],
        )

    def concurrent_signal_sequence_mutation(self, code: str) -> List[str]:
        return self._insert_after_main_open(
            code,
            [
                "Object fuzzLock = new Object(); synchronized (fuzzLock) { fuzzLock.notifyAll(); }",
                "Object fuzzLock = new Object(); synchronized (fuzzLock) { try { fuzzLock.wait(1L); } catch (InterruptedException ignored) { Thread.currentThread().interrupt(); } }",
            ],
        )

    # SECURITY operators
    def security_algorithm_boundary_mutation(self, code: str) -> List[str]:
        return self._replace_first_string_literal(
            code,
            [
                '"AES/GCM/NoPadding"',
                '"AES/CBC/PKCS5Padding"',
                '"RSA/ECB/OAEPWithSHA-256AndMGF1Padding"',
                '"ChaCha20"',
            ],
        )

    def security_provider_mutation(self, code: str) -> List[str]:
        mutated = self._rewrite_first(
            r"(Security\.getProvider\()\s*([^)]+)(\))",
            lambda: [r'\1"SunJCE"\3', r'\1"SUN"\3', r'\1"SunJSSE"\3'],
            code,
        )
        if mutated:
            return mutated
        return self._insert_after_main_open(
            code,
            [
                "java.security.Provider[] providers = java.security.Security.getProviders();",
                'java.security.Provider provider = java.security.Security.getProvider("SunJCE");',
            ],
        )

    def security_material_boundary_mutation(self, code: str) -> List[str]:
        mutated = self._replace_first_numeric_literal(code, ["0", "1", "16", "32"])
        if mutated:
            return mutated
        return self._rewrite_first(
            r"(new\s+byte\[\]\s*\{)([^{}]*)(\})",
            lambda: [
                r"\1(byte) 0\3",
                r"\1(byte) 1, (byte) 2, (byte) 3\3",
                r"\1(byte) 255, (byte) 128\3",
            ],
            code,
        )

    # REFLECT operators
    def reflect_accessibility_flip_mutation(self, code: str) -> List[str]:
        mutated = []
        for src, dst in [
            (".setAccessible(true)", ".setAccessible(false)"),
            (".setAccessible(false)", ".setAccessible(true)"),
        ]:
            if src in code:
                mutated.append(code.replace(src, dst, 1))
        if mutated:
            return mutated
        assignment_match = re.search(
            r"([A-Za-z0-9_<>.\[\]]+\s+([A-Za-z_][A-Za-z0-9_]*)\s*=\s*[^;\n]*getDeclared(?:Method|Field|Constructor)\([^\n;]*\);\s*)",
            code,
        )
        if not assignment_match:
            return []
        whole_line = assignment_match.group(1)
        variable_name = assignment_match.group(2)
        return [code.replace(whole_line, whole_line + f"\n        {variable_name}.setAccessible(true);", 1)]

    def reflect_member_name_mutation(self, code: str) -> List[str]:
        return self._replace_first_string_literal(
            code,
            ['"value"', '"hashCode"', '"nonExistingField"', '"length"'],
        )

    def reflect_receiver_null_mutation(self, code: str) -> List[str]:
        mutated = self._rewrite_first(
            r"(\.\s*invoke\()\s*([^,\n]+)(\s*,)",
            lambda: [r"\1null\3"],
            code,
        )
        if mutated:
            return mutated
        return self._rewrite_first(
            r"(\.\s*(?:get|set)\()\s*([^,\n)]+)(\s*[,)\n])",
            lambda: [r"\1null\3"],
            code,
        )

    # CALLBACK operators
    def callback_duplicate_registration_mutation(self, code: str) -> List[str]:
        pattern = re.compile(r"([A-Za-z_][A-Za-z0-9_]*\.\s*(?:add|register)[^\n;]+;\s*)")
        mutated = []
        replaced, count = pattern.subn(r"\1\n        \1", code, count=1)
        if count:
            mutated.append(replaced)
        return mutated

    def callback_order_reversal_mutation(self, code: str) -> List[str]:
        lines = code.splitlines()
        indices = [
            index
            for index, line in enumerate(lines)
            if ".add" in line or ".remove" in line or ".register" in line or ".unregister" in line
        ]
        if len(indices) < 2:
            return []
        i1, i2 = indices[0], indices[1]
        reordered = list(lines)
        reordered[i1], reordered[i2] = reordered[i2], reordered[i1]
        return ["\n".join(reordered)]

    def callback_null_event_mutation(self, code: str) -> List[str]:
        mutated = self._rewrite_first(
            r"(\.\s*(?:handle|accept|actionPerformed|stateChanged|itemStateChanged|windowOpened|mouseClicked)\()\s*([^)]+)(\))",
            lambda: [r"\1null\3"],
            code,
        )
        if mutated:
            return mutated
        return self._rewrite_first(
            r"(\.\s*firePropertyChange\(\s*[^,\n]+,\s*)([^,\n]+)(\s*,\s*)([^)\n]+)(\))",
            lambda: [r'\1null\3null\4', r'\1""\3null\4'],
            code,
        )

    # TIME operators
    def time_epoch_boundary_mutation(self, code: str) -> List[str]:
        return self._replace_first_numeric_literal(
            code,
            ["0L", "-1L", "Long.MAX_VALUE", "Long.MIN_VALUE"],
        )

    def time_duration_sign_mutation(self, code: str) -> List[str]:
        pattern = re.compile(r"(\b(?:Duration|Period)\.\w+\()\s*([^,\n)]+)(\))")
        mutated = []
        for replacement in ["-1", "0", "1"]:
            replaced, count = pattern.subn(
                lambda m: f"{m.group(1)}{replacement}{m.group(3)}",
                code,
                count=1,
            )
            if count:
                mutated.append(replaced)
        return mutated

    def time_zone_boundary_mutation(self, code: str) -> List[str]:
        return self._replace_first_string_literal(
            code,
            ['"UTC"', '"GMT+14"', '"UTC-12"', '"Asia/Shanghai"'],
        )

    # NETWORK operators
    def network_endpoint_boundary_mutation(self, code: str) -> List[str]:
        return self._replace_first_string_literal(
            code,
            ['"127.0.0.1"', '"::1"', '"http://127.0.0.1:1"', '""'],
        )

    def network_timeout_boundary_mutation(self, code: str) -> List[str]:
        pattern = re.compile(r"(\.\s*set(?:So)?Timeout\()\s*([^)\n]+)(\))")
        mutated = []
        for replacement in ["0", "1", "Integer.MAX_VALUE"]:
            replaced, count = pattern.subn(
                lambda m: f"{m.group(1)}{replacement}{m.group(3)}",
                code,
                count=1,
            )
            if count:
                mutated.append(replaced)
        if mutated:
            return mutated
        return self._replace_first_numeric_literal(code, ["0", "1", "65535", "Integer.MAX_VALUE"])

    def network_sequence_mutation(self, code: str) -> List[str]:
        socket_match = re.search(r"\b(?:Socket|ServerSocket|DatagramSocket)\s+([A-Za-z_][A-Za-z0-9_]*)\s*=", code)
        if not socket_match:
            return []
        socket_var = socket_match.group(1)
        return self._insert_after_first_match(
            code,
            rf"(\b(?:Socket|ServerSocket|DatagramSocket)\s+{re.escape(socket_var)}\s*=\s*[^\n;]+;\s*)",
            [
                f"{socket_var}.close();",
                f"try {{ {socket_var}.setSoTimeout(1); }} catch (Exception ignored) {{ }}",
            ],
        )

    # UTILITY operators
    def utility_parse_boundary_mutation(self, code: str) -> List[str]:
        mutated = self._replace_first_string_literal(
            code,
            ['""', '"-1"', '"2147483647"', '"NaN"'],
        )
        if mutated:
            return mutated
        return self._replace_first_numeric_literal(code, ["0", "-1", "Integer.MAX_VALUE"])

    def utility_format_boundary_mutation(self, code: str) -> List[str]:
        return self._replace_first_string_literal(
            code,
            ['"%s%s%s"', '"%1$tm"', '"%020d"', '"%1$tF %1$tT"'],
        )

    def utility_collection_seed_mutation(self, code: str) -> List[str]:
        return self._insert_after_main_open(
            code,
            [
                'java.util.List<String> fuzzList = java.util.Arrays.asList("a", "b", "a");',
                'java.util.Locale fuzzLocale = java.util.Locale.ROOT;',
            ],
        )

    # JVM_MGMT operators
    def jvm_mgmt_query_name_mutation(self, code: str) -> List[str]:
        mutated = self._replace_first_string_literal(
            code,
            [
                '"java.lang:type=Memory"',
                '"java.lang:type=Threading"',
                '"java.lang:type=Runtime"',
                '"bad:name="',
            ],
        )
        if mutated:
            return mutated
        return self._insert_after_main_open(
            code,
            [
                'javax.management.ObjectName memoryName = new javax.management.ObjectName("java.lang:type=Memory");',
                'javax.management.ObjectName threadName = new javax.management.ObjectName("java.lang:type=Threading");',
            ],
        )

    def jvm_mgmt_runtime_toggle_mutation(self, code: str) -> List[str]:
        return self._insert_after_main_open(
            code,
            [
                "java.lang.management.ManagementFactory.getRuntimeMXBean().getInputArguments();",
                "java.lang.management.ManagementFactory.getMemoryMXBean().getHeapMemoryUsage();",
                "java.lang.management.ManagementFactory.getThreadMXBean().getThreadCount();",
            ],
        )

    def jvm_mgmt_sampling_boundary_mutation(self, code: str) -> List[str]:
        mutated = self._replace_first_numeric_literal(code, ["0L", "1L", "Long.MAX_VALUE"])
        if mutated:
            return mutated
        return self._insert_after_main_open(
            code,
            [
                "long[] ids = java.lang.management.ManagementFactory.getThreadMXBean().getAllThreadIds();",
                "java.lang.management.ManagementFactory.getMemoryMXBean().getObjectPendingFinalizationCount();",
            ],
        )

    # MARK_SUPPORT operators
    def mark_support_limit_mutation(self, code: str) -> List[str]:
        pattern = re.compile(r"(\.\s*mark\()\s*([^)\n]+)(\))")
        mutated = []
        for replacement in ["0", "1", "-1", "8192"]:
            replaced, count = pattern.subn(
                lambda m: f"{m.group(1)}{replacement}{m.group(3)}",
                code,
                count=1,
            )
            if count:
                mutated.append(replaced)
        return mutated

    def mark_support_reset_mutation(self, code: str) -> List[str]:
        variable_match = re.search(
            r"(?:BufferedInputStream|BufferedReader|ByteArrayInputStream|CharArrayReader)\s+([A-Za-z_][A-Za-z0-9_]*)\s*=",
            code,
        )
        if not variable_match:
            return []
        variable_name = variable_match.group(1)
        return self._insert_after_first_match(
            code,
            rf"((?:BufferedInputStream|BufferedReader|ByteArrayInputStream|CharArrayReader)\s+{re.escape(variable_name)}\s*=\s*[^\n;]+;\s*)",
            [
                f"try {{ {variable_name}.reset(); }} catch (Exception ignored) {{ }}",
                f"{variable_name}.mark(1); try {{ {variable_name}.reset(); }} catch (Exception ignored) {{ }}",
            ],
        )

    def mark_support_reuse_mutation(self, code: str) -> List[str]:
        variable_match = re.search(
            r"(?:BufferedInputStream|BufferedReader|ByteArrayInputStream|CharArrayReader)\s+([A-Za-z_][A-Za-z0-9_]*)\s*=",
            code,
        )
        if not variable_match:
            return []
        variable_name = variable_match.group(1)
        return self._insert_after_first_match(
            code,
            rf"((?:BufferedInputStream|BufferedReader|ByteArrayInputStream|CharArrayReader)\s+{re.escape(variable_name)}\s*=\s*[^\n;]+;\s*)",
            [
                f"{variable_name}.mark(1); {variable_name}.mark(8);",
                f"{variable_name}.mark(1); try {{ {variable_name}.reset(); {variable_name}.reset(); }} catch (Exception ignored) {{ }}",
            ],
        )

    # Generic fallback operators.
    def generic_null_boundary(self, code: str) -> List[str]:
        mutated = []
        for pattern in [r"new\s+[A-Za-z_][A-Za-z0-9_<>.]*\([^\)]*\)", r"\bSystem\.out\b"]:
            replaced, count = re.subn(pattern, "null", code, count=1)
            if count:
                mutated.append(replaced)
        return mutated

    def generic_numeric_boundary(self, code: str) -> List[str]:
        mutated = []
        for replacement in ["0", "-1", "1", "Integer.MAX_VALUE"]:
            replaced, count = re.subn(r"\b\d+\b", replacement, code, count=1)
            if count:
                mutated.append(replaced)
        return mutated

    def generic_sequence_reorder(self, code: str) -> List[str]:
        lines = code.splitlines()
        write_lines = [i for i, line in enumerate(lines) if ".write(" in line or ".flush(" in line]
        if len(write_lines) < 2:
            return []
        i1, i2 = write_lines[0], write_lines[1]
        reordered = list(lines)
        reordered[i1], reordered[i2] = reordered[i2], reordered[i1]
        return ["\n".join(reordered)]

    # Backward-compatible aliases so existing configs/results still work.
    def constructor_size_edge(self, code: str) -> List[str]:
        return self.resource_constructor_edge(code)

    def write_single_edge(self, code: str) -> List[str]:
        return self.buffer_write_single_edge(code)

    def write_bulk_edge(self, code: str) -> List[str]:
        return self.buffer_write_bulk_edge(code)

    def lifecycle_sequence(self, code: str) -> List[str]:
        return self.resource_lifecycle_sequence(code)
