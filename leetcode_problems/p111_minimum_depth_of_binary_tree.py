# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path
#   from the root node down to the nearest leaf node.
# ------------------
# The number of nodes in the tree is in the range [0, 10 ** 5].
# -1000 <= Node.val <= 1000


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDepth(root: TreeNode) -> int:
    # working_sol (65.95%, 43.6%) -> (553ms, 57.2mb)  time: O(n) | space: O(log n)
    if not root:
        return 0
    min_depth: list[int | None] = [None]

    def inorder(node: TreeNode, level: int = 0) -> None:
        level += 1
        if node.left is None and node.right is None:
            if min_depth[0] is None:
                min_depth[0] = level
            else:
                min_depth[0] = min(min_depth[0], level)
            return
        if node.left:
            inorder(node.left, level)
        if node.right:
            inorder(node.right, level)

    inorder(root)
    return min_depth[0]


# Time complexity: O(n) -> standard inorder traverse of the whole BT, once => O(n).
# n - num of nodes in BT^^|
# Auxiliary spae: O(log n) -> using recursion, and for every call we're storing link_nodes in a stack,
#                             we're not creating nodes, but still storing links to them, and they depend on input_BT =>
#                             => O(log n).
# ! Or we can call it O(1) <- because we're operating only with links to a nodes and one constant value min_depth[0] !
# ------------------
# What a joke. Literally tried to create EMPTY TREE with just [] used in test_case and didn't allow me.
# And second test_case is empty tree as expected, and needs to return 0 not Null. Wow.
# --------------------
# Not building trees for this.
# Only thing I don't understand is how to test case with length of tree 0.
# If there's no Nodes this should return None, but maybe it's 0 depth?
# Guess it's just a trap like always, fail to see.
