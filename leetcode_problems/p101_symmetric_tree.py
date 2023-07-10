# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# ---------------
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: TreeNode) -> bool:
    # working_sol (46.74%, 81.91%) -> (52ms, 16.4mb)  time: O(n) | space: O(n)
    if root.left is None and root.right is None:
        return True
    if root.left is None and root.right:
        return False
    if root.right is None and root.left:
        return False
    # left_part of BT
    left_part: list[int | None] = []
    # mirrored right_part of BT
    right_part: list[int | None] = []

    def inorder(node: TreeNode, left_p: bool, right_p: bool) -> None:
        # reading left_subtree
        if left_p:
            if node.left:
                inorder(node.left, left_p, False)
            else:
                left_part.append(None)
            if node.right:
                inorder(node.right, left_p, False)
            else:
                left_part.append(None)
            left_part.append(node.val)
        # mirror reading right_subtree
        if right_p:
            if node.right:
                inorder(node.right, False, right_p)
            else:
                right_part.append(None)
            if node.left:
                inorder(node.left, False, right_p)
            else:
                right_part.append(None)
            right_part.append(node.val)

    inorder(root.left, True, False)
    inorder(root.right, False, True)
    if left_part == right_part:
        return True
    return False


# Time complexity: O(n) -> inorder traversal of whole input_BT, to store values of both sides => O(n-1) ->
# n - nodes in input_BT^^| -> comparing both lists with summarized length of (n - 1) => O(n - 1) ->
#                          -> O(n - 1) + O(n - 1) => O(2 * (n - 1)) => O(n - 1) => O(n).
# Auxiliary space: O(n) -> creating 2 extra lists with summarized length of (n - 1) to store values
#                          from both subtrees of a root_node => O(n - 1) ->
#                          -> and because we're using recursion, it's taking extra space of O(n - 1) ->
#                          -> O(n - 1) + O(n - 1) => O(2 * (n - 1)) => O(n - 1) => O(n).
# ---------------
# Using extra memory, because didn't come up with solution how we can traverse both subtrees
#   at the same time and break when values aren't equal.
# If it's even possible, maybe extra search later.
# Works fine at speed of 52ms 45+%, but with extra memory usage to store lists.
# Failed commit because forgot to add -> case with one of the subtrees being empty.
