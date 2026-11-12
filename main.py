#!/usr/bin/env python3
"""cutest-picture-01 round-3 entry: write the image to the output dir.

The image (a husky puppy hugging a penguin, supplied by the user) is stored
as entry.png next to this program. This program copies it byte-for-byte to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output). Stdlib only, no network,
deterministic: every run writes identical bytes.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Post-copy check: the written file must be a complete copy.
    if os.path.getsize(dst) != os.path.getsize(src):
        print("error: incomplete copy of entry.png", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
