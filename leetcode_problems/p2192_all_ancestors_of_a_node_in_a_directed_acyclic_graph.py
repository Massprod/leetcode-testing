# You are given a positive integer n representing the number of nodes
#  of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).
# You are also given a 2D integer array edges, where edges[i] = [fromi, toi]
#  denotes that there is a unidirectional edge from fromi to toi in the graph.
# Return a list answer, where answer[i] is the list of ancestors of the ith node,
#  sorted in ascending order.
# A node u is an ancestor of another node v if u can reach v via a set of edges.
# ------------------------
# 1 <= n <= 1000
# 0 <= edges.length <= min(2000, n * (n - 1) / 2)
# edges[i].length == 2
# 0 <= fromi, toi <= n - 1
# fromi != toi
# There are no duplicate edges.
# The graph is directed and acyclic.
from collections import defaultdict


def get_ancestors(n: int, edges: list[list[int]]) -> list[list[int]]:
    # working_sol (79.07%, 48.95%) -> (451ms, 47.94mb)  time: O(k * n + n * log n) | space: O(n + k)
    # [True == doesn't have a parent, False = have a parent]
    # We only care about Nodes from which we can travel a full paths.
    no_parent: list[int] = [True] * n
    # {Node: [edges]} <- acyclic, so we can leave it a list.
    # Reversing the original Graph because it's going to be easier to collect parents in reverse.
    # Otherwise, we can have a situation when Node is having 2 parents, and we will need to add
    #  a full path from both parents to every child.
    # While in reverse, we can just record both parents for every child on the `path` we traveled.
    graph: dict[int, list[int]] = defaultdict(list)
    for start, end in edges:
        graph[end].append(start)
        no_parent[start] = False
    out: list[list[int]] | list[set[int]] = [set() for _ in range(n)]

    def dfs(node: int, path: set[int]) -> None:
        # End of the route.
        if node not in graph:
            return
        # We already visited every parent of this Node.
        # But now, we come to this Node from a different path.
        # So, every parent of this Node should be added to every Node on the path.
        # We can either reTravel the same path, or add them from `out`.
        if 0 < len(out[node]):
            for prev_node in path:
                out[prev_node].update(out[node])
            return
        # Mar every Node on the `path`.
        path.add(node)
        for edge in graph[node]:
            # Every node on the `path` is always having the same parents.
            # In top -> down manner.
            for prev_node in path:
                out[prev_node].add(edge)
            dfs(edge, path)
        # Unmark after using it.
        path.remove(node)

    for _node, parent in enumerate(no_parent):
        if parent:
            dfs(_node, set())
    # ! Return a list answer, where answer[i] is the list of ancestors of the ith node,
    #   sorted in ascending order. !
    for index in range(len(out)):
        out[index] = sorted(out[index])
    return out


# Time complexity: O(k * n + n * log n) <- n - number of Nodes in `graph`, k - number of edges in `graph`.
# The worst case should be something like:
#  the whole graph is just a linked list.
# So, when we travel it, we will loop through the whole `path` over and over again, for every `edge`.
# And our path is starting from 1 -> (n - 1), with every newNode => O(k * n)
# After DFS, we're sorting everything, and in our case we can have (n - 1) nodes as parents.
# In the worst case, we're having oneNode and others are parents.
# So, we will sort (n - 1) parents => O(n * log n).
# ------------------------
# Auxiliary space: O(n + k)
# `no_parent` is always of size `n` => O(n).
# `graph` can be at max of size `n - 1` with only 1 parent present => O(n - 1).
# In the same worst case, our `dfs` stack can be a size of `n` => O(n).
# `out` will store every Node and all the connected parents.
# In the worst case, we're having oneNode, and others are parents == all empty and oneNode with `k` edge => O(n + k).


test_n: int = 8
test: list[list[int]] = [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]
test_out: list[list[int]] = [[], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3]]
assert test_out == get_ancestors(test_n, test)

test_n = 5
test = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
test_out = [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
assert test_out == get_ancestors(test_n, test)
