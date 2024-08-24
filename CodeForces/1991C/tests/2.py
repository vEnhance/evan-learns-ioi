import random

random.seed(20240823)

MAX = 200000
print(1)
print(MAX)
print(" ".join(str(random.randrange(0, 10**9, 2)) for _ in range(200000)))
