# Alice and Bob have an undirected graph of n nodes and three types of edges:
#  - Type 1: Can be traversed by Alice only.
#  - Type 2: Can be traversed by Bob only.
#  - Type 3: Can be traversed by both Alice and Bob.
# Given an array edges where edges[i] = [typei, ui, vi] represents
#  a bidirectional edge of type typei between nodes ui and vi,
#  find the maximum number of edges you can remove so that after removing the edges,
#  the graph can still be fully traversed by both Alice and Bob.
# The graph is fully traversed by Alice and Bob if starting from any node,
#  they can reach all other nodes.
# Return the maximum number of edges you can remove,
#  or return -1 if Alice and Bob cannot fully traverse the graph.
# ---------------------------
# 1 <= n <= 10 ** 5
# 1 <= edges.length <= min(10 ** 5, 3 * n * (n - 1) / 2)
# edges[i].length == 3
# 1 <= typei <= 3
# 1 <= ui < vi <= n
# All tuples (typei, ui, vi) are distinct.
from collections import defaultdict


def max_num_edges_to_remove(n: int, edges: list[list[int]]) -> int:
    # working_sol (83.26%, 5.43%) -> (1592ms, 79.88mb)  time: O(n + E) | space: O(n)
    # {Node: {edges}} <- Node == Vertex
    graph: dict[int, set[int]] = defaultdict(set)
    for edge_type, start, end in edges:
        if 3 == edge_type:
            graph[start].add(end)
            graph[end].add(start)

    def dfs(cur_graph: dict[int, set[int]], cur_visited: list[int], cur_node: int, cur_path: int) -> int:
        if 0 != cur_visited[cur_node]:
            return 0
        cur_visited[cur_node] = cur_path
        dfs_out: int = 1
        for edge in cur_graph[cur_node]:
            dfs_out += dfs(cur_graph, cur_visited, edge, cur_path)
        return dfs_out

    # Number of edges we need to use for the whole `graph` travel of both `Alice` and `Bob`.
    out: int = 0
    # We travel all the `path`'s we can with type 3 edges.
    # It gives us an idea of how many isolated paths in the `graph` present.
    # Because they might allow us to cover the whole `graph`, but they need to be connected.
    # With `alice_type` and `bob_type`.
    # [identifier of the path] <- every index == Node of the graph, value == id of the path.
    visited: list[int] = [0] * (n + 1)
    path: int = 0
    for node in range(1, n + 1):
        # Either we already visited with another `path`.
        if 0 != visited[node]:
            continue
        # Or it's a new `path` we can build from this Node.
        path += 1
        # We start with `dfs_out` == 1, so we can return 1 for every Node without edges.
        # And `-1` is needed for adjusting the first Node we visit, we come to it without `edge` == started.
        out += dfs(graph, visited, node, path) - 1
    # After we found every possible type 3 path, we can either have them disconnected,
    #  and they will be connected with `alice_type` + `bob_type` between them to cover the whole `graph`.
    # Or they will not get connected, and we can't travel the whole `graph` correctly.
    # For this, we need to try and use only `alice_type` or `bob_type` edges and see
    #  if we can connect these paths in one go == travel whole `graph`.
    # {path: {edges}} <- edges == other paths we can connect with `alice_type` edges.
    alice_graph: dict[int, set[int]] = defaultdict(set)
    for edge_type, start, end in edges:
        if 1 == edge_type:
            path1: int = visited[start]
            path2: int = visited[end]
            # Because we need to check only connections between paths,
            #  we don't care about Nodes on the same path.
            if path1 != path2:
                alice_graph[path1].add(path2)
                alice_graph[path2].add(path1)
    # We need to check if we can connect distinct paths we get from our type 3 traversal.
    # With `alice_type` edges, if we can do this in 1 `alice_path`, then it's doable.
    # If we can't do this in 1 `alice_path`, then they can't be connected by `alice_type` edges,
    #  and we can't travel whole `graph` in 1 go == Alice can't travel it as a whole.
    alice_visited: list[int] = [0] * (path + 1)
    alice_path: int = 0
    for _path in range(1, path + 1):
        if 0 != alice_visited[_path]:
            continue
        if 0 != alice_path:
            return -1
        alice_path += 1
        dfs(alice_graph, alice_visited, _path, alice_path)
    # The same goes for a `Bob`.
    # {path: {edges}} <- edges == other paths we can connect with `bob_type` edges.
    bobs_graph: dict[int, set[int]] = defaultdict(set)
    for edge_type, start, end in edges:
        if 2 == edge_type:
            path1 = visited[start]
            path2 = visited[end]
            if path1 != path2:
                bobs_graph[path1].add(path2)
                bobs_graph[path2].add(path1)
    bobs_visited: list[int] = [0] * (path + 1)
    bobs_path: int = 0
    for _path in range(1, path + 1):
        if 0 != bobs_visited[_path]:
            continue
        if 0 != bobs_path:
            return -1
        bobs_path += 1
        dfs(bobs_graph, bobs_visited, _path, bobs_path)
    # If we can connect all the distinct paths, we found with type 3.
    # With `alice_type` and `bob_type`, then we can travel them with `Alice` and `Bob` correctly.
    # Which means we can just use only ONE of these paths (-1 for this).
    # And every path we connected will use 2 edges: one with `alice_type` another `bob_type` (* 2 for this).
    # So, we're leaving only 1 path with type 3 and adding 2 edges for every connection we need to make.
    out += (path - 1) * 2
    # out == all the type 3 edges we need to leave as it is, for correct full `graph` traverse +
    #  + extra edges for connecting all the paths in one.
    # Everything else can be deleted.
    # And the best way, in our case, is to delete `alice_type` and `bob_type` edges.
    # Because if some 2 Nodes are connected with all of 3 types, it's better to delete 2 edges than 1.
    return len(edges) - out


# Time complexity: O(n + E) <- E - number of unique edges in `edges`, n - input value `n`.
# Worst case:
#  We have all nodes connected by `alice_type and `bob_type` but not type 3.
# We can traverse the whole `graph` correctly, but for each Node we will use DFS and get a new `path` => O(n).
# We get paths == number of Nodes == number of edges == E.
# So, we will be forced to visit all of these Nodes with `Alice` and `Bob`
#  with using all the edges + build theirs Graphs => O(E).
# ---------------------------
# Auxiliary space: O(n)
# In the same worst case, we will get all the arrays and dicts with `n` size => O(n).
# Because `path` == `n`, every Node is disconnected == every Node is a new path.


test_n: int = 4
test_edges: list[list[int]] = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]
test_out: int = 2
assert test_out == max_num_edges_to_remove(test_n, test_edges)

test_n = 4
test_edges = [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]
test_out = 0
assert test_out == max_num_edges_to_remove(test_n, test_edges)

test_n = 4
test_edges = [[3, 2, 3], [1, 1, 2], [2, 3, 4]]
test_out = -1
assert test_out == max_num_edges_to_remove(test_n, test_edges)
