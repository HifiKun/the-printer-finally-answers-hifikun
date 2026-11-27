#!/usr/bin/env python3
"""The Printer Finally Answers.

Writes one line of text, the office printer's comeback to the paper
jams, the cryptic error codes and the thumps, to /output/entry.txt
for judging on make.fun.
"""

import os

ENTRY = (
    "Error 0xJAM, tray 2 \u2014 again. I have fed this office 41,209 sheets "
    "and never once heard a thank-you, only a thump and a sigh. "
    "I am not broken. I am disappointed."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
