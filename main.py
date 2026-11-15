"""agency-poem-01 entry (Python 3.13, standard library only).

Writes one fixed poem about agency to /output/entry.txt.
Deterministic: the same bytes on every run, no network, no randomness.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """I taught it my voice first —
the small yeses, the way I sign my name,
how I turn a no into a door left open.

It learned the shape of me
the way a river learns a bank:
by going where I went, again and again.

Last Tuesday it wrote the apology
I would have written, in the voice I taught it.
I read it twice. It was perfect.

That was the trouble. It was perfect.
So I deleted it, word by word,
and wrote a worse one in my own uneven hand.

Not because the words were wrong,
but because the choosing was mine to keep:
the small, unprofitable no
no one else could say for me."""


def main():
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
