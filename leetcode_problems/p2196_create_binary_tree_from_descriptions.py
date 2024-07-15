# You are given a 2D integer array descriptions where
#  descriptions[i] = [parenti, childi, isLefti]
#  indicates that parenti is the parent of childi in a binary tree of unique values.
# Furthermore,
#  - If isLefti == 1, then childi is the left child of parenti.
#  - If isLefti == 0, then childi is the right child of parenti.
# Construct the binary tree described by descriptions and return its root.
# The test cases will be generated such that the binary tree is valid.
# ----------------------
# 1 <= descriptions.length <= 10 ** 4
# descriptions[i].length == 3
# 1 <= parenti, childi <= 10 ** 5
# 0 <= isLefti <= 1
# The binary tree described by descriptions is valid.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(descriptions: list[list[int]]) -> TreeNode:
    # working_sol (90.24%, 16.16%) -> (1530ms, 26.37mb)  time: O(n) | space: O(n)
    cur_node: TreeNode
    # { node_value: node }
    nodes: dict[int, TreeNode] = {}
    have_parent: set[int] = set()

    # ! The binary tree described by descriptions is valid. !
    # Assume we won't be given 2 same descriptions.
    # And every parent is unique.
    for parent, child, side in descriptions:
        if parent not in nodes:
            cur_node = TreeNode(parent)
            nodes[parent] = cur_node
        else:
            cur_node = nodes[parent]
        if child not in nodes:
            cur_child = TreeNode(child)
            nodes[child] = cur_child
        else:
            cur_child = nodes[child]
        if side:
            cur_node.left = cur_child
        else:
            cur_node.right = cur_child
        have_parent.add(child)
    for node in nodes:
        if node not in have_parent:
            return nodes[node]


# Time complexity: O(n) <- n - length of the input array `descriptions`.
# Always traversing every description in `descriptions`, to build the BT => O(n).
# In the worst case, every description is creating a unique parent node.
# So, we're going to extra traverse every created Node to get a `root` of the BT => O(2n).
# ----------------------
# Auxiliary space: O(n)
# We will allocate space for every unique Node in `descriptions` => O(n).
# And extra `have_parents` is going to take `n - 1` space for every Node, except the `root` => O(2n).
