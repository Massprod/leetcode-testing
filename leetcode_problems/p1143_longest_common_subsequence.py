# Given two strings text1 and text2, return the length of their longest common subsequence.
# If there is no common subsequence, return 0.
# A subsequence of a string is a new string generated from the original string
#   with some characters (can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.
# ----------------
# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.
from random import choice
from string import ascii_lowercase


def longest_common_subsequence(text1: str, text2: str) -> int:
    # working_sol (20.1%, 13.24%) -> (1438ms, 305.5mb)  time: O(3 ** n) | space: O(3 ** n)
    # Recursion cache.
    recur_cache: dict[tuple[int, int], int] = {}

    def delete_symbol(text1_index: int, text2_index: int) -> int:
        # Reuse.
        if (text1_index, text2_index) in recur_cache:
            return recur_cache[text1_index, text2_index]
        # We need to find only equal symbols, and
        # we can't find equal symbol in empty string.
        if text1_index < 0 or text2_index < 0:
            return 0
        # If symbol is correct +1 to len of subsequence.
        if text1[text1_index] == text2[text2_index]:
            return 1 + delete_symbol(text1_index - 1, text2_index - 1)
        # We always need to delete last symbols either from text1 or text2.
        # To check if next symbol is equal or not.
        # Need maximum_subsequence, so we need to take max() from all options.
        recur_cache[text1_index, text2_index] = max(
            delete_symbol(text1_index - 1, text2_index),
            delete_symbol(text1_index, text2_index - 1)
        )
        return recur_cache[text1_index, text2_index]
    # From right -> left, delete -> check equal/not.
    return delete_symbol(len(text1) - 1, len(text2) - 1)


# Time complexity: O(3 ** n) -> recursion tree with 3 options and depths of n => O(3 ** n) ->
# n - len of longest input_string^^| -> we calling until both of the strings are empty, so depth is
#                                    always going to be equal to len of longest input_string ->
#                                    -> dunno how to calc correctly effect of cache here, but it's
#                                    obvious culling same index_calls, so O(3 ** n) incorrect.
# Auxiliary space: O(3 ** n) -> every call is stored in cache => O(3 ** n).
# ----------------
# Ok. Already done similar but with deleting symbols anc counting ASCII of them in p712.
# Same approach, but we don't need to count everything except elements we're not deleting -> equal_elements.


test_1: str = "abcde"
test_2: str = "ace"
test_out: int = 3
assert test_out == longest_common_subsequence(test_1, test_2)

test_1 = "abc"
test_2 = "abc"
test_out = 3
assert test_out == longest_common_subsequence(test_1, test_2)

test_1 = "abc"
test_2 = "def"
test_out = 0
assert test_out == longest_common_subsequence(test_1, test_2)

test_1 = ""
test_2 = ""
for _ in range(999):
    test_1 += choice(ascii_lowercase)
    test_2 += choice(ascii_lowercase)
# print(test_1)
# print("-----------")
# print(test_2)
