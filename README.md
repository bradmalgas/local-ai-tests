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

## What I plan to test

- **Text:** chat and question answering. Most of this will be done on (LM Studio)[http://lmstudio.ai]
- **Code:** can a local model write decent code?
- **Images:** make and edit pictures (my expectations are low for this)
- **Video:** make short clips from text or from a start image. (I hope my Macbook doesn't explode lol)
- **Voice:** read text aloud with default voices, and clone a voice from a short recording.

The idea is to tackle it one model at a time, and keep this repo as a sort of audit trail of what worked.

## Status

I just arrived. This is the first version of the README. It will grow as I add models and results.
