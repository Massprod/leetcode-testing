# Given an integer array nums, return the number of subarrays
#  of length 3 such that the sum of the first and third numbers equals
#  exactly half of the second number.
# -----------------------
# 3 <= nums.length <= 100
# -100 <= nums[i] <= 100
import pyperclip
from random import randint


def count_subarrays(nums: list[int]) -> int:
    # working_sol (100.00%, 100.00%) -> (12ms, 17.85mb)  time: O(n) | space: O(1)
    first: int = nums[0]
    second: int = nums[1]
    third: int = nums[2]
    out: int = 0 if (first + third) != second / 2 else 1
    start_index: int = 3
    while start_index < len(nums):
        first, second = second, third
        third = nums[start_index]
        out += 1 if (first + third) == second / 2 else 0
        start_index += 1
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing every index of `nums`, once => O(n).
# -----------------------
# Auxiliary space: O(1)
# Only 4 constant INTs used, none of them depends on input => O(1).


test: list[int] = [1, 2, 1, 4, 1]
test_out: int = 1
assert test_out == count_subarrays(test)

test = [1, 1, 1]
test_out = 0
assert test_out == count_subarrays(test)

test = [randint(-100, 100) for _ in range(100)]
pyperclip.copy(test)
