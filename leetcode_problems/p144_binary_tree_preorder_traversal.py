# Given the root of a binary tree, return the preorder traversal of its nodes' values.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root: TreeNode) -> list[int] | None:
    # working_sol (97.85%, 38.73%) -> (35ms, 16.4mb)  time: O(n) | space: O(n)
    if not root:
        return None
    preorder: list[int] = []

    def pre_order(node: TreeNode) -> None:
        preorder.append(node.val)
        if node.left:
            pre_order(node.left)
        if node.right:
            pre_order(node.right)

    pre_order(root)
    return preorder


# Time complexity: O(n) -> every node will be used once => O(n).
# n - nodes of input_BT^^|
# Auxiliary space: O(n) -> worst case unbalanced tree with only 1 subtree like linked_list,
#                          recursion stack will hold every node of input_BT => O(n).
