# You are given an integer array nums consisting only of 0, 1, and 2.
# A pair of indices (i, j) is called valid if nums[i] == 1 and nums[j] == 2.
# Return the minimum absolute difference between i and j among all valid pairs.
# If no valid pair exists, return -1.
# The absolute difference between indices i and j is defined as abs(i - j).
# --- --- --- ---
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 2
from random import randint
from pyperclip import copy


def min_absolute_difference(nums: list[int]) -> int:
    # working_solution: (100%, 96.72%) -> (0ms, 19.20mb)  Time: O(n) Space: O(1)
    out: int = 1_000
    ind_one: int = -1
    ind_two: int = -1
    for index, value in enumerate(nums):
        if 1 == value:
            ind_one = index
        elif 2 == value:
            ind_two = index
        if -1 != ind_one and -1 != ind_two:
            out = min(out, abs(ind_one - ind_two))

    return out if -1 != ind_one and -1 != ind_two else -1


# Time complexity: O(n)
# n - length of the input array `nums`
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [1, 0, 0, 2, 0, 1]
test_out: int = 2
assert test_out == min_absolute_difference(test)

test = [1, 0, 1, 0]
test_out = -1
assert test_out == min_absolute_difference(test)

test = [randint(0, 2) for _ in range(100)]
copy(test)  # type: ignore
