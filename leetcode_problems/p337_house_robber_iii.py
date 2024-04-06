# The thief has found himself a new place for his thievery again.
# There is only one entrance to this area, called root.
# Besides the root, each house has one and only one parent house.
# After a tour, the smart thief realized that all houses in this place form a binary tree.
# It will automatically contact the police if two directly-linked houses were broken into on the same night.
# Given the root of the binary tree, return the maximum amount of money the thief can rob
#  without alerting the police.
# ---------------------------
# The number of nodes in the tree is in the range [1, 10 ** 4].
# 0 <= Node.val <= 10 ** 4
from random import randint
from functools import cache


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rob(root: TreeNode) -> int:
    # working_sol (73.92%, 79.19%) -> (43ms, 18.10mb)  time: O(n) | space: O(n)
    def dfs(node: TreeNode) -> tuple[int, int]:
        if not node:
            return 0, 0
        left: tuple[int, int] = dfs(node.left)
        right: tuple[int, int] = dfs(node.right)
        skip: int = max(left) + max(right)
        not_skip: int = node.val + left[1] + right[1]
        return not_skip, skip

    return max(dfs(root))


# Time complexity: O(n) <- n - number of Nodes inside input BT `root`.
# Traversing whole BT once.
# ---------------------------
# Auxiliary space: O(n).
# Worst case: BT in style of LinkedList, so every Node will be in recursion stack.
