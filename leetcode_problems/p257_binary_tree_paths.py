# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.
# ----------------
# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_paths(root: TreeNode) -> list[str]:
    # working_sol (89.99%, 58.86%) -> (38ms, 16.34mb)  time: O(n) | space: O(n)
    paths: list[str] = []

    def in_order(node: TreeNode, path: str) -> None:
        # Standard in_order traverse with saving of the path.
        if not node.left and not node.right:
            path += f'{node.val}'
            paths.append(path)
            return
        path += f'{node.val}->'
        if node.left:
            in_order(node.left, path)
        if node.right:
            in_order(node.right, path)

    in_order(root, '')
    return paths


# Time complexity: O(n) -> standard in_order traversal of a BST, every node will be visited once => O(n).
# Auxiliary space: O(n) -> because I'm using a recursion, it could be a size of whole BST ->
#                          -> like: one left subtree for every node and BST will be a linked list with n size => O(n).
# ----------------
# Not building trees for this. Should just InOrder traverse with path_recording on every node,
# and saving when Leaf found.
