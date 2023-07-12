# There is a directed graph of n nodes with each node labeled from 0 to n - 1.
# The graph is represented by a 0-indexed 2D integer array graph where graph[i]
#   is an integer array of nodes adjacent to node i,
#   meaning there is an edge from node i to each node in graph[i].
# A node is a terminal node if there are no outgoing edges.
# A node is a safe node if every possible path starting from that node
#   leads to a terminal node (or another safe node).
# Return an array containing all the safe nodes of the graph.
# The answer should be sorted in ascending order.
# --------------------
# n == graph.length  ,  1 <= n <= 10 ** 4
# 0 <= graph[i].length <= n  ,  0 <= graph[i][j] <= n - 1
# graph[i] is sorted in a strictly increasing order.
# The graph may contain self-loops.
# The number of edges in the graph will be in the range [1, 4 * 10 ** 4].


def eventual_safe_nodes(graph: list[list[int]]) -> list[int]:
    safe_nodes: set[int] = set()
    unsafe_nodes: set[int] = set()

    def check_edges(graph_index: int, path: set[int]) -> bool:
        for edge in graph[graph_index]:
            if edge in path or edge in unsafe_nodes:
                for _ in path:
                    unsafe_nodes.add(_)
                    if _ in safe_nodes:
                        safe_nodes.remove(_)
                return False
            path.add(edge)
            if not check_edges(edge, path):
                return False
            path.remove(edge)
        for _ in path:
            safe_nodes.add(_)
        return True

    for x in range(len(graph)):
        if x not in safe_nodes:
            if (x not in unsafe_nodes) and check_edges(x, {x}):
                safe_nodes.add(x)
    return safe_nodes - unsafe_nodes


# Ok. Extra search, there's some part I just don't know how to use faster.
#
# --------------------
# 93/112 and TLE. Well it's working, but what can we cull?
# Add extra check if X is already in unsafe_nodes which is ignoring recursion call for that,
# and added whole path with a loop into unsafe_nodes, not enough.
# I could extra remember correct path, but then I would need to delete unsafe nodes from it, after we found them.
# It's going to be even slower, or use set for this, but then we need to sort it after...
# --------------------
# !
# The graph may contain self-loops. ! if loops than it's insta_False, cuz it can't have all path leading to terminals.
# Recursion with checking every node in graphs to check every path of this node leading to terminal,
# or having a loop? But what is PATH here?
# Like in first test 0 -> 1 -> 2 -> 5 correct path, but there's another path from 1 which doesn't lead
# to the terminal 1 -> 3 -> 0 it's a loop, and it's incorrect in example.
# So every path STARTING from 0 should be correct even if it SPLITS?
# Because 0 -> 1 is correct path if we consider his continuation as 2 -> 5 but, if we split it
# than it should have both path correct. Only way why it can be False in example.
# So we need to have all SPLITS a.k.a node being safe or terminal.
# Guess loop should be insta False for every node included in it,
# cuz it's one of their ways(splits) leading to a loop.
# No idea about TLE, but if we have 10 ** 4 nodes it's need to be sorted along the way for ->
# -> ! The answer should be sorted in ascending order. ! -> otherwise it's extra slow.


test1 = [[1, 2], [2, 3], [5], [0], [5], [], []]
test1_out = [2, 4, 5, 6]
print(eventual_safe_nodes(test1))

test2 = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]
test2_out = [4]
print(eventual_safe_nodes(test2))

test3 = [[]]
test3_out = 0
print(eventual_safe_nodes(test3))
