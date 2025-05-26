# There is a directed graph of n colored nodes and m edges.
# The nodes are numbered from 0 to n - 1.
# You are given a string colors where colors[i] is a lowercase English letter
#  representing the color of the ith node in this graph (0-indexed).
# You are also given a 2D array edges where edges[j] = [aj, bj] indicates
#  that there is a directed edge from node aj to node bj.
# A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk
#  such that there is a directed edge from xi to xi+1 for every 1 <= i < k.
# The color value of the path is the number of nodes that are colored
#  the most frequently occurring color along that path.
# Return the largest color value of any valid path in the given graph,
#  or -1 if the graph contains a cycle.
# -----------------------------
# n == colors.length
# m == edges.length
# 1 <= n <= 10 ** 5
# 0 <= m <= 10 ** 5
# colors consists of lowercase English letters.
# 0 <= aj, bj < n
from collections import defaultdict


def largest_path_value(colors: str, edges: list[list[int]]) -> int:
    # working_sol (5.63%, 5.85%) -> (2705ms, 161.8mb)  time: O(m * n) | space: O(n + m)
    # directed graph { node: [edges] }
    graph: dict[int, list[int]] = defaultdict(list)
    for start, end in edges:
        graph[start].append(end)
    
    visited: list[int] = [-1 for _ in colors]
    # { starting_node: [color occurrences] } - every path from each `starting_node`
    max_colors: dict[int, list[int]] = defaultdict(list)
    for node in graph:
        # 26 == a - z unique colors
        max_colors[node] = [0 for _ in range(26)]

    def dfs(node: int) -> bool:
        # Returned to the start node == cycle.
        if 0 == visited[node]:
            return False
        # Alredy visited == skip.
        elif 1 == visited[node]:
            return True
        
        visited[node] = 0
        path_colors: list[int] = [0 for _ in range(26)]
        for edge in graph[node]:
            if not dfs(edge):
                return False
            path_colors = [
                max(path_colors[index], max_colors[edge][index]) for index in range(len(path_colors))
            ]
        path_colors[ord(colors[node]) - ord('a')] += 1
        max_colors[node] = path_colors

        visited[node] = 1
        return True

    for node in range(len(colors)):
        if not dfs(node):
            return -1
        
    out: int = 0
    for occurrences in max_colors.values():
        out = max(out, max(occurrences))

    return out


# Time complexity: O(m * n) <- m - length of the input string `colors`,
#                              n - length of the input array `edges`.
# We check every path starting from each `node` of the graph and traverse all
#  of the connecting edges => O(m * n).
# Loops are constant size == 26 == alphabet == ignore.
# -----------------------------
# Auxiliary space: O(n + m)
# `graph` <- allocates space for each [start, end] pairt from `edges`.
# `visited` <- allocates space for each `node` from `colors`.


test_colors: str = "abaca"
test_edges: list[list[int]] = [[0, 1], [0, 2], [2, 3], [3, 4]]
test_out: int = 3
assert test_out == largest_path_value(test_colors, test_edges)

test_colors = "a"
test_edges = [[0, 0]]
test_out = -1
assert test_out == largest_path_value(test_colors, test_edges)
