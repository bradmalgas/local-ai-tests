#!/bin/bash
set -e

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Variables
# Edit these, or override them when running the script.
TEXT=${TEXT:-"Let's begin. Meeting summary. We agreed to keep transcription local. The next action is to improve recording reliability."}
# Voxtral has preset voices. English ones: casual_male, casual_female, cheerful_female, neutral_male, neutral_female.
# It needs the mlx-audio[tts] extra, which is in voice/requirements.txt.
VOICE="${VOICE:-neutral_female}"

"${PYTHON:-$SCRIPT_DIR/../../.venv/bin/python}" -m mlx_audio.tts.generate \
  --model "mlx-community/Voxtral-4B-TTS-2603-mlx-bf16" \
  --text "$TEXT" \
  --voice "$VOICE" \
  --audio_format wav \
  --output_path audio/tts \
  --file_prefix "voxtral-4B-TTS-test-$(date -u +"%Y%m%d-%H%M%S")" \
  --join_audio \
  --verbose
