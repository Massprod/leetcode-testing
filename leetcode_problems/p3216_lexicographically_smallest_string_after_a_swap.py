# Given a string s containing only digits,
#  return the lexicographically smallest string
#  that can be obtained after swapping adjacent digits
#  in s with the same parity at most once.
# Digits have the same parity if both are odd or both are even.
# For example, 5 and 9, as well as 2 and 4, have the same parity, while 6 and 9 do not.
# -------------------------
# 2 <= s.length <= 100
# s consists only of digits.
from random import choice
from string import digits

from pyperclip import copy


def get_smallest_string(s: str) -> str:
    # working_sol (100.00%, 75.77%) -> (0ms, 17.74mb)  time: O(s) | space: O(s)
    # Essentially, we only care about swapping two digits.
    # They should be adjacent and left > right.
    # It will 100% give us smaller lexo string.
    string: list[int] = [int(digit) for digit in s]
    for index in range(1, len(string)):
        if ((string[index] < string[index - 1])
            and string[index] % 2 == string[index - 1] % 2):
            string[index], string[index - 1] = string[index - 1], string[index]
            return ''.join([str(digit) for digit in string])
    
    return s


# Time complexity: O(s)
# Always traversing whole input string `s`, twice.
# First to recreate `string`, second to `join` => O(2 * s)
# -------------------------
# Auxiliary space: O(s)
# `string` <- allocates space for each char from `s` => O(s).


test: str = "45320"
test_out: str = "43520"
assert test_out == get_smallest_string(test)

test = "001"
test_out = "001"
assert test_out == get_smallest_string(test)

test = ''.join([choice(digits)for _ in range(100)])
copy(test)
