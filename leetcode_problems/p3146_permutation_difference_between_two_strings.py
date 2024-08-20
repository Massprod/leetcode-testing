# You are given two strings s and t such that every character occurs
#  at most once in s and t is a permutation of s.
# The permutation difference between s and t is defined as the sum of the absolute difference
#  between the index of the occurrence of each character in s
#  and the index of the occurrence of the same character in t.
# Return the permutation difference between s and t.
# -------------------------
# 1 <= s.length <= 26
# Each character occurs at most once in s.
# t is a permutation of s.
# s consists only of lowercase English letters.
from random import shuffle
from string import ascii_lowercase
from collections import defaultdict


def find_permutation_difference(s: str, t: str) -> int:
    # working_sol (62.67%, 66.06%) -> (38ms, 16.43mb)  time: O(s) | space: O(s)
    s_occurs: dict[str, int] = defaultdict(int)
    t_occurs: dict[str, int] = defaultdict(int)
    for index, char in enumerate(s):
        s_occurs[char] = index
    for index, char in enumerate(t):
        t_occurs[char] = index
    out: int = 0
    for char, index_occur in s_occurs.items():
        out += abs(t_occurs[char] - index_occur)
    return out


# Time complexity: O(s)
# len(s) == len(t)
# Always traversing all chars from `s` | `t`, 3 times => O(3 * s).
# -------------------------
# Auxiliary space: O(s)
# `s_occurs` <- allocates space for each char from `s` => O(s).
# `t_occurs` <- allocates space for each char from `t` => O(2 * s).


test_s: str = "abc"
test_t: str = "bac"
test_out: int = 2
assert test_out == find_permutation_difference(test_s, test_t)

test_s = "abcde"
test_t = "edbac"
test_out = 12
assert test_out == find_permutation_difference(test_s, test_t)

test_list: list[str] = list(ascii_lowercase)
shuffle(test_list)
test_s = ''.join(test_list)
shuffle(test_list)
test_t = ''.join(test_list)
print(test_s, '\n\n', test_t)
