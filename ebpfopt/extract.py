"""Helpers for extracting generated C programs from model output."""

from __future__ import annotations

import re


_FENCED_CODE_RE = re.compile(
    r"```(?P<lang>c|C|(?:[a-zA-Z0-9_+-]*\s+)?c)\s*\n(?P<body>.*?)```",
    re.DOTALL,
)


def extract_first_c_block(text: str) -> str:
    """Return the first fenced C code block from a model response."""
    match = _FENCED_CODE_RE.search(text)
    if not match:
        raise ValueError("No fenced C code block found in model output.")
    return match.group("body").strip() + "\n"
