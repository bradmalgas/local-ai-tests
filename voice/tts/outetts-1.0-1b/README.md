# OuteTTS 1.0 (1B)

OuteTTS writes speech as audio codes, one at a time, like a language model. This folder runs it with one script, `test.sh`.

- **Model:** [`mlx-community/Llama-OuteTTS-1.0-1B-fp16`](https://huggingface.co/mlx-community/Llama-OuteTTS-1.0-1B-fp16). It is an MLX copy of [`OuteAI/Llama-OuteTTS-1.0-1B`](https://huggingface.co/OuteAI/Llama-OuteTTS-1.0-1B). There are also 8-bit, 6-bit and 4-bit versions.
- **Python setup:** it runs in the shared `voice/.venv`.

## Three things that went wrong, and how `test.sh` fixes them

### 1. There is only one voice

In `mlx_audio`, the `--voice` flag for OuteTTS must be the path to a speaker file. It does not take a name like `EN-FEMALE-1-NEUTRAL`. Those names come from OuteTTS's own library, which `mlx_audio` does not include. If you use one, you get "Speaker file not found".

So `test.sh` has no voice flag. It uses the one speaker that ships with `mlx_audio`. To get other voices, OuteTTS builds a speaker from a reference recording. That is voice cloning, so I left it for the cloning tests.

### 2. The temperature must be set to 0.4

OuteTTS's own default temperature is 0.4. But the `mlx_audio` command line has its own default of 0.7, and it always passes that value in. With 0.7 the voice sighed and rushed. `test.sh` sets `--temperature 0.4`, and that made a big difference in my test.

### 3. The speech is cut off at about 7 seconds

The default `--max_tokens` is 1200. That only fits about 7 seconds of speech, so a longer text stops in the middle of a word. `test.sh` sets `--max_tokens 4096`.

## Run it

From this folder:

```bash
bash ./test.sh
```

To say your own sentence, set `TEXT`:

```bash
TEXT="This is a sample sentence for the model." bash ./test.sh
```

## Sample output

A sample from my run is in `audio/tts/`. It is not perfect. The voice is a little rushed. I am showing what the model does with these settings, not trying to make it sound better than it can.
