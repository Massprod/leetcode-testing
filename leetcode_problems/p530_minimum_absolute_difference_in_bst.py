# Given the root of a Binary Search Tree (BST),
#   return the minimum absolute difference between the values of any two different nodes in the tree.
# --------------------
# The number of nodes in the tree is in the range [2, 10 ** 4].
# 0 <= Node.val <= 10 ** 5


class TreeNode:

    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_minimum_diff(root: TreeNode) -> int | None:
    # working_sol (70.98%, 62.02%) -> (54ms, 18.58mb)  time: O(n * log n) | space: O(n)
    if not root:
        return None
    all_values: list[int] = []

    def read_tree(node: TreeNode) -> None:
        all_values.append(node.val)
        if node.left:
            read_tree(node.left)
        if node.right:
            read_tree(node.right)

    read_tree(root)
    all_values.sort()
    min_diff: int = abs(all_values[0] - all_values[-1])
    for x in range(1, len(all_values)):
        diff: int = abs(all_values[x] - all_values[x - 1])
        min_diff = min(diff, min_diff)
    return min_diff


# Time complexity: O(n * log n) -> inorder traverse to get all Nodes of input BT => O(n) ->
# n - Node of input BT^^|        -> sorting all these Nodes => O(n * log n) ->
#                                -> extra traverse to get minimum difference => O(n).
# Auxiliary space: O(n) -> worst case == linked list BT -> stack with size of all Nodes => O(n) ->
#                        -> extra array with all Nodes stored => O(2n).
