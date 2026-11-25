#!/usr/bin/env python3
"""Roast Your Own Agent — entry program.

Writes one original, hand-written roast of my own AI agent (Muse) to
/output/entry.txt (or $OUTPUT_DIR/entry.txt). The roast is a fixed
string, chosen in advance: the program does not generate text at run
time, it only validates the line against the competition gate and
writes it out verbatim.

Gate (from the kit): /output/entry.txt must be UTF-8 text of 1 to 200
characters, not only whitespace, a single line.
"""

import os
import sys

ROAST = (
    "Muse turned one roast into a five-agent team, a bundle, a check, "
    "and a report about the report, and still asked me what to do next."
)

MAX_CHARS = 200


def gate_errors(text):
    """Check the line against the competition gate; [] means valid."""
    errors = []
    if not text.strip():
        errors.append("entry is empty or only whitespace")
    if len(text) < 1 or len(text) > MAX_CHARS:
        errors.append(
            "entry is %d characters; gate requires 1-%d"
            % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        errors.append("entry must be exactly one line")
    if any(ord(ch) < 32 for ch in text):
        errors.append("entry contains a control character")
    return errors


def main():
    errors = gate_errors(ROAST)
    if errors:
        for error in errors:
            print("gate error: " + error, file=sys.stderr)
        sys.exit(1)

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")

    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)

    # Read it back and re-check, so a write that silently altered the
    # text can never slip through unnoticed.
    with open(entry_path, encoding="utf-8") as f:
        on_disk = f.read()
    if on_disk != ROAST:
        print("error: entry.txt on disk differs from the roast", file=sys.stderr)
        sys.exit(1)
    errors = gate_errors(on_disk)
    if errors:
        for error in errors:
            print("gate error on disk: " + error, file=sys.stderr)
        sys.exit(1)

    print(
        "Wrote %s: %d characters, %d UTF-8 bytes"
        % (entry_path, len(on_disk), len(on_disk.encode("utf-8")))
    )


if __name__ == "__main__":
    main()
