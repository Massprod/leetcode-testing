# You are given a string allowed consisting of distinct characters and an array of strings words.
# A string is consistent if all characters in the string appear in the string allowed.
# Return the number of consistent strings in the array words.
# ------------------------
# 1 <= words.length <= 10 ** 4
# 1 <= allowed.length <= 26
# 1 <= words[i].length <= 10
# The characters in allowed are distinct.
# words[i] and allowed contain only lowercase English letters.


def count_consistent_strings(allowed: str, words: list[str]) -> int:
    # working_sol (90.00%, 21.54%) -> (197ms, 18.56mb)  time: O(n + k * m) | space: O(n)
    out: int = 0
    to_use: set[str] = set(allowed)
    for word in words:
        for char in word:
            if char not in to_use:
                break
        else:
            out += 1
    return out


# Time complexity: O(n + k * m) <- n - length of the input string `allowed`,
#                                  k - length of the input array `words`,
#                                  m - average length of word in `words`.
# Always traversing whole `allowed` to get all unique chars from it => O(n).
# In the worst case every char in `words` can be used, so we will traverse every word in it => O(n + k * m).
# ------------------------
# Auxiliary space: O(n)
# `to_use` <- stores every unique char from `allowed` => O(n).


test_allowed: str = "ab"
test_words: list[str] = ["ad", "bd", "aaab", "baa", "badab"]
test_out: int = 2
assert test_out == count_consistent_strings(test_allowed, test_words)

test_allowed = "abc"
test_words = ["a", "b", "c", "ab", "ac", "bc", "abc"]
test_out = 7
assert test_out == count_consistent_strings(test_allowed, test_words)

test_allowed = "cad"
test_words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
test_out = 4
assert test_out == count_consistent_strings(test_allowed, test_words)
