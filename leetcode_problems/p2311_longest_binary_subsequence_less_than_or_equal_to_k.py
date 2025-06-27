# You are given a binary string s and a positive integer k.
# Return the length of the longest subsequence of s that makes up
#   a binary number less than or equal to k.
# Note:
#  - The subsequence can contain leading zeroes.
#  - The empty string is considered to be equal to 0.
#  - A subsequence is a string that can be derived from another string
#   by deleting some or no characters without changing the order of the remaining characters.
# -------------------
# 1 <= s.length <= 1000
# s[i] is either '0' or '1'.
# 1 <= k <= 10 ** 9
from random import choice

from pyperclip import copy


def longest_subsequence(s: str, k: int) -> int:
    # working_sol (28.78%, 87.77%) -> (9ms, 17.7mb)  time: O(s) | space: O(s)
    out: int = 0
    cur_val: int = 0
    for position, digit in enumerate(s[::-1]):
        if '1' == digit:
            # 2 ** bit_position => added value of the bit.
            cur_val = cur_val + 2 ** position
            if cur_val <= k:
                out += 1
        else:
            out += 1

    return out


# Time complexity: O(s)
# Always reversing -> converting -> traversing whole input string `s`, once => O(s).
# -------------------
# Auxiliary space: O(s)
# Slice + `enumerate` have elements for each char from `s` => O(s).


test: str = "1001010"
test_k: int = 5
test_out: int = 5
assert test_out == longest_subsequence(test, test_k)

test = "00101001"
test_k = 1
test_out = 6
assert test_out == longest_subsequence(test, test_k)

test = ''.join([
    choice(['0', '1']) for _ in range(1000)
])
copy(test)
