import sys

T = int(sys.stdin.readline())

for test_case_number in range(T):
    N = int(sys.stdin.readline())
    pieces = sorted([int(x) for x in sys.stdin.readline().split()])
    diffs = [pieces[i + 1] - pieces[i] for i in range(N - 1)]

    left_mins = [diffs[0]]
    for i in range(1, N - 1):
        left_mins.append(min(left_mins[-1], diffs[i]))

    right_mins = [diffs[-1]]
    for i in range(2, N):
        right_mins.append(min(right_mins[-1], diffs[-i]))
    right_mins.reverse()

    # print(pieces, diffs, left_mins, right_mins)

    print(min(left_mins[i] + right_mins[i + 2] for i in range(N - 3)))
