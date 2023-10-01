# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
#  typically using all the original letters exactly once.
# ------------------------
# 1 <= s.length, t.length <= 5 * 10 ** 4
# s and t consist of lowercase English letters.
# ------------------------
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    # working_sol (98.71%, 99.52%) -> (37ms, 16.53mb)  time: O(n) | space: O(n)
    # Can't be anagram.
    if len(t) != len(s):
        return False
    # Count everything in s|t.
    count_s: dict[str, int] = Counter(s)
    # Check for same # of occurrences in counterpart.
    for sym in count_s:
        if t.count(sym) != count_s[sym]:
            return False
    return True


# Only for cases with same length, otherwise it's O(1), cuz we ignore diff sizes.
# Time complexity: O(n) -> count symbols in 's' string => O(n) -> check every symbol to have correct counter => O(2n).
# n - len of input_string^^|
# Auxiliary space: O(n) -> worst case == every symbol unique -> 1 extra dictionary with size of 'n' => O(n).


test: str = "anagram"
test_t: str = "nagaram"
test_out: bool = True
assert test_out == is_anagram(test, test_t)

test = "rat"
test_t = "car"
test_out = False
assert test_out == is_anagram(test, test_t)

test = "◁◐╡☎♠✝✘✘✘✘™™™✍✍✍"
test_t = "◁✘◐╡™✍☎✘™✍✍✘♠✝✘™"
test_out = True
assert test_out == is_anagram(test, test_t)
