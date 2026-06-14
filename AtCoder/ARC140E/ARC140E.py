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


def f(x: int, y: int) -> int:
    if opts.debug is True:
        p = 5
    else:
        p = 23
    s = x // p  # starting number in zone
    d = 1 + y // p  # common difference in that zone
    a = x % p
    b = y % p
    return (-s - a * d + b) % p


N, M = [int(_) for _ in stream.readline().split(" ")]
for y in range(N):
    print(" ".join(str(1 + f(x, y)) for x in range(M)))
