# Given an integer n, return all the structurally unique BST's (binary search trees),
#   which has exactly n nodes of unique values from 1 to n.
# Return the answer in any order.
# ------------------
# 1 <= n <= 8


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generate_trees(n: int) -> list[TreeNode]:
    # working_sol (97.94%, 98.84%) -> (52ms, 17.04mb)
    recur_cache: dict[tuple[int, int], list[TreeNode]] = {}

    def create_nodes(left_l: int, right_l: int) -> list[TreeNode | None]:
        # For every root(node) we're creating all options of LEFT/RIGHT subtrees.
        roots: list[TreeNode] = []
        if left_l > right_l:
            return [None]
        if (left_l, right_l) in recur_cache:
            return recur_cache[left_l, right_l]
        for x in range(left_l, right_l + 1):
            # We should create nodes with [1, n] values ->
            # -> so we always should use different values for left/right subtrees.
            # x == 3, left_sub only can use 1 -> 2 | +1 node with val=x to create ROOT
            # where subs will be placed | and right_sub can use 4 -> 8 values.
            left_subtree: list[TreeNode] = create_nodes(left_l, x - 1)
            right_subtree: list[TreeNode] = create_nodes(x + 1, right_l)
            # Combine left/right subtrees with ROOT.
            for left in left_subtree:
                for right in right_subtree:
                    node: TreeNode = TreeNode(val=x, left=left, right=right)
                    roots.append(node)
        # Cache.
        recur_cache[left_l, right_l] = roots
        return roots

    return create_nodes(1, n)


# Time complexity: O(4 ** n / square(n)) -> not my level, yet.
# n - input_value^^|
# Auxiliary space: O() -> same.
# https://leetcode.com/problems/unique-binary-search-trees-ii/editorial/ <- Dunno why it's medium.
# Building correct BST's was a lot easier than this value dispersing.
# ------------------
# Nah. It's harder, cuz I need to use VALUES not just disperse nodes between 2 subs.
# In this we need to disperse values to a different subs, and everything else is somewhat the same.
# ----------------
# Already done similar buy with constructing CORRECT BST's, and here we can use w.e values we want.
# So it's should be even easier.
