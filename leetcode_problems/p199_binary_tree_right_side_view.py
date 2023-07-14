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
    # working_sol (71.99%, 97.23%) -> (46ms, 16.2mb)  time: O(n) | space: O(n)
    if not root:
        return None
    # didn't succeed in forcing root into a while_loops
    # cuz we're breaking on delimiter == None
    # and if root is placed in it, we will ignore it -> while que[1]
    # so it's either place it from the start
    # or do this inside of a first loop.
    # But then I need to force extra check, cuz it's 1 time action.
    right_side: list[int] = [root.val]
    que: deque = deque()
    # better to just add first level before looping
    if root.left:
        que.append(root.left)
    if root.right:
        que.append(root.right)
    # add delimiter
    que.append(None)

    while any(que):

        while que[1]:
            # add nodes of a next_level into a que
            cur_node: TreeNode = que.popleft()
            if cur_node.left:
                que.append(cur_node.left)
            if cur_node.right:
                que.append(cur_node.right)
        # breaking with 1 node left in a que,
        # which is one we can see from right_side,
        # because we can see only last node on a level
        last_on_level: TreeNode = que.popleft()
        # extra proceed it as normal
        if last_on_level.left:
            que.append(last_on_level.left)
        if last_on_level.right:
            que.append(last_on_level.right)
        right_side.append(last_on_level.val)
        que.popleft()
        que.append(None)

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
