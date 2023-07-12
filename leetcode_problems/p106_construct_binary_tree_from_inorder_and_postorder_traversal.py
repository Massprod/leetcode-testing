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


def build_tree(inorder: list[int], postorder: list[int]) -> TreeNode | None:
    # working_sol (22.55%, 9.94%) -> (216ms, 91.6mb)  time: O(n ** 2) | space: O(n)
    if not inorder and not postorder:
        return None
    # postorder root is last index
    root: TreeNode = TreeNode(val=postorder[-1])
    # find root position
    in_order_index: int = inorder.index(root.val)
    # divide left/right subtrees by ROOT in inorder
    left_subtree: list[int] = inorder[: in_order_index]
    right_subtree: list[int] = inorder[in_order_index + 1:]
    # divide left/right subtrees by ROOT in postorder
    postorder_left_subtree: list[int] = postorder[:len(left_subtree)]
    postorder_right_subtree: list[int] = postorder[len(left_subtree):-1]
    # go deeper, and build with backtrack path
    root.left = build_tree(left_subtree, postorder_left_subtree)
    root.right = build_tree(right_subtree, postorder_right_subtree)
    return root


# Time complexity: O(n ** 2) -> standard build method for this is O(n ** 2) for unbalanced trees,
# n - len of preorder^^| and O(n * log n) for balanced trees.
# k - len of inorder^^ |
# Auxiliary space: O(n) -> in the worst case we're going to have unbalanced tree with
#                          all it's nodes stored in the one side, left/right w.e ->
#                          -> because of that we're calling recursion for every node and
#                          number of calls will be equal to n, which gives us stack with size of n => O(n).
# ------------------
# Mirror of p105, but in POSTORDER -> ROOT is a last index, and slicing is slightly different.


test1_in = [9, 3, 15, 20, 7]
test1_post = [9, 15, 7, 20, 3]
test1_out = [3, 9, 20, None, None, 15, 7]
test = build_tree(test1_in, test1_post)
print(show_tree_level_order(test))
assert test1_out == show_tree_level_order(test)
del test

test2_in = [-1]
test2_post = [-1]
test2_out = [-1]
test = build_tree(test2_in, test2_post)
print(show_tree_level_order(test))
assert test2_out == show_tree_level_order(test)
del test
