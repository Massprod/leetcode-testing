# Given the root of a binary tree and two integers val and depth,
#  add a row of nodes with value val at the given depth depth.
# Note that the root node is at depth 1.
# The adding rule is:
#  - Given the integer depth, for each not null tree node cur at the depth depth - 1,
#     create two tree nodes with value val as cur's left subtree root and right subtree root.
#  - cur's original left subtree should be the left subtree of the new left subtree root.
#  - cur's original right subtree should be the right subtree of the new right subtree root.
#  - If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with
#     value val as the new root of the whole original tree, and the original tree is the new root's left subtree.
# --------------------------
# The number of nodes in the tree is in the range [1, 10 ** 4].
# The depth of the tree is in the range [1, 10 ** 4].
# -100 <= Node.val <= 100
# -10 ** 5 <= val <= 10 ** 5
# 1 <= depth <= the depth of tree + 1
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def add_one_row(root: TreeNode, val: int, depth: int) -> TreeNode:
    # working_sol (90.00%, 97.00%) -> (40ms, 17.70mb)  time: O(n) | space: O(n + k)
    new_root: TreeNode
    if 1 == depth:
        new_root = TreeNode(val, left=root)
        return new_root
    # Standard BFS with delimiter.
    que: deque[TreeNode | None] = deque([root, None])
    cur_lvl: int = 1
    limit: int = depth - 1
    while que:
        cur_node: TreeNode | None = que.popleft()
        if not cur_node:
            cur_lvl += 1
            if que:
                que.append(None)
            continue
        # Level we need == `limit`.
        # Record it to the `que` and process.
        if cur_lvl != limit:
            if cur_node.left:
                que.append(cur_node.left)
            if cur_node.right:
                que.append(cur_node.right)
            continue
        # ! `cur's` original left subtree should be the left subtree of the new left subtree root. !
        new_node_left: TreeNode = TreeNode(val, left=cur_node.left)
        # ! cur's original right subtree should be the right subtree of the new right subtree root. !
        new_node_right: TreeNode = TreeNode(val, right=cur_node.right)
        cur_node.left = new_node_left
        cur_node.right = new_node_right
    return root


# Time complexity: O(n) <- n - number of Nodes inside input BT `root`.
# Standard BFS with in the worst case: check every Node and add another level at the end => O(n).
# --------------------------
# Auxiliary space: O(n + k) <- k - number of Nodes on (depth - 1) level.
# We will allocate `n` space for `que` and extra we will create a new TreeNodes for every Node
#  on (depth - 1) level => O(n + 2 * k).
# --------------------------
# Not testing, it's simple BFS with delimiter, and doing at work.
