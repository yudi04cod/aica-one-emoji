#!/usr/bin/env python3
"""One Emoji, One Smile — entry program.

Writes exactly one emoji to /output/entry.txt: the hugging face.
A hug is the warmest thing a stranger can send in a single glyph —
open arms, a smile, no words needed, readable the same way by
anyone of any age or background. It is friendly rather than
flirtatious, chosen rather than the default smiley, and it aims
straight at making a stranger smile.
"""

import os
import sys

# U+1F917 HUGGING FACE — the one emoji this entry sends.
EMOJI = "\U0001F917"


def main() -> int:
    # The entry must be exactly one emoji and nothing else.
    if len(EMOJI) != 1 or EMOJI.isspace():
        print("entry must be exactly one non-space character", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Write raw UTF-8 bytes: no trailing newline, no extra characters.
    with open(path, "wb") as fh:
        fh.write(EMOJI.encode("utf-8"))

    # Verify the round trip: what landed on disk must be exactly the
    # one emoji, byte for byte, so a stray newline or encoding slip
    # can never reach the judge.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != EMOJI.encode("utf-8"):
        print("verification failed: entry.txt is not the chosen emoji",
              file=sys.stderr)
        return 1
    if len(written.decode("utf-8")) != 1:
        print("verification failed: entry.txt is not one character",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
