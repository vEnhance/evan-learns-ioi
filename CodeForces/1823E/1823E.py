import sys

n, l, r = [int(_) for _ in sys.stdin.readline().split(" ")]


def nimber_for_line(s: int):
    return s // l


def nimber_for_cycle(s: int):
    if s >= r + l:
        return 0
    elif s >= r or s >= l:
        return nimber_for_line(s - l) + 1
    else:  # s < l
        return 0


graph: dict[int, set[int]] = {v: set() for v in range(1, n + 1)}
for line in sys.stdin.readlines():
    v, w = [int(_) for _ in line.split(" ")]
    graph[v].add(w)
    graph[w].add(v)


# https://stackoverflow.com/a/50639220
def get_all_connected_groups(graph):
    already_seen = set()
    result = []
    for node in graph:
        if node not in already_seen:
            connected_group, already_seen = get_connected_group(
                node, already_seen, graph
            )
            result.append(connected_group)
    return result


# https://stackoverflow.com/a/50639220
def get_connected_group(node, already_seen, graph):
    result = []
    nodes = set([node])
    while nodes:
        node = nodes.pop()
        already_seen.add(node)
        nodes = nodes or graph[node] - already_seen
        result.append(node)
    return result, already_seen


final_nimber = 0
for component in get_all_connected_groups(graph):
    final_nimber ^= nimber_for_cycle(len(component))

print("Bob" if final_nimber == 0 else "Alice")
