# You are given an array of positive integers nums and want to erase a subarray
#  containing unique elements.
# The score you get by erasing the subarray is equal to the sum of its elements.
# Return the maximum score you can get by erasing exactly one subarray.
# An array b is called to be a subarray of a if it forms a contiguous subsequence of a,
#  that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).
# ----------------------------
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 4
from pyperclip import copy

from random import randint

from collections import defaultdict


def maximum_unique_subarray(nums: list[int]) -> int:
    # working_sol (17.60%, 78.00%) -> (327ms, 28.78mb)  time: O(n) | space: O(n)
    # Expand the window until we have all uniques.
    out: int = 0
    run_sum: int = 0
    left: int = 0
    right: int = 0
    # { value: occurrences }
    uniques: dict[int, int] = defaultdict(int)
    while right < len(nums):
        value: int = nums[right]
        run_sum += value
        while 0 < uniques.get(value, 0):
            left_val: int = nums[left]
            run_sum -= left_val
            uniques[left_val] -= 1
            left += 1
        out = max(run_sum, out)
        uniques[value] += 1
        right += 1
    
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# In the worst case every value is a duplicate.
# We're going to use every index of `nums` 2 times => O(2 * n).
# ----------------------------
# Auxiliary space: O(n)
# In the worst case every value is unique.
# `uniques` <- allocates space for each unique value from `nums` => O(n).


test: list[int] = [4, 2, 4, 5, 6]
test_out: int = 17
assert test_out == maximum_unique_subarray(test)

test = [5, 2, 1, 2, 5, 2, 1, 2, 5]
test_out = 8
assert test_out == maximum_unique_subarray(test)

test = [randint(1, 10 ** 4) for _ in range(10 ** 3)]
copy(test) # type: ignore
