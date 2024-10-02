# Two strings word1 and word2 are considered almost equivalent if the differences between the frequencies
#  of each letter from 'a' to 'z' between word1 and word2 is at most 3.
# Given two strings word1 and word2, each of length n,
#  return true if word1 and word2 are almost equivalent, or false otherwise.
# The frequency of a letter x is the number of times it occurs in the string.
# ----------------------------
# n == word1.length == word2.length
# 1 <= n <= 100
# word1 and word2 consist only of lowercase English letters.
from collections import Counter
from string import ascii_lowercase


def check_almost_equivalent(word1: str, word2: str) -> bool:
    # working_sol (99.77%, 84.96%) -> (23ms, 16.48mb)  time: O(n + m) | space: O(1)
    # { char: occurrences }
    word1_chars: dict[str, int] = Counter(word1)
    word2_chars: dict[str, int] = Counter(word2)
    for char in ascii_lowercase:
        word1_count: int = 0
        if char in word1_chars:
            word1_count = word1_chars[char]
        word2_count: int = 0
        if char in word2_chars:
            word2_count = word2_chars[char]
        if 3 < abs(word1_count - word2_count):
            return False
    return True


# Time complexity: O(n + m) <- n - length of the input string `word1`, m - length of the input string `word2`.
# Always traversing both input strings to get their char occurrences => O(n + m).
# Extra traversing every english lowercase char to check `word1` and `word2` difference => O(n + m).
# ----------------------------
# Auxiliary space: O(1)
# In the worst case every char of english lowercase will be present in both.
# Because we can't have more than this amount stored, we can call it constant => O(1).


test_1: str = "aaaa"
test_2: str = "bccb"
test_out: bool = False
assert test_out == check_almost_equivalent(test_1, test_2)

test_1 = "abcdeef"
test_2 = "abaaacc"
test_out = True
assert test_out == check_almost_equivalent(test_1, test_2)

test_1 = "cccddabba"
test_2 = "babababab"
test_out = True
assert test_out == check_almost_equivalent(test_1, test_2)
