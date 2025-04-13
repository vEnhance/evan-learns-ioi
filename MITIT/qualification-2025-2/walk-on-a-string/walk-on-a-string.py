# vEnhance's cp Python template

import argparse
import sys
from typing import Any

parser = argparse.ArgumentParser()
parser.add_argument(
    "-d",
    "--debug",
    action="store_true",
    help="Show debugging statements (prints to stderr)",
)
parser.add_argument("input", nargs="?", type=argparse.FileType("r"), default="-")

opts = parser.parse_args()
stream = opts.input  # input stream


def debug(*args: Any):
    if opts.debug is True:
        print(*args, file=sys.stderr)


T = int(stream.readline())


def get_missing(chunk):
    for c in "rgyb":
        if c not in chunk:
            return c
    raise Exception


for t in range(T):
    N = int(stream.readline())
    s = stream.readline().strip()

    answer = ""
    i = 0
    target = get_missing(s[0:3])
    while i < N:
        while i < N and s[i] != target:
            i += 1
        answer += target
        target = get_missing(s[i - 2 : i + 1])
    print(answer + target * (N - len(answer)))
