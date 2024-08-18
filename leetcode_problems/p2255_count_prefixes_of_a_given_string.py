# You are given a string array words and a string s,
#  where words[i] and s comprise only of lowercase English letters.
# Return the number of strings in words that are a prefix of s.
# A prefix of a string is a substring that occurs at the beginning of the string.
# A substring is a contiguous sequence of characters within a string.
# ------------------------
# 1 <= words.length <= 1000
# 1 <= words[i].length, s.length <= 10
# words[i] and s consist of lowercase English letters only.


def count_prefixes(words: list[str], s: str) -> int:
    # working_sol (84.59%, 61.78%) -> (53ms, 16.76mb)  time: O(n * k) | space: O(1)
    out: int = 0
    for word in words:
        # Or we can check with 2 pointers, but w.e
        if s.startswith(word):
            out += 1
    return out


# Time complexity: O(n * k) <- n - length of the input array `words`, k - average length of word in `words`.
# Always traversing whole input array `words`.
# Worst case: every word is copy of `s`.
# And for each word in it, we check every char to be present in `s` => O(n * k).
# ------------------------
# Auxiliary space: O(1).
# Only 1 constant INT used, extra pointers within `startswith` still constant => O(1).


test: list[str] = ["a", "b", "c", "ab", "bc", "abc"]
test_s: str = "abc"
test_out: int = 3
assert test_out == count_prefixes(test, test_s)

test = ["a", "a"]
test_s = "aa"
test_out = 2
assert test_out == count_prefixes(test, test_s)
