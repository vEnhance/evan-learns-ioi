import random

random.seed("meow")
N = 50

print(N)
for _ in range(N):
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(x)
    pairs = []
    for i in range(9):
        if random.random() < 0.3:
            pairs.append((i + 1, x[i - 1]))

    if _ == 13:
        print(f"3 {len(pairs)}")
        for p in pairs:
            print(f"{p[0]} {p[1]}")
