#!/usr/bin/env bash

set -euo pipefail

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <dimension> <group>"
  echo "Example: $0 primary_tag SECURITY"
  echo "Example: $0 package javax.crypto"
  exit 1
fi

DIMENSION="$1"
GROUP="$2"
ROOT_DIR="${ROOT_DIR:-$(pwd)}"
MANIFEST_PATH="$ROOT_DIR/config/targeted_groups/$DIMENSION/$GROUP.txt"

if [ ! -f "$MANIFEST_PATH" ]; then
  echo "Manifest not found: $MANIFEST_PATH"
  echo "Run: python scripts/build_targeted_manifests.py"
  exit 1
fi

MODEL_NAME="${FUZZING_MODEL:-ollama/qwen2.5:7b}"
BATCH_SIZE="${FUZZING_BATCH_SIZE:-5}"
TARGET_CMD="${FUZZING_TARGET:-javac}"
OFFSET="${GROUP_OFFSET:-0}"
LIMIT="${GROUP_LIMIT:-0}"
SKIP_EXISTING="${SKIP_EXISTING:-1}"

echo "DIMENSION: $DIMENSION"
echo "GROUP: $GROUP"
echo "MODEL_NAME: $MODEL_NAME"
echo "BATCH_SIZE: $BATCH_SIZE"
echo "TARGET_CMD: $TARGET_CMD"
echo "OFFSET: $OFFSET"
echo "LIMIT: $LIMIT"
echo "MANIFEST: $MANIFEST_PATH"

index=0
ran=0

while IFS= read -r config_path || [ -n "$config_path" ]; do
  if [ -z "$config_path" ]; then
    continue
  fi

  index=$((index + 1))
  if [ "$index" -le "$OFFSET" ]; then
    continue
  fi

  config_name="$(basename "$config_path" .yaml)"
  output_dir="$ROOT_DIR/outputs/grouped/$DIMENSION/$GROUP/$config_name"

  if [ "$SKIP_EXISTING" = "1" ] && [ -d "$output_dir" ] && [ -f "$output_dir/prompts/best_prompt.txt" ]; then
    echo "[skip] $config_name"
    continue
  fi

  echo "[run] $config_name"
  python "$ROOT_DIR/Fuzz4All/fuzz.py" \
    --config "$config_path" \
    main_with_config \
    --folder "$output_dir" \
    --batch_size "$BATCH_SIZE" \
    --model_name "$MODEL_NAME" \
    --target "$TARGET_CMD"

  ran=$((ran + 1))
  if [ "$LIMIT" -gt 0 ] && [ "$ran" -ge "$LIMIT" ]; then
    break
  fi
done < "$MANIFEST_PATH"

echo "Completed $ran run(s) from group $GROUP"
