n, p, k = [int(_) for _ in input().split(" ")]
a_list = [int(_) for _ in input().split(" ")]

d = {}  # F_p -> count
for a in a_list:
    x = (pow(a, 4, p) - k * a + p) % p
    if x in d:
        d[x] += 1
    else:
        d[x] = 1

print(sum(c * (c - 1) // 2 for c in d.values()))
