import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "config" / "documentation"
OUT_DIR = ROOT / "outputs" / "api_classification"


TAG_PRIORITY = [
    "FILE",
    "TIME",
    "CONCURRENT",
    "SECURITY",
    "NETWORK",
    "CALLBACK",
    "REFLECT",
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
    "type": 3,
    "interface": 2,
    "field": 2,
    "method": 2,
    "boundary": 1,
}

TAG_RULES = {
    "RESOURCE": {
        "package": [".io", ".net", "stream", "reader", "writer"],
        "type": ["stream", "reader", "writer", "channel", "session"],
        "interface": ["closeable", "autocloseable", "flushable"],
        "field": ["buf", "count", "out", "in"],
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
        "type": ["bufferedinputstream", "reader"],
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
        "method": ["byte[]", "char[]", "int off", "int len", "offset", "length"],
        "boundary": ["off+len", "0, -1, integer.max_value", "0/-1/max"],
    },
    "CALLBACK": {
        "package": [".event", ".awt.event", ".beans"],
        "type": ["listener", "callback", "handler", "event"],
        "interface": ["eventlistener"],
        "field": [],
        "method": ["listener", "callback", "handler"],
        "boundary": [],
    },
    "CONCURRENT": {
        "package": [".concurrent", ".lang.thread"],
        "type": ["thread", "lock", "executor", "semaphore", "future", "callable", "runnable"],
        "interface": ["runnable", "callable", "future"],
        "field": ["volatile", "atomic"],
        "method": ["synchronized", "lock(", "unlock(", "submit(", "execute("],
        "boundary": ["concurrentmodificationexception"],
    },
    "TIME": {
        "package": [".time"],
        "type": ["date", "time", "instant", "clock", "duration", "zone"],
        "interface": [],
        "field": [],
        "method": ["millis", "epoch", "instant", "clock"],
        "boundary": ["long.max_value", "gmt+14"],
    },
    "FILE": {
        "package": [".io.file", ".nio.file", "java.io.file", "java.nio.file"],
        "type": ["file", "path", "files", "filesystem", "watchservice", "filestore"],
        "interface": [],
        "field": [],
        "method": ["path", "file", "files", "watch", "resolve("],
        "boundary": ["../../", "\\0", "*", "?", "securityexception"],
    },
    "SECURITY": {
        "package": [".security", ".crypto", ".ssl", ".auth", ".cert"],
        "type": ["cipher", "digest", "key", "trustmanager", "keymanager", "permission", "ssl", "tls", "certificate"],
        "interface": [],
        "field": ["provider"],
        "method": ["encrypt", "decrypt", "sign", "verify", "sslpermission", "permission"],
        "boundary": ["provider", "md5", "securityexception"],
    },
    "REFLECT": {
        "package": [".reflect"],
        "type": ["class", "method", "field", "constructor", "loader", "proxy"],
        "interface": [],
        "field": [],
        "method": ["invoke(", "getdeclared", "setaccessible", "newinstance("],
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
        "lifecycle_sequence",
        "write_single_edge",
    ],
    "generic_java": [
        "constructor_size_edge",
        "write_single_edge",
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


def derive_mutation_profile(primary_tag: str, all_tags: list[str]) -> str:
    tags = set(all_tags)
    if primary_tag == "RESOURCE" and ("BUFFER" in tags or "BATCH_OP" in tags):
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

    if not scores:
        scores["GENERIC"] = 1
        evidence["GENERIC"]["boundary"].append("fallback")

    # Generic is also useful as a secondary catch-all when many edge-case words appear.
    generic_keywords = ["nullpointerexception", "integer.max_value", "integer.min_value", "0", "-1", "null"]
    generic_hits = [kw for kw in generic_keywords if kw in dimensions["boundary"]]
    if generic_hits:
        scores["GENERIC"] += len(generic_hits)
        evidence["GENERIC"]["boundary"].extend(generic_hits)

    all_tags = sorted(scores.keys(), key=lambda tag: (-scores[tag], TAG_PRIORITY.index(tag) if tag in TAG_PRIORITY else 999, tag))
    primary_tag = all_tags[0]
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
