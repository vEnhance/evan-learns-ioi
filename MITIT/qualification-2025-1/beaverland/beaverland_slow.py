import sys
from heapq import heappop, heappush

T = int(sys.stdin.readline())


# goddamn how do you implement this stupid thing
# EDIT: yeah i implemented this wrong in contest no wonder it didn't work
def djikstra(N, G):
    neighbors: dict[int, list[int]] = {}
    distances: dict[int, int | None] = {}

    for v in range(1, N + 1):
        neighbors[v] = []
        distances[v] = None
    for e in G:
        neighbors[e[0]].append(e[1])
        neighbors[e[1]].append(e[0])

    pq = []
    heappush(pq, (0, 1))
    distances[1] = 0

    while pq:
        (d, u) = heappop(pq)
        assert isinstance(d, int)
        if (cur := distances[u]) is not None and d > cur:
            continue
        else:
            distances[u] = d
        for neighbor in neighbors[u]:
            if (cur := distances[neighbor]) is None or cur > d + 1:
                distances[neighbor] = d + 1
                heappush(pq, (d + 1, neighbor))

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

    distances = djikstra(N, G)
    print(distances, file=sys.stderr)

    if all(((d := distances[t]) is not None and d == i) for i, t in enumerate(targets)):
        print(len(roads_to_build))
        for a, b in roads_to_build:
            print(a, b)
    else:
        print(-1)
