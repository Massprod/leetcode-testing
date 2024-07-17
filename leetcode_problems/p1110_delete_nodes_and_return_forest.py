# Given the root of a binary tree, each node in the tree has a distinct value.
# After deleting all nodes with a value in to_delete,
#  we are left with a forest (a disjoint union of trees).
# Return the roots of the trees in the remaining forest. You may return the result in any order.
# ----------------------
# The number of nodes in the given tree is at most 1000.
# Each node has a distinct value between 1 and 1000.
# to_delete.length <= 1000
# to_delete contains distinct values between 1 and 1000.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def del_nodes(root: TreeNode, to_delete: list[int]) -> list[TreeNode]:
    # working_sol (95.04%, 61.78%) -> (46ms, 16.92mb)  time: O(n + k) | space: O(n + k)
    to_del: set[int] = set(to_delete)
    forest: list[TreeNode] = []
    if root.val not in to_del:
        forest.append(root)

    def traverse(node: TreeNode) -> None:
        nonlocal forest
        # We delete `node` itself, and his childs become new roots.
        # But only they shouldn't be deleted as well.
        if node.val in to_del:
            if node.left and node.left.val not in to_del:
                forest.append(node.left)
            if node.right and node.right.val not in to_del:
                forest.append(node.right)
        # Even if `node` should be deleted, we still need to check his subtrees.
        if node.left:
            traverse(node.left)
            # And delete it after.
            if node.left.val in to_del:
                node.left = None
        if node.right:
            traverse(node.right)
            if node.right.val in to_del:
                node.right = None

    traverse(root)
    return forest


# Time complexity: O(n + k) <- n - number of Nodes inside the input BT `root`,
#                              k - length of the input array `to_delete`.
# Creating set with all unique values to delete from `to_delete` => O(k).
# We're always traversing whole input BT `root`, once => O(k + n).
# ----------------------
# Auxiliary space: O(n + k)
# Dunno about deleting nodes, because if we delete everything `forest` is empty.
# If we delete only half we will get forest with `n // 2` and if we just delete first node == `root`.
# And leave his childs in `forest` it's going to be `n - 1` (with BT like 1 -> [2, 3]).
# So, it's definitely Linear or even lower, but I don't think we can say it's logarithmic => O(n).
# Extra we allocate space for every INT in `to_delete`, in our set `to_del` => O(n + k).
