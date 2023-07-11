# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
# (i.e., from left to right, then right to left for the next level and alternate between).
# --------------------
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root: TreeNode) -> list[list[int]]:
    # working_sol (92.43%, 31.2%) -> (41ms, 16.6mb)  time: O(n + k) | space: O(n)
    if not root:
        return []
    levels: dict[int] = {}

    def levels_inorder(node: TreeNode, level: int = 0) -> None:
        """"
        in order traversal of BT, to store every BT node values sorted by its level
        """
        level += 1
        if level not in levels:
            levels[level] = []
        if node.left:
            levels_inorder(node.left, level)
        if node.right:
            levels_inorder(node.right, level)
        levels[level].append(node.val)

    levels_inorder(root)
    max_level: int = max(levels.keys())
    level_order: list[list[int]] = []
    for _ in range(1, max_level + 1):
        if _ % 2 == 0:
            level_order.append(levels[_][::-1])
        else:
            level_order.append(levels[_])
    return level_order


# Time complexity: O(n + k) -> in_order traverse of whole input_BT to get node_values and levels => O(n) ->
# n - num of nodes in input_BT^^ | -> after that getting value of the most deep level(max_level) => O(k) ->
# k - num of levels in input_BT^^| -> for every level visited appending this level_values into level_order,
#                                     number of lists will be equal to number of levels => O(k) ->
#                                  -> O(n) + O(k) + O(k) => O(n + k).
# Auxiliary space: O(n) -> using dictionary to store all values from input_BT nodes => O(n) ->
#                          -> extra creating of a list with this values => O(n) -> O(n) + O(n) => O(n).
# ------------------
# Copy of the p102 and p107, with zigzag order.
