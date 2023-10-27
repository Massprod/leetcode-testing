# Given two integer arrays preorder and inorder where preorder is the preorder traversal
#   of a binary tree and inorder is the inorder traversal of the same tree,
#   construct and return the binary tree.
# -----------------------
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.
from collections import deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def show_tree_level_order(root: TreeNode) -> list[int | None]:
    # Leetcode result list == level_order.
    if not root:
        return []
    show_tree: list[int | None] = []
    que: deque[TreeNode | None] = deque([root])
    while que:
        current_node: TreeNode = que.popleft()
        if not current_node:
            show_tree.append(None)
            continue
        show_tree.append(current_node.val)
        que.append(current_node.left)
        que.append(current_node.right)
    while not show_tree[-1]:
        show_tree.pop()
    return show_tree


def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    # working_sol (25.95%, 7.02%) -> (178ms, 91.22mb)  time: O(n ** 2) | space: O(n)
    if not preorder and not inorder:
        return None
    root: TreeNode = TreeNode(val=preorder[0])
    # Find current root position.
    in_order_index: int = inorder.index(root.val)
    # Divide left and right subtrees by ROOT in inorder.
    inorder_left_subtree: list[int] = inorder[:in_order_index]
    inorder_right_subtree: list[int] = inorder[in_order_index + 1:]
    # Divide left and right subtrees by ROOT in preorder.
    preorder_left_subtree: list[int] = preorder[1: len(inorder_left_subtree) + 1]
    preorder_right_subtree: list[int] = preorder[len(inorder_left_subtree) + 1:]
    # Go deeper, and build with backtrack path.
    root.left = build_tree(preorder_left_subtree, inorder_left_subtree)
    root.right = build_tree(preorder_right_subtree, inorder_right_subtree)
    return root


# Time complexity: O(n ** 2) -> standard build method for this is O(n ** 2) for unbalanced trees,
# n - len of input list 'preorder'^^|  and O(n * log n) for balanced trees.
# k - len of input list 'inorder'^^ |
# Auxiliary space: O(n) -> in the worst case we're going to have unbalanced tree with
#                          all it's nodes stored on one side, left/right w.e ->
#                          -> because of that we're calling recursion for every node and
#                          number of calls will be equal to n, which gives us stack with size of n => O(n).
# -----------------------
# First index of preorder is always ROOT, left_part and right_part of inorder around this ROOT is
# subtrees left and right of this ROOT. Slice with length of these subtrees in preorder is also
# left/right subtrees, slice it until we hit leaf. Basic idea.


test_preorder: list[int] = [3, 9, 20, 15, 7]
test_inorder: list[int] = [9, 3, 15, 20, 7]
test_out: list[int | None] = [3, 9, 20, None, None, 15, 7]
assert test_out == show_tree_level_order(build_tree(test_preorder, test_inorder))

test_preorder = [-1]
test_inorder = [-1]
test_out = [-1]
assert test_out == show_tree_level_order(build_tree(test_preorder, test_inorder))
