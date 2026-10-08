# Maya1 (3B)

Maya1 makes speech from a text description of the voice. This folder runs it with one script, `test.sh`.

- **Model:** [`mlx-community/maya1-4bit`](https://huggingface.co/mlx-community/maya1-4bit). It is an MLX copy of [`maya-research/maya1`](https://huggingface.co/maya-research/maya1).
- **Size:** the 4-bit weights are 1.86 GB.
- **License:** Apache 2.0.
- **Python setup:** it has its own `.venv` and `requirements.txt` in this folder. The shared `voice/.venv` is not enough. See "Four things that went wrong" below.

## It has no built-in voices

Like Breeze, Maya1 does not let you pick a voice by name. You describe the voice in plain words. In `test.sh`, the `VOICE` variable holds this description. I kept the name `VOICE` so that all the test scripts use the same variable.

The default description is the same one that Breeze uses, so the two models are easier to compare:

> A young American woman in her mid-twenties, with a warm, friendly, conversational voice. Medium pitch, natural pace, clear and relaxed.

To try your own description:

```bash
VOICE="A calm middle-aged man with a deep, slow voice." bash ./test.sh
```

## Four things that went wrong

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

## Sample output

Each run saves a new wav file in `audio/tts/`, named with the date and time.

The clip in `audio/tts/` now comes from the `mlx_audio` route, with no voice description. It sounds like a robot that reads a document. It is only there until `generate.py` can save audio.

The folder `audio/mlx-audio-route/` holds one clip made with a voice description. It has the buzz from problem 4. The script no longer makes it. I kept it as a "before" example.
