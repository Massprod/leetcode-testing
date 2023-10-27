# Given two integer arrays inorder and postorder where inorder
#   is the inorder traversal of a binary tree
#   and postorder is the postorder traversal of the same tree,
#   construct and return the binary tree.
# ------------------
# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder and postorder consist of unique values.
# Each value of postorder also appears in inorder.
# inorder is guaranteed to be the inorder traversal of the tree.
# postorder is guaranteed to be the postorder traversal of the tree.
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


def build_tree(inorder: list[int], postorder: list[int]) -> TreeNode | None:
    # working_sol (11.37%, 6.31%) -> (190ms, 91.54mb)  time: O(n ** 2) | space: O(n)
    if not inorder and not postorder:
        return None
    # Current ROOT is last index of postorder.
    root: TreeNode = TreeNode(val=postorder[-1])
    # Find root position inside inorder.
    inorder_index: int = inorder.index(root.val)
    # Divide left and right subtrees by ROOT in the inorder.
    left_subtree: list[int] = inorder[: inorder_index]
    right_subtree: list[int] = inorder[inorder_index + 1:]
    # Divide left and right subtrees by ROOT in the postorder.
    postorder_left_subtree: list[int] = postorder[:len(left_subtree)]
    postorder_right_subtree: list[int] = postorder[len(left_subtree):-1]
    # Go deeper, and build with backtrack path.
    root.left = build_tree(left_subtree, postorder_left_subtree)
    root.right = build_tree(right_subtree, postorder_right_subtree)
    return root


# Time complexity: O(n ** 2) -> standard build method for this is O(n ** 2) for unbalanced trees,
# n - len of input list 'preorder'^^|  and O(n * log n) for balanced trees.
# k - len of input list 'inorder'^^ |
# Auxiliary space: O(n) -> in the worst case we're going to have unbalanced tree with
#                          all it's nodes stored in the one side, left/right w.e ->
#                          -> because of that we're calling recursion for every node and
#                          number of calls will be equal to n, which gives us stack with size of n => O(n).
# ------------------
# Mirror of p105, but in POSTORDER -> ROOT is a last index, and slicing is slightly different.
# Slicing doesn't include last index of postorder.


test_inorder: list[int] = [9, 3, 15, 20, 7]
test_postorder: list[int] = [9, 15, 7, 20, 3]
test_out: list[int | None] = [3, 9, 20, None, None, 15, 7]
assert test_out == show_tree_level_order(build_tree(test_inorder, test_postorder))

test_inorder = [-1]
test_postorder = [-1]
test_out = [-1]
assert test_out == show_tree_level_order(build_tree(test_inorder, test_postorder))
