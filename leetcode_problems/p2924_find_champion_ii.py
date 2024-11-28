# There are n teams numbered from 0 to n - 1 in a tournament; each team is also a node in a DAG.
# You are given the integer n and a 0-indexed 2D integer array edges of length m representing the DAG,
#  where edges[i] = [ui, vi] indicates that there is a directed edge from team ui to team vi in the graph.
# A directed edge from a to b in the graph means that team a
#  is stronger than team b and team b is weaker than team a.
# Team a will be the champion of the tournament if there is no team b
#  that is stronger than team a.
# Return the team that will be the champion of the tournament if there is a unique champion, otherwise, return -1.
# Notes:
#  - A cycle is a series of nodes a1, a2, ..., an, an+1 such that node a1 is the same node as node an+1,
#   the nodes a1, a2, ..., an are distinct,
#   and there is a directed edge from the node ai to node ai+1 for every i in the range [1, n].
#  - A DAG is a directed graph that does not have any cycle.
# -------------------------
# 1 <= n <= 100
# m == edges.length
# 0 <= m <= n * (n - 1) / 2
# edges[i].length == 2
# 0 <= edge[i][j] <= n - 1
# edges[i][0] != edges[i][1]
# The input is generated such that if team a is stronger than team b, team b is not stronger than team a.
# The input is generated such that if team a is stronger than team b and team b is stronger than team c,
#  then team a is stronger than team c.


def find_champion(n: int, edges: list[list[int]]) -> int:
    # working_sol (5.30%, 9.65%) -> (76ms, 18.29mb)  time: O(n + m) | space: O(n)
    nodes: set[int] = {node for node in range(n)}
    for start, end in edges:
        if end in nodes:
            nodes.remove(end)
    return -1 if len(nodes) != 1 else nodes.pop()


# Time complexity: O(n + m) <- m - length of the input array `edges`.
# Always creating `nodes` with the size of `n` => O(n).
# Extra traversing all edges in `edges` => O(n + m).
# -------------------------
# Auxiliary space: O(n)
# `nodes` <- allocates space for all nodes in range `0 -> n` inclusive => O(n).


test: int = 3
test_edges: list[list[int]] = [[0, 1], [1, 2]]
test_out: int = 0
assert test_out == find_champion(test, test_edges)

test = 4
test_edges = [[0, 2], [1, 3], [1, 2]]
test_out = -1
assert test_out == find_champion(test, test_edges)
