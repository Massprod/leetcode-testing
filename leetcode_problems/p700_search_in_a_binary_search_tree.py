# You are given the root of a binary search tree (BST) and an integer val.
# Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
# If such a node does not exist, return null.
# ------------------------
# The number of nodes in the tree is in the range [1, 5000].
# 1 <= Node.val <= 10 ** 7
# root is a binary search tree.
# 1 <= val <= 10 ** 7


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def search_bst(root: TreeNode, val: int) -> TreeNode:
    # working_sol (87.40%, 73.5%) -> (70ms, 18.4mb)  time: O(log n) | space: O(log n)

    def search(node: TreeNode) -> TreeNode | None:
        if not node:
            return
        if node.val == val:
            return node
        # Every LeftSubtree only values lower than Parent.
        if val < node.val:
            return search(node.left)
        # Every RightSubtree only values higher than Parent.
        if val > node.val:
            return search(node.right)

    return search(root)


# Time complexity: O(log n) -> we always move only in one of the subtrees of the node, so its should never
# n - nodes of input_BST^^| cover whole tree node, but only a part of them => O(log n).
# Auxiliary space: O(log n) -> stack of recursion for every node checked, only part of the all nodes => O(log n).
# ------------------------
# By default, BST -> every LeftSubtree only values lower than ParentNode, and RightSubtree only values higher.
# Standard move left or right until hit or None.
