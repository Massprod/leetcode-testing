# You are given a 0-indexed integer array nums.
# Return the maximum value over all triplets of indices (i, j, k)
#  such that i < j < k.
# If all such triplets have a negative value, return 0.
# The value of a triplet of indices (i, j, k)
#  is equal to (nums[i] - nums[j]) * nums[k].
# ------------------------
# 3 <= nums.length <= 100
# 1 <= nums[i] <= 10 ** 6
from collections import deque

from random import randint

from pyperclip import copy


def maximum_triplet_value(nums: list[int]) -> int:
    # working_sol (83.43%, 21.69%) -> (3ms, 17.99mb)  time: O(n) | space: O(n)
    out: int = 0
    prefixes: list[int] = [0, nums[0]]
    suffixes: deque[int] = deque([nums[-1], 0])
    for index in range(1, len(nums) - 1):
        prefixes.append(
            max(prefixes[-1], nums[index])
        )
    for index in range(len(nums) - 2, 0, -1):
        suffixes.appendleft(
            max(suffixes[0], nums[index])
        )
    for index in range(1, len(nums) - 1):
        out = max(
            out,
            (prefixes[index] - nums[index]) * suffixes[index]
        )

    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole input array `nums`, three times => O(n).
# ------------------------
# Auxiliary space: O(n)
# `prefixes` <- allocates space for each index in `nums` => O(n).
# `suffixes` <- allocates space for each index in `nums` => O(2 * n).


test: list[int] = [12, 6, 1, 2, 7]
test_out: int = 77
assert test_out == maximum_triplet_value(test)

test = [1, 10, 3, 4, 19]
test_out = 133
assert test_out == maximum_triplet_value(test)

test = [1, 2, 3]
test_out = 0
assert test_out == maximum_triplet_value(test)

test = [randint(1, 10 ** 6) for _ in range(100)]
copy(test)
