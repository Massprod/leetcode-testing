# Given the root of a binary tree and an integer targetSum,
#   return true if the tree has a root-to-leaf path such
#   that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.
# ------------------
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root: TreeNode, targetSum: int) -> bool:
    # working_sol (78.43%, 82.20%) -> (55ms, 17.4mb)  time: O(n) | space: O(log n)
    if not root:
        return False

    def inorder(node: TreeNode, path) -> None | bool:
        if node.left is None and node.right is None:
            if path == targetSum:
                return True
            return False
        if node.left:
            if inorder(node.left, path + node.left.val):
                return True
        if node.right:
            if inorder(node.right, path + node.right.val):
                return True

    if inorder(root, root.val):
        return True
    return False


# Time complexity: O(n) -> in the worst case it's last right leaf of the right_subtree,
# n - nodes in input BT^^| and we will visit every node in input_BT => O(n).
# Auxiliary space: O(log n) -> if we ignore stack of recursion than it's constant, otherwise O(log n).
