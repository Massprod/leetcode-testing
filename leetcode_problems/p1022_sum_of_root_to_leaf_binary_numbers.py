# You are given the root of a binary tree where each node has a value 0 or 1.
# Each root-to-leaf path represents a binary number starting with the most significant bit.
#  - For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
# Return the sum of these numbers.
# The test cases are generated so that the answer fits in a 32-bits integer.
# -------------------
# The number of nodes in the tree is in the range [1, 1000].
# Node.val is 0 or 1.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_root_to_leaf(root: TreeNode) -> int:
    # working_sol (81.48%, 78.93%) -> (34ms, 16.64mb)  time: O(n) | space: O(n)
    out: int = 0

    def traverse(node: TreeNode, path: int) -> None:
        nonlocal out
        path = (path << 1) + node.val
        if not node.left and not node.right:
            out += path
            return
        if node.left:
            traverse(node.left, path)
        if node.right:
            traverse(node.right, path)

    traverse(root, 0)
    return out


# Time complexity: O(n) <- n - number of Nodes inside the BT `root`.
# Always traversing whole input BT `root`, once => O(n).
# -------------------
# Auxiliary space: O(n).
# Stack of a recursion can be at max of `n` size => O(n).
