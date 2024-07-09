# Given the root of a binary search tree, rearrange the tree in in-order
#  so that the leftmost node in the tree is now the root of the tree,
#  and every node has no left child and only one right child.
# ----------------------
# The number of nodes in the given tree will be in the range [1, 100].
# 0 <= Node.val <= 1000


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def increasing_bst(root: TreeNode) -> TreeNode:
    # working_sol (6.52%, 20.61%) -> (44ms, 16.58mb)  time: O(n) | space: O(n)
    out: list[TreeNode] = []

    def inorder(node: TreeNode) -> None:
        if node.left:
            inorder(node.left)
        out.append(node)
        if node.right:
            inorder(node.right)

    inorder(root)
    for index in range(1, len(out)):
        out[index - 1].right = out[index]
        out[index - 1].left = None
    out[-1].right = None
    return out[0]


# Time complexity: O(n) <- n - number of Nodes inside the input BST `root`.
# Always traversing whole BST with inorder traverse to get increasing order => O(n).
# Traversing all the Nodes again to reshuffle connections => O(2n).
# ----------------------
# Auxiliary space: O(n)
# `out` will contain links to every Node of the input BST `root`
