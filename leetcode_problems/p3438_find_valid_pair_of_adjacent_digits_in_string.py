# You are given a string s consisting only of digits.
# A valid pair is defined as two adjacent digits in s such that:
#  - The first digit is not equal to the second.
#  - Each digit in the pair appears in s exactly as many times as its numeric value.
# Return the first valid pair found in the string s when traversing from left to right.
# If no valid pair exists, return an empty string.
# ----------------------
# 2 <= s.length <= 100
# s only consists of digits from '1' to '9'.
from random import randint

from pyperclip import copy

from collections import defaultdict


def find_valid_pair(s: str) -> str:
    # working_sol (100.00%, 100.00%) -> (1ms, 17.58mb)  time: O(s) | space: O(s)
    val1: str
    val2: str

    # { char: occurs }
    chars: dict[str, int] = defaultdict(int)
    for char in s:
        chars[char] += 1
    for index in range(1, len(s)):
        val1, val2 = s[index - 1], s[index]
        if (val1 != val2
             and chars[val1] == int(val1)
             and chars[val2] == int(val2)):
            
            return f'{val1}{val2}'
        
    return ''


# Time complexity: O(s)
# Always traversing whole input string `s`, twice => O(2 * s).
# ----------------------
# Auxiliary space: O(s).
# In the worst case, there's only unique digits in `s`.
# `chars` <- allocates space for each unique digit in `s` => O(s).


test: str = '2523533'
test_out: str = '23'
assert test_out == find_valid_pair(test)

test = '221'
test_out = '21'
assert test_out == find_valid_pair(test)

test = '22'
test_out = ''
assert test_out == find_valid_pair(test)

test = ''.join([str(randint(1, 9)) for _ in range(100)])
copy(test)
