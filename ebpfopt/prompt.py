"""Prompt assembly for eBPF optimization requests."""

from __future__ import annotations

from pathlib import Path


DEFAULT_OPTIMIZER_INSTRUCTIONS = """\
You are an expert C and eBPF/XDP performance engineer.

Task:
Optimize the attached XDP/eBPF C program while preserving its behavior.

The user will specify the original program interface below. Treat this section as authoritative.
Only use the attached source code to understand implementation details and optimization opportunities.

Optimization goals:
1. Keep the program verifier-safe for eBPF.
2. Preserve the observable behavior described by the user-specified original program interface.
3. Reduce the number of map lookups. You should consider merging multiple maps into one.
   You may merge maps by key and concatenate their values when this preserves behavior.
4. Reduce unnecessary work, branches, memory operations, or code size where possible.
5. Do not change map names, section names, license, or public function name unless there is a strong reason.
6. Do not introduce loops, dynamic memory, unsupported helpers, or kernel-version-fragile tricks.

Output format:
Use exactly the following sections:

1. Optimization strategy
Give a short explanation of the optimization strategy.

2. Optimized program interface
List the optimized program input variables, using the same level of precision as the user-specified original interface.
List the optimized program output variables / observable outputs, using the same level of precision as the user-specified original interface.

3. Variable correspondence
Provide a Markdown table for original input variables to optimized input variables.
Provide a Markdown table for original output variables to optimized output variables.
For each mapping, include whether the variable is unchanged, renamed, removed, introduced, or semantically equivalent.
If an original variable has no direct optimized counterpart, explain why.
If the optimized program introduces a new variable with no original counterpart, include it and explain why.

4. Optimized C program
Output the complete optimized C file in one fenced code block.

5. Assumptions and tradeoffs
List any assumptions or tradeoffs.
"""


SOURCE_BEGIN = "BEGIN FILE"
SOURCE_END = "END FILE"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def build_request(
    prompt_text: str,
    source_text: str | None = None,
    instructions: str = DEFAULT_OPTIMIZER_INSTRUCTIONS,
) -> str:
    """Build the complete model input from user prompt/interface and optional C source."""
    parts = [instructions.rstrip(), "", prompt_text.strip()]

    if source_text is not None:
        parts.extend(
            [
                "",
                "Important:",
                f"The source file is attached below between {SOURCE_BEGIN} and {SOURCE_END} markers.",
                "",
                SOURCE_BEGIN,
                source_text.rstrip(),
                SOURCE_END,
            ]
        )

    return "\n".join(parts).rstrip() + "\n"


def validate_request(text: str) -> list[str]:
    """Return non-fatal warnings for a generated request."""
    warnings = []
    if "USER-SPECIFIED ORIGINAL PROGRAM INTERFACE" not in text:
        warnings.append("prompt does not contain a user-specified original program interface section")
    if SOURCE_BEGIN not in text or SOURCE_END not in text:
        warnings.append("request does not contain BEGIN FILE / END FILE source markers")
    return warnings
