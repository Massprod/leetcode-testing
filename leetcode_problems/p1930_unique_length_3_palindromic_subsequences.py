# Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
# A palindrome is a string that reads the same forwards and backwards.
# A subsequence of a string is a new string generated from the original string
#  with some characters (can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
# -----------------
# 3 <= s.length <= 10 ** 5
# s consists of only lowercase English letters.
from random import choice
from string import ascii_lowercase


def count_palindromic_subsequence(s: str) -> int:
    # working_sol (91.45%, 70.72%) -> (140ms, 17.2mb)  time: O(k * log n) | space: O(n)
    # Essentially all we care is how many unique values between first and last encounters of every unique symbol.
    uniques: set[str] = set(s)
    subs: int = 0
    for sym in uniques:
        subs += len(set(s[s.find(sym) + 1: s.rfind(sym)]))
    return subs


# Time complexity: O(k * log n) -> worst case == 'abcde..zzz...edcba' max sized ->
# n - len of input string 's'^^| -> we will check all 26 symbols of alphabet, and they will be edges ->
# k - # of unique syms in 's'^^| -> so we're always check 26 symbols on left side and search them with (str.find(sym))
#                                   which check some part of the string and same for the right side ->
#                                -> extra traverse of 's' to get set(uniques) => O(52 * log n) or O(2 * (k * log n)).
# Auxiliary space: O(n) -> worst case == every symbol is unique -> extra set with all symbols of 's' => O(n).
# -----------------
# Works but slow. What are we essentially doing?
# We're finding 2 same characters and check len of slice between them with only unique symbols.
# So, can't we just check this slices for every unique symbol in 's'?
# Like most left and most right positions == maximum size we can get, and only thing left is to delete duplicates.
# Should be much faster.
# Ok. It's faster with build_in methods. Just str.find() and str.rfind() is better.
# -----------------
# Store first occurrence in dict, store everything after first occurrence as unique values in subseq.
# And when second encounter we will just count everything we met as 1 subsequence.
# Only problem with cases like 'abaa' we need to include 'aaa'.
# For every encounter after first calc subsequences, and remember what we already added?
# Should be correct, but extra space to maintain this. Let's try.


test: str = "aabca"
test_out: int = 3
assert test_out == count_palindromic_subsequence(test)

test = "adc"
test_out = 0
assert test_out == count_palindromic_subsequence(test)

test = "bbcbaba"
test_out = 4
assert test_out == count_palindromic_subsequence(test)

test = ''.join([choice(ascii_lowercase) for _ in range(10 ** 5)])
print(test)
