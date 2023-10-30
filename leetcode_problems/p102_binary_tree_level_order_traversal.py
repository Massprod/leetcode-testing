# Given the root of a binary tree,
#   return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
# ----------------
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
from collections import deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: TreeNode) -> list[list[int]]:
    # working_sol (79.66%, 92.86%) -> (41ms, 16.90mb)  time: O(n) | space: O(n)
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
    return levels


# Time complexity: O(n) -> standard BFS traverse of whole input BT => O(n).
# n - Node of input BT^^|
# Auxiliary space: O(n) -> que with allocated space for every Node of input BT => O(n) ->
#                       -> extra list with all Nodes of input BT => O(2n).
