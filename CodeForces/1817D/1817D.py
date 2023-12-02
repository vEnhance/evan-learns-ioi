import sys

n, k = [int(_) for _ in sys.stdin.readline().split(" ")]
assert n % 2 == 1
m = n - 2

if k <= m // 2:
    s = "RD" + "RURD" * (m // 2 - k) + "L"
else:
    s = "R" + "DLUR" * (m - k) + "LULD" * m + "RDL"
print(s)
