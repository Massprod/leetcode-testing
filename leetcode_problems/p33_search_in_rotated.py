# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown
#  pivot index == k (1 <= k < nums.length) such that the resulting array is
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.
# --------------------------
# 1 <= nums.length <= 5000
# -10 ** 4 <= nums[i] <= 10 ** 4
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -10 ** 4 <= target <= 10 ** 4
from random import randint


def search_rotated(nums: list[int], target: int) -> int:
    # working_sol (77.24%, 79.58%) -> (44ms, 16.6mb)  time: O(log n) | space: O(1)
    if not nums:
        return -1
    left: int = 0
    right: int = len(nums) - 1
    while left < right:
        middle: int = (left + right) // 2 + 1
        # Ascending slice: left -> middle.
        if nums[left] <= nums[middle]:
            # Target inside this slice.
            if nums[left] <= target < nums[middle]:
                right = middle - 1
            else:
                left = middle
        # Middle in pivoted part.
        else:
            # Ascending slice with target in pivoted part: middle -> right.
            if nums[middle] <= target <= nums[right]:
                left = middle
            else:
                right = middle - 1
    if nums[left] == target:
        return left
    return -1


# Time complexity: O(log n) <- n - length of input array 'nums'.
# Standard BinarySearch algorithm.
# --------------------------
# Auxiliary space: O(1).
# Only 2 extra constant INTs used.


test: list[int] = [4, 5, 6, 7, 0, 1, 2]
test_target: int = 0
test_out: int = 4
assert search_rotated(test, test_target) == test_out

test = [1]
test_target = 1
test_out = 0
assert search_rotated(test, test_target) == test_out

test = []
test_target = 5
test_out = -1
assert search_rotated(test, test_target) == test_out

test = [1, 2, 3, 4, 5, 6, 7]
test_target = 4
test_out = 3
assert search_rotated(test, test_target) == test_out

test = [4, 5, 6, 7, 0, 1, 2]
test_target = 0
test_out = 4
assert search_rotated(test, test_target) == test_out

test = sorted(set([randint(-10 ** 4, 10 ** 4) for _ in range(5000)]))
pivot_point: int = randint(0, len(test) - 1)
print(test[pivot_point], 'pivoted at:', pivot_point)
test = test[pivot_point:] + test[:pivot_point]
print(test)
