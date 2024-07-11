# A sentence is a string of single-space separated words where
#  each word consists only of lowercase letters.
# A word is uncommon if it appears exactly once in one of the sentences,
#  and does not appear in the other sentence.
# Given two sentences s1 and s2, return a list of all the uncommon words.
# You may return the answer in any order.
# -----------------------
# 1 <= s1.length, s2.length <= 200
# s1 and s2 consist of lowercase English letters and spaces.
# s1 and s2 do not have leading or trailing spaces.
# All the words in s1 and s2 are separated by a single space.
from collections import defaultdict


def uncommon_from_sentences(s1: str, s2: str) -> list[str]:
    # working_sol (97.64%, 28.53%) -> (26ms, 16.58mb)  time: O(s1 + s2) | space: O(s1 + s2)
    out: list[str] = []
    words_s1: dict[str, int] = defaultdict(int)
    for word in s1.split(' '):
        words_s1[word] += 1
    words_s2: dict[str, int] = defaultdict(int)
    for word in s2.split(' '):
        words_s2[word] += 1
    for word, occurs in words_s1.items():
        if word in words_s2:
            words_s2.pop(word)
        elif 1 == occurs:
            out.append(word)
    for word, occurs in words_s2.items():
        if 1 == occurs:
            out.append(word)
    return out


# Time complexity: O(s1 + s2)
# Worst case, every word in both strings are unique and doesn't appear in each other.
# We will traverse both strings, once to get all the words => O(s1 + s2).
# Extra traversing all the words from both strings, to check if they're present in counterpart => O(2 * (s1 + s2)).
# -----------------------
# Auxiliary space: O(s1 + s2)
# All of the unique words from `s1` and `s2` will be stored in `words_s1` + `words_s2` => O(s1 + s2).
# `out` is also going to store all the words from both strings => O(2 * (s1 + s2)).


test_s1: str = "this apple is sweet"
test_s2: str = "this apple is sour"
test_out: list[str] = ["sweet", "sour"]
assert test_out == uncommon_from_sentences(test_s1, test_s2)

test_s1 = "apple apple"
test_s2 = "banana"
test_out = ["banana"]
assert test_out == uncommon_from_sentences(test_s1, test_s2)
