# You are given a string s formed by digits and '#'.
# We want to map s to English lowercase characters as follows:
#  - Characters ('a' to 'i') are represented by ('1' to '9') respectively.
#  - Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
# Return the string formed after mapping.
# The test cases are generated so that a unique mapping will always exist.
# -------------------
# 1 <= s.length <= 1000
# s consists of digits and the '#' letter.
# s will be a valid string such that mapping is always possible.
from collections import deque


def freq_alphabets(s: str) -> str:
    # working_sol (86.88%, 28.00%) -> (30ms, 16.54mb)  time: O(s) | space: O(s)
    out: deque[str] = deque([])
    index: int = len(s) - 1
    while -1 < index:
        if '#' == s[index]:
            out.appendleft(chr(int(s[index - 2:index]) + 96))
            index -= 3
        else:
            out.appendleft(chr(int(s[index]) + 96))
            index -= 1
    return ''.join(out)


# Time complexity: O(s)
# Always using every char of `s`, once => O(s).
# -------------------
# Auxiliary space: O(s)
# In the worst case, there's no `#` in `s`.
# `out` <- will store every char from `s` => O(s).


test: str = "10#11#12"
test_out: str = "jkab"
assert test_out == freq_alphabets(test)

test = "1326#"
test_out = "acz"
assert test_out == freq_alphabets(test)
