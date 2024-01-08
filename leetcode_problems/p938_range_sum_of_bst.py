# Given the root node of a binary search tree and two integers low and high,
#  return the sum of values of all nodes with a value in the inclusive range [low, high].
# ------------------
# The number of nodes in the tree is in the range [1, 2 * 10 ** 4].
# 1 <= Node.val <= 10 ** 5
# 1 <= low <= high <= 10 ** 5
# All Node.val are unique.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def range_sum_bst(root: TreeNode, low: int, high: int) -> int:
    # working_sol (97.15%, 87.42%) -> (109ms, 24.4mb)  time: O(n) | space: O(n)

    def dfs(node: TreeNode) -> int:
        # BST -> left subtree all lower than node.val
        #        right subtree all higher than node.val
        out: int = 0
        if not node:
            return out
        if low <= node.val <= high:
            out += node.val
        # If `node.val` already lower than `low`, everything in left subtree
        #  will be even smaller, we don't need it.
        if node.val >= low:
            out += dfs(node.left)
        # If `node.val` already higher than `high`, everything in right subtree
        #   will be even higher, we don't need it.
        if node.val <= high:
            out += dfs(node.right)
        return out

    return dfs(root)


# Time complexity: O(n) <- n - number of Nodes in input BST.
# Worst case: we will have all Nodes within low -> high range.
# We will traverse all BST once => O(n).
# ------------------
# Auxiliary space: O(n)
# Worst case: all Nodes within low -> high range, and they all placed on One subtree.
# So, it will be traverse of BST in style of Linked list and recursion depths of 'n' => O(n).
# ------------------
# Not building reader for testcases, might be later.
# It's just harder than this task, and no time to search for copy from other tasks.
# Actually, need to store useful methods somewhere standalone.
