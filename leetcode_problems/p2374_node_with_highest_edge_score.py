# You are given a directed graph with n nodes labeled from 0 to n - 1,
#   where each node has exactly one outgoing edge.
# The graph is represented by a given 0-indexed integer array edges of length n,
#   where edges[i] indicates that there is a directed edge from node i to node edges[i].
# The edge score of a node i is defined as the sum of the labels of all the nodes that have an edge pointing to i.
# Return the node with the highest edge score. If multiple nodes have the same edge score,
#   return the node with the smallest index.
# -------------------
# n == edges.length
# 2 <= n <= 10 ** 5
# 0 <= edges[i] < n
# edges[i] != i
from random import randint


def edge_score(edges: list[int]) -> int:
    # working_sol (99.48%, 95.31%) -> (969ms, 30.2mb)  time: O(n) | space: O(n)
    # Store edge sums for every node.
    nodes: list[int] = [0 for _ in edges]
    # Indexes of all edges should be summarized.
    for x in range(len(edges)):
        nodes[edges[x]] += x
    # index() + max() is 2 traverses,
    # and it can be done in 1:
    max_val: int = 0
    max_index: int = 0
    for y in range(len(nodes)):
        # Equal ignore, to save first_occurrence.
        if nodes[y] > max_val:
            max_val = nodes[y]
            max_index = y
    return max_index


# Time complexity: O(n) -> traversing whole input_array once to recreate same size list of nodes => O(n) ->
# n - len of input_array^^| -> extra traverse to summarize all edges => O(n) -> extra traverse to get maximum => O(n)
#                           and another extra traverse to get index of this max_value, in the worst case it's the last
#                           index => O(n).
#                           Can I take max_value without index? Well we can't maintain max_val, cuz next nodes can
#                           point backwards, so it's 100% extra max() to get it. And only way I escape from index(),
#                           it's just record all indexes with max_val while searching max. Not really improvement,
#                           but it's better on speed.
# Auxiliary space: O(n) -> creating extra list size with size of original input_array => O(n).
# -------------------
# How it's medium? Just store every index and add every index pointing on it.
# Guess there's some tricky part, I can't see for now.
# Medium == Kappa.


test: list[int] = [1, 0, 0, 0, 0, 7, 7, 5]
test_out: int = 7
assert test_out == edge_score(test)

test = [2, 0, 0, 2]
test_out = 0
assert test_out == edge_score(test)

test = []
for _ in range(10 ** 5):
    value: int = randint(0, (10 ** 5) - 1)
    while value == _:
        value = randint(0, (10 ** 5) - 1)
    test.append(value)
# print(test)
