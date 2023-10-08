# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
# ---------------------
# The number of nodes in the tree will be in the range [0, 10 ** 4].
# -2 ** 31 <= Node.val <= 2 ** 31 - 1
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def largest_values(root: TreeNode) -> list[int]:
    # working_sol (69.59%, 96.2%) -> (49ms, 18.5mb)  time: O(n) | space: O(n)
    out: list[int] = []
    if not root:
        return out
    # Standard BFS with delimiter.
    que: deque[TreeNode | None] = deque([root, None])
    # ! -2 ** 31 <= Node.val <= 2 ** 31 - 1 !
    min_val: int = -2 ** 31
    cur_max: int = min_val
    while que:
        cur_node: TreeNode = que.popleft()
        if not cur_node:
            out.append(cur_max)
            cur_max = min_val
            if que:
                que.append(None)
            continue
        if cur_node.left:
            que.append(cur_node.left)
        if cur_node.right:
            que.append(cur_node.right)
        cur_max = max(cur_max, cur_node.val)
    return out


# Time complexity: O(n) -> always traversing all nodes of input BT, once => O(n).
# n - number of nodes in BT^^|
# Auxiliary space: O(n) -> worst case == every level holds only 1 node -> we will store every node in 'out' => O(n).
# ---------------------
# Standard BFS with delimiter should be enough.
