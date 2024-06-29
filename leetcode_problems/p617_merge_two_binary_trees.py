# You are given two binary trees root1 and root2.
# Imagine that when you put one of them to cover the other,
#  some nodes of the two trees are overlapped while the others are not.
# You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap,
#  then sum node values up as the new value of the merged node.
# Otherwise, the NOT null node will be used as the node of the new tree.
# Return the merged tree.
# Note: The merging process must start from the root nodes of both trees.
# --------------------------
# The number of nodes in both trees is in the range [0, 2000].
# -10 ** 4 <= Node.val <= 10 ** 4


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def merge_trees(root1: TreeNode, root2: TreeNode) -> TreeNode:
    # working_sol (83.56%, 97.07%) -> (57ms, 16.75mb)  time: O(max(n, k)) | space: O(max(n, k))
    def merge(node1: TreeNode, node2: TreeNode) -> TreeNode | None:
        if not node1 and not node2:
            return
        if not node1:
            return node2
        if not node2:
            return node1
        node1.val = node1.val + node2.val
        node1.left = merge(node1.left, node2.left)
        node1.right = merge(node1.right, node2.right)
        return node1

    return merge(root1, root2)


# Time complexity: O(max(n, k)) <- n - number of nodes in BT `root1`, k - number of nodes in BT `root2`.
# In the worst case, we're going to have 2 BTs, and they will have the same number of Nodes and the same structure.
# So, we will traverse all of these Nodes and calc their sums => O(2 * max(n, k)).
# --------------------------
# Auxiliary space: O(max(n, k)).
# We will expand one of the trees to the same size as other == same Nodes in both but maximized => O(max(n, k)).
# Extra stack of the recursion can be a size of `max(n, k)` because we're traversing both BT with the same size =>
#  O(2 * max(n, k))
# --------------------------
# Not building trees.
