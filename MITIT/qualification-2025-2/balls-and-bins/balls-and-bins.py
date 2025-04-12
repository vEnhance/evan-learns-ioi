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

for test_case_number in range(T):
    N = int(stream.readline())
    a = [int(x) for x in stream.readline().split()]
    s = [int(x) for x in stream.readline().split()]
    pairs = [(s[i] - a[i], s[i]) for i in range(N)]
    pairs.sort(key=lambda p: p[0])
    total = 0

    for t in pairs:
        debug(total, t)
        if t[0] > total:
            print("NO")
            break
        else:
            total += t[1] - t[0]
    else:
        print("YES")
