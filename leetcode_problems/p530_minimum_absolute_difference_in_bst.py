# Given the root of a Binary Search Tree (BST),
#   return the minimum absolute difference between the values of any two different nodes in the tree.
# --------------------
# The number of nodes in the tree is in the range [2, 10 ** 4].
# 0 <= Node.val <= 10 ** 5


class TreeNode:

    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_minimum_diff(root: TreeNode) -> int:
    if not root:
        return root
    all_values: list[int] = []

    def search_tree(node: TreeNode) -> None:
        all_values.append(node.val)
        if node.left:
            search_tree(node.left)
        if node.right:
            search_tree(node.right)

    search_tree(root)
    min_diff: int | None = None
    for x in range(len(all_values) - 1):
        for y in range(x + 1, len(all_values)):
            diff: int = abs(all_values[x] - all_values[y])
            if min_diff:
                min_diff = min(diff, min_diff)
                continue
            min_diff = diff
    return min_diff


# Failed first_commit, because didn't understand task correctly, and I was checking
# diff between every 2 connected nodes, which was harder and I made it work...
# Failed second_commit, no idea why, TimeLimit without actual test_case given ->
# -> because the test case is * root = whitespaces *, like what?
# Is that root = None, or what?         ^^ And in constraints we're given -> there will be at least  2 nodes.
# Can't even use this TestCase -> * Failed to parse your input, please check again. * error when adding this.
# ---------------
# Not creating TreeNodes to test, and not using tests in this case.
# Because I know how to search BTS, but if I made creation of BTS it's the same as reading it,
# and I can't do this today. So just reading for now.
