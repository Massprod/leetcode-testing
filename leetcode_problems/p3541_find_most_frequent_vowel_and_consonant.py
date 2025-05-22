# You are given a string s consisting of lowercase English letters ('a' to 'z').
# Your task is to:
#  - Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
#  - Find the consonant (all other letters excluding vowels) with the maximum frequency.
# Return the sum of the two frequencies.
# Note: If multiple vowels or consonants have the same maximum frequency,
#  you may choose any one of them.
# If there are no vowels or no consonants in the string, consider their frequency as 0.
# The frequency of a letter x is the number of times it occurs in the string.
# -------------------------
# 1 <= s.length <= 100
# s consists of lowercase English letters only.
from collections import defaultdict


def max_freq_sum(s: str) -> int:
    # working_sol (100.00%, 42.34%) -> (0ms, 17.88mb)  time: O(s) | space: O(s)
    vowels: set[str] = { 'a', 'e', 'i', 'o', 'u' }
    # { char: occurs }
    count: dict[str, int] = defaultdict(int)
    for char in s:
        count[char] += 1
    
    max_vow: int = 0
    max_con: int = 0
    for char in count:
        if char not in vowels:
            max_con = max(max_con, count[char])
        else:
            max_vow = max(max_vow, count[char])
    
    return max_vow + max_con


# Time complexity: O(s)
# In the worst case, every char of `s` is unique.
# We're going to traverse whole `s`, once => O(s).
# And every unique char after it, because char are limited to alphabet == constant => O(s).
# -------------------------
# Auxiliary space: O(s)
# `count` <- allocates space for each unique char from `s`.


test: str = 'successes'
test_out: int = 6
assert test_out == max_freq_sum(test)

test = 'aeiaeia'
test_out = 3
assert test_out == max_freq_sum(test)
