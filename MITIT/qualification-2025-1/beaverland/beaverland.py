import sys
from collections import deque

T = int(sys.stdin.readline())


# TIL if your graph is unweighted you should use bfs and not djikstra
def bfs(N, G):
    neighbors: dict[int, list[int]] = {}
    distances: dict[int, int | None] = {}

    for v in range(1, N + 1):
        neighbors[v] = []
        distances[v] = None
    for e in G:
        neighbors[e[0]].append(e[1])
        neighbors[e[1]].append(e[0])

    q = deque()
    q.append(1)
    distances[1] = 0

    while q:
        u = q.popleft()
        d = distances[u]
        for neighbor in neighbors[u]:
            if distances[neighbor] is None:
                distances[neighbor] = d + 1
                q.append(neighbor)

    return distances


for test_case_number in range(T):
    N, M, K = [int(_) for _ in sys.stdin.readline().split()]
    targets = [int(_) for _ in sys.stdin.readline().split()]
    G: list[tuple[int, int]] = []

    for _ in range(M):
        str_a, str_b = sys.stdin.readline().split()
        a = int(str_a)
        b = int(str_b)
        a, b = min(a, b), max(a, b)
        G.append((a, b))

    # edge case city 1
    if 1 in targets[1:]:
        print(-1)
        continue
    if targets[0] != 1:
        targets = [1] + targets

    roads_to_build = []
    for i in range(len(targets) - 1):
        a, b = targets[i], targets[i + 1]
        a, b = min(a, b), max(a, b)
        G.append((a, b))
        roads_to_build.append((a, b))

    distances = bfs(N, G)

    if all(((d := distances[t]) is not None and d == i) for i, t in enumerate(targets)):
        print(len(roads_to_build))
        for a, b in roads_to_build:
            print(a, b)
    else:
        print(-1)
