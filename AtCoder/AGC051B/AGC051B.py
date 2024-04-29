import itertools
n = 9

def f(seq) -> int:
    return sum(3**i * d for (i,d) in enumerate(seq))

print(3**n)
for xseq in itertools.product([0,1], repeat=n):
    for yseq in itertools.product([0,1], repeat=n):
        if any(xseq[i] < yseq[i] for i in range(n)):
            continue
        print(f(xseq), f(yseq))

