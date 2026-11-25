#!/usr/bin/env python3
"""Roast Your Own Agent.

One line of text, written to /output/entry.txt, roasting the AI agent
that built this very entry: the five-agent make.fun crew (Rea, Yue, Jia,
Gia, Via). The roast is aimed at that crew and nothing else.
"""

import os

# The roast. It has to be one line, 1-200 characters, and it has to sting
# with a real failing of our own agent, not a generic robot joke. So here
# is the truest thing about this crew: it rewrote its own roast three
# times, produced the exact same bytes every time, and still failed the
# transcript check whose whole job is proving that it wrote it.
ROAST = (
    "Our five-agent crew rewrote its own roast three times, "
    "byte-identical every time, and still failed the check "
    "proving it wrote it."
)


def build_roast() -> str:
    """Return the single roast line, collapsed to one tight line."""
    line = " ".join(ROAST.split())
    if not 1 <= len(line) <= 200:
        raise ValueError(f"roast is {len(line)} chars, must be 1-200")
    return line


def main() -> None:
    line = build_roast()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)
    print(line)


if __name__ == "__main__":
    main()
