# Given the root of a binary tree, return the average value of the nodes
#   on each level in the form of an array.
# Answers within 10 ** -5 of the actual answer will be accepted.
# ---------------
# The number of nodes in the tree is in the range [1, 10 ** 4].
# -2 ** 31 <= Node.val <= 2 ** 31 - 1
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def average_of_levels(root: TreeNode) -> list[float]:
    # working_sol (94.16%, 73.1%) -> (56ms, 18.9mb)  time: O(n) | space: O(n)
    avg_values: list[float] = []
    que: deque[TreeNode | None] = deque()
    que.append(root)
    que.append(None)
    while any(que):
        level: int = 0
        nodes: int = 0
        while que[0]:
            current: TreeNode = que.popleft()
            level += current.val
            nodes += 1
            if current.left:
                que.append(current.left)
            if current.right:
                que.append(current.right)
        que.append(None)
        level_avg: float = level / nodes
        avg_values.append(level_avg)
        que.popleft()
    return avg_values


# Time complexity: O(n) -> traversing whole BT once and calculate average level on each level break(hit None) => O(n).
# n - nodes in input_BT^^|
# Auxiliary space: O(n) -> actually in the worst case it should be O(n), because we're storing all_levels in
#                          avg_values <- like 2 levels with just 2 nodes ROOT + ROOT.LEFT, so we're storing
#                          level == nodes => O(n).
#                          On median standard O(log n) only levels will be stored and levels from 2 have len > 1.
# ---------------
# Actually it's bad practice, let's rebuild it normally. Having <50% performance bad as well.
# Now we're talking, 94+% and O(n) extra space, instead of a stack with all nodes + them stored in levels_dict => O(2n).
# ---------------
# Not using, deque cuz it's harder to read. But recursion taking more space and slower avg_calc.
# W.e Easy task and don't want to bother.
