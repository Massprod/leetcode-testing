# Given two string arrays words1 and words2, return the number of strings
#  that appear exactly once in each of the two arrays.
# ------------------
# 1 <= words1.length, words2.length <= 1000
# 1 <= words1[i].length, words2[j].length <= 30
# words1[i] and words2[j] consists only of lowercase English letters.
from collections import Counter


def count_words(words1: list[str], words2: list[str]) -> int:
    # working_sol (63.47%, 55.14%) -> (71ms, 16.95mb)  time: O(n + m) | space: O(n + m)
    out: int = 0
    unique_words1: dict[str, int] = Counter(words1)
    unique_words2: dict[str, int] = Counter(words2)
    for unique_word, occurrences in unique_words1.items():
        if 1 == occurrences and unique_word in unique_words2 and 1 == unique_words2[unique_word]:
            out += 1
    return out


# Time complexity: O(n + m) <- n - length of the input array `words1`, m - length of the input array `words2`.
# Always traversing `words1` and `words2` to get all unique words from it => O(n + m).
# Extra traversing unique words from `words1` => O(n + m + n).
# ------------------
# Auxiliary space: O(n + m)
# In the worst case, every char in the input words are unique.
# `unique_words1` <- will be of size `n` => O(n).
# `unique_words2` <- will be of size `m` => O(n + m).


test_1: list[str] = ["leetcode", "is", "amazing", "as", "is"]
test_2: list[str] = ["amazing", "leetcode", "is"]
test_out: int = 2
assert test_out == count_words(test_1, test_2)

test_1 = ["b", "bb", "bbb"]
test_2 = ["a", "aa", "aaa"]
test_out = 0
assert test_out == count_words(test_1, test_2)

test_1 = ["a", "ab"]
test_2 = ["a", "a", "a", "ab"]
test_out = 1
assert test_out == count_words(test_1, test_2)
