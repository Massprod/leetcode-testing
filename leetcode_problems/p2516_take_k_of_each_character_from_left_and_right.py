# You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k.
# Each minute, you may take either the leftmost character of s, or the rightmost character of s.
# Return the minimum number of minutes needed for you to take at least k of each character,
#  or return -1 if it is not possible to take k of each character.
# -----------------------
# 1 <= s.length <= 10 ** 5
# s consists of only the letters 'a', 'b', and 'c'.
# 0 <= k <= s.length
from random import choice
from collections import defaultdict


def take_characters(s: str, k: int) -> int:
    # working_sol (81.11%, 79.81%) -> (183ms, 17.17mb)  time: O(n) | space: O(1)
    if 0 == k:
        return 0
    out: int = len(s)
    chars_count: dict[str, int] = defaultdict(int)
    for char in s:
        chars_count[char] += 1
    options: list[str] = ['a', 'b', 'c']
    max_window: int = -1
    for option in options:
        present: int = chars_count.get(option, 0)
        # We don't have required chars at all.
        if present < k:
            return max_window
    left: int = 0
    right: int = 0
    while right < len(s):
        chars_count[s[right]] -= 1
        while chars_count[s[right]] < k:
            chars_count[s[left]] += 1
            left += 1
        right += 1
        # Maximum chars we can delete, and still have correct amount of chars to use.
        max_window = max(max_window, right - left)
    return out - max_window


# Time complexity: O(n) <- n - length of the input string `s`.
# Always traversing whole input string `s` to get all chars count => O(n).
# Extra building windows to get how many chars we can delete => O(n).
# -----------------------
# Auxiliary space: O(1)
# `chars_count` - always contains the same 3 chars 'abc' or less => O(1).


test: str = "aabaaaacaabc"
test_k: int = 2
test_out: int = 8
assert test_out == take_characters(test, test_k)

test = "a"
test_k = 1
test_out = -1
assert test_out == take_characters(test, test_k)

test = ''.join([choice(['a', 'b', 'c']) for _ in range(10 ** 5)])
print(test)
