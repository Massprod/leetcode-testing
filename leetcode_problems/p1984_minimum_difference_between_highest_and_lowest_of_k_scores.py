# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student.
# You are also given an integer k.
# Pick the scores of any k students from the array so that the difference between the highest
#  and the lowest of the k scores is minimized.
# Return the minimum possible difference.
# -----------------------
# 1 <= k <= nums.length <= 1000
# 0 <= nums[i] <= 10 ** 5
from random import randint


def minimum_difference(nums: list[int], k: int) -> int:
    # working_sol (92.07%, 47.69%) -> (81ms, 16.73mb)  time: O(n * log n) | space: O(n)
    nums.sort()
    out: int = nums[-1]
    start: int = 0
    end: int = k - 1
    while end < len(nums):
        out = min(
            out, nums[end] - nums[start]
        )
        start += 1
        end += 1
    return out


# Time complexity: O(n * log n) <- n - length of the input array `nums`.
# Always sorting input array `nums`, once => O(n * log n).
# Extra traversing this array, in the worst case using every index => O(n * log n + n).
# -----------------------
# Auxiliary space: O(n)
# `sort` <- takes O(n) by itself => O(n).


test: list[int] = [90]
test_k: int = 1
test_out: int = 0
assert test_out == minimum_difference(test, test_k)

test = [9, 4, 1, 7]
test_k = 2
test_out = 2
assert test_out == minimum_difference(test, test_k)

test = [randint(0, 10 ** 5) for _ in range(1000)]
print(test)
