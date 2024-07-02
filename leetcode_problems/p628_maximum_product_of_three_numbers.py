# Given an integer array nums,
#  find three numbers whose product is maximum and return the maximum product.
# -------------------------
# 3 <= nums.length <= 10 ** 4
# -1000 <= nums[i] <= 1000
from random import randint


def maximum_product(nums: list[int]) -> int:
    # working_sol (97.75%, 96.46%) -> (187ms, 17.65mb)  time: O(n) | space: O(1)
    first: int = -1001
    second: int = -1001
    third: int = -1001
    first_negative: int = 0
    second_negative: int = 0
    for num in nums:
        if num >= first:
            second, third = first, second
            first = num
        elif num >= second:
            third = second
            second = num
        elif num >= third:
            third = num
        if num <= first_negative:
            second_negative = first_negative
            first_negative = num
        elif num <= second_negative:
            second_negative = num
    return max(first * second * third, first_negative * second_negative * first)


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing `nums` only once => O(n).
# -------------------------
# Auxiliary space: O(1)
# Only 5 constant INT's used, none of them depends on input => O(1)


test: list[int] = [1, 2, 3]
test_out: int = 6
assert test_out == maximum_product(test)

test = [1, 2, 3, 4]
test_out = 24
assert test_out == maximum_product(test)

test = [-1, -2, -3]
test_out = -6
assert test_out == maximum_product(test)

test = [-1, -2, -3, 4, 5, -10, 0]
test_out = 150
assert test_out == maximum_product(test)

test = [randint(-1000, 1000) for _ in range(10 ** 4)]
print(test)
