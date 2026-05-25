"""Command-line entry point for eBPFOPT."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from openai import OpenAI

from .extract import extract_first_c_block
from .prompt import build_request, read_text, validate_request


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def optimize(args: argparse.Namespace) -> int:
    prompt_text = read_text(args.prompt)
    source_text = read_text(args.source) if args.source else None
    request = build_request(prompt_text, source_text)

    for warning in validate_request(request):
        print(f"warning: {warning}", file=sys.stderr)

    if args.dry_run:
        write_text(args.output, request)
        print(f"Wrote assembled prompt to {args.output}")
        return 0

    if not os.environ.get("OPENAI_API_KEY"):
        print("error: OPENAI_API_KEY is not set", file=sys.stderr)
        return 2

    client = OpenAI()
    response = client.responses.create(
        model=args.model,
        input=request,
    )

    output_text = response.output_text
    write_text(args.output, output_text)
    print(f"Wrote optimizer response to {args.output}")

    if args.c_output:
        c_program = extract_first_c_block(output_text)
        write_text(args.c_output, c_program)
        print(f"Wrote optimized C program to {args.c_output}")

    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ebpfopt",
        description="Generate optimized XDP/eBPF C programs from an interface prompt and source file.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    optimize_parser = subparsers.add_parser(
        "optimize",
        help="Call the optimizer model for one BPF C program.",
    )
    optimize_parser.add_argument(
        "--prompt",
        required=True,
        type=Path,
        help="Path to the user prompt/interface markdown file.",
    )
    optimize_parser.add_argument(
        "--source",
        type=Path,
        help="Optional path to the original BPF C source file. If omitted, the prompt must include it.",
    )
    optimize_parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Path for the full optimizer response.",
    )
    optimize_parser.add_argument(
        "--c-output",
        type=Path,
        help="Optional path for the extracted optimized C program.",
    )
    optimize_parser.add_argument(
        "--model",
        default=os.environ.get("OPENAI_MODEL", "gpt-5"),
        help="OpenAI model name. Defaults to OPENAI_MODEL or gpt-5.",
    )
    optimize_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Write the assembled model prompt to --output without calling the API.",
    )
    optimize_parser.set_defaults(func=optimize)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
