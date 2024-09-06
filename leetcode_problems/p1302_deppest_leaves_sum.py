# Given the root of a binary tree, return the sum of values of its deepest leaves.
# -------------------
# The number of nodes in the tree is in the range [1, 10 ** 4].
# 1 <= Node.val <= 100
from collections import deque
from utils.binary_tree import bt_from_level_order, TreeNode


def deepest_leaves_sum(root: TreeNode) -> int:
    # working_sol (99.32%, 29.87%) -> (93ms, 19.50mb)  time: O(n) | space: O(n)
    que: deque[TreeNode | None] = deque([root, None])
    cur_level: list[int] = []
    while que:
        cur_node: TreeNode | None = que.popleft()
        if cur_node is None:
            if que:
                que.append(None)
                cur_level = []
            continue
        cur_level.append(cur_node.val)
        if cur_node.left:
            que.append(cur_node.left)
        if cur_node.right:
            que.append(cur_node.right)
    return sum(cur_level)


# Time complexity: O(n) <- n - number of Nodes in the input BT `root`.
# We're using BFS to traverse BT, once => O(n).
# -------------------
# Auxiliary space: O(n)
# Standard BFS `que` in the worst case allocates space for all the Nodes we visit => O(n).


test: TreeNode = bt_from_level_order([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])
test_out: int = 15
assert test_out == deepest_leaves_sum(test)

test = bt_from_level_order([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5])
test_out: int = 19
assert test_out == deepest_leaves_sum(test)
