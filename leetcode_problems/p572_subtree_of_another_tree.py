# Given the roots of two binary trees root and subRoot,
#  return true if there is a subtree of root with the same structure and node values of subRoot
#  and false otherwise.
# A subtree of a binary tree is a tree that consists of a node in tree and all of this node's descendants.
# The tree could also be considered as a subtree of itself.
# ------------
# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -10 ** 4 <= root.val <= 10 ** 4
# -10 ** 4 <= subRoot.val <= 10 ** 4


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_subtree(root: TreeNode, subRoot: TreeNode) -> bool:
    # working_sol (33.74%, 44.74%) -> (111ms, 17.6mb)  time: O(n * log n) | space: O(n)
    def check(node: TreeNode, sub_node: TreeNode) -> bool:
        # We need correct pair subtree == subRoot.
        # Both shouldn't have extra childs.
        if not node and not sub_node:
            return True
        # Someone still have a child when other is done.
        if (not node and sub_node) or (node and not sub_node):
            return False
        return node.val == sub_node.val and check(node.left, sub_node.left) and check(node.right, sub_node.right)

    if not root:
        return False
    # Start from current Node.
    if root.val == subRoot.val and check(root, subRoot):
        return True
    # If we can't find correct subtree from it, check descendants as Roots.
    return is_subtree(root.left, subRoot) or is_subtree(root.right, subRoot)


# Time complexity: O(n * log n) -> worst case == every node will have same value, and none of them will be correct pair
# n - number of nodes in BT^^| -> we will start DFS from every node and check some part of the BT => O(n * log n).
# Auxiliary space: O(n) -> worst case == Tree in style of linked_list, we will traverse all nodes, stack == n => O(n).
