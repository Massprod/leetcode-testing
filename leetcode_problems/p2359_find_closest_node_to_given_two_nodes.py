# You are given a directed graph of n nodes numbered from 0 to n - 1,
#  where each node has at most one outgoing edge.
# The graph is represented with a given 0-indexed array edges of size n,
#  indicating that there is a directed edge from node i to node edges[i].
# If there is no outgoing edge from i, then edges[i] == -1.
# You are also given two integers node1 and node2.
# Return the index of the node that can be reached from both node1 and node2,
#  such that the maximum between the distance from node1 to that node,
#  and from node2 to that node is minimized.
# If there are multiple answers, return the node with the smallest index,
#  and if no possible answer exists, return -1.
# Note that edges may contain cycles.
# -------------------------
# n == edges.length
# 2 <= n <= 10 ** 5
# -1 <= edges[i] < n
# edges[i] != i
# 0 <= node1, node2 < n
from collections import deque


def closest_meeting_node(edges: list[int], node1: int, node2: int) -> int:
    # working_sol (43.4%, 57.01%) -> (247ms, 46.74mb)  time: O(n) | space: O(n)
    # Essentially, we need maximum distance difference, between some node
    #  and both input nodes. But, minimized between all of the node differences.
    # BFS to get all the distances + get maximum diff for each node +
    # + get minimum from these checks + reset for lesser indexes (if diff equal).

    def bfs(start: int, graph: dict[int, int]) -> list[int]:
        # we can have unreachable nodes == `-1`.
        distances: list[int] = [-1 for _ in graph]
        # distance to the `start` node == 0.
        distances[start] = 0
        # We start from the distance == `1` <- (distance == level).
        level: int = 1
        que: deque[int | None] = deque([start, None])
        # We build with saving `-1` as an empty edge == ignore it.
        visited: set[int] = {start, -1}
        while que:
            node: int | None = que.popleft()
            if node is None:
                level += 1
                if que:
                    que.append(None)
                    continue
                break
            edge: int = graph[node]
            if edge in visited:
                continue
            que.append(edge)
            visited.add(edge)
            distances[edge] = level
        return distances

    # ~! each node has at most one outgoing edge !~
    # { node: edge }
    main_graph: dict[int, int] = {
        index: edge for index, edge in enumerate(edges)
    }
    node1_distances: list[int] = bfs(node1, main_graph)
    node2_distances: list[int] = bfs(node2, main_graph)
    
    out: int = -1
    # can't be higher than length == all nodes + 1
    difference: int = len(edges) + 1
    for node in range(len(edges)):
        # We should have them connected.
        if -1 == node1_distances[node] or -1 == node2_distances[node]:
            continue
        check_dif: int = max(node1_distances[node], node2_distances[node])
        # Unreachable
        # We check in left -> right pattern, so it always give us minimum index.
        if difference > check_dif:
            out, difference = node, check_dif
    
    return out


# Time complexity: O(n) <- n - length of the input array `edges`.
# Input array `edges` contains all of the graph nodes.
# In the worst case, we're going to have `node1` and `node2` available to visit
#  every other node.
# BFS is going to traverse whole `graph`, twice => O(2 * n).
# Extra traversing every `node` of the `graph` to check the distances => O(3 * n).
# -------------------------
# Auxiliary space: O(n)
# `que` <- allocates space for each `node` of the `graph` => O(n).
# `visited` <- allocates space for each `node` of the `graph` => O(2 * n).
# `node1_distances` & `node2_distances` <- allocates space for each `node` => O(4 * n).


test: list[int] = [2, 2, 3, -1]
test_node1: int = 0
test_node2: int = 1
test_out: int = 2
assert test_out == closest_meeting_node(test, test_node1, test_node2)

test = [1, 2, -1]
test_node1 = 0
test_node2 = 2
test_out = 2
assert test_out == closest_meeting_node(test, test_node1, test_node2)
