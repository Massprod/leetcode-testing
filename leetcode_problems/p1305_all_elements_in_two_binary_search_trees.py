# Given two binary search trees root1 and root2,
#  return a list containing all the integers from both trees sorted in ascending order.
# ----------------------------------
# The number of nodes in each tree is in the range [0, 5000].
# -10 ** 5 <= Node.val <= 10 ** 5
from utils.binary_tree import TreeNode


def get_all_elements(root1: TreeNode, root2: TreeNode) -> list[int]:
    # working_sol (98.58%, 26.09%) -> (160ms, 20.51mb)  time: O((m + n) * log (m + n)) | space: O(m + n)
    out: list[int] = []

    def inorder(node: TreeNode) -> None:
        if node.left:
            inorder(node.left)
        out.append(node.val)
        if node.right:
            inorder(node.right)

    inorder(root1)
    inorder(root2)
    # No idea, how we can traverse them at once, alternative is to use 2 stacks.
    # And merge them later, which is essentially the same as `sorted`.
    return sorted(out)


# Time complexity: O((m + n) * log (m + n)) <- m - number of Nodes in `root1`, n - number of Nodes in `root2`.
# Always traversing both input BSTs and extra sorting their combined values => O((m + n) * log (m + n)).
# ----------------------------------
# Auxiliary space: O(m + n)
# `out` <- allocates space for value from each node of both input BSTs => O(m + n).
