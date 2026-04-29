import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLASSIFICATION_JSON = ROOT / "outputs" / "api_classification" / "java_api_5d_classification.json"
TARGETED_DIR = ROOT / "config" / "targeted"
OUT_DIR = ROOT / "config" / "targeted_groups"


def ensure_classification() -> list[dict]:
    if not CLASSIFICATION_JSON.exists():
        raise FileNotFoundError(
            f"Missing classification file: {CLASSIFICATION_JSON}. "
            "Run scripts/classify_java_apis.py first."
        )
    return json.loads(CLASSIFICATION_JSON.read_text(encoding="utf-8"))


def doc_to_config(doc_path: str) -> str:
    return doc_path.replace("config/documentation/", "config/targeted/").replace(".md", ".yaml")


def stem_to_module(stem: str) -> str:
    return stem.split("_", 1)[0]


def stem_to_package(stem: str) -> str:
    parts = stem.split("_")
    if len(parts) <= 2:
        return "root"
    return ".".join(parts[1:-1])


def write_manifest(directory: Path, group_name: str, items: list[str]) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    manifest_path = directory / f"{group_name}.txt"
    manifest_path.write_text("\n".join(items) + "\n", encoding="utf-8")


def main() -> None:
    classification = ensure_classification()
    grouped: dict[str, dict[str, list[str]]] = {
        "primary_tag": defaultdict(list),
        "mutation_profile": defaultdict(list),
        "module": defaultdict(list),
        "package": defaultdict(list),
    }

    for item in classification:
        doc_path = item["file"]
        config_path = doc_to_config(doc_path)
        config_abs = ROOT / config_path
        if not config_abs.exists():
            continue

        config_name = Path(config_path).name
        stem = Path(config_name).stem
        grouped["primary_tag"][item["primary_tag"]].append(config_path)
        grouped["mutation_profile"][item["mutation_profile"]].append(config_path)
        grouped["module"][stem_to_module(stem)].append(config_path)
        grouped["package"][stem_to_package(stem)].append(config_path)

    summary_lines = [
        "# Targeted Group Summary",
        "",
        f"- Classification source: `{CLASSIFICATION_JSON.relative_to(ROOT).as_posix()}`",
        f"- Targeted config root: `{TARGETED_DIR.relative_to(ROOT).as_posix()}`",
        "",
    ]

    for dimension, buckets in grouped.items():
        dimension_dir = OUT_DIR / dimension
        summary_lines.append(f"## {dimension}")
        summary_lines.append("")
        for group_name in sorted(buckets):
            items = sorted(buckets[group_name])
            write_manifest(dimension_dir, group_name, items)
            summary_lines.append(f"- {group_name}: {len(items)}")
        summary_lines.append("")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "README.md").write_text("\n".join(summary_lines), encoding="utf-8")

    print("Generated targeted group manifests:")
    for dimension, buckets in grouped.items():
        print(f"- {dimension}: {len(buckets)} groups")


if __name__ == "__main__":
    main()
