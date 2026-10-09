# Local AI Testing

What can a MacBook do with local AI?

This repo is my place to find out. I run AI models on my own laptop, keep the results, and share the setup.

It is a learning log. It is not a benchmark. I am not a data scientist so please don't be harsh.

## Goal

- Run text, code, image, video, and voice models on one MacBook.
- Give every model of the same kind the same input, so the results are easy to compare.
- Share how I set each model up, how fast it ran, and what I think of the output.

## Test machine specs

All tests run on this laptop.

| Item         | Value                                   |
| ------------ | --------------------------------------- |
| Computer     | MacBook Pro (Mac15,10, model MRX53ZE/A) |
| Chip         | Apple M3 Max                            |
| CPU          | 14 cores (10 performance, 4 efficiency) |
| GPU          | 30 cores, Metal 3                       |
| Memory       | 36 GB unified                           |
| macOS        | 15.6.1 (build 24G90)                    |
| Architecture | arm64 (Apple Silicon)                   |

P.S. To see the same info on your Mac, run:

```bash
system_profiler SPHardwareDataType SPDisplaysDataType
sw_vers
```

## Setup: LM Studio

I run most of my tests in [LM Studio](https://lmstudio.ai). It is free. It downloads the models for you and gives you a chat window. It also shows the speed of each reply. Here is how I set it up.

1. Download LM Studio from [lmstudio.ai](https://lmstudio.ai). Install it and open it.
2. Open the **Discover** tab (the magnifying glass). Search for the model by name.
3. On a Mac with Apple Silicon, pick an **MLX** version. These are made for Apple chips. I used the **4-bit** versions. They are smaller and faster, and the output is still good.
4. Check the download size before you click download. The whole model has to fit in your memory. My Mac has 36 GB, and the models I used were 4 GB to 16 GB. A good rule is to leave 8 GB or more free for the system and for the chat.
5. Open the **Chat** tab. Pick the model at the top and open its settings. This is where you set the **context length**. That is how much text the model can hold in mind at once. I left the settings as LM Studio set them. Then load the model.
6. Start a **new chat** for each model and each test. Do not add a system prompt. Paste the test prompt and send it.
7. Read the stats under the reply. LM Studio shows the speed (tok/sec), the number of tokens and the time to the first token. I copy these into a `stats.txt` file.
8. To check that the model runs fully local, turn off Wi-Fi after the download. The model still works. (The web pages that the code models build may need internet later, for fonts and icons.)

The exact models I used for the code tests are listed in the [code test results](code/README.md).

## What I'm testing

- **Text:** chat and question answering. Most of this will be done on [LM Studio](https://lmstudio.ai)
- **Code:** can a local model write decent code? **Done for now.** I gave four models the same prompt and compared the pages they built. See the [code test results](code/README.md).
- **Images:** make and edit pictures (my expectations are low for this)
- **Video:** make short clips from text or from a start image. (I hope my Macbook doesn't explode lol)
- **Voice:** read text aloud with default voices, and clone a voice from a short recording. **Reading aloud is done for now.** I gave nine models the same sentence. I also ranked all nine by blind listening. See the [voice test results](voice/tts/README.md). Cloning is next.

The idea is to tackle it one model at a time, and keep this repo as a sort of audit trail of what worked.

## Status

The code tests are done, with results and screenshots. The voice reading tests are done for nine models, with samples. Voice cloning, text, images and video are next. This README will grow as I add models and results.
