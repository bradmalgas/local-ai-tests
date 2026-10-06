#!/bin/bash
set -e

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Variables
# Edit these, or override them when running the script.
# Breeze has no built-in voices. VOICE is a text description of the voice, not a name.
# It keeps the name VOICE so every model's test.sh can run with the same command.
TEXT=${TEXT:-"Let's begin. Meeting summary. We agreed to keep transcription local. The next action is to improve recording reliability."}
VOICE=${VOICE:-"A young American woman in her mid-twenties, with a warm, friendly, conversational voice. Medium pitch, natural pace, clear and relaxed."}

"${PYTHON:-$SCRIPT_DIR/../../.venv/bin/python}" -m mlx_audio.tts.generate \
  --model "mlx-community/Breeze-TTS-2-mlx" \
  --text "$TEXT" \
  --instruct "$VOICE" \
  --cfg_scale 4 \
  --audio_format wav \
  --output_path audio/tts \
  --file_prefix "breeze-tts-2-test-$(date -u +"%Y%m%d-%H%M%S")" \
  --join_audio \
  --verbose
