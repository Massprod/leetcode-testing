# You are given the root of a binary tree containing digits from 0 to 9 only.
# Each root-to-leaf path in the tree represents a number.
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers.
# Test cases are generated so that the answer will fit in a 32-bit integer.
# A leaf node is a node with no children.
# ------------------------
# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 9
# The depth of the tree will not exceed 10.


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_numbers(root: TreeNode) -> int:
    # working_sol (66.35%, 48.89) -> (46ms, 16.4mb)  time: O(n) | space: O(n)
    paths_sum: list[int] = [0]

    def inorder(node: TreeNode, path: str) -> None:
        if node.left is None and node.right is None:
            paths_sum[0] += int(path)
        if node.left:
            inorder(node.left, path + str(node.left.val))
        if node.right:
            inorder(node.right, path + str(node.right.val))

    inorder(root, str(root.val))
    return paths_sum[0]


# Time complexity: O(n) -> standard in-order traversal with recorded path, once => O(n).
# n - nodes of input_BT^^|
# Auxiliary space: O(n) -> in the worst case imbalanced tree with only left_subtree from root, like linked list ->
#                          -> in that case recursion stack will be of n size => O(n).
# ------------------------
# Read in w.e order, but record every Node in the path. If we hit leaf record whole path as STRING.
# After just, convert string into INT and calc.
# Should be correct.
# Or we can ignore storing them, cuz we only need to summarize them anyway.
# ------------------------
# Not building test cases, cuz they give us order-level, and it's like extra task to bother.
