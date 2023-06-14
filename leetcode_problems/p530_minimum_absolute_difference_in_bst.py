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


def get_minimum_diff(root: TreeNode) -> int | None:
    # working_sol (50.61%, 15.28%) -> (71ms, 18.9mb)  time: O(n * (log n)) | space: O(n)
    if not root:
        return None
    all_values: list[int] = []

    def search_tree(node: TreeNode) -> None:
        all_values.append(node.val)
        if node.left:
            search_tree(node.left)
        if node.right:
            search_tree(node.right)

    search_tree(root)
    all_values.sort()
    min_diff: int | None = None
    for x in range(1, len(all_values)):
        diff: int = abs(all_values[x] - all_values[x - 1])
        if min_diff:
            min_diff = min(diff, min_diff)
            continue
        min_diff = diff
    return min_diff


# Time complexity: O(n * (log n)) -> traversing whole BT once to store all node values from it => O(n) ->
# n - num of nodes in BT^^|  -> sorting this values after => O(n * (log n)) -> traversing sorted all_values
#                            to get minimal difference between values inside => O(n) -> O(n * (log n)).
# Auxiliary space: O(n) -> using recursion for every node in BT, stack will be a size of summ of every node => O(n) ->
#                          -> storing every value from these nodes in a list => O(n) -> O(2n) => O(n).
# ---------------
# Still fine to fail at this rate, because it's a first time dealing with BinaryTress, because I skipped them before.
# But didn't want to break daily_task. Totally need to return and complete all basic BT tasks, which I planned.
# ---------------
# Ok. It's all correct except for finding difference is too slow.
# Which is why I wanted to see 189/189 test_case, one that gives TLE,
# but they don't give it and I assumed that it's None.
# Because of that I was focused on different problem, and didn't see that it's just slow diff_calc.
# Which can be faster just checking values after sorting, because ever value will be checked with their
# most lowest neighbor.
# [5, 3, 2, 1, 4] -> sorted[1, 2, 3, 4, 5] -> every x + 1 is most_lowest check we can find for x.
# ---------------
# Failed first_commit, because didn't understand task correctly, and I was checking
# diff between every 2 connected nodes, which was harder and I made it work...
# Failed second_commit, no idea why, TimeLimit without actual test_case given ->
# -> because the test case is * root = whitespaces *, like what?
# Is that root = None, or what?         ^^ And in constraints we're given -> there will be at least  2 nodes.
# Can't even use this TestCase -> * Failed to parse your input, please check again. * error when adding this.
# ---------------
# Not creating TreeNodes to test, and not using tests in this case.
# Because I know how to search BTS, but if I made creation of BTS it's the same as reading it,
# and I can't do this today (no time). So just reading for now.
