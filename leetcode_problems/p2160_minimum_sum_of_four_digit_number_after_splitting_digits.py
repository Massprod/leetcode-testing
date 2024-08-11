# You are given a positive integer num consisting of exactly four digits.
# Split num into two new integers new1 and new2 by using the digits found in num.
# Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.
# For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3.
# Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
# Return the minimum possible sum of new1 and new2.
# ----------------------
# 1000 <= num <= 9999


def minimum_sum(num: int) -> int:
    # working_sol (73.12%, 57.97%) -> (32ms, 16.42mb)  time: O(1) | space: O(1)
    digits: list[int] = []
    while num:
        digit: int = num % 10
        num //= 10
        if digit:
            digits.append(digit)
    digits.sort()
    if 2 >= len(digits):
        return sum(digits)
    left: int = 0
    right: int = len(digits) - 1
    new1: str = ''
    new2: str = ''
    new1 += str(digits[left]) + str(digits[right])
    left += 1
    right -= 1
    if left == right:
        new2 += str(digits[left])
    elif left < right:
        new2 += str(digits[left]) + str(digits[right])
    new1_int: int = int(new1) if new1 else 0
    new2_int: int = int(new2) if new2 else 0
    return new1_int + new2_int


# Time complexity: O(1)
# We always have input value with 4 digits, and check the same options => O(1).
# ----------------------
# Auxiliary space: O(1)
# `digits` <- can hold from 1 -> 4 digits => O(1).


test: int = 2932
test_out: int = 52
assert test_out == minimum_sum(test)

test = 4009
test_out = 13
assert test_out == minimum_sum(test)
