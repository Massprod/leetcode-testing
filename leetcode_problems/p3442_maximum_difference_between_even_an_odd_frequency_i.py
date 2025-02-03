# You are given a string s consisting of lowercase English letters.
# Your task is to find the maximum difference between the frequency
#  of two characters in the string such that:
#  - One of the characters has an even frequency in the string.
#  - The other character has an odd frequency in the string.
# Return the maximum difference, calculated as the frequency
#  of the character with an odd frequency minus the frequency
#  of the character with an even frequency.
# ---------------------
# 3 <= s.length <= 100
# s consists only of lowercase English letters.
# s contains at least one character with an odd frequency and one with an even frequency.
from pyperclip import copy

from random import choice
from string import ascii_lowercase

from collections import defaultdict


def max_difference(s: str) -> int:
    # working_sol (100.00%, 100.00%) -> (4ms, 17.90mb)  time: O(s) | space: O(s)
    # { char: occurrences }
    chars: dict[str, int] = defaultdict(int)
    for char in s:
        chars[char] += 1
    # We need maximum `odd` frequency and minimum `even` frequency.
    max_odd: int = 0
    min_even: int = 100  # ! 3 <= s.length <= 100 !
    for char, frequency in chars.items():
        if frequency % 2:
            max_odd = max(max_odd, frequency)
        else:
            min_even = min(min_even, frequency)
    return max_odd - min_even


# Time complexity: O(s)
# In the worst case every char occurs only once.
# We will traverse whole input string `s`, twice => O(2 * s).
# ---------------------
# Auxiliary space: O(s)
# `chars` <- allocates space for each unique char from `s` => O(s).


test: str = 'aaaaabbc'
test_out: int = 3
assert test_out == max_difference(test)

test = 'abcabcab'
test_out = 1
assert test_out == max_difference(test)

test = ''.join([choice(ascii_lowercase) for _ in range(100)])
copy(test)
