# Given the array nums, obtain a subsequence of the array whose sum of elements
#  is strictly greater than the sum of the non included elements in such subsequence.
# If there are multiple solutions, return the subsequence with minimum size
#  and if there still exist multiple solutions,
#  return the subsequence with the maximum total sum of all its elements.
# A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array.
# Note that the solution with the given constraints is guaranteed to be unique.
# Also return the answer sorted in non-increasing order.
# ----------------------
# 1 <= nums.length <= 500
# 1 <= nums[i] <= 100
from random import randint


def min_subsequence(nums: list[int]) -> list[int]:
    # working_sol (98.13%, 51.33%) -> (47ms, 16.59mb)  time: O(n * log n) | space: O(n)
    nums.sort(reverse=True)
    all_sum: int = sum(nums)
    cur_seq: int = 0
    out: list[int] = []
    for val in nums:
        cur_seq += val
        all_sum -= val
        out.append(val)
        if cur_seq > all_sum:
            return out

# Time complexity: O(n * log n) <- n - length of the input array `nums`.
# Always sorting `nums`, once => O(n * log n).
# Extra traversing it to get the correct sequence, with sum() before it => O(2 * n + n * log n).
# ----------------------
# Auxiliary space: O(n)
# `out` <- will contain some part of the `n` => O(n).


test: list[int] = [4, 3, 10, 9, 8]
test_out: list[int] = [10, 9]
assert test_out == min_subsequence(test)

test = [4, 4, 7, 6, 7]
test_out = [7, 7, 6]
assert test_out == min_subsequence(test)

test = [randint(1, 100) for _ in range(500)]
print(test)
