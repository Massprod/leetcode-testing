# Given a string s, find any substring of length 2 which is also present in the reverse of s.
# Return true if such a substring exists, and false otherwise.
# ---------------------
# 1 <= s.length <= 100
# s consists only of lowercase English letters.


def is_substring_present(s: str) -> bool:
    # working_sol (99.56%, 92.93%) -> (23ms, 16.39mb)  time: O(s) | space: O(s)
    reversed_s: str = s[::-1]
    for index in range(2, len(s) + 1):
        if s[index - 2: index] in reversed_s:
            return True
    return False


# Time complexity: O(s)
# We always use 2 -> len(s) indexes => O(s - 2).
# ---------------------
# Auxiliary space: O(s)
# `reversed_s` <- copy of the original input string `s`, but reversed => O(s).


test: str = "leetcode"
test_out: bool = True
assert test_out == is_substring_present(test)

test = "abcba"
test_out = True
assert test_out == is_substring_present(test)

test = "abcd"
test_out = False
assert test_out == is_substring_present(test)

test = "ausoee"
test_out = True
assert test_out == is_substring_present(test)
