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

Install this package in editable mode:

```bash
pip install -e .
```

If editable install fails with a `build_editable` or PEP 660 error, upgrade the user-local Python packaging tools and retry:

```bash
python3 -m pip install --user --upgrade pip setuptools wheel
python3 -m pip install -e .
```

Set your OpenAI API key:

```bash
export OPENAI_API_KEY="<your key>"
```

You can also copy `.env.example` to a local `.env` file if your tooling loads environment files.

## Usage

Create a user interface prompt like [examples/interface_prompt.md](examples/interface_prompt.md), then run a dry run to inspect the assembled model request:

```bash
ebpfopt optimize \
  --prompt examples/interface_prompt.md \
  --source examples/control_counter.bpf.c \
  --output build/request.md \
  --dry-run
```

Generate an optimized program:

```bash
ebpfopt optimize \
  --prompt examples/interface_prompt.md \
  --source examples/control_counter.bpf.c \
  --output build/optimizer_response.md \
  --c-output build/optimized.bpf.c
```

The full model response is written to `--output`. When `--c-output` is provided, the first fenced C code block from the response is also written as a standalone C file.
