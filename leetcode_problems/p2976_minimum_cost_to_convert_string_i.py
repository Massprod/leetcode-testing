# You are given two 0-indexed strings source and target,
#  both of length n and consisting of lowercase English letters.
# You are also given two 0-indexed character arrays original and changed,
#  and an integer array cost, where cost[i] represents the cost of changing
#  the character original[i] to the character changed[i].
# You start with the string source. In one operation,
#  you can pick a character x from the string and change it to the character y
#  at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.
# Return the minimum cost to convert the string source to the string target
#  using any number of operations. If it is impossible to convert source to target, return -1.
# Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].
# -----------------------
# 1 <= source.length == target.length <= 10 ** 5
# source, target consist of lowercase English letters.
# 1 <= cost.length == original.length == changed.length <= 2000
# original[i], changed[i] are lowercase English letters.
# 1 <= cost[i] <= 10 ** 6
# original[i] != changed[i]
from string import ascii_lowercase


def minimum_cost(source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
    # working_sol (46.19%, 74.62%) -> (1881ms, 18.15mb)  time: O(n) | space: O(1)
    # !
    # We could use a dictionary instead of a matrix.
    # Then we could use only len(`source`) | len(`target`) Nodes.
    # But no time for rebuilding, maybe later.
    # And it could be much faster if there's < len(ascii_lowercase) chars present.
    # !
    # # Floyd-Warshall.
    # row <- Node, col <- Edge, cell_value <- Edge weight
    graph_distances: list[list[int | float]] = [
        [float('inf') for _ in ascii_lowercase] for _ in ascii_lowercase
    ]
    # Distances to Nodes to themselves == 0.
    for index in range(len(ascii_lowercase)):
        graph_distances[index][index] = 0
    # Distances we know.
    # And we can't transform `changed` -> `original`, so it's directed Graph.
    for index in range(len(original)):
        orig_node: int = ord(original[index]) - 97
        changed_node: int = ord(changed[index]) - 97
        weight: int = cost[index]
        graph_distances[orig_node][changed_node] = min(graph_distances[orig_node][changed_node], weight)
    # Find minimum distances, between two Nodes and two Nodes + connector Node between them.
    for con in range(len(graph_distances)):
        for node1 in range(len(graph_distances)):
            for node2 in range(len(graph_distances)):
                graph_distances[node1][node2] = min(
                    graph_distances[node1][node2],
                    graph_distances[node1][con] + graph_distances[con][node2]
                )
    out: int = 0
    for index in range(len(source)):
        node1: int = ord(source[index]) - 97
        node2: int = ord(target[index]) - 97
        distance: int = graph_distances[node1][node2]
        # We can't reach `node2` from `node1` == we can't convert it.
        if distance == float('inf'):
            return - 1
        out += graph_distances[node1][node2]
    return out


# Time complexity: O(n) <- n - length of the input arrays `original` | `changed`.
# Floyd-Warshall by default O(n ** 3), where `n` is a number of Nodes we use.
# No matter the input, we're always building a `graph_distances` for every lowercase_english_char.
# And traversing all of these Nodes.
# So, we can even call it constant time, and only loop to get `orig -> changed` distances are going to change
#  depending on the input `original` and `changed` => O(n).
# -----------------------
# Auxiliary space: O(1).
# `graph_distances` <- always of the same size `len(ascii_lowercase) * len(ascii_lowercase)`.


test_source: str = "abcd"
test_target: str = "acbe"
test_original: list[str] = ["a", "b", "c", "c", "e", "d"]
test_changed: list[str] = ["b", "c", "b", "e", "b", "e"]
test_cost: list[int] = [2, 5, 5, 1, 2, 20]
test_out: int = 28
assert test_out == minimum_cost(test_source, test_target, test_original, test_changed, test_cost)

test_source = "aaaa"
test_target = "bbbb"
test_original = ["a", "c"]
test_changed = ["c", "b"]
test_cost = [1, 2]
test_out = 12
assert test_out == minimum_cost(test_source, test_target, test_original, test_changed, test_cost)

test_source = "abcd"
test_target = "abce"
test_original = ["a"]
test_changed = ["e"]
test_cost = [10000]
test_out = -1
assert test_out == minimum_cost(test_source, test_target, test_original, test_changed, test_cost)
