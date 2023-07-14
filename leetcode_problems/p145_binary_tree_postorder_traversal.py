# Given the root of a binary tree, return the postorder traversal of its nodes' values.
# ---------------
# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorder_traversal(root: TreeNode) -> list[int] | None:
    # working_sol (98.71%, 39.78%) -> (33ms, 16.34mb)  time: O(n) | space: O(n)
    if not root:
        return None
    postorder: list[int] = []

    def post_order(node: TreeNode) -> None:
        if node.left:
            post_order(node.left)
        if node.right:
            post_order(node.right)
        postorder.append(node.val)

    post_order(root)
    return postorder


# Time complexity: O(n) -> every node will be used once => O(n).
# n - nodes of input_BT^^|
# Auxiliary space: O(n) -> worst case unbalanced tree with only 1 subtree like linked_list,
#                          recursion stack will hold every node of input_BT => O(n).
