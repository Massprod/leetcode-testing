# Given the root of a Binary Search Tree (BST),
#  return the minimum difference between the values of any two different nodes in the tree.
# -----------------------
# The number of nodes in the tree is in the range [2, 100].
# 0 <= Node.val <= 10 ** 5


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_diff_in_bst(root: TreeNode) -> int:
    # working_sol (84.78%, 68.43%) -> (31ms, 16.50mb)  time: O(n) | space: O(n)
    inorder_traverse: list[int] = []

    def inorder(node: TreeNode) -> None:
        if node.left:
            inorder(node.left)
        inorder_traverse.append(node.val)
        if node.right:
            inorder(node.right)

    inorder(root)
    out: int = 10 ** 9
    for index in range(1, len(inorder_traverse)):
        out = min(out, inorder_traverse[index] - inorder_traverse[index - 1])
    return out


# Time complexity: O(n) <- n - number of Nodes inside the input BST `root`.
# Always traversing whole input BST `root`, once => O(n).
# Extra traversing all the node values stored in `inorder_traverse` to get minimum diff => O(2n).
# -----------------------
# Auxiliary space: O(n)
# Every node value is always stored in `inorder_traverse` => O(n)
