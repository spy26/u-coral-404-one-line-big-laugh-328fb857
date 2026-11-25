#!/usr/bin/env python3
"""One Line, Big Laugh — u-coral-404-one-line-big-laugh-328fb857.

Writes a single original funny line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Pure stdlib, deterministic: no randomness, no time,
no network, no input. The line is a fixed string constant.
"""

import os

LINE = "My neighbor's dog barks at me every morning, so I barked back once. Now HR wants to see us both."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts characters, and the entry is
    # exactly one line.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
