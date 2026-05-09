#!/usr/bin/env bash
set -euo pipefail

MODEL_NAME="${1:-ollama/qwen2.5:7b}"
OUTPUT_ROOT="${2:-outputs/targeted200}"
JVMGMT_MODE="${3:-handwritten}"  # handwritten | autoprompt

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

if command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
  PYTHON_BIN="python"
else
  echo "python3/python not found" >&2
  exit 1
fi

TEMP_CONFIG_DIR="$REPO_ROOT/config/targeted_200_temp"
mkdir -p "$TEMP_CONFIG_DIR"
mkdir -p "$REPO_ROOT/$OUTPUT_ROOT"

TARGETS=(
  "java.base_java_io_BufferedInputStream.yaml"
  "java.base_java_io_File.yaml"
  "java.base_java_lang_Thread.yaml"
  "java.base_java_lang_reflect_Method.yaml"
  "java.base_java_net_Socket.yaml"
  "java.base_java_net_URI.yaml"
  "java.base_java_time_Duration.yaml"
  "java.base_javax_crypto_Cipher.yaml"
  "java.desktop_java_beans_PropertyChangeSupport.yaml"
)

if [[ "$JVMGMT_MODE" == "autoprompt" ]]; then
  TARGETS+=("java.management_java_lang_management_ManagementFactory_autoprompt.yaml")
else
  TARGETS+=("java.management_java_lang_management_ManagementFactory.yaml")
fi

for target in "${TARGETS[@]}"; do
  source_path="$REPO_ROOT/config/targeted/$target"
  base_name="${target%.yaml}"
  dest_path="$TEMP_CONFIG_DIR/$target"
  run_output="$OUTPUT_ROOT/$base_name"

  "$PYTHON_BIN" - "$source_path" "$dest_path" "$run_output" <<'PY'
import pathlib
import re
import sys

source_path = pathlib.Path(sys.argv[1])
dest_path = pathlib.Path(sys.argv[2])
run_output = sys.argv[3].replace("\\", "/")

text = source_path.read_text(encoding="utf-8")

replacements = [
    (r"(?m)^(\s*num:\s*)\d+", r"\g<1>200"),
    (r"(?m)^(\s*resume:\s*)(true|false)", r"\g<1>false"),
    (r"(?m)^(\s*output_folder:\s*).+$", rf"\g<1>{run_output}"),
    (r"(?m)^(\s*temperature:\s*)[\d.]+", r"\g<1>0.9"),
    (r"(?m)^(\s*autoprompt_candidates:\s*)\d+", r"\g<1>4"),
    (r"(?m)^(\s*autoprompt_temperature:\s*)[\d.]+", r"\g<1>0.7"),
    (r"(?m)^(\s*autoprompt_validation_batch_size:\s*)\d+", r"\g<1>10"),
    (r"(?m)^(\s*runtime_autoprompt_temperature:\s*)[\d.]+", r"\g<1>0.6"),
    (r"(?m)^(\s*runtime_refresh_validation_batch_size:\s*)\d+", r"\g<1>5"),
]

for pattern, replacement in replacements:
    text = re.sub(pattern, replacement, text)

dest_path.write_text(text, encoding="utf-8")
PY

  echo "=== Running $base_name ==="
  echo "Config: $dest_path"
  echo "Output: $run_output"

  "$PYTHON_BIN" Fuzz4All/fuzz.py \
    --config "$dest_path" \
    main_with_config \
    --folder "$run_output" \
    --model_name "$MODEL_NAME" \
    --target javac
done

echo "All 10 targeted runs completed."
