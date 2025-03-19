# Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.
# Recall that:
#  - The node of a binary tree is a leaf if and only if it has no children
#  - The depth of the root of the tree is 0. if the depth of a node is d,
#    the depth of each of its children is d + 1.
#  - The lowest common ancestor of a set S of nodes,
#    is the node A with the largest depth such that every node in S
#    is in the subtree with root A.
# ----------------------------
# The number of nodes in the tree will be in the range [1, 1000].
# 0 <= Node.val <= 1000
# The values of the nodes in the tree are unique.
from utils.binary_tree import TreeNode


def lca_deepest_leaves(root: TreeNode) -> TreeNode:
    # working_sol (100.00%, 71.16%) -> (0ms, 18.14mb)  time: O(n) | space: O(1)
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
