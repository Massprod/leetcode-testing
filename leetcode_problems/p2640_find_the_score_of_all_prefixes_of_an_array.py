# We define the conversion array conver of an array arr as follows:
#  - conver[i] = arr[i] + max(arr[0..i]) where max(arr[0..i])
#     is the maximum value of arr[j] over 0 <= j <= i.
# We also define the score of an array arr as the sum of the values
#  of the conversion array of arr.
# Given a 0-indexed integer array nums of length n,
#  return an array ans of length n where ans[i] is the score of the prefix nums[0..i].
# ---------------------
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 9
from pyperclip import copy

from random import randint


def find_prefix_score(nums: list[int]) -> list[int]:
    # working_sol: (54.86%, 36.22%) -> (39ms, 42.23mb)  time: O(n) | space: O(n)
    max_prefix: int = nums[0]
    conv_sum: int = nums[0] + max_prefix
    # [ max_value_before + sum of conv_array ]
    out: list[int] = [conv_sum]
    for index in range(1, len(nums)):
        value: int = nums[index]
        max_prefix = max(max_prefix, value)
        conv_sum += value + max_prefix
        out.append(conv_sum)
        
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole input array `nums`, once => O(n).
# ---------------------
# Auxiliary space: O(n)
# `out` <- allocates space for each value from `nums` => O(n).


test: list[int] = [2, 3, 7, 5, 10]
test_out: list[int] = [4, 10, 24, 36, 56]
assert test_out == find_prefix_score(test)

test = [1, 1, 2, 4, 8, 16]
test_out = [2, 4, 8, 16, 32, 64]
assert test_out == find_prefix_score(test)

test = [randint(1, 10 ** 9) for _ in range(10 ** 5)]
copy(test)
