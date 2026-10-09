#!/bin/bash
set -e

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Variables
# Edit these, or override them when running the script.
TEXT=${TEXT:-"Let's begin. Meeting summary. We agreed to keep transcription local. The next action is to improve recording reliability."}
VOICE="${VOICE:-tara}"

"${PYTHON:-$SCRIPT_DIR/../../.venv/bin/python}" -m mlx_audio.tts.generate \
  --model "mlx-community/orpheus-3b-0.1-ft-bf16" \
  --text "$TEXT" \
  --voice "$VOICE" \
  --temperature 0.6 \
  --repetition_penalty 1.1 \
  --audio_format wav \
  --output_path audio/tts \
  --file_prefix "orpheus-3b-test-$(date -u +"%Y%m%d-%H%M%S")" \
  --join_audio \
  --verbose
