#!/bin/bash
set -e

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Variables
# Edit these, or override them when running the script.
TEXT=${TEXT:-"Let's begin. Meeting summary. We agreed to keep transcription local. The next action is to improve recording reliability."}
VOICE="${VOICE:-af_heart}"

"${PYTHON:-$SCRIPT_DIR/.venv/bin/python}" -m mlx_audio.tts.generate \
  --model "mlx-community/Kokoro-82M-bf16" \
  --text "$TEXT" \
  --voice "$VOICE" \
  --audio_format wav \
  --output_path audio/tts \
  --file_prefix "kokoro-82M-test-$(date -u +"%Y%m%d-%H%M%S")" \
  --join_audio \
  --lang_code a \
  --verbose
