n, m, k, r, c = [int(_) for _ in input().split()]
ax, ay, bx, by = [int(_) for _ in input().split()]

MODULUS = 10**9 + 7

if ax == bx and ay == by:
    print(pow(k, n * m, MODULUS))
else:
    overlap = max(n - abs(ax - bx), 0) * max(m - abs(ay - by), 0)
    area_outside = m * n - (2 * r * c - overlap)

    print(pow(k, area_outside + (r * c - overlap), MODULUS))
