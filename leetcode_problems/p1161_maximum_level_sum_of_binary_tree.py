# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
# ---------------------
# The number of nodes in the tree is in the range [1, 10 ** 4].
# -10 ** 5 <= Node.val <= 10 ** 5


class TreeNode:

    def __init__(self, val: int = 0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode = left
        self.right: TreeNode = right


def max_level_sum(root: TreeNode) -> int:
    pass


# Same as p530, but record every level not just all nodes.
# And I'm still not going to create function to made BT.
# Just daily streak, I will build it after returning to BT practice at 94+ problems.
