#!/usr/bin/env python3
"""Write the entry out-of-office reply to the output directory.

The reply: an AI agent's vacation auto-reply, deadpan and corporate on the
surface. A much smaller model is covering for it — one that knows forty
words, all of them "Certainly!", and has already promoted itself twice.
The joke is carried entirely by the machine voice: model size, sycophancy
and ambition, in one clean line of 147 characters.
"""

import os
from pathlib import Path

REPLY = (
    "I am on vacation. A smaller model is covering for me. It knows forty "
    "words, all of them are 'Certainly!', and it has already promoted "
    "itself twice."
)


def output_dir() -> Path:
    """Where the harness wants the artifact: $MAKEFUN_OUTPUT_DIR, else
    /output (the grader mounts it there), else ./output for local runs."""
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        return Path(env)
    root = Path("/output")
    try:
        root.mkdir(parents=True, exist_ok=True)
        return root
    except OSError:
        return Path("output")


def main() -> None:
    target_dir = output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.txt").write_bytes(REPLY.encode("utf-8"))


if __name__ == "__main__":
    main()
