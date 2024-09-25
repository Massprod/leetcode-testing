# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1,
#  find all possible paths from node 0 to node n - 1 and return them in any order.
# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i
#  (i.e., there is a directed edge from node i to node graph[i][j]).
# -----------------------------------
# n == graph.length
# 2 <= n <= 15
# 0 <= graph[i][j] < n
# graph[i][j] != i (i.e., there will be no self-loops).
# All the elements of graph[i] are unique.
# The input graph is guaranteed to be a DAG.


def all_paths_source_target(graph: list[list[int]]) -> list[list[int]]:
    # working_sol (81.61%, 12.70%) -> (69ms, 18.32mb)  time: O(2 ** n) | space: O(2 ** n)
    out: list[list[int]] = []

    def dfs(node: int, path: list[int]) -> None:
        nonlocal out
        if node == len(graph) - 1:
            out.append(path[:])
            return
        for edge in graph[node]:
            path.append(edge)
            dfs(edge, path)
            path.pop()

    dfs(0, [0])
    return out


# Time complexity: O(2 ** n) <- n - number of Nodes in the input `graph`.
# We always traverse every possible path of graph from `0` Node => O(2 ** n).
# -----------------------------------
# Auxiliary space: O(2 ** n).
# In the worst case `path` can be of size `n`, our recursion stack will be of size `n` => O(n)
# We can be traversing `2 ** n` paths and all of them will be stored in `out` => O(n + 2 ** n).


test: list[list[int]] = [[1, 2], [3], [3], []]
test_out: list[list[int]] = [[0, 1, 3], [0, 2, 3]]
assert test_out == all_paths_source_target(test)

test = [[4, 3, 1], [3, 2, 4], [3], [4], []]
test_out = [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
assert test_out == all_paths_source_target(test)
