import os
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
