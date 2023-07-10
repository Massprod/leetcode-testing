# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical,
#   and the nodes have the same value.
# --------------
# The number of nodes in both trees is in the range [0, 100].
# -10 ** 4 <= Node.val <= 10 ** 4


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    # working_sol (58.52%, 17.21%) -> (47ms, 16.4mb)  time: O(n + k) | space: O(n + k)
    if p is None and q is None:
        return True
    if p is None and q:
        return False
    if q is None and p:
        return False
    # left BT
    left: list[int | None] = []
    # right BT
    right: list[int | None] = []

    def inorder(node: TreeNode, left_t: bool, right_t: bool) -> None:
        # saving BT node_values in left
        if left_t:
            if node.left:
                inorder(node.left, left_t, right_t)
            else:
                left.append(None)
            if node.right:
                inorder(node.right, left_t, right_t)
            else:
                left.append(None)
            left.append(node.val)
        # saving BT node_values in right
        if right_t:
            if node.left:
                inorder(node.left, left_t, right_t)
            else:
                right.append(None)
            if node.right:
                inorder(node.right, left_t, right_t)
            else:
                right.append(None)
            right.append(node.val)

    inorder(p, True, False)
    inorder(q, False, True)
    if left == right:
        return True
    return False


# Time complexity: O(n + k) -> in order traversal of both input_BTs: n and k, once => O(n + k) ->
# n - nodes of p ^^| -> comparing all node_values from both input_BTs, stored in left, right
# k - nodes ok k ^^|    with summarized length of (n + k) => O(n + k) -> O(n + k) + O(n + k) => O(n + k).
# Auxiliary space: O(n + k) -> 2 extra lists to store all node_values from both input_BTs => O(n + k).
# --------------
# Same approach as mirror, just don't make right_part mirrored.
