# You are given the root of a binary tree that consists of exactly 3 nodes:
#  the root, its left child, and its right child.
# Return true if the value of the root is equal to the sum of the values of its two children,
#  or false otherwise.
# ---------------------
# The tree consists only of the root, its left child, and its right child.
# -100 <= Node.val <= 100
from utils.binary_tree import bt_from_level_order, TreeNode


def check_tree(root: TreeNode) -> bool:
    # working_sol (87.89%, 46.11%) -> (30ms, 16.46mb)  time: O(1) | space: O(1)
    return (root.left.val + root.right.val) == root.val


# Time complexity: O(1)
# ---------------------
# Auxiliary space: O(1)


test: TreeNode = bt_from_level_order([10, 4, 6])
test_out: bool = True
assert test_out == check_tree(test)

test = bt_from_level_order([5, 3, 1])
test_out = False
assert test_out == check_tree(test)
