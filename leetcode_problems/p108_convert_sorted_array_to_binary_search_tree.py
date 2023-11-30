# Given an integer array nums where the elements are sorted in ascending order,
#  convert it to a  height-balanced binary search tree.
# -------------------
# 1 <= nums.length <= 10 ** 4
# -10 ** 4 <= nums[i] <= 10 ** 4
# nums is sorted in a strictly increasing order.
from collections import deque


class TreeNode:

    def __init__(self, val: int = 0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


def show_tree_level_order(root: TreeNode) -> list[int | None]:
    if not root:
        return []
    show_tree: list[int | None] = []
    que: deque[TreeNode, None] = deque([root])
    # any() because we don't care about Last level empty childs.
    # Either we delete them after we add, or any() will break when only None left.
    while any(que):
        current_node: TreeNode = que.popleft()
        # Empty child.
        if not current_node:
            show_tree.append(None)
            continue
        show_tree.append(current_node.val)
        que.append(current_node.left)
        que.append(current_node.right)
    return show_tree


def sorted_array_to_bst(nums: list[int]) -> TreeNode | None:
    # working_sol (88.54%, 61.66%) -> (56ms, 17.9mb)  time: O(n * log n) | space: O(n)
    if len(nums) == 0:
        return None
    # ! convert it to a  height-balanced binary search tree !
    # We need to use same number of nodes for each subtree.
    mid: int = len(nums) // 2
    root: TreeNode = TreeNode(val=nums[mid])
    # 'nums' already in not_decreasing order.
    # So, everything before is correctly placed for BST -> lower than root.val.
    left_subtree: list[int] = nums[:mid]
    # Same goes for higher subtree.
    right_subtree: list[int] = nums[mid + 1:]
    root.left = sorted_array_to_bst(left_subtree)
    root.right = sorted_array_to_bst(right_subtree)
    return root


# Time complexity: O(n * log n) -> recursion will be called for every value in 'nums' to create 'root' from it and
# n - len of input array 'nums'^^| extra to this we will always slice for 2 parts without 'mid' => O(n * (2 * log n)).
# Auxiliary space: O(n) -> creating new TreeNode for every index in nums => O(n) ->
#                        -> in the worst case with unbalanced trees recursion stack can be size of n, when
#                        every node is in one subtree, but in this case we're always taking middle as a ROOT,
#                        so recursion stack will be only part of the input_nums => O(log n) -> O(n) + O(log n) => O(n).
# -------------------
# Same approach as before, just use middle as a root.
# Because in_order traversal always returns sorted in ascending order array, for correct BT.
# And if we take middle it should be height-balanced, cuz we're not going to overuse any of the sides(subtrees).


test: list[int] = [-10, -3, 0, 5, 9]
test_out: list[int, None] = [0, -3, 9, -10, None, 5]
test_bt: TreeNode = sorted_array_to_bst(test)
assert test_out == show_tree_level_order(test_bt)

test = [1, 3]
test_out = [3, 1]
test_bt = sorted_array_to_bst(test)
assert test_out == show_tree_level_order(test_bt)
