import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List


ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "config" / "documentation"
OUT_DIR = ROOT / "outputs" / "api_classification"


TAG_PRIORITY = [
    "SECURITY",
    "REFLECT",
    "FILE",
    "CONCURRENT",
    "NETWORK",
    "CALLBACK",
    "TIME",
    "JVM_MGMT",
    "RESOURCE",
    "BUFFER",
    "MARK_SUPPORT",
    "BATCH_OP",
    "UTILITY",
    "GENERIC",
]

DIMENSION_WEIGHTS = {
    "package": 4,
    "type": 4,
    "interface": 2,
    "field": 2,
    "method": 2,
    "boundary": 1,
}

DOMAIN_TAGS = {
    "SECURITY",
    "REFLECT",
    "FILE",
    "CONCURRENT",
    "NETWORK",
    "CALLBACK",
    "TIME",
    "JVM_MGMT",
    "UTILITY",
}

STRUCTURAL_TAGS = {
    "RESOURCE",
    "BUFFER",
    "MARK_SUPPORT",
    "BATCH_OP",
    "GENERIC",
}

TAG_RULES = {
    "RESOURCE": {
        "package": [".io", ".net", "stream", "reader", "writer"],
        "type": ["stream", "reader", "writer", "channel", "session"],
        "interface": ["closeable", "autocloseable", "flushable"],
        "field": ["buf", "count", "out", "in", "inputstream", "outputstream"],
        "method": ["close(", "flush(", "open(", "read(", "write("],
        "boundary": ["ioexception", "illegalstateexception"],
    },
    "BUFFER": {
        "package": [".nio", ".io"],
        "type": ["buffer", "buffered", "bytearray", "chararray"],
        "interface": [],
        "field": ["buf", "count", "pos", "position", "limit", "capacity", "byte[]", "char[]"],
        "method": ["read(byte[]", "write(byte[]", "put(", "get(", "remaining("],
        "boundary": ["off+len", "integer.max_value", "null"],
    },
    "MARK_SUPPORT": {
        "package": [".io"],
        "type": ["bufferedinputstream", "reader", "inputstream"],
        "interface": [],
        "field": ["marklimit", "markpos"],
        "method": ["mark(", "reset("],
        "boundary": ["marklimit", "markpos", "-1"],
    },
    "BATCH_OP": {
        "package": [".io", ".nio"],
        "type": ["stream", "reader", "writer", "buffer"],
        "interface": [],
        "field": ["byte[]", "char[]"],
        "method": ["write(byte[]", "read(byte[]", "char[]", "int off", "int len", "offset", "length"],
        "boundary": ["off+len", "0, -1, integer.max_value", "0/-1/max"],
    },
    "CALLBACK": {
        "package": [".event", ".awt.event", ".beans"],
        "type": ["listener", "callback", "handler", "event"],
        "interface": ["eventlistener"],
        "field": [],
        "method": ["listener", "callback", "handler", "addlistener", "removelistener", "register", "unregister"],
        "boundary": [],
    },
    "CONCURRENT": {
        "package": [".concurrent", ".lang.thread"],
        "type": ["thread", "lock", "executor", "semaphore", "future", "callable", "runnable"],
        "interface": ["runnable", "callable", "future"],
        "field": ["volatile", "atomic"],
        "method": ["synchronized", "lock(", "unlock(", "submit(", "execute(", "start(", "join(", "interrupt(", "sleep("],
        "boundary": ["concurrentmodificationexception", "illegalthreadstateexception"],
    },
    "TIME": {
        "package": [".time"],
        "type": ["date", "time", "instant", "clock", "duration", "zone"],
        "interface": [],
        "field": [],
        "method": ["millis", "epoch", "instant", "clock", "duration", "period", "zoneid"],
        "boundary": ["long.max_value", "gmt+14"],
    },
    "FILE": {
        "package": [".io.file", ".nio.file", "java.io.file", "java.nio.file"],
        "type": ["file", "path", "files", "filesystem", "watchservice", "filestore"],
        "interface": [],
        "field": [],
        "method": ["path", "file", "files", "watch", "resolve(", "delete(", "exists(", "mkdir", "create", "tocanonical"],
        "boundary": ["../../", "\\0", "*", "?", "securityexception"],
    },
    "SECURITY": {
        "package": [".security", ".crypto", ".ssl", ".auth", ".cert"],
        "type": ["cipher", "digest", "signature", "mac", "keystore", "key", "trustmanager", "keymanager", "permission", "ssl", "tls", "certificate"],
        "interface": [],
        "field": ["provider"],
        "method": ["encrypt", "decrypt", "sign", "verify", "init(", "dofinal(", "getinstance(", "sslpermission", "permission"],
        "boundary": ["provider", "md5", "sha-1", "securityexception", "nosuchalgorithmexception", "invalidkeyexception"],
    },
    "REFLECT": {
        "package": [".reflect"],
        "type": ["class", "method", "field", "constructor", "loader", "proxy"],
        "interface": [],
        "field": [],
        "method": ["invoke(", "getdeclared", "setaccessible", "newinstance(", "getmethod(", "getfield(", "getconstructor("],
        "boundary": ["illegalaccessexception", "private"],
    },
    "UTILITY": {
        "package": [".util"],
        "type": ["math", "string", "objects", "arrays", "optional", "random", "formatter", "utils"],
        "interface": [],
        "field": [],
        "method": ["parse", "format", "compare", "hash", "equals"],
        "boundary": ["integer.max_value", "integer.min_value", "unicode", "null"],
    },
    "NETWORK": {
        "package": [".net", ".http"],
        "type": ["socket", "serversocket", "url", "uri", "httpclient", "inetaddress", "datagram"],
        "interface": [],
        "field": [],
        "method": ["connect(", "send(", "receive(", "openconnection(", "bind("],
        "boundary": ["sockettimeoutexception", "http"],
    },
    "JVM_MGMT": {
        "package": [".management"],
        "type": ["mxbean", "runtime", "memory", "threadmxbean", "operatingsystemmxbean"],
        "interface": [],
        "field": [],
        "method": ["getheap", "getthread", "getruntime", "getmemory"],
        "boundary": [],
    },
}


PROFILE_RULES = {
    "resource_buffer_batch": ["RESOURCE", "BUFFER", "BATCH_OP"],
    "file_path_state": ["FILE"],
    "concurrent_sequence": ["CONCURRENT"],
    "security_provider_flow": ["SECURITY"],
    "reflection_dispatch": ["REFLECT"],
    "callback_registration_flow": ["CALLBACK"],
    "time_boundary_mix": ["TIME"],
    "network_endpoint_state": ["NETWORK"],
    "utility_value_boundary": ["UTILITY"],
    "jvm_mgmt_runtime_state": ["JVM_MGMT"],
    "mark_reset_sequence": ["MARK_SUPPORT"],
    "generic_java": ["GENERIC"],
}


PROFILE_OPERATORS = {
    "resource_buffer_batch": [
        "constructor_size_edge",
        "write_bulk_edge",
        "lifecycle_sequence",
        "write_single_edge",
    ],
    "file_path_state": [
        "constructor_size_edge",
        "lifecycle_sequence",
    ],
    "concurrent_sequence": [
        "concurrent_yield_injection",
        "concurrent_thread_wrapper_mutation",
        "concurrent_signal_sequence_mutation",
    ],
    "security_provider_flow": [
        "security_algorithm_boundary_mutation",
        "security_provider_mutation",
        "security_material_boundary_mutation",
    ],
    "reflection_dispatch": [
        "reflect_accessibility_flip_mutation",
        "reflect_member_name_mutation",
        "reflect_receiver_null_mutation",
    ],
    "callback_registration_flow": [
        "callback_duplicate_registration_mutation",
        "callback_order_reversal_mutation",
        "callback_null_event_mutation",
    ],
    "time_boundary_mix": [
        "time_epoch_boundary_mutation",
        "time_duration_sign_mutation",
        "time_zone_boundary_mutation",
    ],
    "network_endpoint_state": [
        "network_endpoint_boundary_mutation",
        "network_timeout_boundary_mutation",
        "network_sequence_mutation",
    ],
    "utility_value_boundary": [
        "utility_parse_boundary_mutation",
        "utility_format_boundary_mutation",
        "utility_collection_seed_mutation",
    ],
    "jvm_mgmt_runtime_state": [
        "jvm_mgmt_query_name_mutation",
        "jvm_mgmt_runtime_toggle_mutation",
        "jvm_mgmt_sampling_boundary_mutation",
    ],
    "mark_reset_sequence": [
        "mark_support_limit_mutation",
        "mark_support_reset_mutation",
        "mark_support_reuse_mutation",
    ],
    "generic_java": [
        "generic_null_boundary",
        "generic_numeric_boundary",
        "generic_sequence_reorder",
    ],
}


PROFILE_RISK_POINTS = {
    "resource_buffer_batch": [
        "resource_lifecycle",
        "buffer_size_boundary",
        "write_offset_length",
    ],
    "file_path_state": [
        "path_argument",
        "file_state_transition",
    ],
    "concurrent_sequence": [
        "interleaving_order",
        "shared_state",
    ],
    "security_provider_flow": [
        "provider_selection",
        "algorithm_boundary",
        "key_material_boundary",
    ],
    "reflection_dispatch": [
        "member_resolution",
        "accessibility_flip",
        "receiver_contract",
    ],
    "callback_registration_flow": [
        "registration_order",
        "duplicate_registration",
        "callback_argument_contract",
    ],
    "time_boundary_mix": [
        "epoch_extreme",
        "duration_sign",
        "timezone_boundary",
    ],
    "network_endpoint_state": [
        "endpoint_boundary",
        "timeout_boundary",
        "connect_bind_order",
    ],
    "utility_value_boundary": [
        "parse_boundary",
        "format_boundary",
        "value_aliasing",
    ],
    "jvm_mgmt_runtime_state": [
        "mxbean_name",
        "runtime_snapshot",
        "management_query",
    ],
    "mark_reset_sequence": [
        "mark_limit",
        "reset_without_mark",
        "mark_position_reuse",
    ],
    "generic_java": [
        "general_boundary",
    ],
}


def normalize(text: str) -> str:
    return " ".join(text.lower().split())


def extract_section(text: str, start_header: str, end_headers: list[str]) -> str:
    start = text.find(start_header)
    if start == -1:
        return ""
    start += len(start_header)
    end_positions = [text.find(header, start) for header in end_headers if text.find(header, start) != -1]
    end = min(end_positions) if end_positions else len(text)
    return text[start:end]


def extract_headings(section_text: str) -> list[str]:
    return re.findall(r"^####\s+(.+)$", section_text, flags=re.MULTILINE)


def _append_bias(
    scores: Dict[str, int],
    evidence: Dict[str, Dict[str, List[str]]],
    tag: str,
    weight: int,
    reason: str,
):
    scores[tag] += weight
    evidence[tag]["package"].append(reason)


def apply_domain_bias(
    scores: Dict[str, int],
    evidence: Dict[str, Dict[str, List[str]]],
    source: str,
    path: Path,
    api_name: str,
):
    context = normalize(f"{source} {path.stem} {api_name}")
    api_lower = api_name.lower()

    if any(token in context for token in [".crypto", "javax crypto", ".security", ".ssl", ".auth", ".cert"]):
        _append_bias(scores, evidence, "SECURITY", 8, "domain_bias_security_package")
    if any(token in api_lower for token in ["cipher", "signature", "digest", "keystore", "key", "mac", "ssl", "trustmanager", "keymanager"]):
        _append_bias(scores, evidence, "SECURITY", 6, "domain_bias_security_type")

    if any(token in context for token in [".reflect", "lang reflect"]):
        _append_bias(scores, evidence, "REFLECT", 8, "domain_bias_reflect_package")
    if any(token in api_lower for token in ["method", "field", "constructor", "proxy", "accessibleobject", "invocation"]):
        _append_bias(scores, evidence, "REFLECT", 6, "domain_bias_reflect_type")

    if any(token in context for token in ["java.io.file", "java.nio.file", ".nio.file", ".io.file"]):
        _append_bias(scores, evidence, "FILE", 8, "domain_bias_file_package")
    if any(token in api_lower for token in ["file", "path", "watchservice", "filestore", "filesystem"]):
        _append_bias(scores, evidence, "FILE", 5, "domain_bias_file_type")

    if any(token in context for token in [".concurrent", "lang.thread"]):
        _append_bias(scores, evidence, "CONCURRENT", 8, "domain_bias_concurrent_package")
    if any(token in api_lower for token in ["thread", "executor", "lock", "future", "callable", "runnable", "semaphore"]):
        _append_bias(scores, evidence, "CONCURRENT", 6, "domain_bias_concurrent_type")

    if any(token in context for token in [".management", "jmx", "mxbean"]):
        _append_bias(scores, evidence, "JVM_MGMT", 8, "domain_bias_jvm_mgmt_package")
    if any(token in api_lower for token in ["mxbean", "managementfactory", "runtime", "memory", "threadmxbean"]):
        _append_bias(scores, evidence, "JVM_MGMT", 6, "domain_bias_jvm_mgmt_type")

    if any(token in context for token in [".time", "java time"]):
        _append_bias(scores, evidence, "TIME", 8, "domain_bias_time_package")
    if any(token in api_lower for token in ["time", "date", "instant", "duration", "period", "zone", "clock"]):
        _append_bias(scores, evidence, "TIME", 5, "domain_bias_time_type")

    if any(token in context for token in [".net", ".http", "httpclient"]):
        _append_bias(scores, evidence, "NETWORK", 8, "domain_bias_network_package")
    if any(token in api_lower for token in ["socket", "url", "uri", "http", "inet", "datagram"]):
        _append_bias(scores, evidence, "NETWORK", 5, "domain_bias_network_type")

    if any(token in context for token in [".event", ".awt.event", ".beans"]):
        _append_bias(scores, evidence, "CALLBACK", 8, "domain_bias_callback_package")
    if any(token in api_lower for token in ["listener", "callback", "handler", "event"]):
        _append_bias(scores, evidence, "CALLBACK", 5, "domain_bias_callback_type")

    if any(token in context for token in [".util"]) and ".concurrent" not in context and ".time" not in context:
        _append_bias(scores, evidence, "UTILITY", 4, "domain_bias_utility_package")


def choose_primary_tag(
    scores: Dict[str, int],
    evidence: Dict[str, Dict[str, List[str]]],
    ranked_tags: List[str],
) -> str:
    primary_tag = ranked_tags[0]
    top_score = scores[primary_tag]

    if primary_tag in DOMAIN_TAGS:
        return primary_tag

    for tag in ranked_tags:
        if tag not in DOMAIN_TAGS:
            continue
        domain_score = scores[tag]
        strong_domain_signal = bool(
            evidence[tag].get("package")
            or evidence[tag].get("type")
            or evidence[tag].get("interface")
        )
        if not strong_domain_signal:
            continue
        if domain_score >= max(4, top_score - 3):
            return tag

    return primary_tag


def derive_mutation_profile(primary_tag: str, all_tags: list[str]) -> str:
    tags = set(all_tags)
    if primary_tag == "SECURITY":
        return "security_provider_flow"
    if primary_tag == "REFLECT":
        return "reflection_dispatch"
    if primary_tag == "CALLBACK":
        return "callback_registration_flow"
    if primary_tag == "TIME":
        return "time_boundary_mix"
    if primary_tag == "NETWORK":
        return "network_endpoint_state"
    if primary_tag == "UTILITY":
        return "utility_value_boundary"
    if primary_tag == "JVM_MGMT":
        return "jvm_mgmt_runtime_state"
    if primary_tag == "MARK_SUPPORT":
        return "mark_reset_sequence"
    if primary_tag == "RESOURCE" and ("BUFFER" in tags or "BATCH_OP" in tags):
        return "resource_buffer_batch"
    if primary_tag == "BUFFER" and ("RESOURCE" in tags or "BATCH_OP" in tags):
        return "resource_buffer_batch"
    if primary_tag == "BATCH_OP" and "SECURITY" in tags:
        return "security_provider_flow"
    if primary_tag == "BATCH_OP" and ("RESOURCE" in tags or "BUFFER" in tags):
        return "resource_buffer_batch"
    if primary_tag == "FILE":
        return "file_path_state"
    if primary_tag == "CONCURRENT":
        return "concurrent_sequence"
    return "generic_java"


def classify_doc(path: Path) -> dict:
    raw_text = path.read_text(encoding="utf-8", errors="ignore")
    text = normalize(raw_text)

    source_match = re.search(r"\*\*source:\*\*\s+`([^`]+)`", raw_text, flags=re.IGNORECASE)
    source = source_match.group(1) if source_match else ""

    title_match = re.search(r"^#\s+(Class|Interface|Enum|Annotation Interface)\s+(.+)$", raw_text, flags=re.MULTILINE)
    kind = title_match.group(1) if title_match else "Unknown"
    api_name = title_match.group(2).strip() if title_match else path.stem

    interface_section = extract_section(
        raw_text,
        "**All Implemented Interfaces:**",
        ["---", "### Field Details", "### Constructor Details", "### Method Details"],
    )
    field_section = extract_section(
        raw_text,
        "### Field Details",
        ["### Constructor Details", "### Method Details", "### Additional Sections"],
    )
    method_section = extract_section(
        raw_text,
        "### Method Details",
        ["### Additional Sections"],
    )

    fields = extract_headings(field_section)
    methods = extract_headings(method_section)

    dimensions = {
        "package": normalize(source + " " + path.stem),
        "type": normalize(api_name),
        "interface": normalize(interface_section),
        "field": normalize(" ".join(fields) + " " + field_section),
        "method": normalize(" ".join(methods) + " " + method_section),
        "boundary": normalize(raw_text),
    }

    scores = defaultdict(int)
    evidence = defaultdict(lambda: defaultdict(list))

    for tag, rules in TAG_RULES.items():
        for dimension, keywords in rules.items():
            haystack = dimensions[dimension]
            for keyword in keywords:
                if keyword and keyword.lower() in haystack:
                    scores[tag] += DIMENSION_WEIGHTS[dimension]
                    evidence[tag][dimension].append(keyword)

    apply_domain_bias(scores, evidence, source, path, api_name)

    if not scores:
        scores["GENERIC"] = 1
        evidence["GENERIC"]["boundary"].append("fallback")

    # Generic is also useful as a secondary catch-all when many edge-case words appear.
    generic_keywords = ["nullpointerexception", "integer.max_value", "integer.min_value", "0", "-1", "null"]
    generic_hits = [kw for kw in generic_keywords if kw in dimensions["boundary"]]
    if generic_hits:
        scores["GENERIC"] += len(generic_hits)
        evidence["GENERIC"]["boundary"].extend(generic_hits)

    all_tags = sorted(
        scores.keys(),
        key=lambda tag: (
            -scores[tag],
            TAG_PRIORITY.index(tag) if tag in TAG_PRIORITY else 999,
            tag,
        ),
    )
    primary_tag = choose_primary_tag(scores, evidence, all_tags)
    all_tags = [primary_tag] + [tag for tag in all_tags if tag != primary_tag]
    mutation_profile = derive_mutation_profile(primary_tag, all_tags)

    return {
        "file": str(path.relative_to(ROOT)).replace("\\", "/"),
        "api_name": api_name,
        "kind": kind,
        "source": source,
        "primary_tag": primary_tag,
        "all_tags": all_tags,
        "mutation_profile": mutation_profile,
        "priority_operators": PROFILE_OPERATORS[mutation_profile],
        "risk_points": PROFILE_RISK_POINTS[mutation_profile],
        "scores": dict(sorted(scores.items(), key=lambda item: (-item[1], item[0]))),
        "dimensions": {tag: dict(dim_map) for tag, dim_map in evidence.items()},
        "field_count": len(fields),
        "method_count": len(methods),
    }


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    docs = sorted(DOCS_DIR.glob("*.md"))
    results = [classify_doc(path) for path in docs]

    json_path = OUT_DIR / "java_api_5d_classification.json"
    csv_path = OUT_DIR / "java_api_5d_classification.csv"
    summary_path = OUT_DIR / "java_api_5d_summary.md"

    with json_path.open("w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "file",
                "api_name",
                "kind",
                "source",
                "primary_tag",
                "all_tags",
                "mutation_profile",
                "priority_operators",
                "risk_points",
                "field_count",
                "method_count",
            ],
        )
        writer.writeheader()
        for item in results:
            writer.writerow(
                {
                    "file": item["file"],
                    "api_name": item["api_name"],
                    "kind": item["kind"],
                    "source": item["source"],
                    "primary_tag": item["primary_tag"],
                    "all_tags": ",".join(item["all_tags"]),
                    "mutation_profile": item["mutation_profile"],
                    "priority_operators": ",".join(item["priority_operators"]),
                    "risk_points": ",".join(item["risk_points"]),
                    "field_count": item["field_count"],
                    "method_count": item["method_count"],
                }
            )

    counter = Counter(item["primary_tag"] for item in results)
    with summary_path.open("w", encoding="utf-8") as f:
        f.write("# Java API 5D Classification Summary\n\n")
        f.write(f"- Total docs: {len(results)}\n")
        f.write(f"- Output JSON: `{json_path.relative_to(ROOT).as_posix()}`\n")
        f.write(f"- Output CSV: `{csv_path.relative_to(ROOT).as_posix()}`\n\n")
        f.write("## Primary Tag Counts\n\n")
        for tag, count in counter.most_common():
            f.write(f"- {tag}: {count}\n")
        f.write("\n## Samples\n\n")
        sample_names = [
            "BufferedOutputStream",
            "BufferedInputStream",
            "SSLSession",
            "File",
            "Thread",
        ]
        by_name = {item["api_name"]: item for item in results}
        for name in sample_names:
            item = by_name.get(name)
            if not item:
                continue
            f.write(f"### {name}\n\n")
            f.write(f"- Primary tag: {item['primary_tag']}\n")
            f.write(f"- All tags: {', '.join(item['all_tags'])}\n")
            f.write(f"- Mutation profile: {item['mutation_profile']}\n")
            f.write(f"- Priority operators: {', '.join(item['priority_operators'])}\n")
            f.write(f"- File: `{item['file']}`\n\n")

    print(f"Classified {len(results)} docs.")
    print(json_path)
    print(csv_path)
    print(summary_path)


if __name__ == "__main__":
    main()
