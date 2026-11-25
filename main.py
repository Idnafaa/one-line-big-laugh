#!/usr/bin/env python3
"""One Line, Big Laugh — a single original joke line.

Writes exactly one funny line (<=200 chars) to /output/entry.txt.
The judge compares entries two at a time, so the line has to land
entirely on its own: setup and punchline in one breath.
"""

import os

LINE = "I tried to impress my date by cooking, so now the smoke alarm and I are in a committed relationship."

OUT_DIR = "/output"
OUT_FILE = os.path.join(OUT_DIR, "entry.txt")


def main():
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry line is {len(text)} chars, must be 1-200")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry line must be exactly one line")
    if text != text.strip() or text != LINE:
        raise SystemExit("entry line must have no leading/trailing whitespace")
    if not text.strip():
        raise SystemExit("entry line must not be only whitespace")
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUT_FILE}")


if __name__ == "__main__":
    main()
