#!/usr/bin/env python3
"""Say What Actually Broke — make.fun entry (u-po-pu-say-what-actually-broke-a2c153b5).

Writes one original line of software error copy (a single line, at most
200 characters) to /output/entry.txt. The line names the real failure —
a database crash mid-save — says the user's work is safe, and tells them
what to do next, with a twist a reader repeats out loud.
"""

import os

ENTRY = "Our database crashed halfway through saving your file — your work is safe on this screen, our database is not. Try saving again in a minute."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip() == ENTRY and ENTRY.strip(), "entry must not be blank"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Confirm what landed on disk matches the line exactly.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        assert f.read() == ENTRY, "output does not match entry"


if __name__ == "__main__":
    main()
