# A string is good if there are no repeated characters.
# Given a string s, return the number of good substrings of length three in s.
# Note that if there are multiple occurrences of the same substring,
#  every occurrence should be counted.
# A substring is a contiguous sequence of characters in a string.
# ---------------------
# 1 <= s.length <= 100
# s consists of lowercase English letters.
from collections import Counter


def count_good_substrings(s: str) -> int:
    # working_sol (19.83%, 62.84%) -> (42ms, 16.41mb)  time: O(s) | space: O(1)
    out: int = 0
    left: int = 0
    right: int = 2
    cur_window: dict[str, int] = Counter(s[left:right + 1])
    if 3 == len(cur_window.values()):
        out += 1
    while right < len(s) - 1:
        cur_window[s[left]] -= 1
        if 0 == cur_window[s[left]]:
            cur_window.pop(s[left])
        left += 1
        right += 1
        if s[right] in cur_window:
            cur_window[s[right]] += 1
        else:
            cur_window[s[right]] = 1
        if 3 == len(cur_window.values()):
            out += 1
    return out


# Time complexity: O(s)
# Always using every index of `s`, once => O(s).
# ---------------------
# Auxiliary space: O(1)
# `cur_window` <- always allocate space for 3 STRING keys and INT for each of them => O(1).


test: str = "xyzzaz"
test_out: int = 1
assert test_out == count_good_substrings(test)

test = "aababcabc"
test_out = 4
assert test_out == count_good_substrings(test)
