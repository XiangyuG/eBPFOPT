# eBPFOPT

## Setup

Clone submodules after cloning this repository:

```bash
git submodule update --init --recursive
```

Install system dependencies:

```bash
sudo apt update
sudo apt install -y python3-pip clang
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Set your OpenAI API key:

```bash
export OPENAI_API_KEY="<your key>"
```

You can also copy `.env.example` to a local `.env` file if your tooling loads environment files.
