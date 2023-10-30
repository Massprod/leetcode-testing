# Given the root of a binary tree, imagine yourself standing on the right side of it,
#   return the values of the nodes you can see ordered from top to bottom.
# ---------------------
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: TreeNode) -> list[int] | None:
    # working_sol (64.85%, 97.1%) -> (39ms, 16.1mb)  time: O(n) | space: O(n)
    if not root:
        return None
    right_side: list[int] = []
    # Standard BFS.
    que: deque[TreeNode | None] = deque([root, None])
    while que:
        cur_node: TreeNode = que.popleft()
        if not cur_node:
            if que:
                que.append(None)
            continue
        # Last Node on level == pre-delimiter Node.
        if not que[0]:
            right_side.append(cur_node.val)
        if cur_node.left:
            que.append(cur_node.left)
        if cur_node.right:
            que.append(cur_node.right)

    return right_side


# Time complexity: O(n) -> standard order-level traversal, every node will be used once => O(n).
# n - nodes in input_BT^^|
# Auxiliary space: O(n) -> order-level traversal with a que, only one level will be stored at max,
#                          in the worst case there's only one level, so we're storing all nodes => O(n) ->
#                          -> creating extra array holding only right_side node in our worst case,
#                          every node can be placed on the right side, so we're storing all nodes => O(n).
# ---------------------
# Same approach as p116, but now we're just reading only last node of every level.
# Because every other node in BT will be blocked from a view by these nodes.
