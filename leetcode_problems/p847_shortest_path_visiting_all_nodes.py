# You have an undirected, connected graph of n nodes labeled from 0 to n - 1.
# You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.
# Return the length of the shortest path that visits every node.
# You may start and stop at any node, you may revisit nodes multiple times,
#  and you may reuse edges.
# --------------------
# n == graph.length
# 1 <= n <= 12
# 0 <= graph[i].length < n
# graph[i] does not contain i.
# If graph[a] contains b, then graph[b] contains a.
# The input graph is always connected.
from collections import deque


def shortest_path_length(graph: list[list[int]]) -> int:
    # working_sol (87.08%, 72.31%) -> (150ms, 21.2mb)  time: O(2 ** n * n) | space: O(2 ** n * n)
    # (node, path, path_length)
    que: deque[tuple[int, int, int]] = deque()
    # ! 1 <= n <= 12 ! <- maximum 12 nodes, labeled 0-indexed.
    # path == bit mask with 0 -> 11 bits used as positions, inclusive.
    #  for graph nodes: '1' == node visited, '0' == not visited.
    path: int = 1
    # For every used node we will place '1'.
    #  fully correct == all nodes of the graph placed in the bit mask.
    # I.e. all nodes being used on the path we travelled.
    full_path: int = 0
    for _ in range(len(graph)):
        full_path = (full_path << 1) + 1
    # (node, path)
    # node - lastly used node on saved path.
    # If we ever try to add node into the same path twice, we can ignore it.
    visited: set[tuple[int, int]] = set()
    for x in range(len(graph)):
        que.append(
            (
                x,  # node index.
                path << x,  # Place '1' bit to denote node position in the path.
                1,  # We only used node itself, path_length == 1.
            )
        )
        visited.add((x, path << x))
    # Check every path possible with BFS.
    while que:
        data: tuple[int, int, int] = que.popleft()
        check_node: int = data[0]
        path: int = data[1]
        path_length: int = data[2]
        # If we used every node in the graph.
        if path == full_path:
            # ! Return the length of the shortest path that visits every node. !
            # We actually need to return edges we used, not # of nodes.
            print(len(visited))
            return path_length - 1
        for node in graph[check_node]:
            # | => 0 -> 1, 1 -> 0 place '1' on empty spot.
            new_path: int = path | (1 << node)
            # If node wasn't used with this path, we can use it.
            if (node, new_path) not in visited:
                que.append((node, new_path, path_length + 1))
                visited.add((node, new_path))


# Time complexity: O(2 ** n * n) -> we're checking all subsets of nodes in the input_array => O(2 ** n) ->
# n - len of input_array^^| -> and for every subset we're travelling it with using n nodes => O(2 ** n * n).
# Auxiliary space: O(2 ** n * n) -> we're storing every possible subset and nodes used in them => O(2 ** n * n).
# --------------------
# Tags:
# ! Dynamic Programming, Bit Manipulation, Breadth-First Search, Graph, Bitmask !
# Never done any BFS with bitmask, so can't even think for what reason we need it.
# Ok. We can use bitmask to store current path we're travelling.
# Data structure to store in a que: (node, path, path_length)
# node - last node we used on this path,
# path - already travelled path using BFS,
# path_length - current length of this path.
# We mark visited nodes with: (node, path)
# So if we ever try to use Node with the same path travelled, we will ignore it.
# Everything else is just BFS with incrementing of path_length for every Node used on the path.
# Extra length of the shortest path it's not nodes used, but EDGES == (path_length - 1).


test: list[list[int]] = [[1, 2, 3], [0], [0], [0]]
test_out: int = 4
assert test_out == shortest_path_length(test)

test = [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]
test_out = 4
assert test_out == shortest_path_length(test)
