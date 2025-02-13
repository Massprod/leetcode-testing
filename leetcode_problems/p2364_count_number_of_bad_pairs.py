# You are given a 0-indexed integer array nums.
# A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].
# Return the total number of bad pairs in nums.
# -------------------------
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 9
from collections import defaultdict

from random import randint

from pyperclip import copy


def count_bad_pairs(nums: list[int]) -> int:
    # working_sol (42.38%, 59.29%) -> (91ms, 38.82mb)  time: O(n) | space: O(n)
    # (j - i != nums[j] - num[i]) == (num[i] - i != nums[j] - j)
    # Essentially we just need to check number of `num[i] - i `
    #  for every `j` index we check == correct pairs.
    # We can then subtract the correct pairs from all pairs
    #  to get the bad pairs.
    all_pairs: int = len(nums) * (len(nums) - 1) // 2
    correct: int = 0
    # { num[i] - i: occurrences }
    i_pairs: dict[int, int] = defaultdict(int)
    for index, value in enumerate(nums):
        expr: int = value - index
        correct += i_pairs[expr]
        i_pairs[expr] += 1
    
    return all_pairs - correct


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole input array `nums`, once => O(n).
# -------------------------
# Auxiliary space: O(n)
# In the worst case every `expr` is unique, so we store all of them.
# `all_pairs` <- allocates space for each unique `expr` => O(n).


test: list[int] = [4, 1, 3, 3]
test_out: int = 5
assert test_out == count_bad_pairs(test)

test = [1, 2, 3, 4, 5]
test_out = 0
assert test_out == count_bad_pairs(test)

test = [randint(1, 10 ** 9) for _ in range(10 ** 5)]
copy(test)
