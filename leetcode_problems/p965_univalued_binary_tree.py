# A binary tree is uni-valued if every node in the tree has the same value.
# Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.
# -----------------------
# The number of nodes in the tree is in the range [1, 100].
# 0 <= Node.val < 100


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_univalued(root: TreeNode) -> bool:
    # working_sol (63.50%, 58.28%) -> (35ms, 16.43mb)  time: O(n) | space: O(n)
    univalue: int = root.val

    def traverse(node: TreeNode) -> bool:
        nonlocal univalue
        if node.val != univalue:
            return False
        if node.left and not traverse(node.left):
            return False
        if node.right and not traverse(node.right):
            return False
        return True

    return traverse(root)


# Time complexity: O(n) <- n - number of Nodes inside the input BT `root`.
# Always traversing input BT `root`, once => O(n).
# -----------------------
# Auxiliary space: O(n)
# In the worst case, BT is build like as a LinkedList, and it's univalued.
# So, we're going to have a recursion stack with `n` depth => O(n).
