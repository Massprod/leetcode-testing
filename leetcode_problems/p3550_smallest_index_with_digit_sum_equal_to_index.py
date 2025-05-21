# You are given an integer array nums.
# Return the smallest index i such that the sum of the digits of nums[i] is equal to i.
# If no such index exists, return -1.
# ----------------------
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000
from random import randint

from pyperclip import copy


def smallest_index(nums: list[int]) -> int:
    # working_sol (100.00%, 87.10%) -> (0ms, 17.70mb)  time: O(n * k) | space: O(1)
    def sum_digits(value: int) -> int:
        digit_sum: int = 0
        while value:
            digit_sum += value % 10
            value //=10

        return digit_sum
    

    for index, num in enumerate(nums):
        if index == sum_digits(num):
            return index

    return -1


# Time complexity: O(n * k) <- n - length of the input array `nums`,
#                              k - average # of digits in values of the `nums`.
# Always traversing and count all the digits of value in `nums`, once => O(n * k).
# ----------------------
# Auxiliary space: O(1)
# Nothing extra is used, we ignore `enumerate`.


test: list[int] = [1, 3, 2]
test_out: int = 2
assert test_out == smallest_index(test)

test = [1, 10, 11]
test_out = 1
assert test_out == smallest_index(test)

test = [1, 2, 3]
test_out = -1
assert test_out == smallest_index(test)

test = [randint(0, 1000) for _ in range(100)]
copy(test)
