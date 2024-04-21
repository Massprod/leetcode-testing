# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive).
# The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi]
#  denotes a bi-directional edge between vertex ui and vertex vi.
# Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
# You want to determine if there is a valid path that exists from vertex source to vertex destination.
# Given edges and the integers n, source, and destination, return true if there is a valid path
#  from source to destination, or false otherwise.
# ----------------------
# 1 <= n <= 2 * 10 ** 5
# 0 <= edges.length <= 2 * 10 ** 5
# edges[i].length == 2
# 0 <= ui, vi <= n - 1
# ui != vi
# 0 <= source, destination <= n - 1
# There are no duplicate edges.
# There are no self edges.
from collections import defaultdict, deque


def valid_path(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    # working_sol (97.88%, 85.17%) -> (1354ms, 107.33mb)  time: O(n + k) | space: O(n * n)
    if source == destination:
        return True
    # {node: [edges]}
    graph: dict[int, list[int]] = defaultdict(list)
    # edges[i] == [start, end]
    for start, end in edges:
        if (start == source and end == destination) or (start == destination and end == source):
            return True
        graph[start].append(end)
        graph[end].append(start)
    visited: set[int] = set()
    que: deque[int] = deque([source])
    while que:
        cur_node: int = que.popleft()
        if destination == cur_node:
            return True
        for edge in graph[cur_node]:
            if edge not in visited:
                que.append(edge)
                visited.add(edge)
    return False


# Time complexity: O(n + k) <- n - input value == number of nodes(vertexes), k - len of input array `edges`.
# Standard build of the graph will traverse whole input array `edges` and extra we will use BFS to check
#  for the valid path == we will visit every Node once => O(n + k).
# ----------------------
# Auxiliary space: O(n + n * n)
# `graph` will have every Node as key and because we're given Bidirectional edges.
# We can have Graph with all Node's connected to each other.
# So, we will have `n` nodes as keys and `n` edges for everyone => O(n * n).
# In the worst case, we will traverse whole `graph` with BFS and `visited` will allocate space for `n` Nodes => O(n).
# Extra our `que` will allocate the same space => O(n).
# O(2n + n * n)


test: list[list[int]] = [[0, 1], [1, 2], [2, 0]]
test_n: int = 3
test_source: int = 0
test_destination: int = 2
test_out: bool = True
assert test_out == valid_path(test_n, test, test_source, test_destination)

test = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
test_n = 6
test_source = 0
test_destination = 5
test_out = False
assert test_out == valid_path(test_n, test, test_source, test_destination)
