# Consider all the leaves of a binary tree, from left to right order,
#   the values of those leaves form a leaf value sequence.
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
# -------------------
# The number of nodes in each tree will be in the range [1, 200].
# Both of the given trees will have values in the range [0, 200].


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def leaf_similar(root1: TreeNode, root2: TreeNode) -> bool:
    # working_sol (95.69%, 91.67%) -> (34ms, 16.25mb)  time: O(m + n) | space: O(log m + log n)
    leafs1: list[int] = []
    leafs2: list[int] = []

    def inorder(node: TreeNode, first: bool) -> None:
        if not node.left and not node.right:
            if first:
                leafs1.append(node.val)
            else:
                leafs2.append(node.val)
        if node.left:
            inorder(node.left, first)
        if node.right:
            inorder(node.right, first)
    inorder(root1, True)
    inorder(root2, False)
    return leafs1 == leafs2


# Time complexity: O(m + n) -> traversing both input_BT once => O(m + n) ->
# m - nodes of root1^^| -> extra compare lists with leafs => O(log m + log n).
# n - nodes of root2^^|
# Auxiliary space: O(log m + log n) -> store every leafs possible in lists, it's always only
#                        some part of input_BT => O(log m + log n)
