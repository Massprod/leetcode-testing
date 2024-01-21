# Given the root of a binary tree, return the sum of all left leaves.
# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
# -------------------
# The number of nodes in the tree is in the range [1, 1000].
# -1000 <= Node.val <= 1000


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_of_left_leaves(root: TreeNode) -> int:
    # working_sol (69.52%, 95.54%) -> (37ms, 16.6mb)  time: O(n) | space: O(n)

    def dfs(node: TreeNode, left: bool = False) -> int:
        out: int = 0
        if not node.left and not node.right and left:
            out = node.val
            return out
        if node.left:
            out += dfs(node.left, True)
        if node.right:
            out += dfs(node.right, False)
        return out

    return dfs(root)


# Time complexity: O(n) <- n - number of Nodes in input BT `root`.
# We're always traversing whole BT `root`, because we can have left_child as leaf in w.e place => O(n).
# -------------------
# Auxiliary space: O(n).
# Worst case: our BT is build like LinkedList, so our recursion stack will be of size `n` => O(n).
