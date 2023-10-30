# Given the root of a complete binary tree, return the number of the nodes in the tree.
# According to Wikipedia, every level, except possibly the last,
#   is completely filled in a complete binary tree,
#   and all nodes in the last level are as far left as possible.
# It can have between 1 and 2 ** h nodes inclusive at the last level h.
# Design an algorithm that runs in less than O(n) time complexity.
# ---------------------
# The number of nodes in the tree is in the range [0, 5 * 10 ** 4].
# 0 <= Node.val <= 5 * 10 ** 4
# The tree is guaranteed to be complete.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_nodes(root: TreeNode) -> int:
    # working_sol (97.95%, 96.43%) -> (78ms, 23.7mb)  time: O(log n) | space: O(n)
    count: int = 0
    if not root:
        return count
    # Standard level-order traverse.
    que: deque[TreeNode | None] = deque([root, None])
    while que:
        current: TreeNode = que.popleft()
        if not current:
            if que:
                que.append(None)
            continue
        count += 1
        # We're given complete BT == Node without any of the childs
        #  is the last Node we care about.
        if current.left:
            que.append(current.left)
        else:
            # Last level already in a que, and we won't be having extras.
            # So, we can just return (len(que) ! - 1 !) <- for delimiter.
            count += len(que) - 1
            return count
        if current.right:
            que.append(current.right)
        else:
            count += len(que) - 1
            return count
    return count


# Time complexity: O(log n) -> traversing whole input_BT except last level, once => O(log n).
# n - Nodes of input BT^^|
# Auxiliary_space: O(n) -> que with all Nodes allocated => O(n).
# ---------------------
# Actually I can make it little bit faster, cuz we have 1 delimiter at a time, so we can just
# take len(que) - 1 and use it instead of a looping.
# ---------------------
# For O(n) is basic order-level walk with counting.
# But for ! < O(n) ! we need to skip something, we can't skip node itself,
# but we can skip last level. Because COMPLETE is guaranteed then any time we encounter
# node without left/right child we can just count everything what's left in a que and
# be sure that's next level is last. Cuz last level is leading to nowhere, and it's already recorded(in a que).
