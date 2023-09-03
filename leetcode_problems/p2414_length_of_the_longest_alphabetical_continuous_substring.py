# An alphabetical continuous string is a string consisting of consecutive letters in the alphabet.
# In other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz".
# For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.
# Given a string s consisting of lowercase letters only, return the length
#  of the longest alphabetical continuous substring.
# -------------------------
# 1 <= s.length <= 10 ** 5
# s consists of only English lowercase letters.
from string import ascii_lowercase
from random import choice


def longest_continuous_sub(s: str) -> int:
    # working_sol (41.30%, 84.60%) -> (370ms, 17.37mb)  time: O(n) | space: O(1)
    max_seq: int = 1
    cur_seq: int = 1
    for x in range(1, len(s)):
        # Record on sequence break.
        if (ord(s[x]) - ord(s[x - 1])) != 1:
            max_seq = max(max_seq, cur_seq)
            cur_seq = 1
            continue
        cur_seq += 1
    # Extra max() check, if sequence was never broken.
    return max(cur_seq, max_seq)


# Time complexity: O(n) -> traversing whole input_string, once => O(n).
# n - len of input_string^^|
# Auxiliary space: O(1) -> only 2 extra constant INTs used => O(1).


test: str = "abacaba"
test_out: int = 2
assert test_out == longest_continuous_sub(test)

test = "abcde"
test_out = 5
assert test_out == longest_continuous_sub(test)

# test -> Failed -> I was rebuilding it without pointers, forgot that 0 index is already checked -> range(1, len(s)).
test = "orcvscn"
test_out = 1
assert test_out == longest_continuous_sub(test)

test = ''
for _ in range(10 ** 5):
    test += choice(ascii_lowercase)
print(test)
