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


# set up the map
S = set(range(0, 2**20))
bijection = [-1]
reverse_bijection = {}
x = 0
while len(S) > 0:
    y = S.pop()
    for t in range(20):
        y2 = 2**t ^ y
        if y2 in S:
            S.remove(y2)
        for t2 in range(20):
            y2 = 2**t ^ 2**t2 ^ y
            if y2 in S:
                S.remove(y2)
    bijection.append(y)
    x += 1
    reverse_bijection[y] = x

player = stream.readline().strip()
if player == "first":
    debug("First player")
    num_test_cases = int(stream.readline())
    debug(f"{num_test_cases} test cases")
    for _ in range(num_test_cases):
        x = int(stream.readline())
        debug(x)
        y = bijection[x]
        S = [str(i + 1) for i in range(20) if y & 2**i]
        print(len(S))
        print(" ".join(S))
else:
    assert player == "second"
    debug("Second player")
    num_test_cases = int(stream.readline())
    for _ in range(num_test_cases):
        stream.readline()
        line = stream.readline().strip()
        y = sum(2 ** (int(s) - 1) for s in line.split(" ")) if line else 0
        debug(y)
        if y in reverse_bijection:
            print(reverse_bijection[y])
        else:
            for t in range(20):
                y2 = 2**t ^ y
                if y2 in reverse_bijection:
                    print(reverse_bijection[y2])
                    break
            else:
                raise ValueError("fml")
