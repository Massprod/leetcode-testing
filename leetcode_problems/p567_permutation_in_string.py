# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.
# ------------------------
# 1 <= s1.length, s2.length <= 10 ** 4
# s1 and s2 consist of lowercase English letters.
from collections import Counter


def check_inclusion(s1: str, s2: str) -> bool:
    # working_sol (42.34%, 66.57%) -> (82ms, 16.68mb)  time: O(s1 * (s2 -s1)) | space: O(s1)
    if len(s1) > len(s2):
        return False
    # { char: occurrences }
    s1_chars: dict[str, int] = Counter(s1)
    # { char: occurrences }
    window_chars: dict[str, int] = Counter(s2[:len(s1)])
    start: int = 0
    end: int = len(s1) - 1

    def check_equal(chars_1: dict[str, int], chars_2: dict[str, int]) -> bool:
        if chars_1 == chars_2:
            return True
        return False

    # We only care about permutation, and we can use any of them == we just need chars
    #  to be present in the correct amount.
    # So, basically we just need some substring with `s1_chars` in it, to be present in s2.
    for new_end in range(end + 1, len(s2)):
        if check_equal(s1_chars, window_chars):
            return True
        window_chars[s2[start]] -= 1
        if not window_chars[s2[start]]:
            window_chars.pop(s2[start])
        start += 1
        new_char: str = s2[new_end]
        if new_char in window_chars:
            window_chars[new_char] += 1
        else:
            window_chars[new_char] = 1
    # We're skipping the last index, so we need extra check.
    return check_equal(s1_chars, window_chars)


# Time complexity: O(s1 + s1 + s1 * (s2 - s1))
# Always traversing `s1` to get all of its characters and their occurrences => O(s1).
# Extra traversing the same slice in `s2` => O(2 * s1).
# Check every other index that wasn't included in this slice => O(s1 + s2).
# And for each check, we're traversing all chars in this slice to compare with `s1` => O(s1 + s1 + s1 * (s2 - s1)).
# ------------------------
# Auxiliary space: O(s1)
# `s1_chars` <- allocates space for each char from `s1` => O(s1).
# `window_chars` <- allocates space for each char in slice of size `s1` => O(s1 * 2).


test_s1: str = "ab"
test_s2: str = "eidbaooo"
test_out: bool = True
assert test_out == check_inclusion(test_s1, test_s2)

test_s1 = "ab"
test_s2 = "eidboaoo"
test_out = False
assert test_out == check_inclusion(test_s1, test_s2)

test_s1 = "adc"
test_s2 = "dcda"
test_out = True
assert test_out == check_inclusion(test_s1, test_s2)
