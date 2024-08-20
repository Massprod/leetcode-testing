# An integer divisible by the sum of its digits is said to be a Harshad number.
# You are given an integer x.
# Return the sum of the digits of x if x is a Harshad number,
#  otherwise, return -1.
# -------------------
# 1 <= x <= 100


def sum_of_the_digits_of_harshad_number(x: int) -> int:
    # working_sol (86.61%, 73.21%) -> (29ms, 16.42mb)  time: O(x) | space: O(1)
    num: int = x
    out: int = 0
    while num:
        out += num % 10
        num //= 10
    if not x % out:
        return out
    return -1


# Time complexity: O(x)
# Always depleting all digits of `x` => O(x).
# -------------------
# Auxiliary space: O(1)
# Only 2 constant INTs used => O(1).


test: int = 18
test_out: int = 9
assert test_out == sum_of_the_digits_of_harshad_number(test)

test = 23
test_out = -1
assert test_out == sum_of_the_digits_of_harshad_number(test)
