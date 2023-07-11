# Given a binary tree, determine if it is height-balanced.
# ------------------
# The number of nodes in the tree is in the range [0, 5000].
# -10 ** 4 <= Node.val <= 10 ** 4


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root: TreeNode) -> bool:
    # working_sol (80.15%, 79.59%) -> (62ms, 21mb)  time: O(n) | space: O(log n)
    if not root:
        return True

    def height(node: TreeNode) -> int:
        # set left/right current_node subtrees heights
        left_height: int = 0
        right_height: int = 0
        # find this heights
        if node.left:
            left_height = height(node.left)
        if node.right:
            right_height = height(node.right)
        # only case when left/right heights will be -1 is difference in heights > 1
        # which is unbalanced state
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        # if leaf -> return height of 0 + 1, and backtrack from this leaf to root
        # checking every node subtrees on the way
        return max(left_height, right_height) + 1

    if height(root) != -1:
        return True
    return False

# Time complexity: O(n) -> in_order traversal of whole input_BT, once => O(n).
# n - nodes in input_BT^^|
# Auxiliary space: O(log n) -> standard stack for search in input_BT => O(log n).
# ------------------
# A height-balanced binary tree is a binary tree in which the depth
#   of the two subtrees of every node never differs by more than one.
