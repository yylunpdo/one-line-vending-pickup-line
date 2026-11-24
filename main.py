#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single vending-machine pickup line to /output/entry.txt.
Python standard library only; no dependencies.

Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 200
characters, not only white space. The line is spoken by the machine
itself, uses the machine's own world (dispensing, coils, refunds),
and lands its punch in the last few words.
"""

import os

ENTRY = (
    # The machine speaks in the first person, in its own world:
    # dispensing snacks, a jammed coil, and a no-refunds policy.
    # "Stuck on you" is the double meaning: a coil jammed by the
    # passer-by, and the machine smitten. The punch ("I never give
    # refunds") lands in the last few words, and the line stays
    # charming rather than creepy: no touch, no following, just a
    # machine that would rather keep you than your coins.
    "I dispense snacks to strangers all day, but you just walked by "
    "and jammed my coil \u2014 now I'm stuck on you, and I never give refunds."
)


def main() -> None:
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    assert line.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote {len(line)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
