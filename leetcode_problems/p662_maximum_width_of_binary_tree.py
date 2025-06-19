# Given the root of a binary tree, return the maximum width of the given tree.
# The maximum width of a tree is the maximum width among all levels.
# The width of one level is defined as the length between the end-nodes
#  (the leftmost and rightmost non-null nodes), where the null nodes
#  between the end-nodes that would be present in a complete binary tree
#  extending down to that level are also counted into the length calculation.
# It is guaranteed that the answer will in the range of a 32-bit signed integer.
# -----------------------
# The number of nodes in the tree is in the range [1, 3000].
# -100 <= Node.val <= 100
from collections import deque

from utils.binary_tree import TreeNode, bt_from_level_order 


def width_of_binary_tree(root: TreeNode) -> int:
    # working_sol (72.32%, 93.33%,) -> (3ms, 18.56mb)  time: O(n) | space: O(n)
    # (Node, index on the level)
    que: deque[tuple[TreeNode, int]] = deque([(root, 0)])
    max_width: int = 1
    while que:
        _, leftmost = que[0]
        _, rightmost = que[-1]
        max_width = max(
            max_width, rightmost - leftmost + 1
        )
        new_level: deque[tuple[TreeNode, int]] = deque([])
        # Every next level node shifts it's index value by `x2`.
        # And right-one is obviously extra + 1.
        for node, index in que:
            if node.left:
                new_level.append(
                    (node.left, index * 2)
                )
            if node.right:
                new_level.append(
                    (node.right, index * 2 + 1)
                )
        que = new_level

    return max_width


# Time complexity: O(n) <- n - number of nodes in the input BT `root`.
# Always traversing every node of the input BT => O(n).
# -----------------------
# Auxiliary space: O(n)
# `que` | `new_level` <- allocates space for each node of the input BT => O(n).


test: TreeNode = bt_from_level_order(
    [1, 3, 2, 5, 3, None, 9]
)
test_out: int = 4
assert test_out == width_of_binary_tree(test)

test = bt_from_level_order(
    [1, 3, 2, 5, None, None, 9, 6, None, 7]
)
test_out = 7
assert test_out == width_of_binary_tree(test)

test = bt_from_level_order(
    [1,3, 2, 5]
)
test_out = 2
assert test_out == width_of_binary_tree(test)
