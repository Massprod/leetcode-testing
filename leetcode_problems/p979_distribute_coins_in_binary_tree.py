# You are given the root of a binary tree with n nodes where each node in the tree has node.val coins.
# There are n coins in total throughout the whole tree.
# In one move, we may choose two adjacent nodes and move one coin from one node to another.
# A move may be from parent to child, or from child to parent.
# Return the minimum number of moves required to make every node have exactly one coin.
# ---------------------
# The number of nodes in the tree is n.
# 1 <= n <= 100
# 0 <= Node.val <= n
# The sum of all Node.val is n.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def distribute_coins(root: TreeNode) -> int:
    # working_sol (55.40%, 38.90%) -> (38ms, 16.57mb)  time: O(n) | space: O(n)
    out: int = 0

    def dfs(node: TreeNode) -> int:
        nonlocal out
        if not node:
            return 0
        left: int = dfs(node.left)
        right: int = dfs(node.right)
        # Essentially, all we care is how much there are coins need to fill all children,
        #  either we have extras which will be returned to it's parent or there are some coins needed.
        # In both cases, every coin transfer is 1 move.
        out += abs(left) + abs(right)
        # And in both cases, we're always leaving 1 coin at the current Node.
        # Or we will need 1 coin to fill this child (goes negative).
        return node.val + left + right - 1

    dfs(root)
    return out


# Time complexity: O(n) <- n - number of Nodes inside input BT `root`.
# Always traversing whole BT once, using every node once => O(n).
# ---------------------
# Auxiliary space: O(n)
# BT in style of linkedList, so we will have all Nodes in the recursion stack => O(n).
