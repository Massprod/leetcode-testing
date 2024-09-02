# Given an array of positive integers nums, return an array answer
#  that consists of the digits of each integer in nums
#  after separating them in the same order they appear in nums.
# To separate the digits of an integer is to get all the digits it has in the same order.
# For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].
# ----------------------
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 10 ** 5
from collections import deque


def separate_digits(nums: list[int]) -> list[int]:
    # working_sol (82.85%, 15.38%) -> (56ms, 17.24mb)  time: O(n * k) | space: O(n * k)
    out: list[int] = []
    cur_number: deque[int] = deque([])
    for number in nums:
        while number:
            digit: int = number % 10
            cur_number.appendleft(digit)
            number //= 10
        while cur_number:
            out.append(
                cur_number.popleft()
            )
    return out


# Time complexity: O(n * k) <- n - length of the input array `nums`, k - average number of digits in numbers
# Always traversing whole input array `nums` to get all the digits => O(n * k).
# Using every digit from number to append it to `out` => O(2 * n * k).
# ----------------------
# Auxiliary space: O(n * k)
# `out` <- allocates space for each digit from `nums` => O(n * k).
# In the worst case, there's only one number in `nums`.
# `cur_number` <- allocates space for each digit from `nums` => O(2 * n * k).


test: list[int] = [13, 25, 83, 77]
test_out: list[int] = [1, 3, 2, 5, 8, 3, 7, 7]
assert test_out == separate_digits(test)

test = [7, 1, 3, 9]
test_out = [7, 1, 3, 9]
assert test_out == separate_digits(test)
