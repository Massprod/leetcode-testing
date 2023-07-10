# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
#  1) The left subtree of a node contains only nodes with keys less than the node's key.
#  2) The right subtree of a node contains only nodes with keys greater than the node's key.
#  3) Both the left and right subtrees must also be binary search trees.
# ---------------------
# The number of nodes in the tree is in the range [1, 10 ** 4].
# -2 ** 31 <= Node.val <= 2 ** 31 - 1


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: TreeNode) -> bool:
    if root.left is None and root.right is None:
        return True
    first_val: int = root.val

    def inorder(node: TreeNode, left_p: bool, right_p: bool) -> bool:
        if node.left or node.right:
            if type(node.left) is not TreeNode or type(node.right) is not TreeNode:
                return False
        if left_p:
            if node.left and node.right:
                if node.left.val < node.val < node.right.val < first_val:
                    if inorder(node.left, left_p, right_p) and inorder(node.right, left_p, right_p):
                        return True
                return False
            if node.left and node.right is None:
                if node.left.val < node.val < first_val:
                    if inorder(node.left, left_p, right_p):
                        return True
                return False
            if node.right and (node.left is None):
                if node.val < node.right.val < first_val:
                    if inorder(node.right, left_p, right_p):
                        return True
                return False
            if node.left is None and node.right is None:
                if node.val < first_val:
                    return True
                return False
        if right_p:
            if node.left and node.right:
                if first_val < node.left.val < node.val < node.right.val:
                    if inorder(node.left, left_p, right_p) and inorder(node.right, left_p, right_p):
                        return True
                return False
            if node.left and node.right is None:
                if first_val < node.left.val < node.val:
                    if inorder(node.left, left_p, right_p):
                        return True
                return False
            if node.right and node.left is None:
                if first_val < node.val < node.right.val:
                    if inorder(node.right, left_p, right_p):
                        return True
                return False
            if node.left is None and node.right is None:
                if node.val > first_val:
                    return True
                return False

    left_correct: bool = False
    right_correct: bool = False
    if root.left.val < root.val:
        left_correct = inorder(root.left, True, False)
    if root.right.val > root.val:
        right_correct = inorder(root.right, False, True)
    return left_correct and right_correct


# !
# Both the left and right subtrees must also be binary search trees. !
# ^^Make extra check for type of what stored in node.left, node.right.
# ---------------------
# If understood correctly, all we need is just check EVERY node for 1, 2 cases.
# Every node should be like that ->  node.left.val < node.val < node.right.val
# Shouldn't matter in which way we're reading, just break when this rule isn't correct.
# Incorrect ! THE LEFT SUBTREE ! so every node in left and right subtree should be compared to root?
# Or NODE is changing every time we change it?
