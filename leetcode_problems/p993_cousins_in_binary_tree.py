# Given the root of a binary tree with unique values
#  and the values of two different nodes of the tree x and y,
#  return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.
# Two nodes of a binary tree are cousins if they have the same depth with different parents.
# Note that in a binary tree, the root node is at the depth 0,
#  and children of each depth k node are at the depth k + 1.
# --------------------
# The number of nodes in the tree is in the range [2, 100].
# 1 <= Node.val <= 100
# Each node has a unique value.
# x != y
# x and y are exist in the tree.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_cousins(root: TreeNode, x: int, y: int) -> bool:
    # working_sol (90.07%, 40.03%) -> (30ms, 16.53mb)  time: O(n) | space: O(n)
    # [parent, level]
    x_level: list[int] = [-1, -1]
    y_level: list[int] = [-1, -1]
    if x == root.val:
        x_level[0], x_level[1] = -1, 0
    elif y == root.val:
        y_level[0], y_level[1] = -1, 0
    # Standard BFS.
    que: deque[TreeNode | None] = deque([root, None])
    level: int = 0
    while que:
        if -1 < x_level[1] and -1 < y_level[1]:
            break
        cur_node: TreeNode = que.popleft()
        if not cur_node:
            level += 1
            if que:
                que.append(None)
            continue
        if cur_node.left:
            if x == cur_node.left.val:
                x_level[0], x_level[1] = cur_node.val, level + 1
            elif y == cur_node.left.val:
                y_level[0], y_level[1] = cur_node.val, level + 1
            que.append(cur_node.left)
        if cur_node.right:
            if y == cur_node.right.val:
                y_level[0], y_level[1] = cur_node.val, level + 1
            elif x == cur_node.right.val:
                x_level[0], x_level[1] = cur_node.val, level + 1
            que.append(cur_node.right)
    return x_level[0] != y_level[0] and x_level[1] == y_level[1]


# Time complexity: O(n) <- n - number of Nodes inside the input BT `root`.
# In the worst case, we're going to have first leaf and last leaf as our `x` and `y`.
# In this case, we're going to traverse whole BT `root`, once => O(n).
# --------------------
# Auxiliary space: O(n)
# `que` will allocate space for every Node, in `root` => O(n).
