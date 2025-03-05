# You are given a string s consisting of digits.
# Perform the following operation repeatedly until the string has exactly two digits:
#  - For each pair of consecutive digits in s, starting from the first digit,
#    calculate a new digit as the sum of the two digits modulo 10.
#  - Replace s with the sequence of newly calculated digits,
#     maintaining the order in which they are computed.
# Return true if the final two digits in s are the same; otherwise, return false.
# ---------------------------
# 3 <= s.length <= 100
# s consists of only digits.
from pyperclip import copy

from random import choice

from string import digits


def has_same_digits(s: str) -> bool:
    # working_sol (64.62%, 95.73%) -> (83ms, 17.64mb)  time: O(s ** 2) | space: O(s)
    while 2 < len(s):
        new_s: list[str] = []
        for index in range(1, len(s)):
            new_s.append(
                str((int(s[index]) + int(s[index - 1])) % 10)
            )
        s = ''.join(new_s)

    return s[0] == s[1]


# Time complexity: O(s ** 2)
# We always deplete `s` to 2 digits with series:
#  (s - 1) + (s - 2) + (s - 3) + ... + 2 => O(s ** 2).
# ---------------------------
# Auxiliary space: O(s)
# `new_s` <- allocates space for all chars in `s` => O(s).


test: str = '3902'
test_out: bool = True
assert test_out == has_same_digits(test)

test = '34789'
test_out = False
assert test_out == has_same_digits(test)

test = ''.join([choice(digits) for _ in range(100)])
copy(test)
