# You are given a string s.
# The score of a string is defined as the sum of the absolute difference
#  between the ASCII values of adjacent characters.
# Return the score of s.
# -----------------------
# 2 <= s.length <= 100
# s consists only of lowercase English letters.
from random import choice
from string import ascii_lowercase


def score_of_string(s: str) -> int:
    # working_sol (72.94%, 99.88%) -> (34ms, 16.25mb)  time: O(s) | space: O(1)
    out: int = 0
    for index in range(1, len(s)):
        out += abs(ord(s[index]) - ord(s[index - 1]))
    return out


# Time complexity: O(s)
# Always using (n + (n - 1)) indexes of `s` => O(2s).
# -----------------------
# Auxiliary space: O(1)
# Only one constant INT is used => O(1)


test: str = "hello"
test_out: int = 13
assert test_out == score_of_string(test)

test = "zaz"
test_out = 50
assert test_out == score_of_string(test)

test = ''.join([choice(ascii_lowercase) for _ in range(100)])
print(test)
