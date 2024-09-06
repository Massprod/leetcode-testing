# You are given an integer array nums.
# We consider an array good if it is a permutation of an array base[n].
# base[n] = [1, 2, ..., n - 1, n, n] (in other words, it is an array of length n + 1
#  which contains 1 to n - 1 exactly once, plus two occurrences of n).
# For example, base[1] = [1, 1] and base[3] = [1, 2, 3, 3].
# Return true if the given array is good, otherwise return false.
# Note: A permutation of integers represents an arrangement of these numbers.
# --------------------------
# 1 <= nums.length <= 100
# 1 <= num[i] <= 200
from random import randint


def is_good(nums: list[int]) -> bool:
    # working_sol (87.93%, 80.54%) -> (43ms, 16.47mb)  time: O(n * log n) | space: O(n)
    nums.sort()
    # [1, 2, 3 .... n, n]
    if len(nums) != nums[-1] + 1:
        return False
    # Everything in ascending, except for the last 2 elements.
    for index in range(1, len(nums) - 1):
        if nums[index] <= nums[index - 1]:
            return False
    return nums[-1] == nums[-2]


# Time complexity: O(n * log n) <- n - length of the input array `nums`.
# Always sorting original input array `nums`, once => O(n * log n).
# Extra using every index of `nums` => O(n * log n + n).
# --------------------------
# Auxiliary space: O(n)
# `sort` <- takes O(n).


test: list[int] = [2, 1, 3]
test_out: bool = False
assert test_out == is_good(test)

test = [1, 3, 3, 2]
test_out = True
assert test_out == is_good(test)

test = [1, 1]
test_out = True
assert test_out == is_good(test)

test = [3, 4, 4, 1, 2, 1]
test_out = False
assert test_out == is_good(test)

test = [randint(1, 200) for _ in range(100)]
print(test)
