# Given a string s and an array of strings words,
#  determine whether s is a prefix string of words.
# A string s is a prefix string of words if s can be made by concatenating the first k strings
#  in words for some positive k no larger than words.length.
# Return true if s is a prefix string of words, or false otherwise.
# -----------------------
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# 1 <= s.length <= 1000
# words[i] and s consist of only lowercase English letters.


def is_prefix_string(s: str, words: list[str]) -> bool:
    # working_sol (51.17%, 81.98%) -> (40ms, 16.44mb)  time: O(s) | space: O(s)
    out: str = s
    for word in words:
        if not out:
            return True
        if out.startswith(word):
            out = out.removeprefix(word)
        else:
            return False
    if out:
        return False
    return True


# Time complexity: O(s)
# Essentially we're always using every char in `s` to check and also remove => O(2 * s).
# -----------------------
# Auxiliary space: O(s)
# `out` <- copy of the `s` => O(s).


test: str = "iloveleetcode"
test_words: list[str] = ["i", "love", "leetcode", "apples"]
test_out: bool = True
assert test_out == is_prefix_string(test, test_words)

test = "iloveleetcode"
test_words = ["apples", "i", "love", "leetcode"]
test_out = False
assert test_out == is_prefix_string(test, test_words)
