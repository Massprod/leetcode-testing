# You are given a string s consisting only of letters 'a' and 'b'.
# In a single step you can remove one palindromic subsequence from s.
# Return the minimum number of steps to make the given string empty.
# A string is a subsequence of a given string if it is generated by deleting
#  some characters of a given string without changing its order.
# Note that a subsequence does not necessarily need to be contiguous.
# A string is called palindrome if is one that reads the same backward as well as forward.
# --------------------------
# 1 <= s.length <= 1000
# s[i] is either 'a' or 'b'.
from collections import Counter
from random import choice


def remove_palindrome_sub(s: str) -> int:
    # working_sol (58.82%, 89.84%) -> (35ms, 16.38mb)  time: O(s) | space: O(1)
    left: int = 0
    right: int = len(s) - 1
    a_present: int = 0
    b_present: int = 0
    while left < right:
        if not a_present and ('a' == s[left] or 'b' == s[left]):
            a_present += 1
        if not b_present and ('b' == s[right] or 'a' == s[right]):
            b_present += 1
        if s[left] != s[right]:
            return a_present + b_present
        left += 1
        right -= 1
    return 1


# Time complexity: O(s)
# In the worst case `s` is a palindrome.
# We're going to traverse whole `s`, once => O(s).
# --------------------------
# Auxiliary space: O(1).
# Only 4 constant INT's used, none of them depends on input => O(1).


test: str = "ababa"
test_out: int = 1
assert test_out == remove_palindrome_sub(test)

test = "abb"
test_out = 2
assert test_out == remove_palindrome_sub(test)

test = "baabb"
test_out = 2
assert test_out == remove_palindrome_sub(test)

test = "bbaabaaa"
test_out = 2
assert test_out == remove_palindrome_sub(test)

test = ''.join([choice(['a', 'b']) for _ in range(1000)])
print(test)
