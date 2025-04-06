import sys

T = int(sys.stdin.readline())

for test_case_number in range(T):
    N = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()

    # check parity
    if s.count("E") % 2 != 0:
        print("NO")
        continue

    print("YES")
    k = 0
    i = 0
    while i < N:
        if s[i] == "O":
            print(k + 1, k + 2)
            k += 2
            i += 1
        else:
            assert s[i] == "E"
            start = i
            i += 1
            while s[i] != "E":
                i += 1
                assert i < N
            stop = i + 1
            b = stop - start  # block length

            for j in range(b):
                if j == 0:
                    if b % 2 == 0:
                        print(k + 1, k + b + 1)
                    else:
                        print(k + 1, k + b)
                elif j == b - 1:
                    if b % 2 == 0:
                        print(k + b, k + 2 * b)
                    else:
                        print(k + b + 1, k + 2 * b)
                else:
                    print(k + (j + 1), k + 2 * b + 1 - (j + 1))
            k += 2 * b

            i += 1
