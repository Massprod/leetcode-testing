# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a  height-balanced binary search tree.
# -------------------
# 1 <= nums.length <= 10 ** 4
# -10 ** 4 <= nums[i] <= 10 ** 4
# nums is sorted in a strictly increasing order.
from collections import deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def show_tree_level_order(root: TreeNode) -> list[int | None]:
    if not root:
        return []
    show_tree: list[int | None] = []
    que: deque = deque()
    que.appendleft(root)
    # if there's only None left, then it's last level, and we have nothing to check
    # any() <- checks everything in iterable and if there's no elements we break.
    # any() used to eliminate extra level with nulls, when que is empty,
    #       and still store Nulls for other levels.
    while any(que):
        current_node: TreeNode = que.popleft()
        if current_node is None:
            show_tree.append(None)
            continue
        show_tree.append(current_node.val)
        que.append(current_node.left)
        que.append(current_node.right)

    return show_tree


def sorted_array_to_bst(nums: list[int]) -> TreeNode | None:
    # working_sol (37.25%, 89.18%) -> (79ms, 17.9mb)  time: O(n) | space: O(n)
    if len(nums) == 0:
        return None
    mid: int = len(nums) // 2
    root: TreeNode = TreeNode(val=nums[mid])
    left_subtree: list[int] = nums[:mid]
    right_subtree: list[int] = nums[mid + 1:]
    root.left = sorted_array_to_bst(left_subtree)
    root.right = sorted_array_to_bst(right_subtree)
    return root


# Time complexity: O(n) -> over all, recursion will be called only once for every index in nums => O(n).
# n - len of input_nums^^|
# Auxiliary space: O(n) -> creating new TreeNode for every index in nums => O(n) ->
#                        -> in the worst case with unbalanced trees recursion stack can be size of n, when
#                        every node is in one subtree, but in this case we're always taking middle as a ROOT,
#                        so recursion stack will be only part of the input_nums => O(log n) -> O(n) + O(log n) => O(n).
# -------------------
# Same approach as before, just use middle as a root.
# Because in_order traversal always returns sorted in ascending order array, for correct BT.
# And if we take middle it should be height-balanced, cuz we're not going to overuse any of the sides(subtrees).


test1 = [-10, -3, 0, 5, 9]
test1_out = [0, -3, 9, -10, None, 5]
test = sorted_array_to_bst(test1)
print(show_tree_level_order(test))
assert test1_out == show_tree_level_order(test)
del test

test2 = [1, 3]
test2_out = [3, 1]
test = sorted_array_to_bst(test2)
print(show_tree_level_order(test))
assert test2_out == show_tree_level_order(test)
del test
