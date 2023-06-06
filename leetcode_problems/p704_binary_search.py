# Given an array of integers nums which is sorted in ascending order, and an integer target,
# write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.
# --------------------
# 1 <= nums.length <= 10 ** 4  ,  -10 ** 4 < nums[i], target < 10 ** 4
# All the integers in nums are unique.
# nums is sorted in ascending order.
from math import ceil


def binary_search(nums: list[int], target: int) -> int:
    # working_sol (78.77%, 44.44%) -> (240ms, 17.9mb)  time: O(log n) | space: O(1)
    if nums[0] > target:
        return -1
    if nums[-1] < target:
        return -1
    left: int = 0
    right: int = len(nums) - 1
    while left != right:
        middle: int = ceil((left + right) / 2)
        if nums[middle] > target:
            right = middle - 1
        else:
            left = middle
    if nums[left] == target:
        return left
    return -1


# Time complexity: O(log n)
# Auxiliary space: O(1)
# Default binary_search solution without extra check on - (middle == target)


test1 = [-1, 0, 3, 5, 9, 12]
test1_t = 9
test1_out = 4
print(binary_search(test1, test1_t))
assert test1_out == binary_search(test1, test1_t)

test2 = [-1, 0, 3, 5, 9, 12]
test2_t = 2
test2_out = -1
print(binary_search(test2, test2_t))
assert test2_out == binary_search(test2, test2_t)
