# Given the root of a binary tree, return the leftmost value in the last row of the tree.
# -----------------------
# The number of nodes in the tree is in the range [1, 10 ** 4].
# -2 ** 31 <= Node.val <= 2 ** 31 - 1
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_bottom_left_value(root: TreeNode) -> int:
    # working_sol (84.20%, 97.42%) -> (37ms, 18.19mb)  time: O(n) | space: O(n)
    que: deque[TreeNode | None] = deque([root, None])
    left_most: TreeNode = root
    while que:
        cur_node: TreeNode | None = que.popleft()
        if cur_node is None:
            if que:
                que.append(None)
                left_most = que[0]
                continue
            else:
                return left_most.val
        if cur_node.left:
            que.append(cur_node.left)
        if cur_node.right:
            que.append(cur_node.right)
    return left_most.val


# Time complexity: O(n) <- n - number of Nodes in given BT.
# Worst case: last Node of the pre-last level will have LeftChild.
# So, we will traverse whole BT to get to this Node.
# -----------------------
# Auxiliary space: O(n)
# We will allocate space for every Node of BT into a que.
# -----------------------
# Not building trees, it's longer than task itself.
