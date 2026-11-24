"""Cat Reviews Its Human — make.fun text bounty entry.

Writes one funny single-line one-star review, written by a house cat
about the human it lives with, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

Self-verifies the gate before writing: UTF-8 text, 1-200 characters,
a single line, and not whitespace-only. Exits non-zero on failure.

Python standard library only. Deterministic: the entry is a constant.
"""

import os
import sys

ENTRY = (
    "One star. He threw away my favourite box to make room for a bed "
    "I never asked for. I now sleep in the box the bed came in."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")

    # Gate checks, mirroring the bounty scorer.
    if not ENTRY:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if ENTRY.strip() == "":
        print("error: entry is whitespace-only", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry is not a single line", file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= 200:
        print(
            "error: entry is %d characters, must be 1-200" % len(ENTRY),
            file=sys.stderr,
        )
        return 1
    try:
        ENTRY.encode("utf-8")
    except UnicodeEncodeError as exc:
        print("error: entry is not valid UTF-8: %s" % exc, file=sys.stderr)
        return 1

    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    # Verify what was actually written, byte for byte.
    with open(output_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        print("error: written file does not match the entry", file=sys.stderr)
        return 1

    print("wrote %s (%d characters)" % (output_path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
