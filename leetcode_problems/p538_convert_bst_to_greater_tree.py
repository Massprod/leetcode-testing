# Given the root of a Binary Search Tree (BST),
#  convert it to a Greater Tree such that every key of the original BST
#  is changed to the original key plus the sum of all keys greater than the original key in BST.
# As a reminder, a binary search tree is a tree that satisfies these constraints:
#  - The left subtree of a node contains only nodes with keys less than the node's key.
#  - The right subtree of a node contains only nodes with keys greater than the node's key.
#  - Both the left and right subtrees must also be binary search trees.
# -----------------------------
# The number of nodes in the tree is in the range [0, 10 ** 4].
# -10 ** 4 <= Node.val <= 10 ** 4
# All the values in the tree are unique.
# root is guaranteed to be a valid binary search tree.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bst_to_gst(root: TreeNode) -> TreeNode:
    # working_sol(51.86%, 94.79%) -> (60ms, 18.39mb)  time: O(n) | space: O(n)

    def reverse_in_order(node: TreeNode, path: int) -> int:
        # `path` <- sum of the all Nodes we visited so far.
        # Because we're traveling from right -> left (biggest -> smallest)
        #  we can record our `path` and use it.
        if not node:
            return path
        node.val += reverse_in_order(node.right, path)
        # If we don't have a left child, then we don't need
        #  to include a sum of its nodes in a `path`.
        if not node.left:
            return node.val
        # Otherwise, we need to record this `path` as well.
        # And everything we're going to visit later is lower than that.
        path = reverse_in_order(node.left, node.val)
        return path

    reverse_in_order(root, 0)
    return root


# Time complexity: O(n) <- n - number of Nodes inside the input BST `root`
# Always traversing whole BST `root`, once => O(n).
# -------------------------------
# Auxiliary space: O(n)
# In the worst case, we're going to have a BST which is build like a LinkedList.
# Then we're going to have a stack of recursion with depth == `n` => O(n)
# -------------------------------
# It was the one way to solve it, but I managed to do this in just one traverse.
# A little bit scrappy but working.
# -------------------------------
# Not building trees, we can just go In-order to get BST values in increasing order.
# Then count prefixes and get them from whole BST nodes sum for all of the indexes(Nodes).
