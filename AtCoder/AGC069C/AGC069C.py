import sys

N = int(sys.stdin.readline())
S = sys.stdin.readline().strip().replace("A", "1").replace("B", "0")
T = sys.stdin.readline().strip().replace("A", "1").replace("B", "0")

if S == T:
    print(0)
    sys.exit(0)

i: int | None = None
j: int | None = None
for i in range(N):
    if S[i] == "1" and T[i] == "0":
        break
    elif S[i] == "0" and T[i] == "1":
        print("-1")
        sys.exit(0)
    else:
        pass

for j in range(N - 1, -1, -1):
    if S[j] == "1" and T[j] == "0":
        break
    elif S[j] == "0" and T[j] == "1":
        print("-1")
        sys.exit(0)
    else:
        pass

assert i is not None
assert j is not None
x1 = int(S[i : j + 1], 2)
y1 = int(T[i : j + 1], 2)
x2 = int(S[i : j + 1][::-1], 2)
y2 = int(T[i : j + 1][::-1], 2)

if x1 % 3 != y1 % 3 or x2 % 3 != y2 % 3:
    print("-1")
else:
    n1 = (x1 - y1) // 3
    n2 = (x2 - y2) // 3
    print(max(bin(n1).count("1"), bin(n2).count("1")))
