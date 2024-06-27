# There is an undirected star graph consisting of n nodes labeled from 1 to n.
# A star graph is a graph where there is one center node and exactly n - 1 edges
#  that connect the center node with every other node.
# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates
#  that there is an edge between the nodes ui and vi.
# Return the center of the given star graph.
# ---------------------------
# 3 <= n <= 10 ** 5
# edges.length == n - 1
# edges[i].length == 2
# 1 <= ui, vi <= n
# ui != vi
# The given edges represent a valid star graph.
from collections import defaultdict


def find_center(edges: list[list[int]]) -> int:
    # working_sol (98.71%, 86.58%) -> (629ms, 52.06mb)  time: O(1) | space: O(1)
    # ! one center node and exactly n - 1 edges !
    # So, we're always going to have `center` node with more than 1 edge.
    # And everything else is only connected to him.
    graph: dict[int, list[int]] = defaultdict(list)
    for start, end in edges:
        graph[start].append(end)
        graph[end].append(start)
        if 2 <= len(graph[start]):
            return start
        elif 2 <= len(graph[end]):
            return end


# Time complexity: O(1)
# If we assume that we're always given a `star` graph and with our description is going to always have
#  all the nodes connected to the `center` and never intercourse between themselves.
# Which means w.e 2 edges we're going to take, they always will point to the `center`.
# So, we always check only 2 edges => O(1).
# Even if we're going to have `center` node pointing to them, we're still building undirected graph.
# Still, only 2 edges will be used.
# ---------------------------
# Auxiliary space: O(1).
# And if we use only 2 edges, we will store only them => O(1).


test: list[list[int]] = [[1, 2], [2, 3], [4, 2]]
test_out: int = 2
assert test_out == find_center(test)

test = [[1, 2], [5, 1], [1, 3], [1, 4]]
test_out = 1
assert test_out == find_center(test)
