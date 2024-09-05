# You are given a 0-indexed string array words,
#  where words[i] consists of lowercase English letters.
# In one operation, select any index i such that 0 < i < words.length
#  and words[i - 1] and words[i] are anagrams, and delete words[i] from words.
# Keep performing this operation as long as you can select an index that satisfies the conditions.
# Return words after performing all operations. It can be shown that selecting the indices
#  for each operation in any arbitrary order will lead to the same result.
# An Anagram is a word or phrase formed by rearranging the letters of a different word
#  or phrase using all the original letters exactly once.
# For example, "dacb" is an anagram of "abdc".
# ----------------------------
# 1 <= words.length <= 100
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
from collections import Counter


def remove_anagram(words: list[str]) -> list[str]:
    # working_sol (23.25%, 56.73%) -> (70ms, 16.52mb)  time: O(n * k) | space: O(n * k)
    out: list[int | str] = [0]
    fast_words: dict[int, dict[str, int]] = {
        index: Counter(words[index]) for index in range(len(words))
    }
    for index in range(1, len(words)):
        if fast_words[index] != fast_words[out[-1]]:
            out.append(index)
    return [words[index] for index in out]


# Time complexity: O(n * k) <- n - length of the input array `words`, k - average length of word in `words`.
# Always traversing all words from `words` to get set of `fast_words` => O(n * k).
# Extra traversing all of them to find the correct words => O(n * k * 2).
# Extra traversing correct words to get `out`, and in the worst case all of them correct => O(3 * n * k).
# ----------------------------
# Auxiliary space: O(n * k)
# In the worst case, every word is unique, and there are no anagrams.
# `fast_words` <- allocates space for each unique word from `words` => O(n * k).
# `out` <- allocates space for every word from `words` => O(2 * n * k).


test: list[str] = ["abba", "baba", "bbaa", "cd", "cd"]
test_out: list[str] = ["abba", "cd"]
assert test_out == remove_anagram(test)

test = ["a", "b", "c", "d", "e"]
test_out = ["a", "b", "c", "d", "e"]
assert test_out == remove_anagram(test)

test = ["az", "azz"]
test_out = ["az", "azz"]
assert test_out == remove_anagram(test)
