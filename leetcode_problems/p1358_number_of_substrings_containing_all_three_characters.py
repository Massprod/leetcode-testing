# Given a string s consisting only of characters a, b and c.
# Return the number of substrings containing at least one occurrence
#  of all these characters a, b and c.
# --------------------------
# 3 <= s.length <= 5 x 10 ** 4
# s only consists of a, b or c characters.
from collections import defaultdict

from random import choice

from pyperclip import copy


def number_of_substrings(s: str) -> int:
    # working_sol (35.08%, 90.82%) -> (123ms, 17.79mb)  time: O(s) | space: O(1)
    chars: set[str] = {'a', 'b', 'c'}
    chars_count: dict[str, int] = defaultdict(int)
    left_l: int = 0
    right_l: int = 0
    out: int = 0
    while right_l < len(s):
        chars_count[s[right_l]] += 1
        while len(chars_count) == len(chars):
            # We can expand to maximum and still get valid sub.
            out += len(s) - right_l
            # Until we shrink to incorrect sub.
            chars_count[s[left_l]] -= 1
            if 0 == chars_count[s[left_l]]:
                chars_count.pop(s[left_l])
            left_l += 1
        right_l += 1

    return out


# Time complexity: O(s)
# Every index of the input string `s`, used at most twice => O(2 * s).
# --------------------------
# Auxiliary space: O(1)
# `chars` <- contant size of 3 chars
# `chars_count` <- limited to size of 3 keys, values are always INT.


test: str = 'abcabc'
test_out: int = 10
assert test_out == number_of_substrings(test)

test = 'aaacb'
test_out = 3
assert test_out == number_of_substrings(test)

test = 'abc'
test_out = 1
assert test_out == number_of_substrings(test)

test = ''.join([choice(['a', 'b', 'c']) for _ in range(5 * 10 ** 4)])
copy(test)
