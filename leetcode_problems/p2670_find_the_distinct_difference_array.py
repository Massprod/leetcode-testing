# You are given a 0-indexed array nums of length n.
# The distinct difference array of nums is an array diff of length n
#  such that diff[i] is equal to the number of distinct elements in the
#  suffix nums[i + 1, ..., n - 1] subtracted from the number of distinct elements
#  in the prefix nums[0, ..., i].
# Return the distinct difference array of nums.
# Note that nums[i, ..., j] denotes the subarray of nums starting at index i
#  and ending at index j inclusive.
# Particularly, if i > j then nums[i, ..., j] denotes an empty subarray.
# -------------------------
# 1 <= n == nums.length <= 50
# 1 <= nums[i] <= 50
from random import randint

from pyperclip import copy


def distinct_difference_array(nums: list[int]) -> list[int]:
    # working_sol (78.04%, 42.61%) -> (11ms, 17.85mb)  time: O(n) | space: O(n)
    distincts: set[int] = set()
    # prefix inclusive
    prefixes: list[int] = [0 for _ in range(len(nums))]
    for index in range(len(nums)):
        distincts.add(nums[index])
        prefixes[index] = len(distincts)
    # suffix !inclusive
    # We need to start from the second_last => include last by default.
    distincts = {nums[-1]}
    suffixes: list[int] = [0 for _ in range(len(nums))]
    for index in range(len(nums) - 2, -1, -1):
        suffixes[index] = len(distincts)
        distincts.add(nums[index])
    out: list[int] = [
        prefixes[index] - suffixes[index] for index in range(len(nums))
    ]
    return out


# Time complexity: O(n) <- n - length of the input array `nums`
# Traversing whole input array `nums`, three times => O(3 * n).
# -------------------------
# Auxiliary space: O(n)
# In the worst case there's only unique values in `nums`.
# `distincts` <- allocates space for each unique value from `nums` => O(n).
# `suffixes` & `prefixes` <- allocates space for each value in `nums` => O(3 * n).


test: list[int] = [1, 2, 3, 4, 5]
test_out: list[int] = [-3, -1, 1, 3, 5]
assert test_out == distinct_difference_array(test)

test = [3, 2, 3, 4, 2]
test_out = [-2, -1, 0, 2, 3]
assert test_out == distinct_difference_array(test)

test = [randint(1, 50) for _ in range(50)]
copy(test)
