# Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent.
# If there are no nodes with an even-valued grandparent, return 0.
# A grandparent of a node is the parent of its parent if it exists.
# --------------------------------
# The number of nodes in the tree is in the range [1, 10 ** 4].
# 1 <= Node.val <= 100
from utils.binary_tree import TreeNode


def sum_even_grandparent(root: TreeNode) -> int:
    # working_sol (57.68%, 49.47%) -> (69ms, 19.38mb)  time: O(n) | space: O(n)
    out: int = 0

    def check(node: TreeNode, parent: int, grand_p: int) -> None:
        nonlocal out
        if not node:
            return
        if not grand_p:
            out += node.val
        parent, grand_p = node.val % 2, parent
        check(node.left, parent, grand_p)
        check(node.right, parent, grand_p)

    par = root.val % 2
    check(root.left, par, 1)
    check(root.right, par, 1)
    return out


# Time complexity: O(n) <- n - number of Nodes inside the input BT `root`.
# Always traversing every node of the input BT `root`, once => O(n).
# --------------------------------
# Auxiliary space; O(n)
# In the worst case == BT like a linked list with only 1 subtree, recursion stack will be of size `n` => O(n).
