import sys

t = int(sys.stdin.readline())
for line in sys.stdin.readlines():
    line = line.strip()
    n = int(line)
    if n < 10:
        print((n + 1) - 2)
    elif n < 100:
        print((n // 10 + 1) * (n % 10 + 1) - 2)
    else:
        s_a = ""
        s_b = ""
        for i in range(len(line)):
            if i % 2 == 0:
                s_a += line[i]
            else:
                s_b += line[i]
        print((int(s_a) + 1) * (int(s_b) + 1) - 2)
