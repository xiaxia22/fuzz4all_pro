import json
from pathlib import Path
from typing import Any, Dict, List


DEFAULT_CLASSIFICATION_PATH = (
    Path("outputs") / "api_classification" / "java_api_5d_classification.json"
)

PROFILE_ORDER = [
    "RESOURCE",
    "BUFFER",
    "BATCH_OP",
    "MARK_SUPPORT",
    "FILE",
    "CONCURRENT",
    "SECURITY",
    "REFLECT",
    "CALLBACK",
    "TIME",
    "NETWORK",
    "UTILITY",
    "JVM_MGMT",
    "GENERIC",
]

FALLBACK_PROFILE = "GENERIC"

DOMAIN_PRIMARY_PREFERENCE = [
    "SECURITY",
    "REFLECT",
    "FILE",
    "CONCURRENT",
    "NETWORK",
    "CALLBACK",
    "TIME",
    "JVM_MGMT",
    "UTILITY",
]

MUTATION_PROFILE_DEFINITIONS: Dict[str, Dict[str, Any]] = {
    "resource_buffer_batch": {
        "active_profiles": ["RESOURCE", "BUFFER", "BATCH_OP", "MARK_SUPPORT"],
        "description": "Resource/buffer heavy APIs that benefit from lifecycle and bulk-operation mutations.",
    },
    "file_path_state": {
        "active_profiles": ["FILE", "RESOURCE"],
        "description": "File/path APIs that stress state transitions and path boundaries.",
    },
    "concurrent_sequence": {
        "active_profiles": ["CONCURRENT", "CALLBACK"],
        "description": "Concurrent APIs that stress ordering, registration, and scheduling.",
    },
    "security_provider_flow": {
        "active_profiles": ["SECURITY", "UTILITY"],
        "description": "Security APIs with provider/algorithm selection pressure.",
    },
    "reflection_dispatch": {
        "active_profiles": ["REFLECT", "UTILITY"],
        "description": "Reflection APIs with accessibility and member-resolution pressure.",
    },
    "callback_registration_flow": {
        "active_profiles": ["CALLBACK", "UTILITY"],
        "description": "Listener and callback APIs with registration ordering pressure.",
    },
    "time_boundary_mix": {
        "active_profiles": ["TIME", "UTILITY"],
        "description": "Time APIs with epoch, zone, and sign-boundary pressure.",
    },
    "network_endpoint_state": {
        "active_profiles": ["NETWORK", "RESOURCE"],
        "description": "Network/socket APIs with endpoint and timeout state pressure.",
    },
    "utility_value_boundary": {
        "active_profiles": ["UTILITY", "GENERIC"],
        "description": "Utility-style APIs driven by value parsing and formatting boundaries.",
    },
    "jvm_mgmt_runtime_state": {
        "active_profiles": ["JVM_MGMT", "UTILITY"],
        "description": "JVM management APIs that expose runtime and MXBean state transitions.",
    },
    "mark_reset_sequence": {
        "active_profiles": ["MARK_SUPPORT", "BUFFER", "RESOURCE"],
        "description": "Mark/reset capable APIs that benefit from lifecycle and limit mutations.",
    },
    "generic_java": {
        "active_profiles": ["GENERIC"],
        "description": "Fallback generic Java boundary profile.",
    },
}

PROFILE_CATALOG: Dict[str, Dict[str, Any]] = {
    "RESOURCE": {
        "profile_class": "RESOURCE",
        "description": "Lifecycle-oriented APIs such as streams, readers, writers, and sessions.",
        "risk_points": [
            "resource_lifecycle",
            "close_flush_order",
            "wrapper_nesting",
        ],
        "priority_operators": [
            "resource_constructor_edge",
            "resource_lifecycle_sequence",
            "resource_wrapper_depth",
            "resource_exception_shell",
        ],
        "repair_rules": {
            "byte_literal_cast": True,
            "imports": ["java.util.Arrays;"],
        },
        "filter_rules": {
            "reject_tokens": [
                ".size()",
                ".getBuffer()",
                ".getBufSize()",
                ".getBufferSize()",
                ".isClosed()",
                "DEFAULT_BUFFER_SIZE",
                "defaultBufferSize",
            ],
            "reject_patterns": [
                r"\.write\([^\n;]*\)\s*==",
                r"\bwrite\s*\(\s*new\s+FileOutputStream\(",
                r"\bwrite\s*\(\s*new\s+ByteArrayOutputStream\(",
                r"\bwrite\s*\(\s*System\.out\s*,",
            ],
        },
    },
    "BUFFER": {
        "profile_class": "BUFFER",
        "description": "Buffer-like APIs whose core behavior depends on capacity and slice boundaries.",
        "risk_points": [
            "buffer_size_boundary",
            "offset_length_window",
            "shared_backing_array",
        ],
        "priority_operators": [
            "buffer_write_bulk_edge",
            "buffer_write_single_edge",
            "buffer_array_alias_mutation",
            "buffer_length_constant_mutation",
        ],
        "repair_rules": {
            "byte_literal_cast": True,
            "imports": ["java.util.Arrays;"],
        },
        "filter_rules": {
            "reject_tokens": [
                "largeOffsetArray",
            ],
            "reject_patterns": [],
        },
    },
    "BATCH_OP": {
        "profile_class": "BATCH_OP",
        "description": "APIs dominated by off/len style batched operations.",
        "risk_points": [
            "zero_length_batch",
            "negative_offset_or_length",
            "oversized_batch",
        ],
        "priority_operators": [
            "buffer_write_bulk_edge",
            "buffer_length_constant_mutation",
        ],
        "repair_rules": {
            "byte_literal_cast": True,
            "imports": [],
        },
        "filter_rules": {"reject_tokens": [], "reject_patterns": []},
    },
    "FILE": {
        "profile_class": "FILE",
        "description": "Path and file state APIs.",
        "risk_points": ["path_state", "existence_transition", "permission_transition"],
        "priority_operators": [
            "file_path_traversal_mutation",
            "file_state_transition_mutation",
            "file_permission_toggle_mutation",
        ],
        "repair_rules": {
            "byte_literal_cast": True,
            "imports": [
                "java.io.File;",
                "java.io.IOException;",
                "java.nio.file.Path;",
                "java.nio.file.Paths;",
                "java.nio.file.Files;",
            ],
        },
        "filter_rules": {
            "reject_tokens": [],
            "reject_patterns": [
                r"\\x[0-9A-Fa-f]{2}",
                r"new\s+File\s*\(\s*null\s*,",
            ],
        },
    },
    "CONCURRENT": {
        "profile_class": "CONCURRENT",
        "description": "Threading and scheduling APIs.",
        "risk_points": ["interleaving_order", "shared_state", "lifecycle_state"],
        "priority_operators": [
            "concurrent_yield_injection",
            "concurrent_thread_wrapper_mutation",
            "concurrent_signal_sequence_mutation",
        ],
        "repair_rules": {"byte_literal_cast": True, "imports": []},
        "filter_rules": {
            "reject_tokens": [],
            "reject_patterns": [
                r"while\s*\(\s*true\s*\)",
                r"for\s*\(\s*;;\s*\)",
                r"Thread\.sleep\s*\(\s*Long\.MAX_VALUE",
            ],
        },
    },
    "SECURITY": {
        "profile_class": "SECURITY",
        "description": "Security, crypto, and provider-related APIs.",
        "risk_points": ["provider_selection", "algorithm_boundary", "permission_path"],
        "priority_operators": [
            "security_algorithm_boundary_mutation",
            "security_provider_mutation",
            "security_material_boundary_mutation",
        ],
        "repair_rules": {"byte_literal_cast": True, "imports": []},
        "filter_rules": {"reject_tokens": [], "reject_patterns": []},
    },
    "REFLECT": {
        "profile_class": "REFLECT",
        "description": "Reflection-oriented APIs for fields, methods, and constructors.",
        "risk_points": ["accessibility", "receiver_type", "invocation_signature"],
        "priority_operators": [
            "reflect_accessibility_flip_mutation",
            "reflect_member_name_mutation",
            "reflect_receiver_null_mutation",
        ],
        "repair_rules": {
            "byte_literal_cast": True,
            "imports": [
                "java.lang.reflect.Method;",
                "java.lang.reflect.Field;",
                "java.lang.reflect.Constructor;",
                "java.util.Map;",
                "java.util.List;",
                "java.util.Arrays;",
                "java.util.HashMap;",
            ],
        },
        "filter_rules": {
            "reject_tokens": ["sun.reflect"],
            "reject_patterns": [
                r"@(?!Override|SuppressWarnings|Deprecated|FunctionalInterface|SafeVarargs|Serial)\b[A-Z][a-zA-Z]+\b",
                r"\bdefault\s+(?:void|int|long|boolean|String|double|float)\s+\w+\s*\(",
                r"public\s+\w+\s+\w+\s*<[A-Z]>\s*\(",
            ],
        },
    },
    "CALLBACK": {
        "profile_class": "CALLBACK",
        "description": "Listener, handler, and event registration APIs.",
        "risk_points": ["registration_order", "duplicate_registration", "reentrant_callback"],
        "priority_operators": [
            "callback_duplicate_registration_mutation",
            "callback_order_reversal_mutation",
            "callback_null_event_mutation",
        ],
        "repair_rules": {
            "byte_literal_cast": True,
            "imports": [
                "java.beans.PropertyChangeEvent;",
                "java.beans.PropertyChangeListener;",
                "java.beans.PropertyChangeSupport;",
            ],
        },
        "filter_rules": {
            "reject_tokens": [],
            "reject_patterns": [
                r"addIndexedPropertyChangeListener",
                r"removeIndexedPropertyChangeListener",
            ],
        },
    },
    "TIME": {
        "profile_class": "TIME",
        "description": "Date, duration, instant, and zone APIs.",
        "risk_points": ["epoch_extreme", "timezone_boundary", "duration_sign"],
        "priority_operators": [
            "time_epoch_boundary_mutation",
            "time_duration_sign_mutation",
            "time_zone_boundary_mutation",
        ],
        "repair_rules": {"byte_literal_cast": True, "imports": []},
        "filter_rules": {"reject_tokens": [], "reject_patterns": []},
    },
    "NETWORK": {
        "profile_class": "NETWORK",
        "description": "Socket, URL, URI, and HTTP style APIs.",
        "risk_points": ["bind_connect_order", "timeout_boundary", "endpoint_state"],
        "priority_operators": [
            "network_endpoint_boundary_mutation",
            "network_timeout_boundary_mutation",
            "network_sequence_mutation",
        ],
        "repair_rules": {"byte_literal_cast": True, "imports": []},
        "filter_rules": {"reject_tokens": [], "reject_patterns": []},
    },
    "UTILITY": {
        "profile_class": "UTILITY",
        "description": "Utility-style APIs for parsing, formatting, and value manipulation.",
        "risk_points": ["parse_boundary", "format_boundary", "value_aliasing"],
        "priority_operators": [
            "utility_parse_boundary_mutation",
            "utility_format_boundary_mutation",
            "utility_collection_seed_mutation",
        ],
        "repair_rules": {"byte_literal_cast": True, "imports": ["java.util.Locale;"]},
        "filter_rules": {"reject_tokens": [], "reject_patterns": []},
    },
    "JVM_MGMT": {
        "profile_class": "JVM_MGMT",
        "description": "JVM runtime and management bean APIs.",
        "risk_points": ["mxbean_name", "runtime_snapshot", "management_query"],
        "priority_operators": [
            "jvm_mgmt_query_name_mutation",
            "jvm_mgmt_runtime_toggle_mutation",
            "jvm_mgmt_sampling_boundary_mutation",
        ],
        "repair_rules": {
            "byte_literal_cast": True,
            "imports": [
                "java.lang.management.ManagementFactory;",
                "java.lang.management.MemoryMXBean;",
                "java.lang.management.ThreadMXBean;",
                "java.lang.management.ClassLoadingMXBean;",
                "java.lang.management.RuntimeMXBean;",
                "java.lang.management.CompilationMXBean;",
                "java.lang.management.MemoryUsage;",
                "javax.management.ObjectName;",
            ],
        },
        "filter_rules": {"reject_tokens": [], "reject_patterns": []},
    },
    "MARK_SUPPORT": {
        "profile_class": "MARK_SUPPORT",
        "description": "Stream/reader APIs with mark/reset semantics.",
        "risk_points": ["mark_limit", "reset_without_mark", "mark_position_reuse"],
        "priority_operators": [
            "mark_support_limit_mutation",
            "mark_support_reset_mutation",
            "mark_support_reuse_mutation",
        ],
        "repair_rules": {"byte_literal_cast": True, "imports": []},
        "filter_rules": {"reject_tokens": [], "reject_patterns": []},
    },
    "GENERIC": {
        "profile_class": "GENERIC",
        "description": "Generic Java fallback mutations for null, numeric, and sequence boundaries.",
        "risk_points": ["general_null", "general_numeric", "general_sequence"],
        "priority_operators": [
            "generic_null_boundary",
            "generic_numeric_boundary",
            "generic_sequence_reorder",
        ],
        "repair_rules": {"byte_literal_cast": True, "imports": []},
        "filter_rules": {"reject_tokens": [], "reject_patterns": []},
    },
}


def _normalize_relpath(path: str) -> str:
    return str(path or "").replace("\\", "/")


def _normalize_identifier(value: str) -> str:
    return _normalize_relpath(str(value or "")).lower()


def _context_domain_hints(target_api: str, doc_path: str) -> List[str]:
    context = _normalize_identifier(f"{target_api} {doc_path}")
    hints = []
    hint_rules = [
        (
            "SECURITY",
            [
                ".crypto",
                ".security",
                ".ssl",
                ".auth",
                ".cert",
                "cipher",
                "signature",
                "digest",
                "keystore",
                "secretkey",
                "keypair",
                "trustmanager",
                "keymanager",
                "mac",
            ],
        ),
        (
            "REFLECT",
            [
                ".reflect",
                ".lang.reflect",
                "accessibleobject",
                "invocationhandler",
                "proxy",
                # Intentionally excludes generic words like "method", "field", "constructor"
                # to avoid false positives on non-reflection APIs.
            ],
        ),
        (
            "FILE",
            [
                ".nio.file",
                ".io.file",
                "watchservice",
                "filestore",
                "filesystem",
                "path",
                "files",
            ],
        ),
        (
            "CONCURRENT",
            [
                ".concurrent",
                "thread",
                "executor",
                "lock",
                "future",
                "callable",
                "runnable",
                "semaphore",
            ],
        ),
        (
            "NETWORK",
            [".net", ".http", "httpclient", "socket", "serversocket", "url", "uri", "inet", "datagram"],
        ),
        ("CALLBACK", [".event", ".awt.event", ".beans", "listener", "callback", "handler", "event"]),
        ("TIME", [".time", "date", "instant", "duration", "period", "zone", "clock"]),
        ("JVM_MGMT", [".management", "mxbean", "managementfactory", "memory", "threadmxbean", "runtime"]),
        ("UTILITY", [".util", "formatter", "optional", "arrays", "objects", "math", "string"]),
    ]
    for tag, keywords in hint_rules:
        if any(keyword in context for keyword in keywords):
            hints.append(tag)
    return hints


def _ordered_profiles(primary_tag: str, all_tags: List[str]) -> List[str]:
    ordered = []
    if primary_tag in PROFILE_ORDER:
        ordered.append(primary_tag)
    for tag in all_tags or []:
        if tag in PROFILE_ORDER and tag not in ordered:
            ordered.append(tag)
    if not ordered:
        ordered.append(FALLBACK_PROFILE)
    return ordered


def _choose_primary_tag(
    primary_tag: str,
    all_tags: List[str],
    classification_scores: Dict[str, Any],
    target_api: str,
    doc_path: str,
) -> str:
    if primary_tag in DOMAIN_PRIMARY_PREFERENCE:
        return primary_tag

    scores = classification_scores or {}
    top_score = scores.get(primary_tag, 0)
    hints = _context_domain_hints(target_api, doc_path)

    for candidate in hints:
        if candidate not in all_tags:
            continue
        candidate_score = scores.get(candidate, 0)
        if candidate_score >= max(4, top_score - 3):
            return candidate

    for candidate in DOMAIN_PRIMARY_PREFERENCE:
        if candidate not in all_tags:
            continue
        candidate_score = scores.get(candidate, 0)
        if candidate_score >= max(5, top_score - 2):
            return candidate

    return primary_tag


def _derive_mutation_profile(
    primary_tag: str,
    all_tags: List[str],
    classification_scores: Dict[str, Any],
    target_api: str,
    doc_path: str,
) -> str:
    tags = set(all_tags or [])
    hints = set(_context_domain_hints(target_api, doc_path))

    if primary_tag == "SECURITY" or "SECURITY" in hints:
        return "security_provider_flow"
    if primary_tag == "REFLECT" or "REFLECT" in hints:
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
    if primary_tag == "FILE" or "FILE" in hints:
        return "file_path_state"
    if primary_tag == "CONCURRENT" or "CONCURRENT" in hints:
        return "concurrent_sequence"
    if primary_tag in {"RESOURCE", "BUFFER"} and (
        "BUFFER" in tags or "BATCH_OP" in tags or "MARK_SUPPORT" in tags
    ):
        return "resource_buffer_batch"
    if primary_tag == "BATCH_OP":
        if "SECURITY" in tags or "SECURITY" in hints:
            return "security_provider_flow"
        if "RESOURCE" in tags or "BUFFER" in tags or "MARK_SUPPORT" in tags:
            return "resource_buffer_batch"
    if primary_tag == "GENERIC":
        if "SECURITY" in hints:
            return "security_provider_flow"
        if "REFLECT" in hints:
            return "reflection_dispatch"
        if "FILE" in hints:
            return "file_path_state"
        if "CONCURRENT" in hints:
            return "concurrent_sequence"
    return "generic_java"


def _resolve_active_profiles(
    mutation_profile: str, primary_tag: str, all_tags: List[str]
) -> List[str]:
    ordered = []
    profile_definition = MUTATION_PROFILE_DEFINITIONS.get(mutation_profile or "")
    if profile_definition is not None:
        for profile_name in profile_definition.get("active_profiles", []):
            if profile_name in PROFILE_ORDER and profile_name not in ordered:
                ordered.append(profile_name)
    for profile_name in _ordered_profiles(primary_tag, all_tags):
        if profile_name not in ordered:
            ordered.append(profile_name)
    if not ordered:
        ordered.append(FALLBACK_PROFILE)
    return ordered


def _merge_profile_details(active_profiles: List[str]) -> Dict[str, Any]:
    merged = {
        "active_profiles": active_profiles,
        "primary_profile": active_profiles[0],
        "secondary_profiles": active_profiles[1:3],
        "priority_operators": [],
        "risk_points": [],
        "repair_rules": {
            "byte_literal_cast": False,
            "imports": [],
        },
        "filter_rules": {
            "reject_tokens": [],
            "reject_patterns": [],
        },
        "profile_details": {},
    }

    seen_operators = set()
    seen_risks = set()
    seen_imports = set()
    seen_reject_tokens = set()
    seen_reject_patterns = set()

    for profile_name in active_profiles:
        detail = PROFILE_CATALOG.get(profile_name)
        if detail is None:
            continue
        merged["profile_details"][profile_name] = detail

        for operator in detail.get("priority_operators", []):
            if operator not in seen_operators:
                seen_operators.add(operator)
                merged["priority_operators"].append(operator)

        for risk_point in detail.get("risk_points", []):
            if risk_point not in seen_risks:
                seen_risks.add(risk_point)
                merged["risk_points"].append(risk_point)

        repair_rules = detail.get("repair_rules", {})
        if repair_rules.get("byte_literal_cast"):
            merged["repair_rules"]["byte_literal_cast"] = True
        for import_line in repair_rules.get("imports", []):
            if import_line not in seen_imports:
                seen_imports.add(import_line)
                merged["repair_rules"]["imports"].append(import_line)

        filter_rules = detail.get("filter_rules", {})
        for token in filter_rules.get("reject_tokens", []):
            if token not in seen_reject_tokens:
                seen_reject_tokens.add(token)
                merged["filter_rules"]["reject_tokens"].append(token)
        for pattern in filter_rules.get("reject_patterns", []):
            if pattern not in seen_reject_patterns:
                seen_reject_patterns.add(pattern)
                merged["filter_rules"]["reject_patterns"].append(pattern)

    return merged


def load_mutation_profile(config_dict: Dict[str, Any]) -> Dict[str, Any]:
    target_cfg = config_dict.get("target", {})
    target_api = target_cfg.get("target_string", "")
    doc_path = _normalize_relpath(target_cfg.get("path_documentation", ""))
    configured_path = target_cfg.get("path_classification_result")
    profile_override = str(target_cfg.get("mutation_profile_override") or "").strip()
    classification_path = (
        Path(configured_path) if configured_path else DEFAULT_CLASSIFICATION_PATH
    )

    default_mutation_profile = "generic_java"
    default_profiles = _resolve_active_profiles(
        default_mutation_profile, FALLBACK_PROFILE, [FALLBACK_PROFILE]
    )
    profile = {
        "target_api": target_api,
        "documentation_file": doc_path,
        "primary_tag": FALLBACK_PROFILE,
        "all_tags": [FALLBACK_PROFILE],
        "classification_scores": {},
        "mutation_profile": default_mutation_profile,
    }
    profile.update(_merge_profile_details(default_profiles))

    if not classification_path.exists():
        return profile

    try:
        items = json.loads(classification_path.read_text(encoding="utf-8"))
    except Exception:
        return profile

    matched = None
    for item in items:
        item_file = _normalize_relpath(item.get("file", ""))
        if doc_path and item_file == doc_path:
            matched = item
            break
        if target_api and item.get("api_name") == target_api:
            matched = item
            break

    if not matched:
        return profile

    all_tags = matched.get("all_tags") or [matched.get("primary_tag", FALLBACK_PROFILE)]
    classification_scores = matched.get("scores", {})
    primary_tag = _choose_primary_tag(
        matched.get("primary_tag", FALLBACK_PROFILE),
        all_tags,
        classification_scores,
        target_api or matched.get("api_name", ""),
        doc_path or _normalize_relpath(matched.get("file", "")),
    )
    all_tags = [primary_tag] + [tag for tag in all_tags if tag != primary_tag]
    derived_mutation_profile = _derive_mutation_profile(
        primary_tag,
        all_tags,
        classification_scores,
        target_api or matched.get("api_name", ""),
        doc_path or _normalize_relpath(matched.get("file", "")),
    )
    if profile_override:
        if profile_override in MUTATION_PROFILE_DEFINITIONS:
            # Override is a profile name (e.g. "resource_buffer_batch"): use directly,
            # primary_tag stays as derived from classification.
            mutation_profile = profile_override
        elif profile_override in PROFILE_ORDER:
            # Override is a classification tag (e.g. "RESOURCE"): update primary_tag
            # and re-derive a matching mutation profile.
            primary_tag = profile_override
            all_tags = [profile_override] + [
                tag for tag in all_tags if tag != profile_override
            ]
            mutation_profile = _derive_mutation_profile(
                primary_tag,
                all_tags,
                classification_scores,
                target_api or matched.get("api_name", ""),
                doc_path or _normalize_relpath(matched.get("file", "")),
            )
        else:
            mutation_profile = derived_mutation_profile
    else:
        mutation_profile = (
            matched.get("mutation_profile")
            if matched.get("mutation_profile") not in ("", None, "generic_java")
            else derived_mutation_profile
        )
    active_profiles = _resolve_active_profiles(
        mutation_profile,
        primary_tag,
        all_tags,
    )

    profile.update(
        {
            "target_api": target_api or matched.get("api_name", ""),
            "documentation_file": doc_path
            or _normalize_relpath(matched.get("file", "")),
            "primary_tag": primary_tag,
            "all_tags": all_tags,
            "classification_scores": classification_scores,
            "mutation_profile": mutation_profile,
        }
    )
    profile.update(_merge_profile_details(active_profiles))
    return profile
