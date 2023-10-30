# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
# (i.e., from left to right, then right to left for the next level and alternate between).
# --------------------
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
from collections import deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root: TreeNode) -> list[list[int]]:
    # working_sol (72.88%, 99.39%) -> (38ms, 16.3mb)  time: O(n + log n) | space: O(n)
    if not root:
        return []
    levels: list[list[int]] = []
    level: list[int] = []
    # Standard BFS with delimiter.
    que: deque[TreeNode | None] = deque([root, None])
    while que:
        cur_node: TreeNode = que.popleft()
        # End of level.
        if not cur_node:
            if que:
                que.append(None)
            levels.append(level)
            level = []
            continue
        level.append(cur_node.val)
        if cur_node.left:
            que.append(cur_node.left)
        if cur_node.right:
            que.append(cur_node.right)
    # Every ODD level => Reverse.
    for x in range(1, len(levels), 2):
        levels[x] = levels[x][::-1]
    return levels


# Time complexity: O(n + log n) -> standard BFS to get all Nodes by levels => O(n) ->
# n - Nodes of input BT^^|        -> reversing every ODD level, only part of original Nodes => O(n + log n).
# Auxiliary space: O(n) -> que with allocated space for every Node of input BT => O(n) ->
#                         -> extra list 'levels' with all Nodes of input BT => O(2n).
