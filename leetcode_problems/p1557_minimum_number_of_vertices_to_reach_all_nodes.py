# Given a directed acyclic graph, with n vertices numbered from 0 to n-1,
#  and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.
# Find the smallest set of vertices from which all nodes in the graph are reachable.
# It's guaranteed that a unique solution exists.
# Notice that you can return the vertices in any order.
# -----------------------
# 2 <= n <= 10  ** 5
# 1 <= edges.length <= min(10 ** 5, n * (n - 1) / 2)
# edges[i].length == 2
# 0 <= fromi, toi < n
# All pairs (fromi, toi) are distinct.


def find_smallest_set_of_vert(n: int, edges: list[list[int]]) -> list[int]:
    # working_sol (97.48%, 91.85%) -> (999ms, 54.5mb)  time: O(n + m) | space: O((n - k) + k)
    pointed: set[int] = set()
    for start, end in edges:
        pointed.add(end)
    nodes: list[int] = []
    # ! with n vertices numbered from 0 to n-1 !
    for node in range(n):
        if node not in pointed:
            nodes.append(node)
    return nodes


# Time complexity: O(n + m) -> traversing whole input array 'edges' to get all Nodes which gets pointed => O(m) ->
# m - len of input array 'edges'^^| -> standard loop from 0 -> n, to get Nodes without a pointer => O(n).
# n - input value 'n'^^|
# Auxiliary space: O((n - k) + k) -> 'pointed' will store only Nodes which gets pointed by something else ->
#                                 -> and it's always equal to # of 'ends' -> Nodes without pointer = (all - pointed) ->
#                                 -> so it should be correct to say: O((n - k) + k)
#                                    or O((n - m) + m) if only unique ends present.
# k - number of pointed Nodes == number of unique 'ends' in edges^^|
# -----------------------
# If something pointing to the Node == it can be reached from somewhere.
# And we only need Minimum option == use only Nodes which Points, but not pointed.
# Should be correct to just count these Nodes, especially when we're given number of all Nodes == 'n'.
# Let's try.


test_n: int = 6
test_edges: list[list[int]] = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
test_out: list[int] = [0, 3]
assert test_out == find_smallest_set_of_vert(test_n, test_edges)

test_n = 5
test_edges = [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]
test_out = [0, 2, 3]
assert test_out == find_smallest_set_of_vert(test_n, test_edges)
