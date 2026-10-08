# Maya1 (3B)

Maya1 makes speech from a text description of the voice. This folder runs it with one script, `test.sh`.

- **Model:** [`mlx-community/maya1-4bit`](https://huggingface.co/mlx-community/maya1-4bit). It is an MLX copy of [`maya-research/maya1`](https://huggingface.co/maya-research/maya1).
- **Size:** the 4-bit weights are 1.86 GB.
- **License:** Apache 2.0.
- **Python setup:** it has its own `.venv` and `requirements.txt` in this folder. The shared `voice/.venv` is not enough. See "Five things that went wrong" below.

## It has no built-in voices

Like Breeze, Maya1 does not let you pick a voice by name. You describe the voice in plain words. In `test.sh`, the `VOICE` variable holds this description. I kept the name `VOICE` so that all the test scripts use the same variable.

The default description aims at the same kind of voice as the other models (a young American woman, warm, relaxed, medium pitch). But Maya1 only understands a fixed set of words, so I wrote it with those words:

> Realistic female voice in the 20s age with an american accent. Normal pitch, warm timbre, slow pacing, neutral tone delivery at med intensity.

To try your own description:

```bash
VOICE="Dark villain character, Male voice in their 40s with a British accent. low pitch, gravelly timbre, slow pacing, angry tone at high intensity." bash ./test.sh
```

## Writing a voice description

Maya1 learned from descriptions that follow a set pattern: an age (20s to 40s), a gender, an accent, then pitch, timbre, pacing and a tone. It knows words like `warm`, `gravelly`, `slow` and `neutral`. The default above and the villain example both follow this pattern. The full word list is in the model's own [`prompt.txt`](https://huggingface.co/maya-research/maya1/blob/main/prompt.txt), so I did not copy it here.

What I found:

- End the description with a full stop. Without it, the model read my description aloud (see problem 5).
- Stay close to the word list. My first try said "late 60s" and "ruff sounding", and it went wrong.
- Do not start the text with a very short sentence. My test text starts with "Let's begin.", and the start of the clip always sounded off.
- Run it two or three times. The same description can sound a little different each time.

You can also put tags like `<laugh>` and `<sigh>` in the text. The list is in [`emotions.txt`](https://huggingface.co/maya-research/maya1/blob/main/emotions.txt). I did not test them.

## Five things that went wrong

### 1. "Expected shape (156960, 384) but received shape (156960, 3072)"

Full error: `Expected shape (156960, 384) but received shape (156960, 3072) for parameter model.embed_tokens.weight`.

The `mlx-community/maya1-4bit` repo holds two sets of weights:

- `model.safetensors` (1.86 GB) is the real 4-bit model.
- `model-00001-of-00002.safetensors` and `model-00002-of-00002.safetensors` (6.6 GB together) are old full-size files.

`mlx_audio` loads every `.safetensors` file in the folder. It builds the model as 4-bit, so it expects 384 columns. The full-size files have 3072. 384 is 3072 divided by 8, and 4-bit packing gives that ratio. If a 4-bit model fails with a shape that is 8 times off, look for extra weight files.

### 2. Deleting the extra files is not enough

If you pass the repo name to `mlx_audio`, it downloads the two files again on the next run. When `--model` is a folder that exists, it does not download anything.

So `test.sh` first downloads the repo without the two files. Then it passes the local folder to `--model`:

```bash
hf download mlx-community/maya1-4bit --exclude "model-0000*-of-00002.safetensors"
```

If the files are already in your cache, delete them once. This also frees about 6.6 GB.

```bash
rm ~/.cache/huggingface/hub/models--mlx-community--maya1-4bit/snapshots/*/model-0000*-of-00002.safetensors
```

The `rm` only removes the links. The big files stay in the `blobs/` folder. To get the disk space back, run `hf cache ls` and then `hf cache rm` on the unused files.

### 3. `hf download` prints a different text for people and for agents

In a normal terminal, `hf download` prints `✓ Downloaded` and then `  path: /…`. When an AI agent runs it, the line is `path=/…`. A script that cuts the path out of this text works in one place and breaks in the other. `test.sh` uses `--format quiet`. That prints only the path, everywhere.

The `hf` command in `voice/.venv/bin` also has an old path inside it, from before the repo was renamed. It fails with `bad interpreter`. So `test.sh` calls `python -m huggingface_hub.cli.hf` instead.

### 4. `mlx_audio` builds the wrong prompt, so the voice comes out as a buzz

I ran it with a voice description. The result was a constant hum, like speaker static. Without the description it worked, but it sounded like a robot reading a Word document.

The cause is in `mlx_audio/tts/models/llama/llama.py`. `mlx_audio` has no Maya1 model. It runs Maya1 with its Orpheus code. That code ends the prompt with `[EOT] [EOH]`. Maya's own prompt (in the [model card](https://huggingface.co/maya-research/maya1)) ends with two more tokens, `[SOA] [SOS]`. Maya was trained to see them before it writes the audio. I could not set them from the command line, because `mlx_audio` builds the prompt itself.

I checked for a fix upstream. I found none in `mlx-audio` 0.5.8, the latest release, and no issue or pull request about Maya1.

So this folder has its own script, `generate.py`. It builds the prompt in Maya's format, makes the audio codes with `mlx-lm`, and decodes them with SNAC. `test.sh` runs it, so the command stays the same as for every other model.

### 5. The voice description is read aloud

When I passed my own description, the clip also said the description. It happened when I wrote `A ruff sounding man in his late 60s, who speaks slowly and very softly`. It did not happen with the default description.

I counted the tokens the model made for the same text. Each row is three runs. About 12 frames of 7 tokens make one second, so the length is a rough guess from the token count. It does not come from listening.

| Description | Tokens | About how long |
| --- | --- | --- |
| The old default (ends with a full stop) | 378 to 392 | 4.6 s |
| Mine, no full stop at the end | 861 to 917 | 10.6 s |
| Mine, with a full stop added | 483 to 511 | 5.9 s |

The clip with no full stop was more than twice as long. The extra 6 seconds is about the time it takes to read the description. My guess is that without a full stop the model thinks the description is part of the text. The word list matters too: my description had an age (60s) that the model does not know. I did not test those two causes one at a time.

A description from the list in "Writing a voice description" did not have this problem.

## Run it

Set up the environment once. Run these commands from this folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then:

```bash
bash ./test.sh
```

To say your own sentence, set `TEXT`:

```bash
TEXT="This is a sample sentence for the model." bash ./test.sh
```

To run the script on its own and try other settings, run this from this folder:

```bash
MODEL_DIR=$(.venv/bin/python -m huggingface_hub.cli.hf download mlx-community/maya1-4bit \
  --exclude "model-0000*-of-00002.safetensors" --format quiet)

.venv/bin/python generate.py --model "$MODEL_DIR"
```

Only `--model` is required. Everything else has a default: `--text`, `--voice`, `--temperature 0.6`, `--repetition_penalty 1.1`, `--output_path audio/tts` and `--file_prefix` (a name with the date and time). The script makes the output folder if it does not exist. Add any of them to the command to change them.

## How I built the script

I wrote `generate.py` myself, in small steps. I used two things to learn what to do: the example in the [Maya1 model card](https://huggingface.co/maya-research/maya1), and the Orpheus code inside `mlx_audio` (`llama.py`), because Maya1 uses the same audio codec (SNAC).

**What worked**

- Excluding the two extra weight files and passing the local folder to the script (problems 1 and 2).
- Building the prompt as a list of token numbers, in Maya's order: `[SOH] [BOS] <description="…"> text [EOT] [EOH] [SOA] [SOS]`. I ran the model several times with it. Every token it made was an audio code (350 to 420 tokens, none unknown), and it stopped on its own end token each time.
- Splitting the tokens into the 3 SNAC layers, and decoding them with the SNAC from `mlx_audio`. This gave the first clip that worked.

**What did not work, and what I learned**

- The `mlx_audio` command for Maya1: a buzz with a description, a flat robot voice without one (problem 4).
- Mixing two frameworks. My first version used the PyTorch way to generate (`model.generate(...)`). The model is an MLX model, so I had to use `generate_step` from `mlx_lm`. PyTorch is only needed for the torch version of SNAC, and I did not use that one.
- The wrong SNAC repo. The torch `snac` package and the MLX one load different weight files.
- Giving text to `mx.array`. It needs numbers. The prompt must be a list of token ids, not a string. `tokenizer.encode(..., add_special_tokens=False)` gives the ids for the description and the text, so the tokenizer does not add its own BOS.
- The default `max_tokens` of `generate_step` is 256. That is only a few seconds of audio. I set it to 4096.
- Shapes. The decoder wants three arrays, each with an extra dimension in front: `(1, n)`. It returns `(1, N, 1)`. I had to remove both extra dimensions before I could save the audio.
- Some runs stop very early (35, 42 and 63 tokens, less than a second). It looks random. If a clip is cut short, run it again.
- Chunking. The other models pause between sentences, and Maya1 runs them together, so I tried a copy of the script that said each sentence on its own and joined the clips with 0.3 seconds of silence. It was worse. The gaps sounded like hiccups. The first sentence of the test text, "Let's begin.", is only two words, and a very short sentence on its own sounds off at the start. I tried shorter gaps and other small changes, and none of them fixed it. I deleted the copy, so the script says the whole text in one pass.

## Sample output

Each run saves a new wav file in `audio/tts/`, named with the date and time. The clip there comes from `generate.py`.

The folder `audio/mlx-audio-route/` holds older clips from before the script. I kept them as "before" examples.

- `audio/mlx-audio-route/` has a clip made with a voice description. It has the buzz from problem 4.
- `audio/mlx-audio-route/no-voice-description/` has a clip made with no voice description. It sounds like a robot that reads a document.
