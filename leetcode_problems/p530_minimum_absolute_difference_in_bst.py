# Given the root of a Binary Search Tree (BST),
#   return the minimum absolute difference between the values of any two different nodes in the tree.
# --------------------
# The number of nodes in the tree is in the range [2, 10 ** 4].
# 0 <= Node.val <= 10 ** 5
from typing import Optional


class TreeNode:

    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_minimum_diff(root: Optional[TreeNode]) -> int:
    pass


# Not creating TreeNodes to test, and not using tests in this case.
# Because I know how to search BTS, but if I made creation of BTS it's the same as reading it,
# and I can't do this today. So just reading for now.
