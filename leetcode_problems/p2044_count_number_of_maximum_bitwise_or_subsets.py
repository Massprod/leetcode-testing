# Given an integer array nums, find the maximum possible bitwise OR of a subset of nums
#  and return the number of different non-empty subsets with the maximum bitwise OR.
# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero)
#  elements of b.
# Two subsets are considered different if the indices of the elements chosen are different.
# The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).
# ---------------------------
# 1 <= nums.length <= 16
# 1 <= nums[i] <= 10 ** 5
from random import randint
from functools import cache


def count_max_or_subsets(nums: list[int]) -> int:
    # working_sol (100%, 22.25%) -> (16ms, 17.77mb)  time: O(2 ** n) | space: O(2 ** n)
    max_pos_or: int = 0
    for num in nums:
        max_pos_or |= num

    @cache
    def check(index: int, current_or: int) -> int:
        nonlocal max_pos_or
        # Check every path and count paths leading to correct `or`.
        if index == len(nums):
            return 1 if current_or == max_pos_or else 0
        use_index: int = check(
            index + 1, current_or | nums[index]
        )
        skip_index: int = check(
            index + 1, current_or
        )
        return use_index + skip_index

    return check(0, 0)


# Time complexity: O(2 ** n) <- n - length of the input array `nums`.
# Tree with 2 options and depths of `n` => O(2 ** n).
# ---------------------------
# Auxiliary space: O(2 ** n)
# Using `cache` to store all call options for every `2 ** n` call => O(2 ** n).


test: list[int] = [3, 1]
test_out: int = 2
assert test_out == count_max_or_subsets(test)

test = [2, 2, 2]
test_out = 7
assert test_out == count_max_or_subsets(test)

test = [3, 2, 1, 5]
test_out = 6
assert test_out == count_max_or_subsets(test)

test = [randint(1, 10 ** 5) for _ in range(16)]
print(test)
