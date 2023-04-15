import sys


def get_indices(n):
    k = n // 2
    if k % 2 == 0:
        for i in range(0, k, 2):
            # left column of ring
            for j in range(i, n - i, 4):
                yield (i, j)
                yield (i, j + 1)
            # right column of ring
            for j in range(i, n - i, 4):
                yield (n - 1 - i, j)
                yield (n - 1 - i, j + 1)
            # top row of ring
            for j in range(3 + i, n - 5 - i + 4, 4):
                yield (j, i)
                yield (j + 1, i)
            # bottom row of ring
            for j in range(1 + i, n - 3 - i + 4, 4):
                yield (j, n - 1 - i)
                yield (j + 1, n - 1 - i)
    else:
        for i in range(0, k, 2):
            # left column of ring
            for j in range(i, n - i, 4):
                yield (i, j)
                yield (i, j + 1)
            # right column of ring
            for j in range(i + 2, n - i, 4):
                yield (n - 1 - i, j)
                yield (n - 1 - i, j + 1)
            # top row of ring
            for j in range(3 + i, n - 5 - i + 4, 4):
                yield (j, i)
                yield (j + 1, i)
            # bottom row of ring
            for j in range(3 + i, n - 3 - i + 4, 4):
                yield (j, n - 1 - i)
                yield (j + 1, n - 1 - i)
    return


# meow
def picture(n):
    arr = [["."] * n for _ in range(n)]
    for i, j in get_indices(n):
        arr[j][i] = "#"
    return arr


# print("\n".join("".join(row) for row in picture(10)))
# print("\n".join("".join(row) for row in picture(12)))


def main(n, arr):
    assert n % 2 == 0
    s = 0
    for i, j in get_indices(n):
        s ^= arr[i][j]
    return s


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    arr = []
    for lineno in range(n):
        arr.append([int(x) for x in sys.stdin.readline().split(" ")])
    print(main(n, arr))
