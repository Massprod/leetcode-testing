# Given the root of a binary tree, split the binary tree into two subtrees 
#  by removing one edge such that the product of the sums of the subtrees is maximized.
# Return the maximum product of the sums of the two subtrees.
# Since the answer may be too large, return it modulo 109 + 7.
# Note that you need to maximize the answer
#  before taking the mod and not after taking it.
# --- --- --- ---
# The number of nodes in the tree is in the range [2, 5 * 10 ** 4].
# 1 <= Node.val <= 10 ** 4
from utils.binary_tree import TreeNode


def max_product(root: TreeNode) -> int:
    # working_solution: (72.62%, 5.32%) -> (54ms, 5.32mb)  Time: O(n) Space: O(1)

    def inorder_sum(node: TreeNode | None) -> int:
        if not node:
            return 0
        left_sum: int = inorder_sum(node.left)
        right_sum: int = inorder_sum(node.right)
        node.val += left_sum + right_sum
        
        return node.val

    total_sum: int = inorder_sum(root)

    out: int = 0

    def dfs_highest(node: TreeNode | None, bt_sum: int) -> int:
        if not node:
            return 0
        highest_left: int = dfs_highest(node.left, bt_sum)
        highest_right: int = dfs_highest(node.right, bt_sum)
        # sum of other nodes * sum of this subtree
        cur_sum: int = (bt_sum - node.val) * node.val

        return max(highest_left, highest_right, cur_sum) 

    out = max(
        dfs_highest(root.left, total_sum),
        dfs_highest(root.right, total_sum)
    )

    return out % (10 ** 9 + 7)


# Time complexity: O(n)
# n - length of the input BT `root`
# ---
# Always traversing the input BT, twice => O(2 * n).
# --- --- --- ---
# Space complexity: O(1)
# Ignore stack size, with the func stack it's O(n).
