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
    # working_sol (64.49%, 45.56%) -> (305ms, 21mb)  time: O(n) | space: O(n)
    all_levels: dict[int, int] = {}

    def search_tree(node: TreeNode, level: int = 1) -> None:
        if level in all_levels:
            all_levels[level] += node.val
        else:
            all_levels[level] = node.val
        if node.left:
            search_tree(node.left, level + 1)
        if node.right:
            search_tree(node.right, level + 1)

    search_tree(root)
    max_lvl: int = 0
    for key in all_levels:
        if max_lvl == 0:
            max_lvl = key
        elif all_levels[max_lvl] < all_levels[key]:
            max_lvl = key
    return max_lvl


# Time complexity: O(n) -> traversing whole binary tree to store every node values by it level => O(n) ->
# n - node of input_BT^^|  -> checking every key in created dictionary to find maximum sum => O(n) ->
#                          -> O(2n) -> O(n).
# Auxiliary space: O(m) -> for every depth level in BT we're creating new key in dictionary to store sum => O(n).
# m - number of levels^^|
# ---------------------
# Same as p530, but record every level not just all nodes.
# And I'm still not going to create function to made BT.
# Just daily streak, I will build it after returning to BT practice at 94+ problems.
