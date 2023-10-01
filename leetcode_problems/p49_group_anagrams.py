# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
#  typically using all the original letters exactly once.
# ---------------------
# 1 <= strs.length <= 10 ** 4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
from collections import Counter


def group_anagrams(strs: list[str]) -> list[list[str]]:
    # working_sol (83.26%, 91.58%) -> (93ms, 19.4mb)  time: O(n * (m * log m)) | space: O(m + n)
    # (sorted: list(orig * occurs))
    uniques: dict[str, list[str]] = {}
    for word in strs:
        s_word: str = ''.join(sorted(word))
        if s_word in uniques:
            uniques[s_word].append(word)
        else:
            uniques[s_word] = [word]
    return list(uniques.values())


# Time complexity: O(n * (m * log m)) -> traverse of whole array with sorting of every word inside of it ->
# n - len of input array^^|           -> worst case == every word is max sized => O(n * (m * log m))
# m - max len of words^^|
# Auxiliary space: O(m + n) -> worst case == every word is unique and max sized -> always sort and use of string
#                              with size == 'm' -> for every word unique key with list(key) => O(m + n).


test: list[str] = ["eat", "tea", "tan", "ate", "nat", "bat"]
test_out: list[list[str]] = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
test_t: list[list[str]] = group_anagrams(test)
for y in range(len(test_t)):
    test_t[y] = sorted(test_t[y])
assert sorted(test_out) == sorted(test_t)

test = [""]
test_out = [[""]]
test_t = group_anagrams(test)
for y in range(len(test_t)):
    test_t[y] = sorted(test_t[y])
assert sorted(test_out) == sorted(test_t)

test = ["a"]
test_out = [["a"]]
test_t = group_anagrams(test)
for y in range(len(test_t)):
    test_t[y] = sorted(test_t[y])
assert sorted(test_out) == sorted(test_t)

test = ["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"]
test_out = [["max"], ["buy"], ["doc"], ["may"], ["ill"], ["duh"], ["tin"], ["bar"], ["pew"], ["cab"]]
test_t = group_anagrams(test)
for y in range(len(test_t)):
    test_t[y] = sorted(test_t[y])
assert sorted(test_out) == sorted(test_t)
