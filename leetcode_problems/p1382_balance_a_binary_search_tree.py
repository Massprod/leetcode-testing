# Given the root of a binary search tree, return a balanced binary search tree with the same node values.
# If there is more than one answer, return any of them.
# A binary search tree is balanced if the depth of the two subtrees
#  of every node never differs by more than 1.
# ---------------------------
# The number of nodes in the tree is in the range [1, 10 ** 4].
# 1 <= Node.val <= 10 ** 5


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def balance_bst(root: TreeNode) -> TreeNode:
    # working_sol (52.73%, 43.13%) -> (202ms, 22.09mb)  time: O(n) | space: O(n)
    inorder_traverse: list[int] = []

    def inorder(node: TreeNode) -> None:
        nonlocal inorder_traverse
        if node.left:
            inorder(node.left)
        inorder_traverse.append(node.val)
        if node.right:
            inorder(node.right)

    def build_balanced(left_l: int, right_l: int) -> TreeNode | None:
        middle: int = (left_l + right_l) // 2
        if left_l > right_l:
            return None
        new_root = TreeNode(val=inorder_traverse[middle])
        new_root.left = build_balanced(left_l, middle - 1)
        new_root.right = build_balanced(middle + 1, right_l)
        return new_root

    inorder(root)
    return build_balanced(0, len(inorder_traverse) - 1)


# Time complexity: O(n) <- n - number of Nodes inside the input BST `root`.
# Always traversing input BST `root` with `inorder`, once => O(n).
# Extra traversing the same number of nodes stored in `inorder_traverse` to build balanced tree => O(n).
# ---------------------------
# Auxiliary space: O(n).
# All of the nodes from `root` are stored in `inorder_traverse` => O(n).
# Extra `inorder` recursion stack can be a size of `n` => O(2n).
