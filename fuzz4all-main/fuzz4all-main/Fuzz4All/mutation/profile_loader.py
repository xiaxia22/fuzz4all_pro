import json
from pathlib import Path
from typing import Any, Dict, List


DEFAULT_CLASSIFICATION_PATH = (
    Path("outputs") / "api_classification" / "java_api_5d_classification.json"
)


def _normalize_relpath(path: str) -> str:
    return str(path or "").replace("\\", "/")


def _profile_from_tags(primary_tag: str, all_tags: List[str]) -> Dict[str, Any]:
    tags = list(all_tags or [])
    primary = primary_tag or (tags[0] if tags else "GENERIC")

    if primary == "RESOURCE" and ("BUFFER" in tags or "BATCH_OP" in tags):
        return {
            "mutation_profile": "resource_buffer_batch",
            "priority_operators": [
                "constructor_size_edge",
                "write_bulk_edge",
                "lifecycle_sequence",
                "write_single_edge",
            ],
            "risk_points": [
                "resource_lifecycle",
                "buffer_size_boundary",
                "write_offset_length",
            ],
        }
    if primary == "FILE":
        return {
            "mutation_profile": "file_path_state",
            "priority_operators": [
                "constructor_size_edge",
                "lifecycle_sequence",
            ],
            "risk_points": ["file_state_transition", "path_argument"],
        }
    if primary == "CONCURRENT":
        return {
            "mutation_profile": "concurrent_sequence",
            "priority_operators": [
                "lifecycle_sequence",
                "write_single_edge",
            ],
            "risk_points": ["interleaving_order", "shared_state"],
        }
    return {
        "mutation_profile": "generic_java",
        "priority_operators": [
            "constructor_size_edge",
            "write_single_edge",
        ],
        "risk_points": ["general_boundary"],
    }


def load_mutation_profile(config_dict: Dict[str, Any]) -> Dict[str, Any]:
    target_cfg = config_dict.get("target", {})
    target_api = target_cfg.get("target_string", "")
    doc_path = _normalize_relpath(target_cfg.get("path_documentation", ""))
    configured_path = target_cfg.get("path_classification_result")
    classification_path = Path(configured_path) if configured_path else DEFAULT_CLASSIFICATION_PATH

    profile = {
        "target_api": target_api,
        "documentation_file": doc_path,
        "primary_tag": "GENERIC",
        "all_tags": ["GENERIC"],
    }
    profile.update(_profile_from_tags("GENERIC", ["GENERIC"]))

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

    all_tags = matched.get("all_tags") or [matched.get("primary_tag", "GENERIC")]
    computed = _profile_from_tags(matched.get("primary_tag", "GENERIC"), all_tags)

    profile.update(
        {
            "target_api": target_api or matched.get("api_name", ""),
            "documentation_file": doc_path or _normalize_relpath(matched.get("file", "")),
            "primary_tag": matched.get("primary_tag", "GENERIC"),
            "all_tags": all_tags,
            "secondary_tags": all_tags[1:3],
            "classification_scores": matched.get("scores", {}),
        }
    )
    profile.update(computed)
    if matched.get("mutation_profile"):
        profile["mutation_profile"] = matched["mutation_profile"]
    if matched.get("priority_operators"):
        profile["priority_operators"] = matched["priority_operators"]
    if matched.get("risk_points"):
        profile["risk_points"] = matched["risk_points"]
    return profile
