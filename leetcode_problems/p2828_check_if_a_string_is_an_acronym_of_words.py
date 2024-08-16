# Given an array of strings words and a string s,
#  determine if s is an acronym of words.
# The string s is considered an acronym of words if it can be formed by concatenating
#  the first character of each string in words in order.
# For example, "ab" can be formed from ["apple", "banana"],
#  but it can't be formed from ["bear", "aardvark"].
# Return true if s is an acronym of words, and false otherwise.
# --------------------
# 1 <= words.length <= 100
# 1 <= words[i].length <= 10
# 1 <= s.length <= 100
# words[i] and s consist of lowercase English letters.


def is_acronym(words: list[str], s: str) -> bool:
    # working_sol (92.43%, 30.34%) -> (46ms, 16.51mb)  time: O(s) | space: O(1)
    if len(words) != len(s):
        return False
    for index in range(len(s)):
        if s[index] != words[index][0]:
            return False
    return True


# Time complexity: O(s)
# Always traversing every character in `s` => O(s).
# --------------------
# Auxiliary space: O(1)
# Nothing extra is used => O(1).


test: list[str] = ["alice", "bob", "charlie"]
test_s: str = "abc"
test_out: bool = True
assert test_out == is_acronym(test, test_s)

test = ["an", "apple"]
test_s = "a"
test_out = False
assert test_out == is_acronym(test, test_s)

test = ["never", "gonna", "give", "up", "on", "you"]
test_s = "ngguoy"
test_out = True
assert test_out == is_acronym(test, test_s)
