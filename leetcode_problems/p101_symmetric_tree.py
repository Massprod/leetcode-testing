# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# ---------------
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: TreeNode) -> bool:
    # working_sol (97%, 84.3%) -> (31ms, 16.3mb)  time: O(n) | space: O(k)

    def check(sub1: TreeNode, sub2: TreeNode) -> bool:
        if sub1 and not sub2:
            return False
        if not sub1 and sub2:
            return False
        if sub1 and sub2:
            if sub1.val != sub2.val:
                return False
            # Mirrored:
            # sub1_left_child == sub2_right_child
            if not check(sub1.left, sub2.right):
                return False
            # sub_1_right_child == sub2_left.child
            if not check(sub1.right, sub2.left):
                return False
        return True

    return check(root.left, root.right)


# Time complexity: O(n) -> worst case == correct symmetric tree -> traversing whole input BT => O(n).
# n - Nodes of input BT^^|
# Auxiliary space: O(k) -> worst_case == BT like: /\  -> recursion call for every level == stack of 'k' => O(k).
# k - levels of input BT^^|                      /  \
#                        ^^Might be even constant, if we ignore recursion stack as before.
