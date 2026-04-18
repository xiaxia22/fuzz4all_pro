import os
import re
import subprocess
import tempfile
import time
from pathlib import Path
from re import search
from typing import List, Union

from Fuzz4All.target.target import FResult, Target
from Fuzz4All.util.Logger import LEVEL
from Fuzz4All.util.util import comment_remover


class JAVATarget(Target):
    FORCED_JAVA_VERSION = "21"
    FORCE_ENABLE_PREVIEW = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if kwargs["template"] == "fuzzing_with_config_file":
            config_dict = kwargs["config_dict"]
            self.prompt_used = self._create_prompt_from_config(config_dict)
            self.config_dict = config_dict
            target_cfg = config_dict.get("target", {})
            self.java_version = str(
                target_cfg.get("java_version", self.FORCED_JAVA_VERSION)
            )
            self.enable_preview = bool(
                target_cfg.get("enable_preview", self.FORCE_ENABLE_PREVIEW)
            )
            self.runtime_feedback_mode = target_cfg.get(
                "runtime_feedback_mode", "normalized"
            )
            self.max_feedback_rules = target_cfg.get("max_feedback_rules", 5)
            self.max_safe_examples = target_cfg.get("max_safe_examples", 2)
            self.prompt_refresh_interval = target_cfg.get(
                "prompt_refresh_interval", 5
            )
        else:
            raise NotImplementedError

    def write_back_file(self, code, write_back_name=""):
        if write_back_name == "":
            write_back_name = self._default_temp_java_file()
        if write_back_name != "":
            try:
                with open(write_back_name, "w", encoding="utf-8") as f:
                    f.write(code)
            except:
                pass
        return write_back_name

    def _temp_root(self) -> Path:
        return Path(tempfile.gettempdir()) / f"fuzz4all_java_{int(self.CURRENT_TIME)}"

    def _default_temp_java_file(self) -> str:
        return str(self._temp_root().with_suffix(".java"))

    def wrap_prompt(self, prompt: str) -> str:
        return f"/* {prompt} */\n{self.prompt_used['separator']}\n{self.prompt_used['begin']}"

    def wrap_in_comment(self, prompt: str) -> str:
        return f"/* {prompt} */"

    def filter(self, code: str) -> bool:
        clean_code = code.replace(self.prompt_used["begin"], "").strip()
        if self.prompt_used["target_api"] not in clean_code:
            return False
        return True

    def clean(self, code: str) -> str:
        code = comment_remover(code)
        return code

    def clean_code(self, code: str) -> str:
        code = comment_remover(code)
        code = "\n".join(
            [
                line
                for line in code.split("\n")
                if line.strip() != "" and line.strip() != self.prompt_used["begin"]
            ]
        )
        return code

    def extract_javac_error_categories(self, message: str) -> List[str]:
        categories = []
        normalized = message or ""

        if "cannot find symbol" in normalized:
            categories.append("missing_public_method")
        if "has protected access" in normalized:
            categories.append("protected_member_access")
        if "void type not allowed here" in normalized:
            categories.append("write_used_as_expression")
        if "no suitable method found for write" in normalized:
            categories.append("invalid_write_overload")
        if "cannot be applied to given types" in normalized:
            categories.append("invalid_method_signature")
        if "no suitable constructor found" in normalized:
            categories.append("invalid_constructor")
        if "unreported exception IOException" in normalized:
            categories.append("unchecked_ioexception")
        if "unreported exception FileNotFoundException" in normalized:
            categories.append("unchecked_ioexception")
        if "possible lossy conversion" in normalized:
            categories.append("lossy_conversion")
        if "should be declared in a file named" in normalized:
            categories.append("public_class_filename_mismatch")
        if "reference to" in normalized and "is ambiguous" in normalized:
            categories.append("ambiguous_reference")
        if "reached end of file while parsing" in normalized:
            categories.append("incomplete_structure")
        if "'try' without 'catch', 'finally' or resource declarations" in normalized:
            categories.append("invalid_try_structure")
        if "not a statement" in normalized:
            categories.append("invalid_statement")
        if "exception IOException is never thrown in body of corresponding try statement" in normalized:
            categories.append("invalid_exception_handling")
        if "cannot find symbol" in normalized and (
            "DEFAULT_BUFFER_SIZE" in normalized
            or "defaultBufferSize" in normalized
        ):
            categories.append("invented_buffer_constant")
        if "cannot find symbol" in normalized and "sun.reflect" in normalized:
            categories.append("internal_jdk_api")
        if "import sun.reflect" in normalized:
            categories.append("internal_jdk_api")
        if "attempting to assign weaker access privileges" in normalized:
            categories.append("weaker_override_access")
        if "cannot be converted to OutputStream" in normalized:
            categories.append("invalid_constructor_argument")
        if "incompatible types" in normalized:
            categories.append("incompatible_types")
        if "method setByte in class Field cannot be applied" in normalized:
            categories.append("reflection_api_misuse")
        if "Field cannot be converted to int" in normalized:
            categories.append("reflection_api_misuse")
        if "int cannot be dereferenced" in normalized:
            categories.append("reflection_api_misuse")
        if "cannot find symbol" in normalized and "Arrays" in normalized:
            categories.append("missing_import")
        if re.search(r"package\s+[A-Za-z0-9_.]+\s+does not exist", normalized):
            categories.append("missing_import")

        return categories

    def extract_target_api_misuse_examples(self, message: str) -> List[str]:
        symbols = []
        for match in re.findall(r"symbol:\s+method\s+([A-Za-z_][A-Za-z0-9_]*)", message):
            if match not in symbols:
                symbols.append(match)
        for match in re.findall(
            r"no suitable method found for\s+([A-Za-z_][A-Za-z0-9_]*\([^\)]*\))",
            message,
        ):
            if match not in symbols:
                symbols.append(match)
        return symbols[:3]

    def map_error_categories_to_rules(
        self, categories: List[str], message: str
    ) -> List[str]:
        target_api = self.prompt_used.get("target_api", "the target API")
        primary_tag = (self.mutation_profile or {}).get("primary_tag", "")
        rules = []
        misuse_symbols = self.extract_target_api_misuse_examples(message)

        if "missing_public_method" in categories:
            if misuse_symbols:
                rules.append(
                    "Do not call undocumented methods such as "
                    + ", ".join(f"{name}()" if "(" not in name else name for name in misuse_symbols)
                    + f" on {target_api}."
                )
            rules.append(
                f"Use only documented public methods and nested types of {target_api}."
            )
        if "protected_member_access" in categories:
            rules.append(
                f"Do not access protected or internal fields of {target_api} from external code."
            )
        if "write_used_as_expression" in categories:
            rules.append(
                "Do not use void-returning API calls as expressions or values."
            )
        if "invalid_write_overload" in categories:
            rules.append(
                f"Match method overloads of {target_api} exactly; do not invent write(...) or off/len signatures."
            )
        if "invalid_method_signature" in categories:
            rules.append(
                f"Match argument types and arity exactly to the documented signatures of {target_api}."
            )
        if "invalid_constructor" in categories:
            rules.append(
                f"Use only documented constructors and valid argument lists for {target_api}."
            )
        if "unchecked_ioexception" in categories:
            rules.append(
                "Handle checked IOExceptions with try/catch or declare throws where required."
            )
        if "lossy_conversion" in categories:
            rules.append(
                "Use explicit byte casts when inserting int values into byte arrays."
            )
        if "public_class_filename_mismatch" in categories:
            rules.append(
                "If a public class is declared, ensure the class name matches the Java file name."
            )
        if "ambiguous_reference" in categories:
            rules.append(
                "Avoid ambiguous imports or duplicate type references; keep imports minimal and consistent."
            )
        if "incomplete_structure" in categories:
            rules.append(
                "Generate complete Java syntax with balanced braces, closed methods, and closed classes."
            )
        if "invalid_try_structure" in categories:
            rules.append(
                "Every try block must include catch/finally or use try-with-resources."
            )
        if "invalid_statement" in categories:
            rules.append(
                "Emit only complete Java statements; do not leave method calls or expressions unfinished."
            )
        if "invalid_exception_handling" in categories:
            rules.append(
                "Catch only exceptions that the enclosed code can actually throw."
            )
        if "invented_buffer_constant" in categories:
            rules.append(
                f"Do not invent undocumented constants, size fields, or helper members for {target_api}."
            )
        if "internal_jdk_api" in categories:
            rules.append(
                "Do not import or rely on internal sun.* JDK APIs."
            )
        if "weaker_override_access" in categories:
            rules.append(
                "When overriding inherited methods, keep visibility compatible with the parent public method."
            )
        if "invalid_constructor_argument" in categories:
            rules.append(
                f"Pass constructor arguments with the exact documented runtime types expected by {target_api}."
            )
        if "reflection_api_misuse" in categories:
            rules.append(
                "If reflection is used, match Field and Method APIs with correct parameter types and receiver objects."
            )
        if "missing_import" in categories:
            rules.append(
                "Add required public imports for referenced JDK classes, or avoid undocumented helpers."
            )
        if "incompatible_types" in categories:
            rules.append(
                f"Keep variable, receiver, and return types consistent with the documented contracts of {target_api}."
            )

        if primary_tag == "SECURITY":
            rules.append(
                f"For {target_api}, prefer documented algorithms, providers, and key/material sizes instead of guessed values."
            )
        elif primary_tag == "FILE":
            rules.append(
                f"For {target_api}, keep file/path objects and lifecycle state transitions explicit and type-correct."
            )
        elif primary_tag == "CONCURRENT":
            rules.append(
                f"For {target_api}, keep thread/interleaving helpers syntactically isolated so concurrency scaffolding still compiles."
            )
        elif primary_tag == "REFLECT":
            rules.append(
                f"For {target_api}, keep reflected member names, receiver objects, and accessibility changes consistent with the reflection API."
            )
        elif primary_tag == "CALLBACK":
            rules.append(
                f"For {target_api}, keep listener registration order valid and callback argument types concrete."
            )
        elif primary_tag == "TIME":
            rules.append(
                f"For {target_api}, keep epoch, duration, and zone arguments within the documented API forms."
            )
        elif primary_tag == "NETWORK":
            rules.append(
                f"For {target_api}, keep endpoint objects, timeout values, and connect/bind order aligned with the documented lifecycle."
            )
        elif primary_tag == "JVM_MGMT":
            rules.append(
                f"For {target_api}, use documented MXBean/runtime query entry points and valid management object names."
            )
        elif primary_tag == "MARK_SUPPORT":
            rules.append(
                f"For {target_api}, keep mark/reset usage tied to the documented stream or reader lifecycle."
            )
        elif primary_tag == "UTILITY":
            rules.append(
                f"For {target_api}, prefer documented parse/format/value helpers and avoid guessed helper methods."
            )

        deduped = []
        for rule in rules:
            if rule not in deduped:
                deduped.append(rule)
        return deduped

    def summarize_feedback_message(self, result: FResult, message: str) -> List[str]:
        if result not in (FResult.FAILURE, FResult.ERROR, FResult.TIMED_OUT):
            return []

        categories = self.extract_javac_error_categories(message or "")
        rules = self.map_error_categories_to_rules(categories, message or "")
        if rules:
            return rules

        summary = self._sanitize_feedback(message, limit=200)
        return [summary] if summary else []

    # If there exists a public class, ensure file name matches
    def determine_file_name(self, code):
        public_class_name = search("\s*public(\s)+class(\s)+([^\s\{]+)", code)
        if public_class_name is None:
            # No public class found, return standard write back file name
            return self._default_temp_java_file()

        # check if folder exists
        temp_dir = self._temp_root()
        temp_dir.mkdir(parents=True, exist_ok=True)

        # Public class is found, ensure that file name matches public class name
        return str(temp_dir / f"{public_class_name[0].split()[-1]}.java")

    def validate_individual(self, filename) -> (FResult, str):
        write_back_name = ""
        try:
            with open(filename, "r", encoding="utf-8") as f:
                code = f.read()
                write_back_name = self.determine_file_name(code)
                self.write_back_file(code, write_back_name=write_back_name)
        except:
            pass

        java_version = self.java_version
        preview_flag = " --enable-preview" if self.enable_preview else ""
        compile_cmd = (
            f"{self.target_name} --source {java_version}{preview_flag}"
            f" --target {java_version} {write_back_name}"
        )

        try:
            exit_code = subprocess.run(
                compile_cmd,
                shell=True,
                capture_output=True,
                encoding="utf-8",
                timeout=5,
                text=True,
            )
        except subprocess.TimeoutExpired as te:
            if os.name == "posix":
                pname = f"'temp{self.CURRENT_TIME}'"
                subprocess.run(
                    ["ps -ef | grep " + pname + " | grep -v grep | awk '{print $2}'"],
                    shell=True,
                )
                subprocess.run(
                    [
                        "ps -ef | grep "
                        + pname
                        + " | grep -v grep | awk '{print $2}' | xargs -r kill -9"
                    ],
                    shell=True,
                )  # kill all tests thank you
            return FResult.TIMED_OUT, "java"
        if exit_code.returncode == 1:
            return FResult.FAILURE, exit_code.stderr
        elif exit_code.returncode == 0:
            return FResult.SAFE, "its safe"
        else:
            return FResult.ERROR, exit_code.stderr
