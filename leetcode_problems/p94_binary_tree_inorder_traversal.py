# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# ------------------
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode) -> list[int]:
    # working_sol (74.53%,  70.47%) -> (43ms, 16.2mb)  time: O(n) | space: O(n)
    if not root:
        return root
    inorder_traver: list[int] = []

    def inorder(node: TreeNode) -> None:
        if node.left is None:
            inorder_traver.append(node.val)
        if node.left:
            inorder(node.left)
            inorder_traver.append(node.val)
        if node.right:
            inorder(node.right)

    inorder(root)
    return inorder_traver


# Time complexity: O(n) -> traversing whole BT(binary tree) only once => O(n)
# n - number of nodes in input_BT^^|
# Auxiliary space: O(n) -> storing every node.val from original BT into list of these values with size of n => O(n)
# ------------------
# Next task is to recreate binary Tree, and then I will build it and made test function.
# In this one I will just traverse InOrder.
# !
# An inorder traversal first visits the left child (including its entire subtree),
# then visits the node, and finally visits the right child (including its entire subtree). !
