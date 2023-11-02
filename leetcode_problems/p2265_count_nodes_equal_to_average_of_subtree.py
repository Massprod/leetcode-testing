# Given the root of a binary tree, return the number of nodes where
#  the value of the node is equal to the average of the values in its subtree.
# Note:
#  The average of n elements is the sum of the n elements divided by n
#   and rounded down to the nearest integer.
#  A subtree of root is a tree consisting of root and all of its descendants.
# ---------------------
# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 1000


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def average_of_sub(root: TreeNode) -> int:
    # working_sol (84.9%, 96.93%) -> (44ms, 17.38mb)  time: O(n) | space: O(n)
    # Backtrack from Leaf -> currentNode.

    def check(node: TreeNode) -> list[int]:
        # (sum of subtree, Nodes in this subtree, correct pairs avg == Node.val)
        out: list[int] = [node.val, 1, 0]
        if node.left:
            temp: list[int] = check(node.left)
            for x in range(len(temp)):
                out[x] += temp[x]
        if node.right:
            temp = check(node.right)
            for x in range(len(temp)):
                out[x] += temp[x]
        # ! rounded down to the nearest integer ! => floor division.
        sub_avg: int = out[0] // out[1]
        if sub_avg == node.val:
            out[2] += 1
        return out

    return check(root)[2]


# Time complexity: O(n) -> essentially we're just traversing every Node of input BT once => O(n) ->
# n - Nodes of input BT^^| -> BUT we're using loop for 3 elements of 'out' should we consider it? ->
#                         -> like it's never changing, and we can call it O(3 * n)?, which is still linear.
# Auxiliary space: O(n) -> same, everything is constant size except number of recursion calls, which depends on 'n' ->
#                         -> so it should be correct to just say O(n).
# ---------------------
# Backtrack from leafs to every Node with calc of left and right subtrees + Node itself?
# Should be correct.
