# Given the root of a binary tree, the depth of each node
#  is the shortest distance to the root.
# Return the smallest subtree such that it contains all the deepest nodes
#  in the original tree.
# A node is called the deepest if it has the largest depth possible
#  among any node in the entire tree.
# The subtree of a node is a tree consisting of that node,
#  plus the set of all descendants of that node.
# ---------------------
# The number of nodes in the tree will be in the range [1, 500].
# 0 <= Node.val <= 500
# The values of the nodes in the tree are unique.
from utils.binary_tree import TreeNode


def subtree_with_all_deepest(root: TreeNode) -> TreeNode:
    # working_sol (100.00%, 60.09%) -> (0ms, 17.90mb)  time: O(n) | space: O(1)
    if not root:
        return root

    # Currently deepest level we have met.
    deepest_level: int = 0
    smallest_sub: TreeNode = root

    def dfs(node: TreeNode, level: int) -> int:
        nonlocal deepest_level, smallest_sub
        # Child `Node` are always deepest options,
        #  we just need to filter them out.
        # And we can have subtree of the 1 Node.
        if not node.left and not node.right:
            if deepest_level < level:
                deepest_level = level
                smallest_sub = node
            return level
        # ! 0 <= Node.val <= 500 ! <- we can't have negative `node.val`
        # So, we can ignore such subs.
        # Check both subtrees to find deepest levels. 
        deepest_left: int = -1
        if node.left:
            deepest_left = dfs(node.left, level + 1)
        deepest_right: int = -1
        if node.right:
            deepest_right = dfs(node.right, level + 1)
        # We only care about subtrees which have 2 `all` deepest Nodes in them.
        if deepest_left == deepest_right == deepest_level:
            smallest_sub = node
        
        # Returns deepest level we reached in both traversals.
        return max(level, deepest_left, deepest_right)

    dfs(root, 0)
    return smallest_sub


# Time complexity: O(n) <- n - number of nodes in the input BT `root`.
# We're always traversing whole input BT `root`, once => O(n).
# ---------------------
# Auxiliary space: O(1)
# We ignore recursion stack and everything else is 2 constant VARs => O(1).
