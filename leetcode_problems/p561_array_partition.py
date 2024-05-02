# Given an integer array nums of 2n integers, group these integers into n pairs
#  (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized.
# Return the maximized sum.
# ---------------------------
# 1 <= n <= 10 ** 4
# nums.length == 2 * n
# -10 ** 4 <= nums[i] <= 10 ** 4
from random import randint


def array_pair_sum(nums: list[int]) -> int:
    # working_sol (57.35%, 34.69%) -> (218ms, 19.94mb)  time: O(n * log n) | space: O(n)
    # We want to get MAX sum of all the min_pairs.
    # The Best strategy is to maximize the HIGHEST values and minimize the LOWEST.
    # So, we can sort in `ascending` and choose minimums and maximums.
    nums_sorted: list[int] = sorted(nums)
    out: int = 0
    for index in range(0, len(nums_sorted) - 1, 2):
        out += min(nums_sorted[index], nums_sorted[index + 1])
    return out


# Time complexity O(n * log n) <- n - length of an input array `nums`.
# Always sorting and using every index of the input array `nums`, once => O(n * log n + n).
# ---------------------------
# Auxiliary space: O(n)
# Standard `sorted()` takes O(n).


test: list[int] = [1, 4, 3, 2]
test_out: int = 4
assert test_out == array_pair_sum(test)

test = [6, 2, 6, 5, 1, 2]
test_out = 9
assert test_out == array_pair_sum(test)

test = [randint(-10 ** 4, 10 ** 4) for _ in range(10 ** 4)]
print(test)
