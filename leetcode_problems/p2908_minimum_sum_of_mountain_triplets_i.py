# You are given a 0-indexed array nums of integers.
# A triplet of indices (i, j, k) is a mountain if:
#  - i < j < k
#  - nums[i] < nums[j] and nums[k] < nums[j]
# Return the minimum possible sum of a mountain triplet of nums.
#  If no such triplet exists, return -1
# ------------------------
# 3 <= nums.length <= 50
# 1 <= nums[i] <= 50
from collections import deque

from random import randint

from pyperclip import copy


def minimum_sum(nums: list[int]) -> int:
    # working_sol (100.00%, 36.89%) -> (33ms, 17.80mb)  time: O(n) | space: O(n)
    out: int = -1
    min_prefix: list[int] = [0, nums[0]]
    min_suffix: deque[int] = deque([nums[-1], 0])
    for index in range(1, len(nums) - 2):
        min_prefix.append(
            min(min_prefix[-1], nums[index])
        )
    for index in range(len(nums) - 2, 0, -1):
        min_suffix.appendleft(
            min(min_suffix[0], nums[index])
        )
    for index in range(1, len(nums) - 1):
        if min_prefix[index] < nums[index] > min_suffix[index]:
            if -1 == out:
                out = min_prefix[index] + nums[index] + min_suffix[index]
            else:
                out = min(
                    out,
                    min_prefix[index] + nums[index] + min_suffix[index]
                )
    
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing input array 3 times.
# Build prefixes, suffixes and calc mountain => O(3 * n).
# ------------------------
# Auxiliary space: O(n)
# `min_prefix` <- allocates space for (n - 1) indexes of `nums` => O(n - 1).
# `min_suffix` <- allocates spacpe for (n - 1) indexes of `nums` => O(n - 1).


test: list[int] = [8, 6, 1, 5, 3]
test_out: int = 9
assert test_out == minimum_sum(test)

test = [5, 4, 8, 7, 10, 2]
test_out = 13
assert test_out == minimum_sum(test)

test = [6, 5, 4, 3, 4, 5]
test_out = -1
assert test_out == minimum_sum(test)

test = [randint(1, 50) for _ in range(50)]
copy(test)
