# You are given the root of a complete binary tree.
# A node x is called dominant if its value is equal to the maximum value
#   among all nodes in the subtree rooted at x.
# Return the number of dominant nodes in the tree.
# --- --- --- ---
# The number of nodes in the tree is in the range [1, 10 ** 5].
# 1 <= Node.val <= 10 ** 9
# The tree is guaranteed to be a complete binary tree.
from utils.binary_tree import TreeNode


def count_dominant_nodes(root: TreeNode | None) -> int:
    # working_solution: (61.58%, 70.23%) -> (300ms, 49.44mb)  Time: O(n) Space: O(1)
    def dfs(node: TreeNode | None) -> tuple[int, int]:
        if not node:
            # (max_val, num_doms)
            return (0, 0)
        
        cur: int = node.val
        left: tuple[int, int] = dfs(node.left)
        right: tuple[int, int] = dfs(node.right)
        max_sub: int = max(left[0], right[0])
        doms: int = left[1] + right[1]
        if cur >= max_sub:
            doms += 1
        
        return (max(cur, max_sub), doms)

    return dfs(root)[1]


# Time complexity: O(n)
# n - number of nodes in the input BT `root`
# --- --- --- ---
# Space complexity: O(1)
