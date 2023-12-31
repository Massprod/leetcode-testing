# Given a string s, return the length of the longest substring between two equal characters,
#  excluding the two characters.
# If there is no such substring return -1.
# A substring is a contiguous sequence of characters within a string.
# ------------------
# 1 <= s.length <= 300
# s contains only lowercase English letters.
from random import choice
from string import ascii_lowercase


def max_length_between_equal_chars(s: str) -> int:
    # working_sol (89.27%, 12.44%) -> (34ms, 17.2mb)  time: O(s) | space: O(s)
    # {char: [first occurrence, last occurrence]}
    all_chars: dict[str, list[int]] = {}
    for index, char in enumerate(s):
        if char not in all_chars:
            all_chars[char] = [index, index]
        else:
            all_chars[char][-1] = index
    # Base case: no such substring == -1.
    out: int = -1
    for char in all_chars:
        # Already 0-indexed, so we don't care about first char of 2 equal, but we still need to remove second.
        # (last occurrence index - first occurrences - 1 to remove second char)
        out = max(out, all_chars[char][1] - all_chars[char][0] - 1)
    return out


# Time complexity: O(s).
# Single traverse to get first and last occurrence indexes for every symbol => O(s).
# Worst case: every symbol is unique.
# So, we will extra traverse whole input string `s` to get substring sizes => O(s).
# O(2s).
# Auxiliary space: O(s).
# Same worst case, we will just store every unique symbol and list with 2 values in it => O(s).


test: str = "aa"
test_out: int = 0
assert test_out == max_length_between_equal_chars(test)

test = "abca"
test_out = 2
assert test_out == max_length_between_equal_chars(test)

test = "cbzxy"
test_out = -1
assert test_out == max_length_between_equal_chars(test)

test = ''.join([choice(ascii_lowercase) for _ in range(300)])
print(test)
