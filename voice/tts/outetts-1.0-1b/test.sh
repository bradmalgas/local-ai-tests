#!/bin/bash
set -e

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Variables
# Edit these, or override them when running the script.
TEXT=${TEXT:-"Let's begin. Meeting summary. We agreed to keep transcription local. The next action is to improve recording reliability."}

# Notes (more in README.md):
# - No voice flag. OuteTTS only has one built-in speaker. In mlx_audio, --voice must be a speaker file, not a name.
# - --temperature 0.4 is needed. The mlx_audio command line passes 0.7 by default, and the voice sighs and rushes.
# - --max_tokens 4096 is needed. The default of 1200 cuts speech off after about 7 seconds.
"${PYTHON:-$SCRIPT_DIR/../../.venv/bin/python}" -m mlx_audio.tts.generate \
  --model "mlx-community/Llama-OuteTTS-1.0-1B-fp16" \
  --text "$TEXT" \
  --temperature 0.4 \
  --audio_format wav \
  --output_path audio/tts \
  --file_prefix "outeTTS-1b-test-$(date -u +"%Y%m%d-%H%M%S")" \
  --join_audio \
  --max_tokens 4096 \
  --verbose
