# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from
#   the root node down to the farthest leaf node.
# ---------------------
# The number of nodes in the tree is in the range [0, 10 ** 4].
# -100 <= Node.val <= 100


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode) -> int:
    # working_sol (79.88%, 35.71%) -> (53ms, 18.8mb)  time: O(n) | space: O(log n)
    if not root:
        return 0
    max_dep: list[int | None] = [None]

    def inorder(node: TreeNode, level: int = 0) -> None:
        level += 1
        if node.left is None and node.right is None:
            if max_dep[0] is None:
                max_dep[0] = level
            else:
                max_dep[0] = max(max_dep[0], level)
            return
        if node.left:
            inorder(node.left, level)
        if node.right:
            inorder(node.right, level)

    inorder(root)
    return max_dep[0]


# Time complexity: O(n) -> in_order traversal of whole input_BT, once => O(n).
# n - nodes in BT^^|
# Auxiliary space: O(log n) -> standard stack for recursion with BT => O(log n).
