# You are given an integer array nums that represents a circular array.
# Your task is to create a new array result of the same size, following these rules:
# For each index i (where 0 <= i < nums.length), perform the following independent actions:
#  - If nums[i] > 0: Start at index i and move nums[i] steps to the right in the circular array.
#    Set result[i] to the value of the index where you land.
#  - If nums[i] < 0: Start at index i and move abs(nums[i]) steps to the left in the circular array.
#    Set result[i] to the value of the index where you land.
#  - If nums[i] == 0: Set result[i] to nums[i].
# Return the new array result.
# Note: Since nums is circular, moving past the last element wraps around to the beginning,
#  and moving before the first element wraps back to the end.
# ---------------------------
# 1 <= nums.length <= 100
# -100 <= nums[i] <= 100
import pyperclip
from random import randint


def construct_transformed_array(nums: list[int]) -> list[int]:
    # working_sol: (76.64%, 80.66%) -> (50ms, 17.29mb)  time: O(n) : space: O(n)
    # We can have values more than len(nums) => just slice it by full circles.
    out: list[int] = []
    for index, value in enumerate(nums):
        if 0 < value:
            out.append(nums[(index + value) % len(nums)])
        elif 0 > value:
            out.append(nums[(index - abs(value)) % len(nums)])
        else:
            out.append(value)
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole input array `nums`, once => O(n).
# ---------------------------
# Auxiliary space: O(n).
# `out` <- allocates space for each values from `nums` => O(n).


test: list[int] = [3, -2, 1, 1]
test_out: list[int] = [1, 1, 1, 3]
assert test_out == construct_transformed_array(test)

test = [-1, 4, -1]
test_out = [-1, -1, 4]
assert test_out == construct_transformed_array(test)

test = [randint(-100, 100) for _ in range(100)]
pyperclip.copy(test)
