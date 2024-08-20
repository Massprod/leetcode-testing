# Given a string s, return the maximum length of a substring
#  such that it contains at most two occurrences of each character.
# -----------------------
# 2 <= s.length <= 100
# s consists only of lowercase English letters.
from random import choice
from string import ascii_lowercase
from collections import defaultdict


def maximum_length_substring(s: str) -> int:
    # working_sol (80.52%, 97.01%) -> (39ms, 16.40mb)  time: O(s) | space: O(s)
    cur_window: dict[str, int] = defaultdict(int)
    left: int = 0
    right: int = 0
    out: int = 0
    while right < len(s):
        cur_window[s[right]] += 1
        while left < right and 2 < cur_window[s[right]]:
            cur_window[s[left]] -= 1
            left += 1
        right += 1
        out = max(out, right - left)
    return out


# Time complexity: O(s)
# Always traversing whole input string `s`, once => O(s).
# -----------------------
# Auxiliary space: O(s)
# `cur_window` <- will allocate space for each char in `s` => O(s).


test: str = "bcbbbcba"
test_out: int = 4
assert test_out == maximum_length_substring(test)

test = "aaaa"
test_out = 2
assert test_out == maximum_length_substring(test)

test = ''.join([choice(ascii_lowercase) for _ in range(100)])
print(test)
