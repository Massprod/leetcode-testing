# Given two integer arrays, preorder and postorder where preorder
#  is the preorder traversal of a binary tree of distinct values
#  and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.
# If there exist multiple answers, you can return any of them.
# --------------------
# 1 <= preorder.length <= 30
# 1 <= preorder[i] <= preorder.length
# All the values of preorder are unique.
# postorder.length == preorder.length
# 1 <= postorder[i] <= postorder.length
# All the values of postorder are unique.
# It is guaranteed that preorder and postorder are the preorder traversal
#  and postorder traversal of the same binary tree.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_read(root: TreeNode) -> list[int]:
    out: list[int | None] = []
    que: deque[TreeNode] = deque([root])
    while que:
        node: TreeNode = que.popleft()
        if not node:
            out.append(None)
            continue
        out.append(node.val)
        que.append(node.left)
        que.append(node.right)
    while out[-1] is None:
        out.pop()
    return out


def construct_from_pre_post(preorder: list[int], postorder: list[int]) -> TreeNode:
    # working_sol (98.10%, 26.29%) -> (39ms 17.15mb)  time: O(n * n) | space: O(h * n)
    # Made from intuition and first test_case.
    # Google for basic knowledge is better, but still works :)
    # preorder = [1,2,4,5,3,6,7]
    # postorder = [4,5,2,6,7,3,1]
    if len(preorder) == 1:
        return TreeNode(
            val=preorder[0],
            left=None,
            right=None
        )
    # By the picture we can see that preorder[1] is 100% left child of preorder[0].
    # So, preorder[0] should be `root` and preorder[1] left child.
    # Everything below left child == left_subtree, is on the left side of preorder[1] in postorder.
    # So, we can take left subtree from this.
    left: int = postorder.index(preorder[1])
    left_sub: list[int] = postorder[:left + 1]
    # But where right subtree starts in preorder?
    # By the picture it seems all values from 1 -> `len(left_sub)` is included in left subtree.
    # So, assume we can start right subtree from (1 + `len(left_sub)`).
    left_limit: int = 1 + len(left_sub)
    # Everything what's left is ! postorder[postorder.index(preorder[1]) + 1:postorder.index(preorder[0])] !.
    # So, assume this is the right subtree of `root` (nothing else is possible).
    right_sub: list[int] = []
    if left_limit < len(postorder):
        right: int = postorder.index(preorder[left_limit])
        right_sub: list[int] = postorder[left + 1:right + 1]
    # But, we can have preorder with len == 2, and only left subtree.
    # We need to ignore right sub in this case.
    if right_sub:
        root: TreeNode = TreeNode(
            val=preorder[0],
            left=construct_from_pre_post(preorder[1:left_limit], left_sub),
            right=construct_from_pre_post(preorder[left_limit:], right_sub),
        )
    else:
        root = TreeNode(
            val=preorder[0],
            left=construct_from_pre_post(preorder[1:left_limit], left_sub),
            right=None
        )
    return root


# Time complexity: O(n * n) <- n - length of input arrays `postorder` | `preorder`.
# Dunno correct explanation, but we create every Node from given arrays.
# Every index == Node and len(postorder) == all Nodes.
# But, we slice and search for index for every Node, in case like pre[2, 1], post[1, 2]:
#  we will traverse partially post[] to get index of '1' and slice post[:1] which is also a part.
# So it should be O(n * log n). Definitely not O(n), maybe O(n * n).
# Because we're actually doing close logic to MergeSort, which is O(N * log N).
# Nah, in MergeSort we're always taking half, and there's we can have (n - 1).
# So, it should be O(n * n).
# --------------------
# Auxiliary space: O(h * n) <- h - height of input BT, if we build it.
# For every level of BT we will create slices, which never be more than `n`.
# Same logic, we're not taking half's but (n - 1) -> (n - 2) etc.
# So, for every level of BT we build we're taking a slice => O(h * n).


test_pre: list[int] = [1, 2, 4, 5, 3, 6, 7]
test_post: list[int] = [4, 5, 2, 6, 7, 3, 1]
test_out: list[int] = [1, 2, 3, 4, 5, 6, 7]
assert test_out == level_order_read(construct_from_pre_post(test_pre, test_post))

test_pre = [1]
test_post = [1]
test_out = [1]
assert test_out == level_order_read(construct_from_pre_post(test_pre, test_post))

test_pre = [2, 1]
test_post = [1, 2]
test_out = [2, 1]
assert test_out == level_order_read(construct_from_pre_post(test_pre, test_post))
