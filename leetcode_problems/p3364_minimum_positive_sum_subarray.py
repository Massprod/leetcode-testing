# You are given an integer array nums and two integers l and r.
# Your task is to find the minimum sum of a subarray whose size is between l and r (inclusive)
#  and whose sum is greater than 0.
# Return the minimum sum of such a subarray. If no such subarray exists, return -1.
# A subarray is a contiguous non-empty sequence of elements within an array.
# ------------------------
# 1 <= nums.length <= 100
# 1 <= l <= r <= nums.length
# -1000 <= nums[i] <= 1000
import pyperclip
from random import randint


def minimum_sum_subarray(nums: list[int], l: int, r: int) -> int:
    # working_sol: (91.29%, 19.85%) -> (18ms, 17.20mb)  time: O(n * n) | space: O(n)
    prefixes: list[int] = [0]
    prefix: int = 0
    for index in range(len(nums) - 1):
        prefix += nums[index]
        prefixes.append(
            prefix
        )
    limit: int = 1001 * 100
    out: int = limit
    # We need to check every subarray of sizes from `l` -> `r`.
    # `-1` <- to get correct end index.
    for size in range(l - 1, r):
        # We can start from any index, but we need to consider index boundaries.
        end_limit: int = len(nums) - size
        for start in range(end_limit):
            end: int = start + size
            sub_sum: int = (nums[end] + prefixes[end]) - prefixes[start]
            if 0 < sub_sum:
                out = min(out, sub_sum)
    return out if out != limit else -1


# Time complexity: O(n * n) <- n - length of the input array `nums`
# In the worst case we're given `r` and `l` which gives us range of size `n`.
# We will check every possible subarray from size 1 -> r - l => O(n * n)
# ------------------------
# Auxiliary space: O(n)
# `prefixes` <- allocates space for each value of `nums` => O(n).


test: list[int] = [3, -2, 1, 4]
test_l: int = 2
test_r: int = 3
test_out: int = 1
assert test_out == minimum_sum_subarray(test, test_l, test_r)

test = [-2, 2, -3, 1]
test_l = 2
test_r = 3
test_out = -1
assert test_out == minimum_sum_subarray(test, test_l, test_r)

test = [7, 3]
test_l = 2
test_r = 2
test_out = 10
assert test_out == minimum_sum_subarray(test, test_l, test_r)

test = [randint(-1000, 1000) for _ in range(100)]
pyperclip.copy(test)
