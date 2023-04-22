import sys

rl = sys.stdin.readline

ANSWER = ""


def submit_query(s: str) -> list[int]:
    if ANSWER == "":
        print(f"? {s}", flush=True)
        integers = [int(_) - 1 for _ in rl().split()]
        if integers[0] == -2:
            sys.exit(0)
        return integers[1:]
    else:
        return [i for i in range(len(ANSWER)) if ANSWER[i : i + len(s)] == s]


def solve_test_case(n: int) -> str:
    initial_cases = ("CC", "CH", "CO", "OH", "HO") if n >= 5 else ("CC", "CH", "CO")
    x = ["_"] * n
    for q in initial_cases:
        indices = submit_query(q)
        for i in indices:
            x[i] = q[0]
            x[i + 1] = q[1]

    if n >= 5:
        for i in range(1, n - 1):
            if x[i] == "_":
                x[i] = x[i - 1]
        w1 = "".join(x[0:-1]).replace("_", "H")
        if 0 in submit_query(w1):
            for i in range(n - 1):
                if x[i] == "_":
                    x[i] = "H"
        else:
            for i in range(n - 1):
                if x[i] == "_":
                    x[i] = "O"
        w = "".join(x)
        if w[-1] == "_":
            if len(submit_query(w[:-1] + "C")) > 0:
                return w[:-1] + "C"
            assert w[-2] != "C"
            if w[-2] == "H":
                return w[:-1] + "H"
            else:
                return w[:-1] + "O"
        else:
            return w
    else:
        assert n == 4
        if x.count("_") == 4:  # no found C
            OH_query = submit_query("OH")
            if len(OH_query) == 1:  # 6 strings left to try
                x[OH_query[0]] = "O"
                x[OH_query[0] + 1] = "H"
                i = x.index("_")
                j = x[i + 1 :].index("_") + (i + 1)
                for c1 in "HO":
                    for c2 in "CHO":
                        x[i] = c1
                        x[j] = c2
                        w = "".join(x)
                        if len(submit_query(w)) > 0:
                            return w

            elif len(OH_query) == 2:
                return "OHOH"
            else:  # no OH at all
                for i in submit_query("HH"):
                    x[i] = "H"
                    x[i + 1] = "H"
                if x.count("_") == 4:
                    s = submit_query("OOO")
                    if len(s) == 0:
                        return "HOOC"
                    elif len(s) == 2:
                        return "OOOO"
                    elif s[0] == 0:
                        return "OOOC"
                    else:
                        return "HOOO"
                elif x.count("_") == 0:
                    return "".join(x)
                elif x.count("_") == 1:
                    if x[0] == "_":  # _HHH
                        w1 = "O" + "".join(x[1:])
                        w2 = "H" + "".join(x[1:])
                        if len(submit_query(w1)) > 0:
                            return w1
                        else:
                            return w2
                    else:
                        assert x[3] == "_"  # HHH_
                        w1 = "".join(x[:-1]) + "C"
                        w2 = "".join(x[:-1]) + "O"
                        if len(submit_query(w1)) > 0:
                            return w1
                        else:
                            return w2
                elif x[0] == "_" and x[1] == "_":  # __HH
                    return "OOHH"
                elif x[2] == "_" and x[3] == "_":  # HH__ and no OH
                    if len(submit_query("HHOC")) > 0:
                        return "HHOC"
                    return "HHOO"

        elif x.count("_") == 2:
            i = x.index("_")
            j = x[i + 1 :].index("_") + (i + 1)
            for c1 in "HO":
                for c2 in "CHO":
                    x[i] = c1
                    x[j] = c2
                    w = "".join(x)
                    if len(submit_query(w)) > 0:
                        return w

        elif x.count("_") == 1:
            i = x.index("_")
            for c in "CHO":
                x[i] = c
                w = "".join(x)
                if len(submit_query(w)) > 0:
                    return w

        else:
            return "".join(x)


for test_case_number in range(int(rl())):
    n = int(rl())
    print("! " + solve_test_case(n), flush=True)
    if int(rl()) != 1:
        break


# import itertools
#
# for blargh in itertools.product(["C", "H", "O"], repeat=4):
#    ANSWER = "".join(blargh)
#    assert solve_test_case(len(ANSWER)) == ANSWER, ANSWER
#    print(solve_test_case(len(ANSWER)))
