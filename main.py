#!/usr/bin/env python3
"""Entry program for the make.fun news-image-20261126 competition.

The repository ships the finished front page as ``entry.png`` beside this
script. The grader runs this program twice, offline, with the repository
read-only and a writable output directory; both runs must produce the
same bytes, so the program does the simplest deterministic thing: it
copies the shipped image, byte for byte, to ``entry.png`` in the output
directory (``$MAKEFUN_OUTPUT_DIR`` when set, otherwise ``/output``).

Python 3.13, standard library only, no network.
"""

import os
import shutil

BASE = os.path.dirname(os.path.abspath(__file__))
IMAGE = os.path.join(BASE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(IMAGE, target)
    print("wrote", target)


if __name__ == "__main__":
    main()
