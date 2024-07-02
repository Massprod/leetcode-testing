# Given the root of a binary search tree and an integer k,
#  return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.
# ------------------------
# The number of nodes in the tree is in the range [1, 10 ** 4].
# -10 ** 4 <= Node.val <= 10 ** 4
# root is guaranteed to be a valid binary search tree.
# -10 ** 5 <= k <= 10 ** 5


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_target(root: TreeNode, k: int) -> bool:
    # working_sol (70.53%, 46.51%) -> (58ms, 18.31mb)  time: O(n) | space: O(n)
    search: set[int] = set()

    def traverse(node: TreeNode) -> bool:
        if not node:
            return False
        to_find: int = k - node.val
        if to_find in search:
            return True
        search.add(node.val)
        if traverse(node.left):
            return True
        if traverse(node.right):
            return True
        return False

    return traverse(root)


# Time complexity: O(n) <- n - number of Nodes inside the input BST `root`.
# Always traversing the whole `root` BST => O(n).
# ------------------------
# Auxiliary space: O(n)
# Recursion stack is going to be a `n` size in case of `linked_list` style of BST.
# In our case, it's BST, so it should be constructed with ascending order.
# ------------------------
# Don't see how it helps us that we're given BST.
# Because even if we want to find something Higher than current `node.val`,
#  we still need to start searching from every Node possible for correct comparison.
# So, it's either I'm missing something or it's just a scary word in task_name.
