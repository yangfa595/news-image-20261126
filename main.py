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

import hashlib
import os
import shutil

BASE = os.path.dirname(os.path.abspath(__file__))
IMAGE = os.path.join(BASE, "entry.png")

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def digest(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def check_source():
    """Fail loudly rather than ship a corrupt image: the shipped file
    must exist and carry the PNG signature."""
    with open(IMAGE, "rb") as f:
        head = f.read(len(PNG_SIGNATURE))
    if head != PNG_SIGNATURE:
        raise SystemExit("entry.png beside main.py is not a PNG file")


def main():
    check_source()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(IMAGE, target)
    if digest(target) != digest(IMAGE):
        raise SystemExit("copied entry.png does not match the shipped image")
    print("wrote", target, os.path.getsize(target), "bytes")


if __name__ == "__main__":
    main()
