# A tree is an undirected graph in which any two vertices are connected by exactly one path.
# In other words, any connected graph without simple cycles is a tree.
# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges
#  where edges[i] = [ai, bi] indicates that there is an undirected edge between
#  the two nodes ai and bi in the tree, you can choose any node of the tree as the root.
# When you select a node x as the root, the result tree has height h.
# Among all possible rooted trees, those with minimum height (i.e. min(h))
#  are called minimum height trees (MHTs).
# Return a list of all MHTs' root labels.
# You can return the answer in any order.
# The height of a rooted tree is the number of edges on the longest downward path
#  between the root and a leaf.
# ------------------------------
# 1 <= n <= 2 * 10 ** 4
# edges.length == n - 1
# 0 <= ai, bi < n
# ai != bi
# All the pairs (ai, bi) are distinct.
# The given input is guaranteed to be a tree and there will be no repeated edges.
from collections import deque, defaultdict


def find_min_height_trees(n: int, edges: list[list[int]]) -> list[int]:
    # working_sol (91.17%, 99.68%) -> (389ms, 25.92mb)  time: O(k + n) | space: O(n + k)
    if not edges:
        return [0]
    # {vertex: [all the edges]}
    graph: dict[int, list[int]] = defaultdict(list)
    for start, end in edges:
        graph[start].append(end)
        graph[end].append(start)
    # index == node_number, [index] == edges of this node.
    neighbours: list[int] = [0] * n
    for node in graph:
        neighbours[node] = len(graph[node])
    leaves: deque[int] = deque([index for index, val in enumerate(neighbours) if val == 1])
    cur_nodes: int = n
    while cur_nodes > 2:
        leaves_to_del: int = len(leaves)
        cur_nodes -= leaves_to_del
        while leaves_to_del:
            leaves_to_del -= 1
            leaf: int = leaves.popleft()
            for edge in graph[leaf]:
                neighbours[edge] -= 1
                if 1 == neighbours[edge]:
                    leaves.append(edge)
    return list(leaves)


# Time complexity: O(k + n) <- k - length of an input array `edges`, n - input value `n`.
# First, we're creating `graph` with using of all the edges in `edges` => O(k)
# Then we're always creating array with size of `n` to assign number of edges (neighbor nodes) they have,
#  and in the worst case, we're given all `n` nodes in `edges` => O(2n).
# Then we're deleting all the leaves level by level, until there's 2 or fewer nodes left.
# Because in our graph we can have at max 2 MHT's(MinimumHeightTree), when we start from one of them,
#  we will always go through other, but end on some distant leaf.
# And when we start from another, we will end on some other distant leaf, but also go through our first node.
# And there's no way we can have 2+ going like this.
# So, we're always using (n - 2) nodes in our deletion process => O(n).
# ------------------------------
# Auxiliary space: O(k + n).
# In the worst case, our `edges` will store `n` nodes, so `graph` holds `n` keys => O(k).
# And in the case of edges, we can have one node connected to everyone else, so it will hold `n - 1` nodes as edges.
# Extra our array `neighbours` will be always of size `n` to show all connections for `n` nodes => O(n).


test_n: int = 4
test_edges: list[list[int]] = [[1, 0], [1, 2], [1, 3]]
test_out: list[int] = [1]
assert test_out == find_min_height_trees(test_n, test_edges)

test_n = 6
test_edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
test_out = [3, 4]
assert test_out == find_min_height_trees(test_n, test_edges)

test_n = 1
test_edges = []
test_out = [0]
assert test_out == find_min_height_trees(test_n, test_edges)
