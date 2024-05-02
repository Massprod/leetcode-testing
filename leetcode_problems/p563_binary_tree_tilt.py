# Given the root of a binary tree, return the sum of every tree node's tilt.
# The tilt of a tree node is the absolute difference between the sum of all left subtree node values
#  and all right subtree node values.
# If a node does not have a left child, then the sum of the left subtree node values is treated as 0.
# The rule is similar if the node does not have a right child.
# ------------------------
# The number of nodes in the tree is in the range [0, 10 ** 4].
# -1000 <= Node.val <= 1000


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_tilt(root: TreeNode) -> int:
    # working_sol(71.23%, 13.80%) -> (46ms, 17.73mb)  time: O(n) | space: O(n)
    def dfs(node: TreeNode) -> tuple[int, int]:
        if not node:
            return 0, 0
        left_sub: int = 0
        right_sub: int = 0
        cur_left_tilts: int = 0
        cur_right_tilts: int = 0
        if node.left:
            cur_left_sub, cur_left_tilts = dfs(node.left)
            left_sub += cur_left_sub
        if node.right:
            cur_right_sub, cur_right_tilts = dfs(node.right)
            right_sub += cur_right_sub
        return node.val + left_sub + right_sub, abs(left_sub - right_sub) + cur_left_tilts + cur_right_tilts

    return dfs(root)[1]


# Time complexity: O(n) <- n - number of nodes inside the input tree `root`
# Always traversing and using every `node` of the tree, once => O(n).
# ------------------------
# Auxiliary space: O(n)
# In the worst case, we will have BT with style of LinkedList, so we're going to have stack with all Nodes => O(n).
