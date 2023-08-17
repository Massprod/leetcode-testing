# Given a binary tree root, a node X in the tree is named good if in the path
#   from root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.
# ----------------
# The number of nodes in the binary tree is in the range [1, 10 ** 5].
# Each node's value is between [-10 ** 4, 10 ** 4].


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def good_nodes(root: TreeNode) -> int:
    # working_sol (93.3%, 34.45%) -> (180ms, 35.1mb)  time: O(n) | space: O(n)

    def inorder(node: TreeNode, cur_max: int) -> int:
        # Standard DFS with counting correct values(nodes)
        cur_max: int = max(cur_max, node.val)
        count: int = 0
        if node.val >= cur_max:
            count += 1
        if node.left:
            count += inorder(node.left, cur_max)
        if node.right:
            count += inorder(node.right, cur_max)
        return count

    return inorder(root, root.val)


# Time complexity: O(n) -> standard DFS with using every node once => O(n).
# n - nodes of input_BT^^|
# Auxiliary space: O(n) -> worst case BT build like linked_list, every possible node
#                          will be in the recursion stack => O(n).
# ----------------
# Standard go deepest and maintain max? Only part is maintain counter in recursion or just store outside?
# Outside is simplier, but will see. Ok. Counted inside.
