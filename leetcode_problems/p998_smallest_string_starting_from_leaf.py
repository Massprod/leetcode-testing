# You are given the root of a binary tree where each node has a value in the range [0, 25]
#  representing the letters 'a' to 'z'.
# Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
# As a reminder, any shorter prefix of a string is lexicographically smaller.
#  - For example, "ab" is lexicographically smaller than "aba".
# A leaf of a node is a node that has no children.
# ----------------------
# The number of nodes in the tree is in the range [1, 8500].
# 0 <= Node.val <= 25


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def smallest_from_leaf(root: TreeNode) -> str:
    # working_sol (99.79%, 17.71%) -> (28ms, 17.90mb)  time: O(n) | space: O(n * k)
    all_paths: list[str] = []

    def dfs(node: TreeNode, path: str) -> None:
        if not node.left and not node.right:
            path = chr(97 + node.val) + path
            all_paths.append(path)
            return
        if node.left:
            dfs(node.left, chr(97 + node.val) + path)
        if node.right:
            dfs(node.right, chr(97 + node.val) + path)

    dfs(root, '')
    return min(all_paths)


# Time complexity: O(n) <- n - number of Nodes inside input BT `root`.
# Always traversing whole BT to get all paths from Root -> Leaf => O(n).
# ----------------------
# Auxiliary space: O(n * k) <- k - depth of the BT `root`.
# Failed to get O(1) backtrack, so we just accumulate all Paths in `all_paths`.
# And every string inside can be a max_depth size or even 2 symbols.
# But in the worst case, they're all same size of depth => O(n * k).
