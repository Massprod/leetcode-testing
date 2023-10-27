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
    # working_sol (99.76%, 99.64%) -> (23ms, 15.90mb)  time: O(n) | space: O(n)
    if not root:
        return root
    # Standard level-order traverse.
    # A.k.a BFS with delimiter.
    que: deque[TreeNode | None] = deque()
    que.append(root)
    que.append(None)
    while que:
        current: TreeNode = que.popleft()
        # New level.
        if not current:
            # Still have Nodes to use.
            if que:
                que.append(None)
            continue
        # Switching every Node children, before we're adding them into the que.
        current.left, current.right = current.right, current.left
        # Adding childs with correct ordering.
        if current.left:
            que.append(current.left)
        if current.right:
            que.append(current.right)
    return root


# Time complexity: O(n) -> traversing all nodes of input BT once => O(n).
# n - Nodes of input BT^^|
# Auxiliary_space: O(n) -> extra space to store all Nodes of input BT => O(n).
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
