# Given the root of a binary tree, determine if it is a complete binary tree.
# In a complete binary tree, every level, except possibly the last, is completely filled,
#  and all nodes in the last level are as far left as possible.
# It can have between 1 and 2h nodes inclusive at the last level h.
# --- --- --- ---
# The number of nodes in the tree is in the range [1, 100].
# 1 <= Node.val <= 1000
from utils.binary_tree import TreeNode, bt_from_level_order

from collections import deque


def is_complete_tree(root: TreeNode) -> bool:
    # working_solution: (100%, 89.31%) -> (0ms, 17.62mb)  Time: O(n) Space: O(n)
    que: deque[TreeNode | None] = deque([root])
    while que and que[0] is not None:
        node: TreeNode = que.popleft()  # type: ignore
        que.append(node.left)
        que.append(node.right)
    
    while que and que[0] is None:
        que.popleft()
    # If something is left => break and we're not allowed to have it.
    return 0 == len(que)


# Time complexity: O(n)
# n - number of nodes inside the input BT `root`
# In the worst case `root` is a complete BT.
# Traversing each node of the BT, once => O(n)
# --- --- --- ---
# Space complexity: O(n)
# `que` <- allocates space for each node.


test: list[int | None] = [1, 2, 3, 4, 5, 6]
test_tree: TreeNode = bt_from_level_order(test)  # type: ignore
test_out: bool = True
assert test_out == is_complete_tree(test_tree)

test = [1, 2, 3, 4, 5, None, 7]
test_tree = bt_from_level_order(test)            # type: ignore
test_out = False
assert test_out == is_complete_tree(test_tree)
