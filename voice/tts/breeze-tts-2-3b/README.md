# Breeze TTS 2 (3B)

Breeze TTS 2 makes speech in English and Chinese. This folder runs it with one script, `test.sh`.

- **Model:** [`mlx-community/Breeze-TTS-2-mlx`](https://huggingface.co/mlx-community/Breeze-TTS-2-mlx). It is an MLX copy of [`BreezeBlue/Breeze-TTS-2`](https://huggingface.co/BreezeBlue/Breeze-TTS-2).
- **Size:** the bf16 version is about 7.6 GB to download. There are also 8-bit and 4-bit versions.
- **License:** research and non-commercial use only.
- **Python setup:** it runs in the shared `voice/.venv`. It does not need its own.

## It has no built-in voices

Other models, like Orpheus and Kokoro, let you pick a voice by name. Breeze does not. You describe the voice you want in plain words, and it makes one.

In `test.sh`, the `VOICE` variable holds this description, not a name. I kept the name `VOICE` so that all the test scripts use the same variable.

The default description is:

> A young American woman in her mid-twenties, with a warm, friendly, conversational voice. Medium pitch, natural pace, clear and relaxed.

I wrote it to sound close to Orpheus `tara` and Kokoro `af_heart`, so the three models are easier to compare.

To try your own description:

```bash
VOICE="A calm middle-aged man with a deep, slow voice." bash ./test.sh
```

Tips:

- Change one thing at a time. If you rewrite the whole description, you cannot tell which words made the difference.
- The same description can give a slightly different voice on each run. Generate it a few times before you decide.

## The `--cfg_scale 4` setting

`test.sh` runs with `--cfg_scale 4`. This setting makes the model follow your description more closely. Breeze's own docs suggest it for voice design.

Without it, the guidance is off. In my test the voice sounded a lot worse. You can hear the difference:

- Without the setting: [`audio/without-cfg-scale/breeze-tts-2-test-20261006-220745.wav`](audio/without-cfg-scale/breeze-tts-2-test-20261006-220745.wav)
- With `--cfg_scale 4`: [`audio/tts/breeze-tts-2-test-20261006-221116.wav`](audio/tts/breeze-tts-2-test-20261006-221116.wav)

Try values from 3 to 5 if you want to experiment.

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

A sample from my run is in `audio/tts/`. Each run saves a new wav file there, named with the date and time.

The folder `audio/without-cfg-scale/` holds one older sample, made before I turned on `--cfg_scale 4`. The script no longer makes it. I kept it as a "before" example.
