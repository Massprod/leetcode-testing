# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
# --------------------
# The number of nodes in the graph is in the range [0, 100].
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# There are no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given node.


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Node) -> Node:
    # working_sol (99.26%, 67.30%) -> (39ms, 16.8mb)  time: O(n) | space: O(n * k)
    if not node:
        return node
    nodes: dict[int, list[int]] = {}

    def search_nodes(node_: Node) -> None:
        # find base to rebuild from
        # if node already recorded then his neighbor values too, ignore
        if node_.val in nodes:
            return
        nodes[node_.val] = []
        # For every neighbor recall to add it as well,
        # for every neighbor store it's unique value to link after,
        # unique values in our case is always a node place in a graph.
        for neighbor in node_.neighbors:
            nodes[node_.val].append(neighbor.val)
            search_nodes(neighbor)

    search_nodes(node)
    # every key represents node place in a graph, and in our case all unique and sorted.
    # We can relink them just from a list with indexes representing their place.
    # Place nodes on their place/index
    copied_nodes: list[Node] = [Node(val=0)] + [Node(val=key) for key in range(1, max(nodes.keys()) + 1)]
    # Link nodes between them
    for x in range(1, len(copied_nodes)):
        cur_node: Node = copied_nodes[x]
        for value in nodes[cur_node.val]:
            cur_node.neighbors.append(copied_nodes[value])
    return copied_nodes[1]


# Time complexity: O(n) -> recursion will call nodes in a graph only once => O(n) ->
# n - nodes in graph^^| -> after storing every node, and it's neighbor values, creating array of n + 1 size,
#                       with Nodes placed on their index in array representing place in graph =>
#                       => O(n + 1) -> for every Node in this array, populating its neighbors with
#                       stored values in dictionary, representing Node places/indexes => O(n) ->
#                       -> O(n) + O(n + 1) + O(n) => O(n).
# Auxiliary space: O(n * k) -> dictionary to store every Node as it's key, and values are representing neighbors =>
# k - num of node_neighbors^^| => O(n * k) -> extra creating array with copies of original Nodes, and placeholder =>
#                              => O(n + 1) -> O(n * k) + O(n + 1) => O(n * k).
# !
# Should i consider neighbors we assign, as extra space? Like it's just a link of a node, like in linked_list and BT.
# Then it's should be taking extra space, it's already stored, and we're just pointing on it. !
# --------------------
# Make dict, store every unique VAL in it <- every node.val is unique and represent its place.
# For every VAL in dict store links to an adjacent nodes, and rebuild from it.
# --------------------
# First encounter with actual GRAPH, not some arrays/dicts representing it.
# So I will do my solution first, and extra search after for better/faster options.
