# Given the root of a binary tree, invert the tree, and return its root.
# ----------------
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: TreeNode) -> TreeNode:
    # working_sol (97.15%, 95.82%) -> (36ms, 16.2mb)  time: O(n) | space: O(log n)
    if not root:
        return root
    # standard que level-order
    que: deque[TreeNode | None] = deque()
    que.append(root)
    que.append(None)
    while any(que):
        while que[0]:
            current: TreeNode = que.popleft()
            # switching every node on a level, before we add their childs in a que
            current.left, current.right = current.right, current.left
            # adding childs with correct ordering
            if current.left:
                que.append(current.left)
            if current.right:
                que.append(current.right)
        # add/delete lvl delimiter
        que.append(None)
        que.popleft()
    return root


# Time complexity: O(n) -> traversing whole nodes of input_BT, once => O(n).
# n - node in input_BT^^|
# Auxiliary_space: O(log n) -> there's case with 1 level only as root, and we're storing O(n) ->
#                           -> normally we're just storing only part of the input_BT ->
#                           -> nodes at current_level and part of the next level => O(log n).
#                           ^^If we can ignore stack/que than it's can be called even constant space,
#                             because we're just switching nodes of input_BT without anything extra.
# ----------------
# Well works correctly, but need more test_cases.
# ----------------
# Well, doing this with recording whole inorder or any other path is simple.
# But can we do this with constant space?
# Don't see how it's possible and there's no requirements so w.e.
# Even if I read with order-level, still we need to store level before we switch them and
# if I switch whole level next level will shuffled in unknown order.
# Actually what if we switch all level -> root (2, 7) 1 level ->
# -> 2 (1, 3) , 7 (6, 9) -> switching 2 7 on 2 level => 7 (6, 9) , 2 (1, 3) ->
# -> now I need to just switch 6 9 and 1 3, and it's correct order. Does it work for all levels?
# cur_node.left, cur_node.right = cur_node.right, cur_node.left <- should be something like this.
# Let's test.
