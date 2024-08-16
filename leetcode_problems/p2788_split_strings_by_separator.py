# Given an array of strings words and a character separator,
#  split each string in words by separator.
# Return an array of strings containing the new strings formed after the splits, excluding empty strings.
# Notes
#  - separator is used to determine where the split should occur,
#    but it is not included as part of the resulting strings.
#  - A split may result in more than two strings.
#  - The resulting strings must maintain the same order as they were initially given.
# ------------------------
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# characters in words[i] are either lowercase English letters
#  or characters from the string ".,|$#@" (excluding the quotes)
# separator is a character from the string ".,|$#@" (excluding the quotes)


def split_words_by_separator(words: list[str], separator: str) -> list[str]:
    # working_sol (71.04%, 78.25%) -> (89ms, 16.59mb)  time: O(n * k) | space: O(n * k)
    out: list[str] = []
    for word in words:
        seq: list[str] = word.split(separator)
        for w in seq:
            if w:
                out.append(w)
    return out


# Time complexity: O(n * k) <- n - length of the input array `words`, k - average length of word in `words`
# Always traversing every word in `words` and split it => O(n * k).
# ------------------------
# Auxiliary space: O(n * k)
# `out` <- in the worst case = there are no separators, will allocate space for every char => O(n * k).


test: list[str] = ["one.two.three", "four.five", "six"]
test_sep: str = "."
test_out: list[str] = ["one", "two", "three", "four", "five", "six"]
assert test_out == split_words_by_separator(test, test_sep)

test = ["$easy$", "$problem$"]
test_sep = "$"
test_out = ["easy", "problem"]
assert test_out == split_words_by_separator(test, test_sep)

test = ["|||"]
test_sep = "|"
test_out = []
assert test_out == split_words_by_separator(test, test_sep)
