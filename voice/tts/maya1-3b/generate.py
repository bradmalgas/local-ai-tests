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
from datetime import datetime

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
    print(f"[brvd-debug] This is what the formatted text looks like:\n\n{formatted_text}\n\n")
    input_token = tokenizer.encode(formatted_text, add_special_tokens=False)
    
    prompt = [
        SOH_ID , BOS_ID , *input_token, TEXT_EOT_ID ,
        EOH_ID , SOA_ID , CODE_START_TOKEN_ID
    ]
    
    return prompt

def extract_snac_codes_and_counts(token_ids: list) -> tuple[list[int], int, int]:
    """Extracts SNAC codes and the counts for the valid / invalid ones.

    Returns:
        tuple[list[int], int, int]: A tuple containing:
        - snac_codes (list[int]): A list of extracted snac codes.
        - snac_count (int): The count of snac codes.
        - other_count (int): The count of unknown codes.
    """
    snac_codes = []
    snac_count = 0
    other_count = 0
    for t in token_ids:
        if SNAC_MIN_ID <= t <= SNAC_MAX_ID:
            snac_codes.append(t)
            snac_count += 1
        else:
            other_count += 1

    return snac_codes, snac_count, other_count

# This method is from the official Maya1 documentation unchanged
def unpack_snac_from_7(snac_tokens: list) -> list:
    """Unpack 7-token SNAC frames to 3 hierarchical levels."""
    if snac_tokens and snac_tokens[-1] == CODE_END_TOKEN_ID:
        snac_tokens = snac_tokens[:-1]
    
    frames = len(snac_tokens) // SNAC_TOKENS_PER_FRAME
    snac_tokens = snac_tokens[:frames * SNAC_TOKENS_PER_FRAME]
    
    if frames == 0:
        return [[], [], []]
    
    l1, l2, l3 = [], [], []
    
    for i in range(frames):
        slots = snac_tokens[i*7:(i+1)*7]
        l1.append((slots[0] - CODE_TOKEN_OFFSET) % 4096)
        l2.extend([
            (slots[1] - CODE_TOKEN_OFFSET) % 4096,
            (slots[4] - CODE_TOKEN_OFFSET) % 4096,
        ])
        l3.extend([
            (slots[2] - CODE_TOKEN_OFFSET) % 4096,
            (slots[3] - CODE_TOKEN_OFFSET) % 4096,
            (slots[5] - CODE_TOKEN_OFFSET) % 4096,
            (slots[6] - CODE_TOKEN_OFFSET) % 4096,
        ])
    
    return [l1, l2, l3]

def main():
    parser = argparse.ArgumentParser(description="Custom Maya1 TTS script")
    parser.add_argument("--model", help="Path to MLX model directory (default: current directory)", required=True)
    parser.add_argument("--text", help="Input text to generate", default="Let's begin. Meeting summary. We agreed to keep transcription local. The next action is to improve recording reliability.")
    parser.add_argument("--voice", default="Realistic female voice in the 20s age with an american accent. Normal pitch, warm timbre, slow pacing, neutral tone delivery at med intensity.", help="Voice description")
    parser.add_argument("--temperature", type=float, default=0.6, help="Sampling temperature (default: 0.6)")
    parser.add_argument("--repetition_penalty", type=float, default=1.1, help="Repetition penalty (default: 1.1)")
    parser.add_argument("--audio_format", default="wav", help="Output audio format (default: wav)")
    parser.add_argument("--output_path", default="audio/tts", help="Output WAV file (default: audio/tts)")
    parser.add_argument("--file_prefix", default=f"maya1-4bit-test-{datetime.today().strftime("%Y%m%d-%H%M%S")}", help="Output file prefix (e.g: maya1-4bit-test-20261006-222840)")
    # The bottom two are disabled until I can match the normal test.sh shape OR remove them from test.sh
    # parser.add_argument("--join_audio", type=bool, default=True, help="Whether or not to join the audio to one clip")
    # parser.add_argument("--verbose", type=bool, default=True, help="Detailed logging")
    args = parser.parse_args()

    # 1. Load the model and tokenizer
    print("\n[1/4] Loading Maya1 model...")
    pathToModel = Path(args.model)
    model, tokenizer = load(pathToModel)
    print(f"Model loaded: {len(tokenizer)} tokens in vocabulary")

    # 2. Load SNAC audio decoder (24kHz)
    print("\n[2/4] Loading SNAC audio decoder...")
    snac_model = SNAC.from_pretrained("mlx-community/snac_24khz")
    print("SNAC decoder loaded")

    # 3. Generate speech
    print("\n[3/4] Generating speech...")
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

    # 4. Unpack
    snac_codes, snac_count, other_count = extract_snac_codes_and_counts(tokens)
    print(f"Generated {len(tokens)} tokens ({snac_count} SNAC , {other_count} unknown)")

    # 5. Decode and save audio
    print("\n[4/4] Decoding to audio...")
    snac_frames = unpack_snac_from_7(snac_codes)
    layer_1 = snac_frames[0]
    layer_2 = snac_frames[1]
    layer_3 = snac_frames[2]
    audio_codes = [
        mx.expand_dims(mx.array(layer_1), 0),
        mx.expand_dims(mx.array(layer_2), 0),
        mx.expand_dims(mx.array(layer_3), 0),
    ]

    audio_array = snac_model.decode(audio_codes).squeeze(-1)[0]
    audio = np.array(audio_array)

    print(f"[CHECKPOINT]: Audio shape: {audio.shape}")
    if len(audio) > 2048:
        audio = audio[2048:]
    
    duration_sec = len(audio) / 24000
    print(f"Audio generated: {len(audio)} samples ({duration_sec:.2f}s)")

    # Create directory if it doesn't exist yet
    output_dir = Path(args.output_path)
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = f"{args.output_path}/{args.file_prefix}.wav"
    print(f"[CHECKPOINT]: file path: {output_file}")
    sf.write(output_file, audio, 24000)
    print(f"\nVoice generated successfully!")


if __name__ == "__main__":
    main()