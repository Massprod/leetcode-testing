# There exist two undirected trees with n and m nodes,
#  labeled from [0, n - 1] and [0, m - 1], respectively.
# You are given two 2D integer arrays edges1 and edges2 of lengths n - 1
#  and m - 1, respectively, where edges1[i] = [ai, bi]
#  indicates that there is an edge between nodes ai and bi in the first tree
#  and edges2[i] = [ui, vi] indicates that there is an edge between nodes
#  ui and vi in the second tree.
# Node u is target to node v if the number of edges on the path from u to v is even.
# Note that a node is always target to itself.
# Return an array of n integers answer, where answer[i] is the maximum possible number
#  of nodes that are target to node i of the first tree if you had to connect one node
#  from the first tree to another node in the second tree.
# Note that queries are independent from each other. That is,
#  for every query you will remove the added edge before proceeding to the next query.
# ----------------------------------
# 2 <= n, m <= 10 ** 5
# edges1.length == n - 1
# edges2.length == m - 1
# edges1[i].length == edges2[i].length == 2
# edges1[i] = [ai, bi]
# 0 <= ai, bi < n
# edges2[i] = [ui, vi]
# 0 <= ui, vi < m
# The input is generated such that edges1 and edges2 represent valid trees.
from collections import defaultdict, deque


def max_target_nodes(edges1: list[list[int]], edges2: list[list[int]]) -> list[int]:
    # working_sol (29.54%, 30.68%) -> (575ms, 114.08mb)  time: O(m + n) | space: O(m + n)
    # Main logic, is that we can count all the nodes by their parity_levels in the trees.
    # Even or odd, because every node on the `even` level is always going to be
    #  distanced with `even` edges from other `even` level nodes. Same goes for `odd`.
    # So, just get number of the `nodes` on each parity level, and count them.

    def bfs_count(
        start: int,
        graph: dict[int, list[int]],
        visited: dict[int, int],
    ) -> tuple[int, int]:
        '''
        Standard BFS that counts even- and odd-level nodes.
        Parity is determined by depth from the `start` node.
        '''
        odd_count: int = 0
        even_count: int = 1  # Start node is level 0
        visited[start] = 0
        level: int = 1
        que: deque[int | None] = deque([start, None])

        while que:
            node = que.popleft()
            if node is None:
                level += 1
                if que:
                    que.append(None)
                continue

            for edge in graph[node]:
                if edge in visited:
                    continue
                que.append(edge)
                visited[edge] = level
                if level % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1

        return even_count, odd_count

    # Build tree1 and tree2 graphs
    tree1_graph: dict[int, list[int]] = defaultdict(list)
    for start, end in edges1:
        tree1_graph[start].append(end)
        tree1_graph[end].append(start)

    tree2_graph: dict[int, list[int]] = defaultdict(list)
    for start, end in edges2:
        tree2_graph[start].append(end)
        tree2_graph[end].append(start)
    # We don't actually need `visited2`,
    #  because we only use `visited1` to get on which parity level node is placed.
    # { node: parity_level }
    visited1: dict[int, int] = {}
    visited2: dict[int, int] = {}

    even1, odd1 = bfs_count(0, tree1_graph, visited1)
    even2, odd2 = bfs_count(0, tree2_graph, visited2)
    # We can combine tree1 and tree2 on ANY nodes.
    # So, we actually should use theb maximized path we can get from the tree2.
    best_parity: int = max(odd2, even2)
    out: list[int] = [0] * len(tree1_graph)

    for node in tree1_graph:
        # We know parity_level of the nodes => use the path with such parity.
        if visited1[node] % 2 == 0:
            out[node] = even1 + best_parity
        else:
            out[node] = odd1 + best_parity
    
    return out


# Time complexity: O(m + n) - m - number of nodes in the first tree,
#                             n - number of nodes in the second tree.
# Always traversing both input trees with BFS, once => O(m + n).
# Extra traversing every node of the first tree => O(m + n + m)
# ----------------------------------
# Auxiliary space: O(m + n)
# `tree1_graph` & `tree2_graph` <- allocates space for each node => O(m + n).
# `visited1` & `visited2` <- allocates space for each node => O(2 * (m + n)).


test_edges1: list[list[int]] = [[0, 1], [0, 2], [2, 3], [2, 4]]
test_edges2: list[list[int]] = [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]]
test_out: list[int] = [8, 7, 7, 8, 8]
assert test_out == max_target_nodes(test_edges1, test_edges2)

test_edges1 = [[0, 1], [0, 2], [0, 3], [0, 4]]
test_edges2 = [[0, 1], [1, 2], [2, 3]]
test_out = [3, 6, 6, 6, 6]
assert test_out == max_target_nodes(test_edges1, test_edges2)
