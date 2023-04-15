import sys

rl = sys.stdin.readline


prev_dyadic_map = [[0]]
dyadic_map = []  # silence pyright
N = 0

while N < 5:
    dyadic_map = []
    for i in range(2**N):
        dyadic_map.append(
            prev_dyadic_map[i] + [4**N + x for x in reversed(prev_dyadic_map[i])]
        )
    for i in range(2**N):
        dyadic_map.append([2 * 4**N + x for x in dyadic_map[2**N - (i + 1)]])
    prev_dyadic_map = dyadic_map
    N += 1


def c(i, j):
    return dyadic_map[i][j]


lookup: dict[int, tuple[int, int]] = {}
for i in range(32):
    for j in range(32):
        lookup[c(i, j)] = (i + 1, j + 1)


n, k = [int(_) for _ in rl().split()]

for i in range(n):
    print(" ".join([str(c(i, j) ^ c(i, j + 1)) for j in range(n - 1)]))
for i in range(n - 1):
    print(" ".join([str(c(i, j) ^ c(i + 1, j)) for j in range(n)]))

sys.stdout.flush()

bnum = 0
for _ in range(k):
    bnum ^= int(rl())
    row, col = lookup[bnum]
    print(row, col)
    sys.stdout.flush()
