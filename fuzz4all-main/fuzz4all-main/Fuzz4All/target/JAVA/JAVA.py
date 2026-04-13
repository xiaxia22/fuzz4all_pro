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
            self.java_version = self.FORCED_JAVA_VERSION
            self.enable_preview = self.FORCE_ENABLE_PREVIEW
            target_cfg = config_dict.get("target", {})
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
        if "unreported exception IOException" in normalized:
            categories.append("unchecked_ioexception")
        if "possible lossy conversion" in normalized:
            categories.append("lossy_conversion")
        if "should be declared in a file named" in normalized:
            categories.append("public_class_filename_mismatch")
        if "reference to" in normalized and "is ambiguous" in normalized:
            categories.append("ambiguous_reference")

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
        rules = []
        misuse_symbols = self.extract_target_api_misuse_examples(message)

        if "missing_public_method" in categories:
            if misuse_symbols:
                rules.append(
                    "Do not call undocumented methods such as "
                    + ", ".join(f"{name}()" if "(" not in name else name for name in misuse_symbols)
                    + " on BufferedOutputStream."
                )
            rules.append(
                "Use only documented public methods of BufferedOutputStream and related stream types."
            )
        if "protected_member_access" in categories:
            rules.append(
                "Do not access protected or internal fields such as buf and count from external code."
            )
        if "write_used_as_expression" in categories:
            rules.append(
                "Do not use BufferedOutputStream.write(...) as an expression; write methods return void."
            )
        if "invalid_write_overload" in categories:
            rules.append(
                "Use only valid overloads: write(int), write(byte[]), and write(byte[], int, int)."
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

        java_version = self.FORCED_JAVA_VERSION
        preview_flag = " --enable-preview" if self.FORCE_ENABLE_PREVIEW else ""
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
