# A binary tree is named Even-Odd if it meets the following conditions:
#   - The root of the binary tree is at level index 0, its children are at level index 1,
#     their children are at level index 2, etc.
#   - For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order
#     (from left to right).
#   - For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order
#     (from left to right).
# Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.
# ------------------------
# The number of nodes in the tree is in the range [1, 10 ** 5].
# 1 <= Node.val <= 10 ** 6
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_even_odd_tree(root: TreeNode) -> bool:
    # working_sol (98.77%, 90.74%) -> (194ms, 37.59mb)  time: O(n) | space: O(n)
    # Lazy == not rebuilding now.
    # Because we're using `prev_val` we're skipping 0-level. Extra check for it.
    if not root.val % 2:
        return False
    prev_val: int = root.val
    # Standard BFS with delimiter.
    que: deque[TreeNode | None] = deque([root, None])
    cur_level: int = 0
    while que:
        cur_node: TreeNode | None = que.popleft()
        if cur_node is None:
            cur_level += 1
            if que:
                cur_node = que.popleft()
                # First value of the level.
                prev_val = cur_node.val
                # Should be ODD for EVEN level.
                if cur_level % 2 and prev_val % 2:
                    return False
                # Should be EVEN for ODD level.
                if not cur_level % 2 and not prev_val % 2:
                    return False
                que.append(None)
                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)
                continue
            break
        odd: int = cur_level % 2
        if cur_level and odd:
            # EVEN value for ODD level and lower than previously visited Node value.
            if not cur_node.val % 2 and cur_node.val < prev_val:
                prev_val = cur_node.val
            else:
                return False
        elif cur_level and not odd:
            # ODD value for EVEN level and higher than previously visited Node value.
            if cur_node.val % 2 and cur_node.val > prev_val:
                prev_val = cur_node.val
            else:
                return False
        if cur_node.left:
            que.append(cur_node.left)
        if cur_node.right:
            que.append(cur_node.right)
    return True


# Time complexity: O(n) <- n - number of Nodes in input BT.
# Standard BFS traversing of the whole BT.
# ------------------------
# Auxiliary space: O(n)
# Allocating space for every Node of BT in a `que`.
