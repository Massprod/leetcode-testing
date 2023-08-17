# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia:
#   “The lowest common ancestor is defined between two nodes p and q as the lowest node in T
#    that has both p and q as descendants (where we allow a node to be a descendant of itself).”
# -------------------
# The number of nodes in the tree is in the range [2, 10 ** 5].
# -10 ** 9 <= Node.val <= 10 ** 9
# All Node.val are unique.
# p != q
# p and q will exist in the tree.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowest_common_anc(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # working_sol (99.51%, 91.77%) -> (51ms, 28.49mb)  time: O(n) | space: O(n)
    def search(node: TreeNode) -> TreeNode | None:
        # ! p and q will exist in the tree. !
        # So we can be sure that after this node,
        # there's other one we need lower, or
        # we will check other subtree and find it here.
        # No reasons to go deeper anyway.
        if node == p or node == q:
            return node
        # Left|Right subtrees.
        left: TreeNode | None = None
        right: TreeNode | None = None
        if node.left:
            left = search(node.left)
        if node.right:
            right = search(node.right)
        # If we found correct nodes in both
        # subtrees then we can return this node.
        if left and right:
            return node
        # Otherwise it's one node which equals to P or Q,
        # and presented in one of the subtrees.
        # And other is somewhere below this node.
        if left:
            return left
        if right:
            return right

    return search(root)


# Time complexity: O(n) -> worst case is both node we search is most right leafs of both subtrees ->
# n - nodes of input_BT^^| -> then we will need to traverse whole BT to find them => O(n).
# Auxiliary space: O(n) -> worst case is nodes will be last_node + leaf of this node in BT
#                          which build in linked_list style, stack will store all nodes => O(n).
# -------------------
# Start from every node and search for both True returns -> every node is unique, so if we found any
# node from what we started is P or Q return this node, or first node with both left|right subs being True.
# Should be correct.
