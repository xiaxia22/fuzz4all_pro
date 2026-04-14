import re
from typing import Any, Dict, List


class JavaMutator:
    def __init__(self, profile: Dict[str, Any]) -> None:
        self.profile = profile

    def generate_mutations(self, code: str, budget: int = 2) -> List[Dict[str, Any]]:
        operators = self.profile.get("priority_operators", [])
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

    def constructor_size_edge(self, code: str) -> List[str]:
        mutated = []
        sized_pattern = re.compile(
            r"new\s+BufferedOutputStream\((.+?),\s*(-?\d+)\)"
        )
        for size in ["1", "8", "8192", "0", "-1"]:
            replaced, count = sized_pattern.subn(
                lambda m: f"new BufferedOutputStream({m.group(1)}, {size})",
                code,
                count=1,
            )
            if count:
                mutated.append(replaced)

        unsized_pattern = re.compile(r"new\s+BufferedOutputStream\(([^,\n]+)\)")
        for size in ["8", "8192"]:
            replaced, count = unsized_pattern.subn(
                lambda m: f"new BufferedOutputStream({m.group(1)}, {size})",
                code,
                count=1,
            )
            if count:
                mutated.append(replaced)
        return mutated

    def write_single_edge(self, code: str) -> List[str]:
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
        return mutated

    def write_bulk_edge(self, code: str) -> List[str]:
        pattern = re.compile(
            r"(\.\s*write\(\s*[^,\n]+,\s*)([^,\n]+)(\s*,\s*)([^)\n]+)(\s*\))"
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

    def lifecycle_sequence(self, code: str) -> List[str]:
        variable_match = re.search(
            r"BufferedOutputStream\s+([A-Za-z_][A-Za-z0-9_]*)\s*=",
            code,
        )
        if not variable_match:
            return []

        variable_name = variable_match.group(1)
        insert_after_write = re.compile(
            rf"({re.escape(variable_name)}\s*\.\s*write\([^\n;]*\);\s*)"
        )
        mutated = []
        for snippet in [
            f"\\1\n        {variable_name}.flush();",
            f"\\1\n        {variable_name}.flush();\n        {variable_name}.write(255);",
            f"\\1\n        {variable_name}.close();\n        {variable_name}.flush();",
        ]:
            replaced, count = insert_after_write.subn(snippet, code, count=1)
            if count:
                mutated.append(replaced)
        return mutated
