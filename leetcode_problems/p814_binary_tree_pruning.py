# Given the root of a binary tree, return the same tree where every subtree
#  (of the given tree) not containing a 1 has been removed.
# A subtree of a node node is node plus every node that is a descendant of node.
# ---------------------------
# The number of nodes in the tree is in the range [1, 200].
# Node.val is either 0 or 1.
from utils.binary_tree import TreeNode


def prune_tree(root: TreeNode) -> TreeNode | None:
    # working_sol (100.00%, 37.89%) -> (0ms, 17.89mb)  time: O(n) | space: O(1)

    def dfs(node: TreeNode) -> bool:
        one_present: bool = 1 == node.val
        if node.left:
            left_one_present: bool = dfs(node.left)
            if not left_one_present:
                node.left = None
            one_present = one_present or left_one_present
        if node.right:
            right_one_present: bool = dfs(node.right)
            if not right_one_present:
                node.right = None
            one_present = one_present or right_one_present
        
        return one_present

    root_exist: bool = dfs(root)
    if not root_exist:
        return None
    return root


# Time complexity: O(n) <- n - number of Nodex in the input BT `root`.
# Always traversing whole input BT `root`, once => O(n).
# ---------------------------
# Auxiliary space: O(1)
# If we ignore stack of recursion, everything is constant.
