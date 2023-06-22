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
    pass


test1 = [1, None, 2, 3]
test1_out = [1, 3, 2]

test2 = []
test2_out = []

test3 = [1]
test3_out = []
