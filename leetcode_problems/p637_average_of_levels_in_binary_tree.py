# Given the root of a binary tree, return the average value of the nodes
#   on each level in the form of an array.
# Answers within 10 ** -5 of the actual answer will be accepted.
# ---------------
# The number of nodes in the tree is in the range [1, 10 ** 4].
# -2 ** 31 <= Node.val <= 2 ** 31 - 1
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def average_of_levels(root: TreeNode) -> list[float]:
    # working_sol (61.98%, 94.15%) -> (52ms, 18.62mb)  time: O(n) | space: O(n)
    avg_values: list[float] = []
    # Standard BFS with delimiter.
    que: deque[TreeNode | None] = deque([root, None])
    # # of Nodes on level.
    nodes: int = 0
    # Summarized values of these Nodes.
    level: int = 0
    while que:
        cur_node: TreeNode = que.popleft()
        if not cur_node:
            if que:
                que.append(None)
            avg_values.append(level / nodes)
            nodes = 0
            level = 0
            continue
        nodes += 1
        level += cur_node.val
        if cur_node.left:
            que.append(cur_node.left)
        if cur_node.right:
            que.append(cur_node.right)
    return avg_values


# Time complexity: O(n) -> traversing whole BT once and calc avg on every delimiter == end of the level => O(n).
# n - Nodes in input BT^^|
# Auxiliary space: O(n + k) -> standard O(n) for que in BFS + extra array of average with size == 'k' => O(n + k).
# k - number of levels in input BT^^|
