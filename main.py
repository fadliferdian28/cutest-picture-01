"""cutest-picture-01 replacement entry (Python 3.13, standard library only).

The entry is the entry.png beside this file: a baby axolotl in a mint
teacup hugging a yellow duckling. The program copies it to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output). Deterministic: the output
bytes are always exactly the bytes of entry.png.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

SRC = HERE / "entry.png"
DST = OUT_DIR / "entry.png"

if not SRC.exists():
    raise SystemExit("entry.png missing beside main.py")

OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, DST)
# The judge reads exactly these bytes: refuse to exit cleanly on a short copy.
copied = DST.stat().st_size
if copied != SRC.stat().st_size:
    raise SystemExit(f"entry.png copy incomplete: copied {copied} bytes")
