# Given an array of integers preorder, which represents the preorder traversal of a BST
#  (i.e., binary search tree), construct the tree and return its root.
# It is guaranteed that there is always possible to find a binary search tree
#  with the given requirements for the given test cases.
# A binary search tree is a binary tree where for every node, any descendant
#  of Node.left has a value strictly less than Node.val,
#  and any descendant of Node.right has a value strictly greater than Node.val.
# A preorder traversal of a binary tree displays the value of the node first,
#  then traverses Node.left, then traverses Node.right.
# ---------------------------
# 1 <= preorder.length <= 100
# 1 <= preorder[i] <= 1000
# All the values of preorder are unique.
from utils.binary_tree import TreeNode


def bst_from_preorder(preorder: list[int]) -> TreeNode:
    # working_sol (92.20%, 22.45%) -> (31ms, 16.74mb)  time: O(n) | space: O(n)
    def construct(
            preorder: list[int],
            index: list[int],
            min_val: int | float = float('-inf'),
            max_val: int | float = float('inf')
    ) -> TreeNode | None:

        if len(preorder) <= index[0]:
            return None
        cur_val: int = preorder[index[0]]
        if not (min_val < cur_val < max_val):
            return None
        node: TreeNode = TreeNode(cur_val)
        index[0] += 1
        if index[0] < len(preorder):
            node.left = construct(preorder, index, min_val, cur_val)
            node.right = construct(preorder, index, cur_val, max_val)
        return node

    return construct(preorder, [0])


# Time complexity: O(n) <- n - length of the input array `preorder`.
# Always using every index of the input array `preorder` => O(n).
# ---------------------------
# Auxiliary space: O(n)
# In the worst case there's only `root` and left_subtree with only left_childs.
# We will have a recursion stack of `n` size => O(n).
# Extra our constructed BST will always have `n` Nodes => O(2 * n).
