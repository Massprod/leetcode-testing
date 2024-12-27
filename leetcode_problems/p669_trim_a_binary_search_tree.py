# Given the root of a binary search tree and the lowest and highest boundaries
#  as low and high, trim the tree so that all its elements lies in [low, high].
# Trimming the tree should not change the relative structure of the elements
#  that will remain in the tree (i.e., any node's descendant should remain a descendant).
# It can be proven that there is a unique answer.
# Return the root of the trimmed binary search tree.
# Note that the root may change depending on the given bounds.
# -------------------------
# The number of nodes in the tree is in the range [1, 10 ** 4].
# 0 <= Node.val <= 10 ** 4
# The value of each node in the tree is unique.
# root is guaranteed to be a valid binary search tree.
# 0 <= low <= high <= 10 ** 4
from utils.binary_tree import TreeNode


def trim_bst(root: TreeNode, low: int, high: int) -> TreeNode | None:
    # working_sol: (100.00%, 8.72%) -> (0ms, 21.07mb)  time: O(n) | space: O(n)

    # Replace Nodes with their childs while we're not getting correct value.
    def check(node: TreeNode) -> None:
        nonlocal low, high

        while (node.left
                and not (low <= node.left.val <= high)):
            if node.left.val < low:
                node.left = node.left.right
            else:
                node.left = node.left.left
        
        if node.left:
            check(node.left)

        while (node.right
               and not (low <= node.right.val <= high)):
            if node.right.val < low:
                node.right = node.right.right
            else:
                node.right = node.right.left
        
        if node.right:
            check(node.right)


    while (root
           and not (low <= root.val <= high)):
        if root.val < low:
            root = root.right
        else:
            root = root.left
    if root:
        check(root)
    return root


# Time complexity: O(n) <- n - number of node in the input BST `root`.
# Always using every node of the input BST `root`, once => O(n).
# -------------------------
# Auxiliary space: O(n)
# In the worst case if we don't need to delete any Nodes and all of them
#  placed in style of linked list `check` stack will be of size `n` => O(n).
