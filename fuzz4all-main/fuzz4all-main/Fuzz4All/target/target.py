import glob
import json
import os
import random
import re
import time
from enum import Enum
from typing import Any, Dict, List, Tuple, Union

import torch
from rich.progress import track

from Fuzz4All.mutation import JavaMutator, load_mutation_profile
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
        self.AP_SYSTEM_MESSAGE = (
            "You are an auto-prompting tool. Your job is to write concise plain-English instructions "
            "for a Java code-generation model. "
            "STRICT FORMAT RULES — violating any rule causes your output to be discarded:\n"
            "1. Write 2-4 sentences of plain English ONLY.\n"
            "2. NEVER write Java, Python, or any other source code.\n"
            "3. NEVER use markdown code fences (``` or `).\n"
            "4. NEVER include import statements, class definitions, or method bodies.\n"
            "5. NEVER use more than 4 numbered list items.\n"
            "6. NEVER use comment delimiters (/* or */).\n"
            "Output ONLY a plain-English paragraph. No preamble, no explanation, no code."
        )
        self.AP_INSTRUCTION = (
            "Summarize the documentation into a concise fuzzing prompt (2-4 sentences, plain English only). "
            "Specify: which constructors or factory methods to call, what edge-case argument values to use "
            "(e.g. null, 0, -1, empty arrays, boundary sizes), and what exception handling is needed. "
            "Do NOT write any code, use code fences (```), or include import or class statements. "
            "Output ONLY a plain-English paragraph. "
            "CORRECT FORMAT EXAMPLE: "
            "\"Construct the API object with valid and boundary-size arguments. "
            "Call the primary read or write methods with sizes 0, 1, and 8192. "
            "Wrap all calls in try { ... } catch (Exception e) { e.printStackTrace(); }.\""
        )
        # prompt based variables
        self.hw = kwargs["use_hw"]
        self.no_input_prompt = kwargs["no_input_prompt"]
        self.prompt_used = None
        self.prompt = None
        self.initial_prompt = None
        self.base_prompt = None
        self.runtime_prompt = None
        self.prev_example = None
        self.feedback_history = []
        self.safe_examples = []
        self.failure_rules = []
        self.failure_rule_counts = {}
        self.batch_feedback_window = []
        self.update_round = 0
        self.prompt_refresh_interval = kwargs.get("prompt_refresh_interval", 5)
        self.max_feedback_rules = kwargs.get("max_feedback_rules", 5)
        self.max_safe_examples = kwargs.get("max_safe_examples", 2)
        self.base_prompt_score = None
        self.last_refresh_round = 0
        self.last_refresh_rule_signature = None
        self.previous_failure_rule_signature = None
        self.stale_feedback_rounds = 0
        self.enable_mutation = False
        self.mutation_budget_per_seed = 0
        self.mutation_profile = None
        self.mutator = None
        self.pending_sample_records = []
        self.sample_records_by_file = {}
        self.mutation_stats = {}
        self.last_mutation_summary = []
        self.manifest_path = os.path.join(self.folder, "mutation_manifest.jsonl")
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

    def _compact_reference_notes(
        self, text: str, max_chars: int = 1600, max_lines: int = 18
    ) -> str:
        text = (text or "").strip()
        if text == "":
            return ""
        cleaned_lines = []
        total_chars = 0
        for raw_line in text.splitlines():
            line = raw_line.strip()
            if not line or line.startswith("```"):
                continue
            if line in {"/*", "*/"}:
                continue
            if total_chars + len(line) > max_chars:
                break
            cleaned_lines.append(line)
            total_chars += len(line) + 1
            if len(cleaned_lines) >= max_lines:
                break
        return "\n".join(cleaned_lines).strip()

    def _summarize_prompt_issues(self, prompt: str) -> List[str]:
        issues = []
        text = prompt or ""
        lowered = text.lower()

        if "```" in text:
            issues.append("contains fenced code block")
        if re.search(r"^\s*import\s+java\.", text, re.MULTILINE):
            issues.append("looks like Java source with imports")
        if re.search(r"\bpublic\s+class\b", text):
            issues.append("looks like full Java class")
        if re.search(r"\bpublic\s+static\s+void\s+main\b", text):
            issues.append("looks like executable Java sample")

        if "non-existent" in lowered or "nonexistent" in lowered:
            issues.append("encourages nonexistent APIs")
        if "does not exist" in lowered:
            issues.append("encourages invalid API exploration")
        if "getnonexistent" in lowered:
            issues.append("contains fabricated method examples")

        numbered_lines = len(re.findall(r"^\s*\d+\.\s", text, re.MULTILINE))
        if numbered_lines >= 5:
            issues.append("looks like long numbered fuzz checklist")

        if text.count("/*") >= 2 or text.count("*/") >= 2:
            issues.append("contains nested comment-style prompt blocks")

        if len(text) > 1800:
            issues.append("prompt too long")

        return issues

    def _reject_prompt_candidate(self, prompt: str) -> bool:
        issues = self._summarize_prompt_issues(prompt)
        severe = {
            "contains fenced code block",
            "looks like Java source with imports",
            "looks like full Java class",
            "looks like executable Java sample",
            "encourages nonexistent APIs",
            "contains fabricated method examples",
            "contains nested comment-style prompt blocks",
        }
        return any(issue in severe for issue in issues)

    def _extract_prompt_inner_text(self, wrapped: str) -> str:
        """Strip the /* ... */ comment wrapper from a wrapped prompt for guard re-validation."""
        text = (wrapped or "").strip()
        if text.startswith("/*"):
            end = text.find("*/")
            if end != -1:
                return text[2:end].strip()
        return text

    def _try_sanitize_prompt_candidate(self, raw: str) -> str:
        """
        Attempt to salvage a fenced-code LLM response before hard guard rejection.
        If the raw text is a single code fence wrapping plain prose, extract the prose.
        Returns the (possibly cleaned) text; the guard still runs afterward.
        """
        text = (raw or "").strip()
        # Strip a single code-fence wrapper: ```lang\ncontent\n```
        fence_re = re.compile(r"^```[a-zA-Z]*\n([\s\S]*?)\n?```\s*$", re.DOTALL)
        m = fence_re.match(text)
        if m:
            inner = m.group(1).strip()
            # Only salvage if inner text is plain prose — no code signatures
            has_code = re.search(
                r"^\s*(def |class |import |public |private |void |```)",
                inner,
                re.MULTILINE,
            )
            if inner and not has_code and "```" not in inner:
                return inner
        # Strip stray leading/trailing fence markers (no full block)
        text = re.sub(r"^```[a-zA-Z]*\s*\n?", "", text)
        text = re.sub(r"\n?```\s*$", "", text)
        return text.strip()

    def _record_rejected_prompt_candidate(
        self, name: str, prompt: str, issues: List[str], stage: str
    ) -> None:
        prompt_dir = os.path.join(self.folder, "prompts")
        os.makedirs(prompt_dir, exist_ok=True)
        with open(
            os.path.join(prompt_dir, f"rejected_{stage}_{name}.txt"),
            "w",
            encoding="utf-8",
        ) as f:
            f.write(prompt or "")
        with open(
            os.path.join(prompt_dir, f"rejected_{stage}_{name}_reason.txt"),
            "w",
            encoding="utf-8",
        ) as f:
            for issue in issues:
                f.write(issue + "\n")

    def summarize_feedback_message(self, result: FResult, message: str) -> List[str]:
        summary = self._sanitize_feedback(message)
        return [summary] if summary else []

    def _build_handwritten_prompt(
        self,
        manual_prompt: str = None,
        include_docstring: bool = True,
        compact_docstring: bool = True,
    ) -> str:
        parts = []
        if manual_prompt:
            parts.append(manual_prompt.strip())
        if self.prompt_used.get("example_code"):
            parts.append(
                "Use the following example style and structural patterns as guidance:\n"
                f"```{self.language}\n{self.prompt_used['example_code'].strip()}\n```"
            )
        if include_docstring and self.prompt_used.get("docstring"):
            doc_notes = self.prompt_used["docstring"].strip()
            if compact_docstring:
                doc_notes = self._compact_reference_notes(doc_notes)
            if doc_notes:
                parts.append(
                    "Use the following reference notes about the target language or feature:\n"
                    f"{doc_notes}"
                )
        if len(parts) == 0:
            return f"{self.prompt_used['separator']}\n{self.prompt_used['begin']}"
        return self.wrap_prompt("\n\n".join(parts))

    # Domain-level hints for the minimal recovery prompt, keyed by primary_tag.
    # Each hint names the characteristic entry-point pattern for that classification
    # domain so the generated code still exercises meaningful state transitions, not
    # just the most trivial usage.  No individual API class names are hard-coded.
    _MINIMAL_RECOVERY_DOMAIN_HINTS: Dict[str, str] = {
        # Security APIs: factory → key-material → operation → result.
        # Cover algorithm-string boundary (valid name, wrong size, unknown provider).
        "SECURITY": (
            "Use the static getInstance(algorithmString) factory to obtain the API object. "
            "Provide a fixed key or IV with a standard size (e.g. 16 bytes for AES). "
            "Call the primary operation method (init / update / doFinal or equivalent) "
            "and print the result length. "
            "Also try at least one boundary value: an empty input, a null argument, "
            "or an algorithm string that is valid but uncommon (e.g. \"AES/CBC/PKCS5Padding\"). "
            "Wrap ALL calls in try { ... } catch (Exception e) { e.printStackTrace(); }."
        ),
        # Concurrent APIs: construction → lifecycle state changes → blocking coordination.
        # Cover constructor arity, start/join/sleep boundary, interrupted-exception path.
        "CONCURRENT": (
            "Construct the API object using its documented constructor with exact parameter types. "
            "Drive it through at least two lifecycle states "
            "(e.g. created → started → finished, or submitted → done). "
            "Include one blocking or waiting call (sleep, join, await, or equivalent) "
            "and one state-query call (isAlive, isDone, getState, or equivalent). "
            "Wrap blocking calls in "
            "try { ... } catch (InterruptedException e) { e.printStackTrace(); }."
        ),
        # Reflection APIs: class-resolution → member-lookup → accessibility → invocation.
        # Cover getDeclaredMethod/Field chain on a known JDK type.
        "REFLECT": (
            "Use Class.forName() or a .class literal to resolve a well-known JDK class. "
            "Look up at least one method via getDeclaredMethod and one field via getDeclaredField. "
            "Call setAccessible(true), then invoke the method or read the field. "
            "Also test one boundary: a method name that exists and one that does not. "
            "Wrap ALL reflective calls in try { ... } catch (Exception e) { e.printStackTrace(); }."
        ),
        # JVM management APIs: static MXBean accessors → documented query methods.
        # The standard entry points are the getXxxMXBean() factory methods — retain them.
        "JVM_MGMT": (
            "Obtain at least two MXBean instances using the standard static accessor methods "
            "(such as getMemoryMXBean, getThreadMXBean, getRuntimeMXBean, "
            "getClassLoadingMXBean, or getCompilationMXBean). "
            "Call one documented query getter on each "
            "(e.g. getHeapMemoryUsage, getThreadCount, getUptime, getLoadedClassCount). "
            "Print the results. "
            "Wrap ALL calls in try { ... } catch (Exception e) { e.printStackTrace(); }."
        ),
        # Network APIs: endpoint creation → connect/bind state → I/O or query.
        # Cover localhost address, timeout boundary, connection state query.
        "NETWORK": (
            "Create a network endpoint using a localhost address or a fixed URI/URL literal. "
            "Perform at least one state-changing call "
            "(connect, bind, open, or equivalent) "
            "and one query call (isConnected, getPort, getScheme, getHost, or equivalent). "
            "Also test one boundary: a zero timeout, an empty path, or a port at 0 or 65535. "
            "Wrap ALL network calls in try { ... } catch (Exception e) { e.printStackTrace(); }."
        ),
        # File/path APIs: path construction → existence/state probe → content operation.
        # Cover relative path, non-existent file, and a simple read or write.
        "FILE": (
            "Construct a path using a fixed relative string literal (e.g. \"test.txt\"). "
            "Probe its state with at least two query methods "
            "(exists, isDirectory, length, lastModified, or equivalent). "
            "Perform one content operation (read, write, list, or createTempFile). "
            "Also test one boundary path: an empty string, a deeply nested path, "
            "or a path with special characters. "
            "Wrap file operations in try { ... } catch (Exception e) { e.printStackTrace(); }."
        ),
        # Time APIs: factory construction → arithmetic → boundary query.
        # Cover epoch-adjacent values, sign boundary, and overflow-safe arithmetic.
        "TIME": (
            "Construct at least two time objects using static factory methods "
            "(e.g. ofSeconds, ofMinutes, parse, now, or equivalent) "
            "with fixed numeric literals. "
            "Chain one arithmetic operation (plus, minus, multipliedBy, or equivalent) "
            "and call at least two boundary-query methods "
            "(isNegative, isZero, compareTo, toMillis, or equivalent). "
            "Include one epoch-adjacent value (0, Long.MIN_VALUE / Long.MAX_VALUE, "
            "or a very large positive/negative literal). "
            "Avoid arithmetic chains that overflow; check results with query methods."
        ),
        # Callback/listener APIs: source creation → listener registration → event dispatch
        # → listener removal. Cover duplicate registration and null-event edge cases.
        "CALLBACK": (
            "Create the event-source object. "
            "Register one listener implemented as an anonymous class that prints the event. "
            "Fire at least one event to confirm the listener is called. "
            "Then remove the listener and fire a second event to confirm it is no longer called. "
            "Also register the same listener twice to test duplicate-registration behaviour. "
            "Keep all code inside the main method; do not introduce extra classes."
        ),
        # Resource/stream APIs: open (try-with-resources) → read/write → boundary sizes.
        # Cover zero-length, single-byte, and bulk transfer edge cases.
        "RESOURCE": (
            "Open the resource inside a try-with-resources block. "
            "Perform three read or write calls with different sizes: "
            "zero bytes, one byte, and a 16-byte array. "
            "If the resource supports mark/reset, call mark(16), read some bytes, "
            "then reset() and verify the position. "
            "Check available() or remaining() before and after each operation. "
            "Wrap any checked exception in try { ... } catch (Exception e) { e.printStackTrace(); }."
        ),
        # Buffer/byte-buffer APIs: allocation → put/get operations → limit/position boundary.
        # Cover zero-capacity, flip, rewind, and compact sequences.
        "BUFFER": (
            "Allocate the buffer with several capacities: 0, 1, and 64 bytes. "
            "Put at least one byte or value, then call flip() before reading. "
            "Test get() at position 0 and at the limit, and call rewind() between sequences. "
            "Also try compact() to verify the unfilled-region semantics. "
            "Wrap ALL calls in try { ... } catch (Exception e) { e.printStackTrace(); }."
        ),
        # Batch-operation APIs: bulk read/write → count boundaries → partial-transfer detection.
        # Cover empty arrays, large arrays, and offset-within-array edge cases.
        "BATCH_OP": (
            "Call the bulk read or write method with arrays of size 0, 1, and 1024. "
            "Use non-zero offsets and lengths that reach the end of the array and one byte past it. "
            "Check the return value (bytes transferred) after each call. "
            "Wrap all operations in try { ... } catch (Exception e) { e.printStackTrace(); }."
        ),
        # Mark/reset APIs: mark → read → reset → verify re-read of same bytes.
        # Cover mark limit, markSupported() guard, and reset-without-mark error path.
        "MARK_SUPPORT": (
            "Call markSupported() first; if true, call mark(8), read 4 bytes, then reset(). "
            "Verify the same bytes can be read again. "
            "Also test reset() before any mark() to confirm an IOException is thrown. "
            "Wrap all stream operations in try { ... } catch (Exception e) { e.printStackTrace(); }."
        ),
        # Utility/helper APIs: static parse or format method → value extraction → comparison.
        # Cover null input, empty string, and out-of-range numeric edge cases.
        "UTILITY": (
            "Call the primary static parse or factory method with a valid input and print the result. "
            "Also call it with an empty string, null (inside a try block), "
            "and a value at numeric boundary (Long.MAX_VALUE, -1, or 0). "
            "Call at least one comparison or equality method on the returned objects. "
            "Wrap all calls in try { ... } catch (Exception e) { e.printStackTrace(); }."
        ),
    }

    def _build_minimal_recovery_prompt(self) -> str:
        target_api = self.prompt_used.get("target_api") or "the target API"
        primary_tag = (self.mutation_profile or {}).get("primary_tag", "")
        domain_hint = self._MINIMAL_RECOVERY_DOMAIN_HINTS.get(primary_tag, "")
        base = (
            f"Write the simplest possible {self.language} program that uses {target_api}. "
            "Use only 1-2 documented public API calls. "
            "Keep all helper objects local to the main method. "
            "Use only standard public library types. "
            "Avoid helper classes, wrappers, and guessed method names."
        )
        if domain_hint:
            instruction = f"{base} {domain_hint}"
        else:
            instruction = (
                f"{base} "
                "If checked exceptions may be thrown, wrap the API calls in "
                "try { ... } catch (Exception e) { e.printStackTrace(); }."
            )
        return self._build_handwritten_prompt(
            manual_prompt=instruction,
            include_docstring=False,
        )

    def _reset_to_minimal_prompt(self, reason: str) -> None:
        self.base_prompt = self._build_minimal_recovery_prompt()
        self.runtime_prompt = self.base_prompt
        self.prompt = self.runtime_prompt
        self.base_prompt_score = None
        self.last_refresh_rule_signature = None
        self.stale_feedback_rounds = 0
        prompt_dir = os.path.join(self.folder, "prompts")
        os.makedirs(prompt_dir, exist_ok=True)
        with open(
            os.path.join(prompt_dir, f"minimal_reset_round_{self.update_round}.txt"),
            "w",
            encoding="utf-8",
        ) as f:
            f.write(self.base_prompt)
        self._write_refresh_status(
            self.update_round,
            "reset",
            reason,
        )
        self.m_logger.logo(
            f"Prompt reset to minimal recovery template: {reason}",
            level=LEVEL.INFO,
        )

    def write_back_file(self, code: str):
        raise NotImplementedError

    # each target defines their way of validating prompts (can overwrite)
    def validate_prompt(self, prompt: str):
        llm_config = getattr(self, "config_dict", {}).get("llm", {})
        eval_batch_size = llm_config.get(
            "autoprompt_validation_batch_size", self.batch_size
        )
        eval_max_length = llm_config.get(
            "autoprompt_validation_max_length", self.max_length
        )
        fos = self._generate_with_prompt(
            prompt,
            batch_size=eval_batch_size,
            temperature=self.temperature,
            max_length=eval_max_length,
        )
        return self._score_generated_samples(fos)

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
            "Do not explain the documentation. "
            "Output ONLY a plain-English paragraph — no code, no code fences (```), "
            "no import statements, no comment delimiters (/* */)."
        )
        return create_chatgpt_docstring_template(
            system_message=self.AP_SYSTEM_MESSAGE,
            user_message=instruction,
            docstring=message,
            example=self.prompt_used.get("example_code") or "",
            first="",
        )

    def _create_prompt_refresh_message(self, summary: str) -> List[dict]:
        target_api = self.prompt_used.get("target_api") or "the target language feature"
        instruction = (
            "Please rewrite the fuzzing prompt so that a code model generates programs "
            f"for {target_api} that are more likely to compile successfully. "
            "Incorporate the observed successful patterns, and explicitly avoid the repeated compiler mistakes. "
            "Do not explain the analysis. "
            "IMPORTANT FORMAT RULES: output ONLY a plain-English paragraph (2-4 sentences). "
            "Do NOT write any Java code, use code fences (```), numbered lists with more than 4 items, "
            "import statements, class definitions, or comment delimiters (/* */)."
        )
        return create_chatgpt_docstring_template(
            system_message=self.AP_SYSTEM_MESSAGE,
            user_message=instruction,
            docstring=self.prompt_used.get("docstring") or "",
            example=summary,
            first="",
        )

    def _request_constrained_autoprompt(self, docstring: str) -> Union[str, None]:
        """
        Last-resort constrained single attempt with an ultra-simple format request.
        Uses low temperature and an explicit one-sentence target to bypass LLM
        tendencies to produce code-fenced or code-contaminated outputs.
        """
        target_api = self.prompt_used.get("target_api") or "the target API"
        instruction = (
            f"Write ONE to THREE plain-English sentences for a code-generation model "
            f"explaining how to use {target_api}. "
            "Mention specific method names, boundary argument values, and exception handling. "
            "Do NOT write any code, use backticks, or use markdown. "
            "Start with: 'Write a Java program that ...'"
        )
        messages = [
            {
                "role": "system",
                "content": (
                    "You write ultra-concise plain-English prompts for Java code generation. "
                    "You NEVER write code or use markdown. Output only the prompt sentence(s)."
                ),
            },
            {"role": "user", "content": instruction},
        ]
        try:
            llm_config = getattr(self, "config_dict", {}).get("llm", {})
            model_name = llm_config.get("autoprompt_model", "deepseek-chat")
            max_tokens = min(llm_config.get("autoprompt_max_tokens", 256), 200)
            greedy, _ = self._request_prompt_candidates_from_messages(
                messages=messages,
                model_name=model_name,
                candidate_count=0,
                greedy_temperature=0.1,
                candidate_temperature=0.5,
                max_tokens=max_tokens,
            )
            return greedy
        except Exception as exc:
            self.m_logger.logo(
                f"Constrained autoprompt request failed: {exc}", level=LEVEL.INFO
            )
            return None

    def _create_feedback_prompt(
        self, safe_examples: List[str], failure_rules: List[str]
    ) -> str:
        prompt_parts = [self.base_prompt or self.initial_prompt or ""]

        if failure_rules:
            rules_block = "\n".join([f"- {rule}" for rule in failure_rules])
            prompt_parts.append(
                self.wrap_in_comment(
                    "Avoid these known compiler mistakes:\n" + rules_block
                )
            )

        if safe_examples:
            examples = []
            for index, example in enumerate(safe_examples, start=1):
                examples.append(
                    f"Example {index}:\n```{self.language}\n{example}\n```"
                )
            prompt_parts.append(
                self.wrap_in_comment(
                    "Recent valid examples to imitate structurally:\n"
                    + "\n\n".join(examples)
                )
            )

        prompt_parts.append(self.prompt_used["separator"])
        prompt_parts.append(self.prompt_used["begin"])
        return "\n".join([part for part in prompt_parts if part != ""]) + "\n"

    def select_safe_examples(self, prev: List[Tuple[FResult, str]]) -> List[str]:
        examples = []
        for result, code in prev:
            if result == FResult.SAFE and self.filter(code):
                cleaned = self.clean_code(code)
                if cleaned and cleaned not in examples:
                    examples.append(cleaned)
        return examples[: self.max_safe_examples]

    def _merge_failure_rules(self, rules: List[str]) -> List[str]:
        for rule in rules:
            if not rule:
                continue
            self.failure_rule_counts[rule] = self.failure_rule_counts.get(rule, 0) + 1
        sorted_rules = sorted(
            self.failure_rule_counts.items(), key=lambda item: (-item[1], item[0])
        )
        self.failure_rules = [
            rule for rule, _ in sorted_rules[: self.max_feedback_rules]
        ]
        return self.failure_rules

    def _dump_runtime_prompt_snapshot(self):
        prompt_dir = os.path.join(self.folder, "prompts")
        os.makedirs(prompt_dir, exist_ok=True)
        round_id = self.update_round
        with open(
            os.path.join(prompt_dir, f"runtime_prompt_{round_id}.txt"),
            "w",
            encoding="utf-8",
        ) as f:
            f.write(self.runtime_prompt or self.prompt or "")
        with open(
            os.path.join(prompt_dir, f"runtime_rules_{round_id}.txt"),
            "w",
            encoding="utf-8",
        ) as f:
            for rule in self.failure_rules:
                f.write(rule + "\n")

    def _write_refresh_status(self, round_id: int, status: str, reason: str) -> None:
        prompt_dir = os.path.join(self.folder, "prompts")
        os.makedirs(prompt_dir, exist_ok=True)
        with open(
            os.path.join(prompt_dir, f"refresh_status_round_{round_id}.txt"),
            "w",
            encoding="utf-8",
        ) as f:
            f.write(f"status={status}\nreason={reason}\n")

    def _init_mutation_components(self):
        config_dict = getattr(self, "config_dict", {})
        target_cfg = config_dict.get("target", {})
        self.enable_mutation = bool(target_cfg.get("enable_mutation", False))
        self.mutation_budget_per_seed = int(target_cfg.get("mutation_budget_per_seed", 0))
        self.mutation_profile = None
        self.mutator = None
        if not self.enable_mutation or self.language != "java":
            return

        self.mutation_profile = load_mutation_profile(config_dict)
        if target_cfg.get("mutation_operator_topk"):
            topk = int(target_cfg["mutation_operator_topk"])
            self.mutation_profile["priority_operators"] = self.mutation_profile.get(
                "priority_operators", []
            )[:topk]
        self.mutator = JavaMutator(self.mutation_profile)

    def _make_sample_metadata(
        self,
        source_type: str,
        operator: str,
        parent_index: int = None,
        mutation_profile: str = None,
    ) -> Dict[str, Any]:
        return {
            "source_type": source_type,
            "operator": operator,
            "parent_index": parent_index,
            "target_api": self.prompt_used.get("target_api", ""),
            "mutation_profile": mutation_profile
            or (self.mutation_profile or {}).get("mutation_profile"),
            "primary_tag": (self.mutation_profile or {}).get("primary_tag"),
            "all_tags": (self.mutation_profile or {}).get("all_tags", []),
            "active_profiles": (self.mutation_profile or {}).get("active_profiles", []),
        }

    def _collect_mutated_samples(self, code: str, parent_index: int) -> List[Tuple[str, Dict[str, Any]]]:
        if not self.enable_mutation or self.mutator is None or self.mutation_budget_per_seed <= 0:
            return []
        if not self._is_viable_mutation_seed(code):
            return []

        mutated = []
        for item in self.mutator.generate_mutations(
            code,
            budget=self.mutation_budget_per_seed,
            operator_offset=self.update_round + parent_index,
        ):
            metadata = self._make_sample_metadata(
                source_type="mutated",
                operator=item["operator"],
                parent_index=parent_index,
                mutation_profile=item.get("profile"),
            )
            prepared = self._prepare_generated_code(item["code"])
            if prepared is None:
                continue
            mutated.append((prepared, metadata))
        return mutated

    def _rewrite_numeric_byte_literals(self, text: str) -> str:
        def rewrite_csv_literals(body: str) -> str:
            parts = [part.strip() for part in body.split(",")]
            rewritten = []
            for part in parts:
                if re.fullmatch(r"-?\d+", part):
                    value = int(part)
                    if value < -128 or value > 127:
                        rewritten.append(f"(byte) {part}")
                    else:
                        rewritten.append(part)
                else:
                    rewritten.append(part)
            return ", ".join(rewritten)

        patterns = [
            re.compile(r"(new\s+byte\[\]\s*\{)([^{}]*)(\})"),
            re.compile(r"(byte\[\]\s+[A-Za-z_][A-Za-z0-9_]*\s*=\s*\{)([^{}]*)(\})"),
        ]

        rewritten = text
        for pattern in patterns:
            rewritten = pattern.sub(
                lambda m: f"{m.group(1)}{rewrite_csv_literals(m.group(2))}{m.group(3)}",
                rewritten,
            )

        return re.sub(
            r"(\bbyte\s+[A-Za-z_][A-Za-z0-9_]*\s*=\s*)(-?\d+)(\s*;)",
            lambda m: (
                f"{m.group(1)}(byte) {m.group(2)}{m.group(3)}"
                if int(m.group(2)) < -128 or int(m.group(2)) > 127
                else m.group(0)
            ),
            rewritten,
        )

    def _ensure_java_import(self, code: str, import_line: str) -> str:
        import_name = import_line.replace("import ", "").replace(";", "")
        class_name = import_name.split(".")[-1]
        if f"import {import_name};" in code:
            return code
        if not re.search(rf"\b{re.escape(class_name)}\b", code):
            return code

        lines = code.splitlines()
        insert_at = 0
        for index, line in enumerate(lines):
            if line.startswith("import "):
                insert_at = index + 1
        lines.insert(insert_at, f"import {import_name};")
        return "\n".join(lines)

    def _profile_repair_java_code(self, code: str) -> str:
        repaired = code
        repair_rules = (self.mutation_profile or {}).get("repair_rules", {})
        if repair_rules.get("byte_literal_cast"):
            repaired = self._rewrite_numeric_byte_literals(repaired)
        for import_line in repair_rules.get("imports", []):
            repaired = self._ensure_java_import(repaired, import_line)
        return repaired

    def _repair_java_code(self, code: str) -> str:
        repaired = code
        repaired = self._profile_repair_java_code(repaired)
        repaired = self._dedup_java_imports(repaired)
        return repaired

    def _dedup_java_imports(self, code: str) -> str:
        seen: set = set()
        deduped: list = []
        for line in code.split("\n"):
            if line.strip().startswith("import "):
                if line.strip() in seen:
                    continue
                seen.add(line.strip())
            deduped.append(line)
        return "\n".join(deduped)

    def _profile_rejects_generated_code(self, normalized: str) -> bool:
        filter_rules = (self.mutation_profile or {}).get("filter_rules", {})
        if any(
            token in normalized for token in filter_rules.get("reject_tokens", [])
        ):
            return True
        for pattern in filter_rules.get("reject_patterns", []):
            if re.search(pattern, normalized):
                return True
        return False

    def _is_viable_generated_code(self, code: str) -> bool:
        normalized = " ".join((code or "").split())
        if normalized.count("{") != normalized.count("}"):
            return False
        return True

    def _prepare_generated_code(self, code: str) -> Union[str, None]:
        prepared = self.clean(code)
        if self.language == "java":
            prepared = self._repair_java_code(prepared)
            if not self._is_viable_generated_code(prepared):
                return None
        return prepared

    def _is_viable_mutation_seed(self, code: str) -> bool:
        if self.language != "java":
            return True

        normalized = " ".join((code or "").split())
        if not self._is_viable_generated_code(code):
            return False

        suspicious_bare_calls = [
            " write(new FileOutputStream(",
            " write(new ByteArrayOutputStream(",
            " write(System.out,",
            " write(null,",
        ]
        if any(token in normalized for token in suspicious_bare_calls):
            return False

        return True

    def consume_last_generation_metadata(self) -> List[Dict[str, Any]]:
        metadata = list(self.pending_sample_records)
        self.pending_sample_records = []
        return metadata

    def register_sample_output(self, file_name: str, metadata: Dict[str, Any] = None):
        if metadata is None:
            if not self.pending_sample_records:
                metadata = self._make_sample_metadata("generated", "llm_seed")
            else:
                metadata = self.pending_sample_records.pop(0)
        metadata["file_name"] = file_name
        self.sample_records_by_file[file_name] = metadata

    def _update_mutation_stats(self, metadata: Dict[str, Any], result: Union["FResult", None]):
        operator = metadata.get("operator", "unknown")
        stats = self.mutation_stats.setdefault(
            operator,
            {"generated": 0, "safe": 0, "failure": 0, "error": 0, "timed_out": 0},
        )
        stats["generated"] += 1
        if result is None:
            return
        if result == FResult.SAFE:
            stats["safe"] += 1
        elif result == FResult.FAILURE:
            stats["failure"] += 1
        elif result == FResult.ERROR:
            stats["error"] += 1
        elif result == FResult.TIMED_OUT:
            stats["timed_out"] += 1

    def record_sample_result(
        self,
        file_name: str,
        result: Union["FResult", None],
        message: str = "",
    ):
        metadata = self.sample_records_by_file.pop(file_name, None)
        if metadata is None:
            metadata = self._make_sample_metadata("generated", "llm_seed")
            metadata["file_name"] = file_name

        metadata["compile_result"] = result.name if result is not None else "UNKNOWN"
        metadata["feedback_summary"] = self.summarize_feedback_message(result, message) if result is not None else []
        metadata["sanitized_message"] = self._sanitize_feedback(message, limit=240)
        self._update_mutation_stats(metadata, result)

        os.makedirs(self.folder, exist_ok=True)
        with open(self.manifest_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(metadata, ensure_ascii=False) + "\n")

    def summarize_mutation_feedback(self) -> List[str]:
        ranked = []
        for operator, stats in self.mutation_stats.items():
            generated = max(stats["generated"], 1)
            safe_rate = stats["safe"] / generated
            ranked.append((safe_rate, stats["safe"], operator, stats))
        ranked.sort(reverse=True)

        summary = []
        for _, _, operator, stats in ranked[:3]:
            summary.append(
                f"{operator}: generated={stats['generated']}, safe={stats['safe']}, "
                f"failure={stats['failure']}, error={stats['error']}, timed_out={stats['timed_out']}"
            )
        self.last_mutation_summary = summary
        return summary

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

    def _request_prompt_candidates_from_messages(
        self,
        messages: List[dict],
        model_name: str,
        candidate_count: int,
        greedy_temperature: float,
        candidate_temperature: float,
        max_tokens: int,
    ) -> Tuple[str, List[str]]:

        def request_one_openai(temp: float) -> str:
            config = create_config(
                prev={},
                messages=messages,
                max_tokens=max_tokens,
                temperature=temp,
                model=model_name,
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

    def _request_auto_prompt_candidates(self, message: str) -> Tuple[str, List[str]]:
        llm_config = getattr(self, "config_dict", {}).get("llm", {})
        autoprompt_model = llm_config.get("autoprompt_model", "deepseek-chat")
        candidate_count = llm_config.get("autoprompt_candidates", 3)
        greedy_temperature = llm_config.get("autoprompt_greedy_temperature", 0.2)
        candidate_temperature = llm_config.get("autoprompt_temperature", 0.9)
        max_tokens = llm_config.get("autoprompt_max_tokens", 256)
        messages = self._create_auto_prompt_message(message)
        return self._request_prompt_candidates_from_messages(
            messages=messages,
            model_name=autoprompt_model,
            candidate_count=candidate_count,
            greedy_temperature=greedy_temperature,
            candidate_temperature=candidate_temperature,
            max_tokens=max_tokens,
        )

    def build_prompt_refresh_request(self) -> str:
        parts = []
        target_api = self.prompt_used.get("target_api") or "the target API"
        parts.append(f"Target API: {target_api}")
        if self.failure_rules:
            parts.append(
                "Observed repeated compiler mistakes:\n"
                + "\n".join([f"- {rule}" for rule in self.failure_rules])
            )
        if self.safe_examples:
            examples = []
            for index, example in enumerate(self.safe_examples, start=1):
                examples.append(f"Successful example {index}:\n```{self.language}\n{example}\n```")
            parts.append("Recent successful patterns:\n" + "\n\n".join(examples))
        if self.batch_feedback_window:
            recent = self.batch_feedback_window[-self.max_feedback_rules :]
            parts.append(
                "Most recent normalized feedback items:\n"
                + "\n".join([f"- {item}" for item in recent])
            )
        mutation_summary = self.summarize_mutation_feedback()
        if mutation_summary:
            parts.append(
                "Recent mutation operator performance:\n"
                + "\n".join([f"- {item}" for item in mutation_summary])
            )
        return "\n\n".join(parts)

    def refresh_prompt_from_feedback(self) -> Union[str, None]:
        summary = self.build_prompt_refresh_request()
        if not summary.strip():
            return None

        llm_config = getattr(self, "config_dict", {}).get("llm", {})
        target_config = getattr(self, "config_dict", {}).get("target", {})
        refresh_model = llm_config.get(
            "runtime_autoprompt_model",
            llm_config.get("autoprompt_model", "deepseek-chat"),
        )
        candidate_count = target_config.get(
            "prompt_refresh_candidates",
            llm_config.get(
                "prompt_refresh_candidates",
                llm_config.get("runtime_prompt_refresh_candidates", 3),
            ),
        )
        greedy_temperature = llm_config.get(
            "runtime_autoprompt_greedy_temperature",
            llm_config.get("autoprompt_greedy_temperature", 0.2),
        )
        candidate_temperature = llm_config.get(
            "runtime_autoprompt_temperature",
            llm_config.get("autoprompt_temperature", 0.7),
        )
        max_tokens = llm_config.get(
            "runtime_autoprompt_max_tokens",
            llm_config.get("autoprompt_max_tokens", 256),
        )
        refresh_eval_batch_size = llm_config.get(
            "runtime_refresh_validation_batch_size",
            llm_config.get(
                "autoprompt_validation_batch_size",
                self.batch_size,
            ),
        )
        refresh_eval_max_length = llm_config.get(
            "runtime_refresh_validation_max_length",
            llm_config.get(
                "autoprompt_validation_max_length",
                self.max_length,
            ),
        )

        prompt_dir = os.path.join(self.folder, "prompts")
        os.makedirs(prompt_dir, exist_ok=True)
        round_id = self.update_round
        with open(
            os.path.join(prompt_dir, f"refreshed_request_round_{round_id}.txt"),
            "w",
            encoding="utf-8",
        ) as f:
            f.write(summary)

        try:
            messages = self._create_prompt_refresh_message(summary)
            greedy_prompt, candidate_summaries = self._request_prompt_candidates_from_messages(
                messages=messages,
                model_name=refresh_model,
                candidate_count=candidate_count,
                greedy_temperature=greedy_temperature,
                candidate_temperature=candidate_temperature,
                max_tokens=max_tokens,
            )
        except Exception as exc:
            self.m_logger.logo(
                f"Runtime prompt refresh failed: {exc}", level=LEVEL.INFO
            )
            return None

        scored_prompts = []

        # Pre-sanitize before guard check
        greedy_prompt = self._try_sanitize_prompt_candidate(greedy_prompt)
        greedy_issues = self._summarize_prompt_issues(greedy_prompt)
        if self._reject_prompt_candidate(greedy_prompt):
            self._record_rejected_prompt_candidate(
                f"greedy_round_{round_id}",
                greedy_prompt,
                greedy_issues,
                "refresh",
            )
            self.m_logger.logo(
                "Rejected refreshed greedy prompt candidate: "
                + ", ".join(greedy_issues),
                level=LEVEL.INFO,
            )
        else:
            greedy_wrapped = self.wrap_prompt(greedy_prompt)
            with open(
                os.path.join(prompt_dir, f"refreshed_greedy_round_{round_id}.txt"),
                "w",
                encoding="utf-8",
            ) as f:
                f.write(greedy_wrapped)
            greedy_score = self._score_prompt_for_refresh(
                greedy_wrapped, refresh_eval_batch_size, refresh_eval_max_length
            )
            scored_prompts.append((greedy_score, greedy_wrapped, "greedy"))

        for index, summary_candidate in enumerate(candidate_summaries):
            # Pre-sanitize before guard check
            summary_candidate = self._try_sanitize_prompt_candidate(summary_candidate)
            issues = self._summarize_prompt_issues(summary_candidate)
            if self._reject_prompt_candidate(summary_candidate):
                self._record_rejected_prompt_candidate(
                    f"candidate_{index}_round_{round_id}",
                    summary_candidate,
                    issues,
                    "refresh",
                )
                self.m_logger.logo(
                    f"Rejected refreshed prompt candidate_{index}: "
                    + ", ".join(issues),
                    level=LEVEL.INFO,
                )
                continue
            wrapped_prompt = self.wrap_prompt(summary_candidate)
            with open(
                os.path.join(prompt_dir, f"refreshed_prompt_round_{round_id}_{index}.txt"),
                "w",
                encoding="utf-8",
            ) as f:
                f.write(wrapped_prompt)
            score = self._score_prompt_for_refresh(
                wrapped_prompt, refresh_eval_batch_size, refresh_eval_max_length
            )
            scored_prompts.append((score, wrapped_prompt, f"candidate_{index}"))

        if not scored_prompts:
            self.m_logger.logo(
                "All refreshed prompt candidates rejected by prompt-quality guard.",
                level=LEVEL.INFO,
            )
            self._write_refresh_status(
                round_id,
                "rejected",
                "all refreshed prompt candidates rejected by prompt-quality guard",
            )
            return None

        best_score, best_prompt, best_name = max(scored_prompts, key=lambda item: item[0])
        with open(
            os.path.join(prompt_dir, f"refreshed_scores_round_{round_id}.txt"),
            "w",
            encoding="utf-8",
        ) as f:
            for score, _, name in scored_prompts:
                f.write(f"{name}\t{score}\n")
            f.write(f"best\t{best_name}\t{best_score}\n")

        should_accept = False
        decision_reason = ""
        if self.base_prompt_score is None:
            should_accept = best_score > 0
            decision_reason = (
                f"baseline=None, accept if best_score > 0; observed best_score={best_score}"
            )
        else:
            should_accept = best_score >= self.base_prompt_score
            decision_reason = (
                f"baseline={self.base_prompt_score}, accept if best_score >= baseline; observed best_score={best_score}"
            )

        if should_accept:
            self.base_prompt_score = best_score
            self.last_refresh_round = round_id
            with open(
                os.path.join(prompt_dir, f"accepted_refreshed_prompt_round_{round_id}.txt"),
                "w",
                encoding="utf-8",
            ) as f:
                f.write(best_prompt)
            with open(
                os.path.join(prompt_dir, "best_prompt.txt"),
                "w",
                encoding="utf-8",
            ) as f:
                f.write(best_prompt)
            with open(
                os.path.join(prompt_dir, f"refresh_decision_round_{round_id}.txt"),
                "w",
                encoding="utf-8",
            ) as f:
                f.write(
                    "status=accepted\n"
                    + f"winner={best_name}\n"
                    + f"score={best_score}\n"
                    + f"{decision_reason}\n"
                )
            self.m_logger.logo(
                f"Accepted refreshed prompt from round {round_id}: {best_name} (score {best_score}).",
                level=LEVEL.INFO,
            )
            self.batch_feedback_window = []
            return best_prompt

        with open(
            os.path.join(prompt_dir, f"refresh_decision_round_{round_id}.txt"),
            "w",
            encoding="utf-8",
        ) as f:
            f.write(
                "status=rejected\n"
                + f"winner={best_name}\n"
                + f"score={best_score}\n"
                + f"{decision_reason}\n"
            )
        self.m_logger.logo(
            f"Rejected refreshed prompt from round {round_id}: best score {best_score} did not beat baseline {self.base_prompt_score}.",
            level=LEVEL.INFO,
        )
        return None

    def _score_prompt_for_refresh(
        self, prompt: str, batch_size: int, max_length: int
    ) -> int:
        fos = self._generate_with_prompt(
            prompt,
            batch_size=batch_size,
            temperature=self.temperature,
            max_length=max_length,
        )
        return self._score_generated_samples(fos)

    def _score_generated_samples(self, fos: List[str]) -> int:
        unique_safe = set()
        safe_count = 0
        structured_failure_count = 0
        syntax_failure_count = 0

        for fo in fos:
            code = self.prompt_used["begin"] + "\n" + fo
            wb_file = self.write_back_file(code)
            result, message = self.validate_individual(wb_file)
            cleaned = self.clean_code(code)

            if (
                result == FResult.SAFE
                and self.filter(code)
                and cleaned not in unique_safe
            ):
                unique_safe.add(cleaned)
                safe_count += 1
                continue

            if result in (FResult.FAILURE, FResult.ERROR):
                summarized = self.summarize_feedback_message(result, message)
                sanitized = self._sanitize_feedback(message, limit=200).lower()
                if summarized:
                    structured_failure_count += 1
                if any(
                    token in sanitized
                    for token in [
                        "reached end of file while parsing",
                        "'try' without 'catch'",
                        "not a statement",
                        "class, interface, enum, or record expected",
                        "illegal start of expression",
                        "illegal start of type",
                    ]
                ):
                    syntax_failure_count += 1

        # Heavily favour prompts that produce compilable programs (safe_count * 5).
        # Structured failures (specific API errors rather than syntax noise) get a small
        # bonus because they show the prompt at least generates recognisable API usage.
        # Pure syntax failures are penalised more aggressively.
        score = (
            safe_count * 5
            + structured_failure_count
            - syntax_failure_count * 3
        )
        return max(score, 0)

    def auto_prompt(self, **kwargs) -> str:
        os.makedirs(self.folder + "/prompts", exist_ok=True)

        # if we have already done auto-prompting, validate and return the best prompt
        if os.path.exists(self.folder + "/prompts/best_prompt.txt"):
            with open(
                self.folder + "/prompts/best_prompt.txt", "r", encoding="utf-8"
            ) as f:
                existing = f.read()
            inner = self._extract_prompt_inner_text(existing)
            if not self._reject_prompt_candidate(inner):
                self.m_logger.logo(
                    "Use existing prompt (guard-validated OK).", level=LEVEL.INFO
                )
                return existing
            issues = self._summarize_prompt_issues(inner)
            self.m_logger.logo(
                "Existing best_prompt.txt failed guard ("
                + ", ".join(issues)
                + "); archiving and regenerating.",
                level=LEVEL.INFO,
            )
            import shutil as _shutil
            stale_dest = self.folder + "/prompts/best_prompt_stale.txt"
            try:
                _shutil.move(self.folder + "/prompts/best_prompt.txt", stale_dest)
            except Exception:
                pass
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

                # Pre-sanitize greedy candidate before guard check
                greedy_prompt = self._try_sanitize_prompt_candidate(greedy_prompt)
                greedy_issues = self._summarize_prompt_issues(greedy_prompt)
                if self._reject_prompt_candidate(greedy_prompt):
                    self._record_rejected_prompt_candidate(
                        "greedy_prompt", greedy_prompt, greedy_issues, "autoprompt"
                    )
                    self.m_logger.logo(
                        "Rejected greedy autoprompt candidate: "
                        + ", ".join(greedy_issues),
                        level=LEVEL.INFO,
                    )
                else:
                    greedy_wrapped = self.wrap_prompt(greedy_prompt)
                    with open(
                        self.folder + "/prompts/greedy_prompt.txt",
                        "w",
                        encoding="utf-8",
                    ) as f:
                        f.write(greedy_wrapped)
                    greedy_score = self.validate_prompt(greedy_wrapped)
                    scored_prompts.append(
                        (greedy_score, greedy_wrapped, "greedy_prompt")
                    )

                for index, summary in enumerate(
                    track(candidate_summaries, description="Generating prompts")
                ):
                    # Pre-sanitize candidate before guard check
                    summary = self._try_sanitize_prompt_candidate(summary)
                    issues = self._summarize_prompt_issues(summary)
                    if self._reject_prompt_candidate(summary):
                        candidate_name = f"prompt_{index}"
                        self._record_rejected_prompt_candidate(
                            candidate_name, summary, issues, "autoprompt"
                        )
                        self.m_logger.logo(
                            f"Rejected autoprompt candidate {candidate_name}: "
                            + ", ".join(issues),
                            level=LEVEL.INFO,
                        )
                        continue
                    wrapped_prompt = self.wrap_prompt(summary)
                    with open(
                        self.folder + f"/prompts/prompt_{index}.txt",
                        "w",
                        encoding="utf-8",
                    ) as f:
                        f.write(wrapped_prompt)
                    score = self.validate_prompt(wrapped_prompt)
                    scored_prompts.append((score, wrapped_prompt, f"prompt_{index}"))

                if not scored_prompts:
                    # All standard candidates failed — try a constrained single-shot
                    # request with explicit format enforcement before giving up.
                    self.m_logger.logo(
                        "All initial autoprompt candidates rejected by guard; "
                        "retrying with constrained format request.",
                        level=LEVEL.INFO,
                    )
                    constrained_raw = self._request_constrained_autoprompt(
                        kwargs["message"]
                    )
                    if constrained_raw:
                        constrained_sanitized = self._try_sanitize_prompt_candidate(
                            constrained_raw
                        )
                        if not self._reject_prompt_candidate(constrained_sanitized):
                            c_wrapped = self.wrap_prompt(constrained_sanitized)
                            with open(
                                self.folder + "/prompts/constrained_retry_prompt.txt",
                                "w",
                                encoding="utf-8",
                            ) as f:
                                f.write(c_wrapped)
                            c_score = self.validate_prompt(c_wrapped)
                            scored_prompts.append((c_score, c_wrapped, "constrained_retry"))
                            self.m_logger.logo(
                                f"Constrained retry prompt accepted (score={c_score}).",
                                level=LEVEL.INFO,
                            )
                        else:
                            retry_issues = self._summarize_prompt_issues(constrained_sanitized)
                            self.m_logger.logo(
                                "Constrained retry prompt also rejected by guard: "
                                + ", ".join(retry_issues),
                                level=LEVEL.INFO,
                            )
                if not scored_prompts:
                    raise ValueError(
                        "All autoprompt candidates rejected by prompt-quality guard."
                    )

                best_score, best_prompt, best_prompt_name = max(
                    scored_prompts, key=lambda item: item[0]
                )
                self.base_prompt_score = best_score
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
                # Distinguish guard rejection (all candidates structurally bad) from
                # network/API errors.  Only in the guard-rejection case do we use the
                # minimal recovery template — a lighter, classification-aware prompt that
                # avoids docstring bloat.  For genuine request failures we still fall back
                # to the documentation prompt, which may carry useful context.
                guard_rejected = "rejected by prompt-quality guard" in str(exc)
                if guard_rejected:
                    self.m_logger.logo(
                        "All autoprompt candidates rejected by guard; "
                        "using classification-aware minimal recovery template.",
                        level=LEVEL.INFO,
                    )
                    best_prompt = self._build_minimal_recovery_prompt()
                    self.m_logger.logo(
                        "Prompt source: minimal recovery template (guard fallback).",
                        level=LEVEL.INFO,
                    )
                else:
                    self.m_logger.logo(
                        f"Auto-prompt request failed, fallback to documentation prompt: {exc}",
                        level=LEVEL.INFO,
                    )
                    best_prompt = self._build_handwritten_prompt()
                    self.m_logger.logo(
                        "Prompt source: fallback documentation/examples prompt.",
                        level=LEVEL.INFO,
                    )
                self.base_prompt_score = None

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

        self.base_prompt = self.auto_prompt(
            message=self.prompt_used["docstring"],
            hw_prompt=self.prompt_used["hw_prompt"] if self.hw else None,
            hw=self.hw,
            no_input_prompt=self.no_input_prompt,
        )
        self.initial_prompt = self.base_prompt
        self.runtime_prompt = self.base_prompt
        self.prompt = self.runtime_prompt
        self._init_mutation_components()
        if self.enable_mutation and self.mutation_profile:
            self.m_logger.logo(
                "Mutation enabled with primary tag "
                f"{self.mutation_profile.get('primary_tag')} "
                f"and profile {self.mutation_profile.get('mutation_profile')} "
                f"(active_profiles={self.mutation_profile.get('active_profiles', [])}, "
                f"operators={self.mutation_profile.get('priority_operators', [])}).",
                level=LEVEL.INFO,
            )
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
            max_length=self.max_length,
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
        metadata_records = []
        seen_codes = set()
        for index, fo in enumerate(fos):
            self.g_logger.logo("========== sample =========", level=LEVEL.VERBOSE)
            cleaned_code = self._prepare_generated_code(
                self.prompt_used["begin"] + "\n" + fo
            )
            if cleaned_code is None:
                continue
            if cleaned_code in seen_codes:
                continue
            seen_codes.add(cleaned_code)
            new_fos.append(cleaned_code)
            metadata_records.append(
                self._make_sample_metadata(
                    source_type="generated",
                    operator="llm_seed",
                    parent_index=index,
                )
            )
            self.g_logger.logo(
                cleaned_code, level=LEVEL.VERBOSE
            )
            self.g_logger.logo("========== sample =========", level=LEVEL.VERBOSE)
            for mutated_code, metadata in self._collect_mutated_samples(cleaned_code, index):
                if mutated_code in seen_codes:
                    continue
                seen_codes.add(mutated_code)
                new_fos.append(mutated_code)
                metadata_records.append(metadata)
                self.g_logger.logo(
                    "========== mutated sample =========", level=LEVEL.VERBOSE
                )
                self.g_logger.logo(mutated_code, level=LEVEL.VERBOSE)
                self.g_logger.logo(
                    "========== mutated sample =========", level=LEVEL.VERBOSE
                )
        self.pending_sample_records = metadata_records
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

    # update
    def update(self, **kwargs):
        if self.p_strategy == -1:
            self.m_logger.logo(
                "Prompt unchanged: prompt strategy disabled.", level=LEVEL.INFO
            )
            return

        new_safe_examples = self.select_safe_examples(kwargs["prev"])
        feedback_rules = []
        for result, message, _ in kwargs.get("feedback", []):
            if result in (FResult.FAILURE, FResult.ERROR, FResult.TIMED_OUT):
                feedback_rules.extend(self.summarize_feedback_message(result, message))

        if feedback_rules:
            self.batch_feedback_window.extend(feedback_rules)
            self.feedback_history.extend(feedback_rules)
            # Keep a generous history window (not capped at max_feedback_rules, which is
            # the limit for the *active* rule set used in prompts, not for the record).
            self.feedback_history = self.feedback_history[-50:]
            self._merge_failure_rules(feedback_rules)
            current_signature = tuple(self.failure_rules)
            if (
                current_signature
                and current_signature == self.previous_failure_rule_signature
                and not new_safe_examples
            ):
                self.stale_feedback_rounds += 1
            else:
                self.stale_feedback_rounds = 0
            self.previous_failure_rule_signature = current_signature
            if self.stale_feedback_rounds >= 2:
                self._reset_to_minimal_prompt(
                    "failure-rule signature unchanged for consecutive rounds without new SAFE examples"
                )

        for example in new_safe_examples:
            if example and example not in self.safe_examples:
                self.safe_examples.append(example)
        self.safe_examples = self.safe_examples[-self.max_safe_examples :]

        if self.safe_examples:
            self.prev_example = self.safe_examples[-1]

        self.update_round += 1

        if self.safe_examples or self.failure_rules:
            refreshed_prompt = None
            current_rule_signature = tuple(self.failure_rules)
            should_refresh = (
                self.prompt_refresh_interval > 0
                and self.update_round % self.prompt_refresh_interval == 0
                and current_rule_signature
                and current_rule_signature != self.last_refresh_rule_signature
            )
            if should_refresh:
                self._write_refresh_status(
                    self.update_round,
                    "attempted",
                    "refresh interval reached with a new failure-rule signature",
                )
                refreshed_prompt = self.refresh_prompt_from_feedback()
                if refreshed_prompt:
                    self.base_prompt = refreshed_prompt
                self.last_refresh_rule_signature = current_rule_signature
            else:
                reasons = []
                if self.prompt_refresh_interval <= 0:
                    reasons.append("prompt refresh disabled")
                if self.prompt_refresh_interval > 0 and self.update_round % self.prompt_refresh_interval != 0:
                    reasons.append("round did not hit refresh interval")
                if not current_rule_signature:
                    reasons.append("no failure-rule signature available")
                if (
                    current_rule_signature
                    and current_rule_signature == self.last_refresh_rule_signature
                ):
                    reasons.append("failure-rule signature unchanged")
                self._write_refresh_status(
                    self.update_round,
                    "skipped",
                    "; ".join(reasons) if reasons else "refresh conditions not met",
                )
            self.runtime_prompt = self._create_feedback_prompt(
                self.safe_examples, self.failure_rules
            )
            self.prompt = self.runtime_prompt
            self._dump_runtime_prompt_snapshot()
            self.m_logger.logo(
                "Prompt updated from structured feedback"
                f" (rules: {len(self.failure_rules)}, safe examples: {len(self.safe_examples)}).",
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
                "{} failed validation with error message: {}".format(file_name, message),
                LEVEL.VERBOSE,
            )
        elif f_result == FResult.ERROR:
            self.v_logger.logo(
                "{} has potential error!\nerror message:\n{}".format(file_name, message),
                LEVEL.VERBOSE,
            )
            self.m_logger.logo(
                "{} has potential error!".format(file_name),
                LEVEL.INFO,
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
