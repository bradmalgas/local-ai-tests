# Local AI Text-to-Speech (TTS) Tests

In order to test the text to audio generation abilities of the local models, I wrote a small python script that runs each model. Each model has it's own test script.

## Prerequisites

You need a Mac with Apple Silicon, because the models run on MLX. I used Python 3.14.

Set up the Python tools once. Run these commands from the `voice` folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The test scripts look for this environment at `voice/.venv`, so you don't have to activate it each time. To use a different Python, set the `PYTHON` variable, like this: `PYTHON=/path/to/python bash ./test.sh`.

Some models need packages that clash with the shared environment. Those models have their own `.venv` and `requirements.txt` inside their folder. Set one up the same way, but run the commands from the model's folder. For example, Kokoro needs this, and I built its environment with Python 3.13.

The first time you run a model, it downloads from Hugging Face. Some models are several GB. After that, it runs fully local, with no internet.

## How to run the script

If you want to run a model's test script, navigate to the folder and run `bash ./test.sh`.

> Hint: You might need to grant the script execution permissions on Mac. To do this, run the command `chmod +x test.sh`

You can also supply a `TEXT` parameter to test the model on custom text.
Example:

```bash
TEXT="This is a better sample text for the audio model to run against" ./test.sh
```

Some models also have additional parameters, you can look at the model's documentation to find out how to use them.

## Output format

Running the test script will produce a wav file that contains the text provided.
