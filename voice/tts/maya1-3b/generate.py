#!/usr/bin/env python3

# We could not get the model to run correctly in our test.sh file
# This meant writing a custom script to match the other models
# Credit to: Maya Research, mlx-audio
"""Small python script to run the Maya1 model on MLX"""
import argparse
from pathlib import Path
import mlx.core as mx
from mlx_lm import load
from mlx_lm.generate import generate_step
from mlx_lm.sample_utils import make_logits_processors, make_sampler
from mlx_audio.codec.models.snac import SNAC
from mlx_lm.tokenizer_utils import TokenizerWrapper
import soundfile as sf
import numpy as np

CODE_START_TOKEN_ID = 128257
CODE_END_TOKEN_ID = 128258
CODE_TOKEN_OFFSET = 128266
SNAC_MIN_ID = 128266
SNAC_MAX_ID = 156937
SNAC_TOKENS_PER_FRAME = 7

SOH_ID = 128259
EOH_ID = 128260
SOA_ID = 128261
BOS_ID = 128000
TEXT_EOT_ID = 128009

def build_prompt(tokenizer: TokenizerWrapper, description: str, text: str) -> list[int]:
    """Build formatted prompt for Maya1."""
    formatted_text = f'<description="{description}"> {text}'
    input_token = tokenizer.encode(formatted_text, add_special_tokens=False)
    
    prompt = [
        SOH_ID , BOS_ID , *input_token, TEXT_EOT_ID ,
        EOH_ID , SOA_ID , CODE_START_TOKEN_ID
    ]
    
    return prompt

def main():
    parser = argparse.ArgumentParser(description="Custom Maya1 TTS script")
    parser.add_argument("--model", help="Path to MLX model directory (default: current directory)", required=True)
    parser.add_argument("--text", help="Input text to generate", default="Let's begin. Meeting summary. We agreed to keep transcription local. The next action is to improve recording reliability.")
    parser.add_argument("--voice", default="A young American woman in her mid-twenties, with a warm, friendly, conversational voice. Medium pitch, natural pace, clear and relaxed.", help="Voice description")
    parser.add_argument("--temperature", type=float, default=0.6, help="Sampling temperature (default: 0.6)")
    parser.add_argument("--repetition_penalty", type=float, default=1.1, help="Repetition penalty (default: 1.1)")
    parser.add_argument("--audio_format", default="wav", help="Output audio format (default: wav)")
    parser.add_argument("--output_path", default="audio/tts", help="Output WAV file (default: audio/tts)")
    parser.add_argument("--file_prefix", help="Output file prefix (e.g: maya1-4bit-test-20261006-222840")
    # The bottom two are disabled until I can match the normal test.sh shape OR remove them from test.sh
    # parser.add_argument("--join_audio", type=bool, default=True, help="Whether or not to join the audio to one clip")
    # parser.add_argument("--verbose", type=bool, default=True, help="Detailed logging")
    args = parser.parse_args()

    # 1. Load the model and tokenizer
    print("\n[1/3] Loading Maya1 model...")
    pathToModel = Path(args.model)
    model, tokenizer = load(pathToModel)
    print(f"Model loaded: {len(tokenizer)} tokens in vocabulary")

    # 2. Load SNAC audio decoder (24kHz)
    print("\n[2/3] Loading SNAC audio decoder...")
    snac_model = SNAC.from_pretrained("mlx-community/snac_24khz").eval()
    print("SNAC decoder loaded")

    # 3. Generate speech
    print("\n[3/3] Generating speech...")
    prompt = build_prompt(tokenizer, args.voice, args.text)
    sampler = make_sampler(temp=args.temperature, top_p=0.9) if args.temperature > 0 else None
    logits_processors = None

    if args.repetition_penalty and args.repetition_penalty != 1.0:
        logits_processors = make_logits_processors(repetition_penalty=args.repetition_penalty)


    tokens = []
    for token, _ in generate_step(
        mx.array(prompt), model,
        sampler=sampler,
        logits_processors=logits_processors,
        max_tokens=4096
    ):
        token_id = token.item() if hasattr(token, "item") else int(token)
        if token_id == CODE_END_TOKEN_ID:
            break
        tokens.append(token_id)
    snac_count = sum(1 for t in tokens if SNAC_MIN_ID <= t <= SNAC_MAX_ID)
    print(f"Generated {len(tokens)} tokens ({snac_count} SNAC)")

    # 4. Unpack

    # 5. Decode and save audio

if __name__ == "__main__":
    main()