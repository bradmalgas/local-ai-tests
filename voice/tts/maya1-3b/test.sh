#!/bin/bash
set -e

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Variables
# Edit these, or override them when running the script.
# Maya1 has no built-in voices. VOICE is a text description of the voice, not a name.
# It keeps the name VOICE so every model's test.sh can run with the same command.
TEXT=${TEXT:-"Let's begin. Meeting summary. We agreed to keep transcription local. The next action is to improve recording reliability."}
VOICE=${VOICE:-"A young American woman in her mid-twenties, with a warm, friendly, conversational voice. Medium pitch, natural pace, clear and relaxed."}

# Known problem: the mlx-community/maya1-4bit repo has two extra bf16 files,
# model-00001-of-00002.safetensors and model-00002-of-00002.safetensors - they need to be excluded from the download for the model to run.
# More details are in ../README.md under "Known problems".
PYTHON=${PYTHON:-$SCRIPT_DIR/../../.venv/bin/python}
MODEL_DIR=$("$PYTHON" -m huggingface_hub.cli.hf download mlx-community/maya1-4bit \
  --exclude "model-0000*-of-00002.safetensors" --format quiet)

"$PYTHON" -m mlx_audio.tts.generate \
  --model "$MODEL_DIR" \
  --text "<description=\"${VOICE}\"> ${TEXT}" \
  --temperature 0.6 \
  --repetition_penalty 1.1 \
  --audio_format wav \
  --output_path audio/tts \
  --file_prefix "maya1-4bit-test-$(date -u +"%Y%m%d-%H%M%S")" \
  --join_audio \
  --verbose
