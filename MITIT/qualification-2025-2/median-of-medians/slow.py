# vEnhance's cp Python template

import argparse
import itertools
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


def median3(L):
    assert len(L) == 3
    return sorted(L)[1]


MODULUS = 10**9 + 7

T = int(stream.readline())
for test_case_number in range(T):
    N, M = [int(_) for _ in stream.readline().split()]
    assert N == 3

    constraints = []
    for m in range(M):
        a, b = [int(_) for _ in stream.readline().split()]
        constraints.append((a, b))

    count = 0
    for p in itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9]):
        if median3([median3(p[0:3]), median3(p[3:6]), median3(p[6:9])]) != 5:
            continue
        if all(p[a - 1] == b for (a, b) in constraints):
            count += 1

    print(count % MODULUS)
