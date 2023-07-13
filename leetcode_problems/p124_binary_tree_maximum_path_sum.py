# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes
#   in the sequence has an edge connecting them.
# A node can only appear in the sequence at most once.
# Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.
# -------------------------
# The number of nodes in the tree is in the range [1, 3 * 10 ** 4].
# -1000 <= Node.val <= 1000


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root: TreeNode) -> int:
    # working_sol (62.34%, 12.8%) -> (102ms, 24mb)  time: O(n) | space: O(n)
    max_sum: list[int | None] = [None]

    def inorder(node: TreeNode) -> int:
        if not node:
            return 0
        # max_sum from left/right subtrees
        # ignoring negatives, because they will only decrease our max_sum
        # which is not what we want, extra it's allowing us to find max_sum correctly
        # if there's only negative values in BT, one of the nodes will have
        # node.val == max_sum by itself, everything else just decreases it.
        left_sub_sum: int = max(0, inorder(node.left))
        right_sub_sum: int = max(0, inorder(node.right))
        # current max_sum, if we start from one of the node leafs
        node_max: int = left_sub_sum + right_sub_sum + node.val
        if max_sum[0] is None:
            max_sum[0] = node_max
        else:
            max_sum[0] = max(max_sum[0], node_max)
        # continue moving backwards, starting from best leaf ->
        # -> leaf which gives highest_sum in its subtree, if we start moving from it.
        return node.val + max(left_sub_sum, right_sub_sum)

    inorder(root)
    return max_sum[0]


# Time complexity: O(n) -> traversing whole BT, once => O(n).
# Auxiliary space: O(n) -> in the worst case, BT will be like linked_list with only left_children ->
#                          -> so recursion stack will be a size of n => O(n).
# -------------------------
# Bruh. Failed first commit -> because forgot to set max_sum as None.
# Think all of this through and forgot that there's placeholder from 1 attempts. Deserved.
# -------------------------
# Main thing is we always need to ignore negatives and calculate in this manner:
#  /\
# /  \
# Then we're checking every possible LEAF and start from it.
# Because we're not allowed to visit nodes more than once, it's always best to start from some LEAF.
# -------------------------
# Made explanation with some *drawings*, after thinking on that overnight.
# Actually not that Hard problem in the end.
