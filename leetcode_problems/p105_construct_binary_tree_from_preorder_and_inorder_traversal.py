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
    # working_sol (33.71%, 6.94%) -> (211ms, 91.4mb)  time: O(n ** 2) | space: O(n)
    if not root:
        return []
    show_tree: list[int | None] = []
    que: deque = deque()
    que.appendleft(root)
    # if there's only None left, then it's last level, and we have nothing to check
    # any() <- checks everything in iterable and if there's no elements we break.
    # any() used to eliminate extra level with nulls, when que is empty,
    #       and still store Nulls for other levels.
    while any(que):
        current_node: TreeNode = que.popleft()
        if current_node is None:
            show_tree.append(None)
            continue
        show_tree.append(current_node.val)
        que.append(current_node.left)
        que.append(current_node.right)

    return show_tree


def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    if not preorder and not inorder:
        return None
    root: TreeNode = TreeNode(val=preorder[0])
    # find root position
    in_order_index: int = inorder.index(root.val)
    # divide left/right subtree by ROOT in inorder
    left_subtree: list[int] = inorder[:in_order_index]
    right_subtree: list[int] = inorder[in_order_index + 1:]
    # divide left/right subtrees by ROOT in preorder
    preorder_left_subtree: list[int] = preorder[1: len(left_subtree) + 1]
    preorder_right_subtree: list[int] = preorder[len(left_subtree) + 1:]
    # go deeper, and build with backtrack path
    root.left = build_tree(preorder_left_subtree, left_subtree)
    root.right = build_tree(preorder_right_subtree, right_subtree)
    return root


# Time complexity: O(n ** 2) -> standard build method for this is O(n ** 2) for unbalanced trees,
# n - len of preorder^^| and O(n * log n) for balanced trees.
# k - len of inorder^^ |
# Auxiliary space: O(n) -> in the worst case we're going to have unbalanced tree with
#                          all it's nodes stored in the one side, left/right w.e ->
#                          -> because of that we're calling recursion for every node and
#                          number of calls will be equal to n, which gives us stack with size of n => O(n).
# -----------------------
# First index of preorder is always ROOT, left_part and right_part of inorder around this ROOT is
# subtrees left and right of this ROOT. Slice with length of these subtrees in preorder is also
# left/right subtrees, slice it until we hit leaf. Basic idea.


test1_pre = [3, 9, 20, 15, 7]
test1_in = [9, 3, 15, 20, 7]
test1_out = [3, 9, 20, None, None, 15, 7]
test = build_tree(test1_pre, test1_in)
assert test1_out == show_tree_level_order(test)
del test

test2_pre = [-1]
test2_in = [-1]
test2_out = [-1]
test = build_tree(test2_pre, test2_in)
assert test2_out == show_tree_level_order(test)
del test
