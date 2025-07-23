# You are given a positive integer n.
# Each digit of n has a sign according to the following rules:
#  - The most significant digit is assigned a positive sign.
#  - Each other digit has an opposite sign to its adjacent digits.
# Return the sum of all digits with their corresponding sign.
# -----------------------
# 1 <= n <= 10 ** 9
from random import randint

from pyperclip import copy


def alternate_digit_sum(n: int) -> int:
    # working_sol (100.00%, 32.70%) -> (0ms, 17.84mb)  time: O(n) | space: O(n)
    digits: list[int] = []
    while n:
        digit: int = n % 10
        n //= 10
        digits.append(digit)
    
    out: int = 0
    sign: int = 1
    for index in range(len(digits) - 1, -1, -1):
        out += digits[index] * sign
        sign *= -1
    
    return out


# Time complexity: O(n)
# Always taking and traversing every digit of the input value `n` => O(n).
# -----------------------
# Auxiliary space: O(n)
# `digits` <- allocates space for each digit of the input value `n` => O(n).


test: int = 521
test_out: int = 4
assert test_out == alternate_digit_sum(test)

test = 111
test_out = 1
assert test_out == alternate_digit_sum(test)

test = 886996
test_out = 0
assert test_out == alternate_digit_sum(test)

test = randint(1, 10 ** 9)
copy(test)  # type: ignore
