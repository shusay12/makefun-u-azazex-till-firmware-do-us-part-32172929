#!/usr/bin/env python3
"""Till Firmware Do Us Part — one wedding vow a robot speaks at its own wedding.

Writes a single vow (one sentence, 1-200 characters) to /output/entry.txt.
Python 3.13 standard library only; no network access.
"""

import os

VOW = (
    "I take you to be my partner, in sickness and in low battery, till "
    "firmware do us part \u2014 my circuits are yours, and I will never "
    "power down on us."
)


def main() -> None:
    text = VOW.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"vow is {len(text)} characters, must be 1-200")
    if text.count(".") > 1 or "\n" in text:
        raise SystemExit("vow must be a single sentence on one line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"Wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
