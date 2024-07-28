# A city is represented as a bi-directional connected graph with n vertices
#  where each vertex is labeled from 1 to n (inclusive).
# The edges in the graph are represented as a 2D integer array edges,
#  where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi.
# Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
# The time taken to traverse any edge is time minutes.
# Each vertex has a traffic signal which changes its color from green to red
#  and vice versa every change minutes.
# All signals change at the same time. You can enter a vertex at any time,
#  but can leave a vertex only when the signal is green.
# You cannot wait at a vertex if the signal is green.
# The second minimum value is defined
#  as the smallest value strictly larger than the minimum value.
#  - For example the second minimum value of [2, 3, 4] is 3,
#    and the second minimum value of [2, 2, 4] is 4.
# Given n, edges, time, and change,
#  return the second minimum time it will take to go from vertex 1 to vertex n.
# Notes:
#  - You can go through any vertex any number of times, including 1 and n.
#  - You can assume that when the journey starts, all signals have just turned green.
# ---------------------------
# 2 <= n <= 10 ** 4
# n - 1 <= edges.length <= min(2 * 10 ** 4, n * (n - 1) / 2)
# edges[i].length == 2
# 1 <= ui, vi <= n
# ui != vi
# There are no duplicate edges.
# Each vertex can be reached directly or indirectly from every other vertex.
# 1 <= time, change <= 10 ** 3
from collections import defaultdict, deque


def second_minimum(n: int, edges: list[list[int]], time: int, change: int) -> int:
    # working_sol (94.70%, 40.40%) -> (1683ms, 26.50mb)  time: O(n + m) | space: O(n + m)
    # In case of single Node in graph.
    # We don't need to travel at all.
    if 1 == n:
        return 0
    cur_node: int
    cur_path: int
    # {Node: [edges]}
    graph: dict[int, list[int]] = defaultdict(list)
    for start, end in edges:
        graph[start].append(end)
        graph[end].append(start)
    # index <- Node, value <- time to travel from 1 -> Node.
    path1: list[int] = [-1 for _ in range(n + 1)]  # 1-indexed.
    path2: list[int] = [-1 for _ in range(n + 1)]
    # We start from `1` Node.
    path1[1] = 0
    # [(Node, path_type)]
    que: deque[tuple[int, int]] = deque([(1, 1)])
    while que:
        cur_node, cur_path = que.popleft()
        cur_time: int = path1[cur_node] if 1 == cur_path else path2[cur_node]
        # Signal color.
        # We always start from `green` so every `change` step we're going to turn to `red`.
        # We can just take a floor of the `cur_time` and check it: odd => `red`, even => `green.`
        # Means we did (`cur_time` // `change`) <- switches.
        switches: int = cur_time // change
        if switches % 2:
            # We're making `switches` + 1 to wait for the `red` light and `time` to get into the next Node.
            cur_time = change * (switches + 1) + time
        else:
            # Otherwise, we move instantly.
            cur_time += time
        # Essentially, we want to expand our shortest path, by as small edges as possible.
        # So, we can either do step_back-step_forward on the last one.
        # Or, we should make some turn on the way to add `1` extra edge (like in 1 example).
        # And both of these options can be covered with `path2`.
        # We will try to make turn from every Node we visit on `path1`.
        # Like, first example:
        # 1 -> 2, 3, 4
        # 3 -> 4
        # `path1` will visit `2, 3, 4` and `path2` will check extra turns from them.
        # 2 -> 1 <- will mark `1` as visited in `path2` and we shouldn't use it anymore.
        # Because w.e the other node going to point here, it will ADD its own travel time from it.
        # 2 -> 1 -> 3 <- not going to be smaller than `path1` 1 -> 3 => we cull it.
        # But, 1 -> 3 -> 4 <- going to give us EXTRA edge we needed => we can use it.
        # And if there are some more Nodes branching from `3` they will have more cost than 3 -> 4.
        # So, this first turn option is always lowest, and we should use it.
        # Additionally, we don't care about edges, which have the same travel time as `path1`.
        # Because they're actually already used in `path1`, and will lead `path2` into the `path1`.
        for edge in graph[cur_node]:
            if -1 == path1[edge]:
                path1[edge] = cur_time
                que.append((edge, 1))
            elif -1 == path2[edge] and path1[edge] != cur_time:
                if n == edge:
                    print(cur_time)
                    return cur_time
                path2[edge] = cur_time
                que.append((edge, 2))
    return -1


# Time complexity: O(n + m) <- m <- length of the input array `edges`
# In the worst case: we're going to visit every Node twice, with `path2` after `path1`.
# Standard BFS using every Node, but we can visit them extra time with `path2`.
# And for each Node, we always traverse all of its edges => O(2 * (n + m)).
# ---------------------------
# Auxiliary space: O(n + m)
# `path1` and `path2` <- always of the size `n` => O(2 * n)
# `que` <- will allocate space for every Node => O(3 * n).
# `graph` <- will store every Node in range 1 -> `n` - inclusive, and all edges => O(n + m + 3 * n)


test_n: int = 5
test_edges: list[list[int]] = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]
test_time: int = 3
test_change: int = 5
test_out: int = 13
assert test_out == second_minimum(test_n, test_edges, test_time, test_change)

test_n = 2
test_edges = [[1, 2]]
test_time = 3
test_change = 2
test_out = 11
assert test_out == second_minimum(test_n, test_edges, test_time, test_change)
