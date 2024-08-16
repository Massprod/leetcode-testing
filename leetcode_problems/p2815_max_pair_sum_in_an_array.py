# You are given an integer array nums.
# You have to find the maximum sum of a pair of numbers from nums
#  such that the largest digit in both numbers is equal.
# For example, 2373 is made up of three distinct digits: 2, 3, and 7, where 7 is the largest among them.
# Return the maximum sum or -1 if no such pair exists.
# ---------------------
# 2 <= nums.length <= 100
# 1 <= nums[i] <= 10 ** 4
from random import randint


def max_sum(nums: list[int]) -> int:
    # working_sol (60.77%, 56.92%) -> (112ms, 16.56mb)  time: O(n) | space: O(1)
    digits: dict[int, list[int]] = {val: [0, 0] for val in range(10)}
    for num in nums:
        largest_digit: int = 0
        tempo: int = num
        while tempo:
            largest_digit = max(largest_digit, tempo % 10)
            tempo //= 10
        pair: list[int] = digits[largest_digit]
        if not any(pair):
            pair[0] = num
        elif pair[0] and not pair[1]:
            if num > pair[0]:
                pair[1] = num
            else:
                pair[0], pair[1] = num, pair[0]
        else:
            if num >= pair[1]:
                pair[1], pair[0] = num, pair[1]
            elif num > pair[0]:
                pair[0] = num
    out: int = -1
    for digit, pair in digits.items():
        if all(pair):
            out = max(out, sum(pair))
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole input array `nums`, once => O(n).
# Extra traversing every pair in `digits` to count a maximum sum.
# There are 0 -> 9 digits and 10 * 2 pairs we always use => O(n).
# ---------------------
# Auxiliary space: O(1)
# `digits` <- always of the same size.


test: list[int] = [112, 131, 411]
test_out: int = -1
assert test_out == max_sum(test)

test = [2536, 1613, 3366, 162]
test_out = 5902
assert test_out == max_sum(test)

test = [51, 71, 17, 24, 42]
test_out = 88
assert test_out == max_sum(test)

test = [randint(1, 10 ** 4) for _ in range(100)]
print(test)
