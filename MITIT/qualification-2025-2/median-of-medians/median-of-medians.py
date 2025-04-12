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


MODULUS = 10**9 + 7

factorials = [1]
for k in range(1, 6 * 10**5):
    factorials.append(factorials[-1] * k % MODULUS)
debug(factorials[0:10])


def binom(n, k):
    if n < 0:
        return 0
    if k < 0:
        return 0
    return (
        factorials[n] * pow(factorials[k] * factorials[n - k], -1, MODULUS)
    ) % MODULUS


def perm(n, k):
    if n < 0:
        return 0
    if k < 0:
        return 0
    return (factorials[n] * pow(factorials[n - k], -1, MODULUS)) % MODULUS


T = int(stream.readline())
for test_case_number in range(T):
    N, M = [int(_) for _ in stream.readline().split()]
    x0, x1, y0, y1, z0, z1 = 0, 0, 0, 0, 0, 0
    zone = ""
    median = (3 * N + 1) // 2
    for m in range(M):
        a, b = [int(_) for _ in stream.readline().split()]
        if b < median:
            if a <= N:
                x0 += 1
            elif a <= 2 * N:
                y0 += 1
            else:
                z0 += 1
        elif b > median:
            if a <= N:
                x1 += 1
            elif a <= 2 * N:
                y1 += 1
            else:
                z1 += 1
        else:  # b == median
            if a <= N:
                zone = "x"
            elif a <= 2 * N:
                zone = "y"
            else:
                zone = "z"

    smalls = (3 * N - 1) // 2 - (x0 + y0 + z0)
    bigs = (3 * N - 1) // 2 - (x1 + y1 + z1)
    # debug(x0, x1, y0, y1, z0, z1, "|", "N =", N, zone)

    if zone == "":
        xcount = (
            (N - x0 - x1)
            * binom(N - x0 - x1 - 1, N // 2 - x0)
            * perm(smalls, N // 2 - x0)
            * perm(bigs, N // 2 - x1)
        ) * factorials[2 * N - (y0 + y1 + z0 + z1)]
        ycount = (
            (N - y0 - y1)
            * binom(N - y0 - y1 - 1, N // 2 - y0)
            * perm(smalls, N // 2 - y0)
            * perm(bigs, N // 2 - y1)
        ) * factorials[2 * N - (z0 + z1 + x0 + x1)]
        zcount = (
            (N - z0 - z1)
            * binom(N - z0 - z1 - 1, N // 2 - z0)
            * perm(smalls, N // 2 - z0)
            * perm(bigs, N // 2 - z1)
        ) * factorials[2 * N - (x0 + x1 + y0 + y1)]
        answer = xcount + ycount + zcount

    elif zone == "x":
        answer = (
            binom(N - x0 - x1 - 1, N // 2 - x0)
            * perm(smalls, N // 2 - x0)
            * perm(bigs, N // 2 - x1)
        ) * factorials[2 * N - (y0 + y1 + z0 + z1)]
    elif zone == "y":
        # debug(N - y0 - y1 - 1, y0, smalls, N // 2 - y0, bigs, N // 2 - y1)
        answer = (
            binom(N - y0 - y1 - 1, N // 2 - y0)
            * perm(smalls, N // 2 - y0)
            * perm(bigs, N // 2 - y1)
        ) * factorials[2 * N - (z0 + z1 + x0 + x1)]
    elif zone == "z":
        answer = (
            binom(N - z0 - z1 - 1, N // 2 - z0)
            * perm(smalls, N // 2 - z0)
            * perm(bigs, N // 2 - z1)
        ) * factorials[2 * N - (x0 + x1 + y0 + y1)]
    else:
        raise Exception

    print(answer % MODULUS)
