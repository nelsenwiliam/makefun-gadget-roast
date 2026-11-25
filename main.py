#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line (1-200 characters) to /output/entry.txt.

The line roasts a pair of wireless earbuds: the left bud always dies first,
mid-sentence, while the right one keeps going -- a specific, concrete,
everyday gripe with a fresh angle (asymmetric battery death) and a tight
punchline, judged on funniness, freshness and neat wording.
"""

import os

# Shortlist judged against the brief (funny first read, fresh angle,
# neatly worded, one person's specific gripe with a concrete detail):
CANDIDATES = (
    # Chosen: asymmetric battery death is a concrete, specific, fresh angle.
    "My earbuds die in the left one only, mid-sentence, every single time "
    "-- the right one just watches.",
    "My Bluetooth pairs with my neighbour's speaker before my own car "
    "every morning, like it has a favourite and it isn't me.",
    "My phone unlocks for my half-asleep face at 3 a.m. but not for me "
    "squinting in the sun -- it trusts me more unconscious.",
    "My laptop fan only screams during video calls, like it wants the "
    "whole meeting to know I own a jet engine.",
    "My charger works at exactly one angle, so every night I hold it like "
    "I'm defusing a bomb and pray.",
    "My watch congratulates me for standing up, as if sitting down was "
    "the crime and it just caught me.",
    "My TV remote has 47 buttons; I use two, and the other 45 are just "
    "there to make me feel illiterate.",
    "My phone deletes my photos to make room for an update that adds a "
    "feature I will never use and a bug I will.",
    "My earbuds case says 3% while the buds claim 100% -- a liar raising "
    "liars in my pocket.",
    "My alarm has learned to negotiate: I set one, it gives me five "
    "snoozes and a guilt trip.",
)

ROAST = CANDIDATES[0]

MAX_CHARS = 200


def main() -> None:
    line = ROAST.strip()
    if not line or "\n" in line or len(line) > MAX_CHARS:
        raise SystemExit("roast line must be a single line of 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
