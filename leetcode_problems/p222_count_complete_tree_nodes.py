# Given the root of a complete binary tree, return the number of the nodes in the tree.
# According to Wikipedia, every level, except possibly the last,
#   is completely filled in a complete binary tree,
#   and all nodes in the last level are as far left as possible.
# It can have between 1 and 2h nodes inclusive at the last level h.
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
    # working_sol (97.95%, 96.43%) -> (78ms, 23.7mb)  time: O(log n) | space: O(log n)
    count: int = 0
    if not root:
        return count
    # standard order-level que
    que: deque[TreeNode | None] = deque()
    que.append(root)
    que.append(None)
    while any(que):
        while que[0]:
            current: TreeNode = que.popleft()
            count += 1
            # if we have given complete BT then
            # any node without any of the child is last node ->
            # -> we can't record next level from it,
            #    cuz all nodes are stuffed on the left side
            if current.left:
                que.append(current.left)
            else:
                count += len(que) - 1
                return count
            # any of the child^^
            if current.right:
                que.append(current.right)
            else:
                count += len(que) - 1
                return count
        # add/delete delimiter
        que.append(None)
        que.popleft()
    return count


# Time complexity: O(log n) -> traversing whole input_BT except last_level, once => O(log n).
# n - nodes in input_BT^^|
# Auxiliary_space: O(log n) -> there's case with 1 level only as root, and we're storing O(n) ->
#                           -> normally we're just storing only part of the input_BT ->
#                           -> nodes at current_level and part of the next level => O(log n).
# ---------------------
# Actually I can make it little bit faster, cuz we have 1 delimiter at a time, so we can just
# take len(que) - 1 and use it instead of a looping.
# ---------------------
# For O(n) is basic order-level walk with counting.
# But for <O(n) we need to skip something, we can't skip node itself,
# but we can skip last level. Because COMPLETE is guaranteed then any time we encounter
# node without left/right child we can just count everything what's left in a que and
# be sure that's next level is last. Cuz last level is leading to nowhere, and it's already recorded(in a que).
