import glob
import os
import random
import time
from enum import Enum
from typing import Any, Dict, List, Tuple, Union

import torch
from rich.progress import track

from Fuzz4All.model import make_model
from Fuzz4All.util.Logger import LEVEL, Logger
from Fuzz4All.util.api_request import create_config, request_engine
from Fuzz4All.util.util import create_chatgpt_docstring_template
from Fuzz4All.util.util import simple_parse

try:
    import ollama

    HAS_OLLAMA = True
except ImportError:
    HAS_OLLAMA = False


def is_ollama_model(model_name: str) -> bool:
    return model_name.startswith("ollama/")


def get_ollama_model_name(model_name: str) -> str:
    if is_ollama_model(model_name):
        return model_name.split("/", 1)[1]
    return model_name


class FResult(Enum):
    SAFE = 1  # validation returns okay
    FAILURE = 2  # validation contains error (something wrong with validation)
    ERROR = 3  # validation returns a potential error (look into)
    LLM_WEAKNESS = (
        4  # the generated input is ill-formed due to the weakness of the language model
    )
    TIMED_OUT = 10  # timed out, can be okay in certain targets


# base class file for target, used for user defined system targets
# the point is to separately define oracles/fuzzing specific functions/and usages
# target should be a stateful objects which has some notion of history (keeping a state of latest prompts)
class Target(object):
    def __init__(self, language="c", timeout=10, folder="/", **kwargs):
        self.language = language
        self.folder = folder
        self.timeout = timeout
        self.CURRENT_TIME = time.time()
        # model based variables
        self.batch_size = kwargs["bs"]
        self.temperature = kwargs["temperature"]
        self.max_length = kwargs["max_length"]
        self.device = kwargs["device"]
        self.model_name = kwargs["model_name"]
        self.model = None
        self.backend = "huggingface"
        # loggers
        self.g_logger = Logger(self.folder, "log_generation.txt", level=kwargs["level"])
        self.v_logger = Logger(self.folder, "log_validation.txt", level=kwargs["level"])
        # main logger for system messages
        self.m_logger = Logger(self.folder, "log.txt")
        # system messages for prompting
        self.SYSTEM_MESSAGE = None
        self.AP_SYSTEM_MESSAGE = "You are an auto-prompting tool"
        self.AP_INSTRUCTION = (
            "Please summarize the documentation into a short fuzzing prompt that teaches a code model "
            "how to generate valid, diverse, and tricky inputs for the target. Focus on syntax, key "
            "constructs, unusual combinations, and edge cases that are likely to stress the compiler."
        )
        # prompt based variables
        self.hw = kwargs["use_hw"]
        self.no_input_prompt = kwargs["no_input_prompt"]
        self.prompt_used = None
        self.prompt = None
        self.initial_prompt = None
        self.prev_example = None
        self.feedback_history = []
        # prompt strategies
        self.se_prompt = self.wrap_in_comment(
            "Please create a semantically equivalent program to the previous "
            "generation"
        )
        self.m_prompt = self.wrap_in_comment(
            "Please create a mutated program that modifies the previous generation"
        )
        self.c_prompt = self.wrap_in_comment(
            "Please combine the two previous programs into a single program"
        )
        self.p_strategy = kwargs["prompt_strategy"]
        # eos based
        self.special_eos = None
        if "model_name" in kwargs:
            self.model_name = kwargs["model_name"]
        if "target_name" in kwargs:
            self.target_name = kwargs["target_name"]

    @staticmethod
    def _create_prompt_from_config(config_dict: Dict[str, Any]) -> Dict:
        """Read the prompt ingredients via a config file."""
        documentation, example_code, hand_written_prompt = None, None, None

        # read the prompt ingredients from the config file
        target = config_dict["target"]
        path_documentation = target["path_documentation"]
        if path_documentation is not None:
            documentation = open(path_documentation, "r").read()
        path_example_code = target["path_example_code"]
        if path_example_code is not None:
            example_code = open(path_example_code, "r").read()
        trigger_to_generate_input = target["trigger_to_generate_input"]
        input_hint = target["input_hint"]
        path_hand_written_prompt = target["path_hand_written_prompt"]
        if path_hand_written_prompt is not None:
            hand_written_prompt = open(path_hand_written_prompt, "r").read()
        target_string = target["target_string"]
        dict_compat = {
            "docstring": documentation,
            "example_code": example_code,
            "separator": trigger_to_generate_input,
            "begin": input_hint,
            "hw_prompt": hand_written_prompt,
            "target_api": target_string,
        }
        return dict_compat

    def _sanitize_feedback(self, text: str, limit: int = 400) -> str:
        text = (text or "").strip()
        if text == "":
            return ""
        text = " ".join(text.split())
        return text[:limit]

    def _build_handwritten_prompt(self, manual_prompt: str = None) -> str:
        parts = []
        if manual_prompt:
            parts.append(manual_prompt.strip())
        if self.prompt_used.get("example_code"):
            parts.append(
                "Use the following example style and structural patterns as guidance:\n"
                f"```{self.language}\n{self.prompt_used['example_code'].strip()}\n```"
            )
        if self.prompt_used.get("docstring"):
            parts.append(
                "Use the following reference notes about the target language or feature:\n"
                f"{self.prompt_used['docstring'].strip()}"
            )
        if len(parts) == 0:
            return f"{self.prompt_used['separator']}\n{self.prompt_used['begin']}"
        return self.wrap_prompt("\n\n".join(parts))

    def write_back_file(self, code: str):
        raise NotImplementedError

    # each target defines their way of validating prompts (can overwrite)
    def validate_prompt(self, prompt: str):
        fos = self._generate_with_prompt(
            prompt,
            batch_size=self.batch_size,
            temperature=self.temperature,
            max_length=self.max_length,
        )
        unique_set = set()
        score = 0
        for fo in fos:
            code = self.prompt_used["begin"] + "\n" + fo
            wb_file = self.write_back_file(code)
            result, _ = self.validate_individual(wb_file)
            if (
                result == FResult.SAFE
                and self.filter(code)
                and self.clean_code(code) not in unique_set
            ):
                unique_set.add(self.clean_code(code))
                score += 1
        return score

    # each target defines their way of validating prompts
    # for example we might want to encode the prompt as a docstring comment to facilitate better generation using
    # smaller LLMs
    def wrap_prompt(self, prompt: str) -> str:
        raise NotImplementedError

    def wrap_in_comment(self, prompt: str) -> str:
        raise NotImplementedError

    def _create_auto_prompt_message(self, message: str) -> List[dict]:
        target_api = self.prompt_used.get("target_api") or "the target language feature"
        instruction = (
            f"{self.AP_INSTRUCTION} Pay special attention to {target_api}. "
            "Do not explain the documentation. Produce a concise prompt for code generation."
        )
        return create_chatgpt_docstring_template(
            system_message=self.AP_SYSTEM_MESSAGE,
            user_message=instruction,
            docstring=message,
            example=self.prompt_used.get("example_code") or "",
            first="",
        )

    def _create_feedback_prompt(self, new_code: str, feedback_items: List[str]) -> str:
        feedback_block = ""
        if feedback_items:
            feedback_lines = "\n".join(
                [self.wrap_in_comment(f"Recent compiler feedback: {item}") for item in feedback_items]
            )
            feedback_block = f"{feedback_lines}\n"
        return (
            self.initial_prompt
            + feedback_block
            + self.update_strategy(new_code)
            + self.prompt_used["begin"]
            + "\n"
        )

    def _create_feedback_only_prompt(self, feedback_items: List[str]) -> str:
        feedback_lines = "\n".join(
            [self.wrap_in_comment(f"Recent compiler feedback: {item}") for item in feedback_items]
        )
        return (
            self.initial_prompt
            + "\n"
            + feedback_lines
            + "\n"
            + self.prompt_used["separator"]
            + "\n"
            + self.prompt_used["begin"]
            + "\n"
        )

    def _generate_with_prompt(
        self,
        prompt: str,
        batch_size: int,
        temperature: float,
        max_length: int,
    ) -> List[str]:
        if getattr(self, "backend", None) == "ollama" and HAS_OLLAMA:
            outputs = []
            for _ in range(batch_size):
                response = ollama.chat(
                    model=self.ollama_model_name,
                    messages=[{"role": "user", "content": prompt}],
                    options={
                        "temperature": max(temperature, 1e-2),
                        "num_predict": max_length,
                    },
                )
                content = response["message"]["content"]
                code = simple_parse(content)
                outputs.append(code if code else content)
            return outputs

        return self.model.generate(
            prompt,
            batch_size=batch_size,
            temperature=temperature,
            max_length=max_length,
        )

    def _request_auto_prompt_candidates(self, message: str) -> Tuple[str, List[str]]:
        llm_config = getattr(self, "config_dict", {}).get("llm", {})
        autoprompt_model = llm_config.get("autoprompt_model", "deepseek-chat")
        candidate_count = llm_config.get("autoprompt_candidates", 3)
        greedy_temperature = llm_config.get("autoprompt_greedy_temperature", 0.2)
        candidate_temperature = llm_config.get("autoprompt_temperature", 0.9)
        max_tokens = llm_config.get("autoprompt_max_tokens", 256)
        messages = self._create_auto_prompt_message(message)

        def request_one_openai(temp: float) -> str:
            config = create_config(
                prev={},
                messages=messages,
                max_tokens=max_tokens,
                temperature=temp,
                model=autoprompt_model,
            )
            ret = request_engine(config)
            return ret.choices[0].message.content.strip()

        def request_one_ollama(temp: float) -> str:
            response = ollama.chat(
                model=self.ollama_model_name,
                messages=messages,
                options={
                    "temperature": max(temp, 1e-2),
                    "num_predict": max_tokens,
                },
            )
            return response["message"]["content"].strip()

        if os.environ.get("DEEPSEEK_API_KEY") or os.environ.get("OPENAI_API_KEY"):
            request_one = request_one_openai
        elif getattr(self, "backend", None) == "ollama" and HAS_OLLAMA:
            request_one = request_one_ollama
        else:
            raise ValueError(
                "Auto-prompting requires DEEPSEEK_API_KEY/OPENAI_API_KEY, or an Ollama model backend. "
                "Otherwise use use_hand_written_prompt/no_input_prompt."
            )

        greedy_prompt = request_one(greedy_temperature)
        candidates = [request_one(candidate_temperature) for _ in range(candidate_count)]
        return greedy_prompt, candidates

    def auto_prompt(self, **kwargs) -> str:
        os.makedirs(self.folder + "/prompts", exist_ok=True)

        # if we have already done auto-prompting, just return the best prompt
        if os.path.exists(self.folder + "/prompts/best_prompt.txt"):
            self.m_logger.logo("Use existing prompt ... ", level=LEVEL.INFO)
            with open(
                self.folder + "/prompts/best_prompt.txt", "r", encoding="utf-8"
            ) as f:
                return f.read()
        if kwargs["no_input_prompt"]:
            self.m_logger.logo("Without any input prompt ... ", level=LEVEL.INFO)
            best_prompt = (
                f"{self.prompt_used['separator']}\n{self.prompt_used['begin']}"
            )
            self.m_logger.logo(
                "Prompt source: no_input_prompt separator/begin template.",
                level=LEVEL.INFO,
            )
        elif kwargs["hw"]:
            self.m_logger.logo("Use handwritten prompt ... ", level=LEVEL.INFO)
            best_prompt = self._build_handwritten_prompt(kwargs["hw_prompt"])
            self.m_logger.logo(
                "Prompt source: handwritten prompt with optional docs/examples.",
                level=LEVEL.INFO,
            )
        else:
            self.m_logger.logo("Use auto-prompting prompt ... ", level=LEVEL.INFO)
            if self.prompt_used["docstring"] is None:
                raise ValueError(
                    "Auto-prompting requires target.path_documentation to be set."
                )
            try:
                greedy_prompt, candidate_summaries = self._request_auto_prompt_candidates(
                    kwargs["message"]
                )
                scored_prompts = []

                greedy_wrapped = self.wrap_prompt(greedy_prompt)
                with open(
                    self.folder + "/prompts/greedy_prompt.txt", "w", encoding="utf-8"
                ) as f:
                    f.write(greedy_wrapped)
                greedy_score = self.validate_prompt(greedy_wrapped)
                scored_prompts.append((greedy_score, greedy_wrapped, "greedy_prompt"))

                for index, summary in enumerate(
                    track(candidate_summaries, description="Generating prompts")
                ):
                    wrapped_prompt = self.wrap_prompt(summary)
                    with open(
                        self.folder + f"/prompts/prompt_{index}.txt",
                        "w",
                        encoding="utf-8",
                    ) as f:
                        f.write(wrapped_prompt)
                    score = self.validate_prompt(wrapped_prompt)
                    scored_prompts.append((score, wrapped_prompt, f"prompt_{index}"))

                best_score, best_prompt, best_prompt_name = max(
                    scored_prompts, key=lambda item: item[0]
                )
                with open(
                    self.folder + "/prompts/scores.txt", "w", encoding="utf-8"
                ) as f:
                    for score, _, name in scored_prompts:
                        f.write(f"{name}\t{score}\n")
                    f.write(f"best_prompt\t{best_score}\n")
                self.m_logger.logo(
                    f"Prompt source: autoprompt selected {best_prompt_name} with score {best_score}.",
                    level=LEVEL.INFO,
                )
            except Exception as exc:
                self.m_logger.logo(
                    f"Auto-prompt request failed, fallback to documentation prompt: {exc}",
                    level=LEVEL.INFO,
                )
                best_prompt = self._build_handwritten_prompt()
                self.m_logger.logo(
                    "Prompt source: fallback documentation/examples prompt.",
                    level=LEVEL.INFO,
                )

        # dump best prompt
        with open(self.folder + "/prompts/best_prompt.txt", "w", encoding="utf-8") as f:
            f.write(best_prompt)

        return best_prompt

    def initialize(self):
        self.m_logger.logo(
            "Initializing ... this may take a while ...", level=LEVEL.INFO
        )
        self.m_logger.logo("Loading model ...", level=LEVEL.INFO)
        eos = [
            self.prompt_used["separator"],
            "<eom>",  # for codegen2
            self.se_prompt,
            self.m_prompt,
            self.c_prompt,
        ]
        if hasattr(self, "config_dict"):
            llm = self.config_dict["llm"]
            model_name = llm["model_name"]
            additional_eos = llm.get("additional_eos", [])
            if additional_eos:
                eos = eos + additional_eos
        else:
            model_name = self.model_name

        if self.special_eos is not None:
            eos = eos + [self.special_eos]

        if HAS_OLLAMA and is_ollama_model(model_name):
            self.backend = "ollama"
            self.ollama_model_name = get_ollama_model_name(model_name)
            self.model = None
            self.m_logger.logo(
                f"Ollama model selected: {self.ollama_model_name}", level=LEVEL.INFO
            )
        else:
            self.backend = "huggingface"
            self.model = make_model(
                eos=eos,
                model_name=model_name,
                device=self.device,
                max_length=self.max_length,
            )
            self.m_logger.logo("HuggingFace model loaded", level=LEVEL.INFO)

        self.initial_prompt = self.auto_prompt(
            message=self.prompt_used["docstring"],
            hw_prompt=self.prompt_used["hw_prompt"] if self.hw else None,
            hw=self.hw,
            no_input_prompt=self.no_input_prompt,
        )
        self.prompt = self.initial_prompt
        self.m_logger.logo(
            f"Initial prompt prepared ({len(self.initial_prompt)} chars).",
            level=LEVEL.INFO,
        )
        self.m_logger.logo("Done", level=LEVEL.INFO)

    def generate_model(self) -> List[str]:
        self.g_logger.logo(self.prompt, level=LEVEL.VERBOSE)
        return self._generate_with_prompt(
            self.prompt,
            batch_size=self.batch_size,
            temperature=self.temperature,
            max_length=1024,
        )

    def generate(self, **kwargs) -> Union[List[str], bool]:
        try:
            fos = self.generate_model()
        except RuntimeError:
            # catch cuda out of memory error.
            self.m_logger.logo("cuda out of memory...", level=LEVEL.INFO)
            del self.model
            torch.cuda.empty_cache()
            return False
        new_fos = []
        for fo in fos:
            self.g_logger.logo("========== sample =========", level=LEVEL.VERBOSE)
            new_fos.append(self.clean(self.prompt_used["begin"] + "\n" + fo))
            self.g_logger.logo(
                self.clean(self.prompt_used["begin"] + "\n" + fo), level=LEVEL.VERBOSE
            )
            self.g_logger.logo("========== sample =========", level=LEVEL.VERBOSE)
        return new_fos

    # helper for updating
    def filter(self, code: str) -> bool:
        raise NotImplementedError

    # difference between clean and clean_code (honestly just backwards compatibility)
    # but the point is that clean should be applied as soon as generation whereas clean code is used
    # more so for filtering
    def clean(self, code: str) -> str:
        raise NotImplementedError

    def clean_code(self, code: str) -> str:
        raise NotImplementedError

    def update_strategy(self, new_code: str) -> str:
        while 1:
            strategy = random.randint(0, self.p_strategy)
            # generate new code using separator
            if strategy == 0:
                return f"\n{new_code}\n{self.prompt_used['separator']}\n"
            # mutate existing code
            elif strategy == 1:
                return f"\n{new_code}\n{self.m_prompt}\n"
            # semantically equivalent code generation
            elif strategy == 2:
                return f"\n{new_code}\n{self.se_prompt}\n"
            # combine previous two code generations
            else:
                if self.prev_example is not None:
                    return f"\n{self.prev_example}\n{self.prompt_used['separator']}\n{self.prompt_used['begin']}\n{new_code}\n{self.c_prompt}\n"

    # update
    def update(self, **kwargs):
        new_code = ""
        feedback_items = []
        for result, code in kwargs["prev"]:
            if (
                result == FResult.SAFE
                and self.filter(code)
                and self.clean_code(code) != self.prev_example
            ):
                new_code = self.clean_code(code)
        for result, message, _ in kwargs.get("feedback", []):
            if result in (FResult.FAILURE, FResult.ERROR, FResult.TIMED_OUT):
                summary = self._sanitize_feedback(message)
                if summary != "":
                    feedback_items.append(summary)
        if feedback_items:
            self.feedback_history.extend(feedback_items)
            self.feedback_history = self.feedback_history[-3:]
        if new_code != "" and self.p_strategy != -1:
            self.prompt = self._create_feedback_prompt(
                new_code, self.feedback_history[-3:]
            )
            self.prev_example = new_code
            self.m_logger.logo(
                "Prompt updated from a SAFE sample"
                f" (feedback items kept: {len(self.feedback_history[-3:])}).",
                level=LEVEL.INFO,
            )
        elif self.feedback_history and self.p_strategy != -1:
            self.prompt = self._create_feedback_only_prompt(
                self.feedback_history[-3:]
            )
            self.m_logger.logo(
                "Prompt updated from compiler feedback only"
                f" (feedback items kept: {len(self.feedback_history[-3:])}).",
                level=LEVEL.INFO,
            )
        else:
            self.m_logger.logo(
                "Prompt unchanged: no SAFE sample and no new compiler feedback.",
                level=LEVEL.INFO,
            )

    # validation
    def validate_individual(self, filename) -> (FResult, str):
        raise NotImplementedError

    def parse_validation_message(self, f_result, message, file_name):
        # TODO: rewrite to include only status in TRACE but full message in VERBOSE
        self.v_logger.logo("Validating {} ...".format(file_name), LEVEL.TRACE)
        if f_result == FResult.SAFE:
            self.v_logger.logo("{} is safe".format(file_name), LEVEL.VERBOSE)
        elif f_result == FResult.FAILURE:
            self.v_logger.logo(
                "{} failed validation with error message: {}".format(
                    file_name, message, LEVEL.VERBOSE
                )
            )
        elif f_result == FResult.ERROR:
            self.v_logger.logo(
                "{} has potential error!\nerror message:\n{}".format(
                    file_name, message, LEVEL.VERBOSE
                )
            )
            self.m_logger.logo(
                "{} has potential error!".format(file_name, message, LEVEL.INFO)
            )
        elif f_result == FResult.TIMED_OUT:
            self.v_logger.logo("{} timed out".format(file_name), LEVEL.VERBOSE)

    def validate_all(self):
        for fuzz_output in track(
            glob.glob(self.folder + "/*.fuzz"),
            description="Validating",
        ):
            f_result, message = self.validate_individual(fuzz_output)
            self.parse_validation_message(f_result, message, fuzz_output)
