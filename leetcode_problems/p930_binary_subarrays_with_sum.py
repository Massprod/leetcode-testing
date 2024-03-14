# Given a binary array nums and an integer goal,
#  return the number of non-empty subarrays with a sum goal.
# A subarray is a contiguous part of the array.
# ----------------------
# 1 <= nums.length <= 3 * 10 ** 4
# nums[i] is either 0 or 1.
# 0 <= goal <= nums.length
from collections import deque


def num_subarray_with_sum(nums: list[int], goal: int) -> int:
    # working_sol (82.80%, 82.06%) -> (214ms, 17.43mb)  time: O(n) | space: O(1)
    left: int = 0
    right: int = 0
    cur_sum: int = 0
    zeroes: int = 0
    out: int = 0
    while right < len(nums):
        cur_sum += nums[right]
        while left < right and (cur_sum > goal or not nums[left]):
            if nums[left]:
                zeroes = 0
            else:
                zeroes += 1
            cur_sum -= nums[left]
            left += 1
        if cur_sum == goal:
            out += 1 + zeroes
        right += 1
    return out


# Time complexity: O(n) <- n - length of input array `nums`.
# Standard SlidingWindow with using every index of the array Twice => O(2n).
# ----------------------
# Auxiliary space: O(1)
# Only constant 5 INTs.


test: list[int] = [1, 0, 1, 0, 1]
test_g: int = 2
test_out: int = 4
assert test_out == num_subarray_with_sum(test, test_g)

test = [0, 0, 0, 0, 0]
test_g = 0
test_out = 15
assert test_out == num_subarray_with_sum(test, test_g)

test = [0, 0, 0, 1, 0]
test_g = 0
test_out = 7
assert test_out == num_subarray_with_sum(test, test_g)
