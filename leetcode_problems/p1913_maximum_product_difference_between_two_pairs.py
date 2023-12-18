# The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).
# For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
# Given an integer array nums, choose four distinct indices w, x, y, and z
#  such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.
# Return the maximum such product difference.
# ------------------
# 4 <= nums.length <= 10 ** 4
# 1 <= nums[i] <= 10 ** 4
from random import randint


def max_product_diff(nums: list[int]) -> int:
    # working_sol (93.96%, 71.41%) -> (146ms, 17.64mb)  time: O(n) | space: O(1)
    # Lowest + second_lowest => minimum product we can have.
    # Highest + second_highest => highest product we can have.
    # And we need maximum diff => maximum_product - minimum_product
    highest: int = 1
    second_highest: int = 1
    lowest: int = 10 ** 4
    second_lowest: int = 10 ** 4
    for num in nums:
        if num >= second_highest:
            if num >= highest:
                highest, second_highest = num, highest
            else:
                second_highest = num
        if num <= second_lowest:
            if num <= lowest:
                lowest, second_lowest = num, lowest
            else:
                second_lowest = num
    return highest * second_highest - lowest * second_lowest


# Time complexity: O(n) <- n - length of input array `nums`.
# Single traverse of original input array `nums`.
# Auxiliary space: O(1).
# Only constant INTs used, none of them depends on input.


test: list[int] = [5, 6, 2, 7, 4]
test_out: int = 34
assert test_out == max_product_diff(test)

test = [4, 2, 5, 9, 7, 4, 8]
test_out = 64
assert test_out == max_product_diff(test)

test = [randint(1, 10 ** 4) for _ in range(10 ** 4)]
print(test)
