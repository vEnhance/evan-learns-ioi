import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    if N % 2 == 0:
        print("2025" + "0" * (N - 4))
    else:
        print("42025" + "0" * (N - 5))
