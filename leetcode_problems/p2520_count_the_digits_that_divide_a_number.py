# Given an integer num, return the number of digits in num that divide num.
# An integer val divides nums if nums % val == 0.
# ---------------
# 1 <= num <= 10 ** 9
# num does not contain 0 as one of its digits.


def count_digits(num: int) -> int:
    # working_sol (82.99%, 97.52%) -> (30ms, 16.40mb)  time: O(n) | space: O(n)
    out: int = 0
    for digit in str(num):
        if not num % int(digit):
            out += 1
    return out


# Time complexity: O(n) <- n - # of digits in `num`.
# Converting and traversing every digit in `num` => O(n).
# ---------------
# Auxiliary space: O(n).
# `str(num)` <- will always be of the size `n` => O(n).


test: int = 7
test_out: int = 1
assert test_out == count_digits(test)

test = 121
test_out = 2
assert test_out == count_digits(test)

test = 1248
test_out = 4
assert test_out == count_digits(test)
