# You are given an integer array nums with no duplicates.
# A maximum binary tree can be built recursively from nums using the following algorithm:
#  1. Create a root node whose value is the maximum value in nums.
#  2. Recursively build the left subtree on the subarray prefix to the left of the maximum value.
#  3. Recursively build the right subtree on the subarray suffix to the right of the maximum value.
# Return the maximum binary tree built from nums.
# ----------------------
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
# All integers in nums are unique.
from utils.binary_tree import TreeNode


def construct_maximum_bt(nums: list[int]) -> TreeNode | None:
    # working_sol (54.08%, 69.26%) -> (136ms, 17.01mb)  time: O(n * n) | space: O(n)
    if not nums:
        return None
    max_val: int = max(nums)
    slice_point: int = nums.index(max_val)
    left_subarray: list[int] = nums[:slice_point]
    right_subarray: list[int] = nums[slice_point + 1:]
    node: TreeNode = TreeNode(max_val)
    node.left = construct_maximum_bt(left_subarray)
    node.right = construct_maximum_bt(right_subarray)
    return node


# Time complexity: O(n * n) <- n - length of the input array `nums`.
# Always slicing `nums` until we check every index, and for each index we check all slice values to get max => O(n * n).
# ----------------------
# Auxiliary space: O(n)
# We will have recursion with depths `n` => O(n).
