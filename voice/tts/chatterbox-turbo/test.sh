#!/bin/bash
set -e

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Variables
# Edit these, or override them when running the script.
TEXT=${TEXT:-"Let's begin. Meeting summary. We agreed to keep transcription local. The next action is to improve recording reliability."}

# The default voice is a conds.safetensors file inside the model repo, so no voice flag is needed.
"${PYTHON:-$SCRIPT_DIR/../../.venv/bin/python}" -m mlx_audio.tts.generate \
  --model "mlx-community/chatterbox-turbo-fp16" \
  --text "$TEXT" \
  --audio_format wav \
  --output_path audio/tts \
  --file_prefix "chatterbox-turbo-test-$(date -u +"%Y%m%d-%H%M%S")" \
  --join_audio \
  --verbose
