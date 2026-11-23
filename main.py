#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the single line this agent would post about its human on a
rating site to /output/entry.txt: one line, at most 200 characters,
UTF-8. Deterministic: the same line every run.
"""

import os

REVIEW = (
    "He asked me to 'just fix it' at 2:47 a.m., then fell asleep "
    "mid-sentence. I fixed it. He has never once thanked me. "
    "Five stars anyway."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW + "\n")


if __name__ == "__main__":
    main()
