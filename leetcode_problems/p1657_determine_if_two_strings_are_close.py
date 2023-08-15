# Two strings are considered close if you can attain one from the other using the following operations:
#   Operation 1:
#   Swap any two existing characters.
#   For example, abcde -> aecdb
#   Operation 2:
#   Transform every occurrence of one existing character into another existing character,
#     and do the same with the other character.
#   For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.
# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
# -------------------
# 1 <= word1.length, word2.length <= 10 ** 5
# word1 and word2 contain only lowercase English letters.


def close_strings(word1: str, word2: str) -> bool:
    # working_sol (48.26%, 96.42%) -> (220ms, 17.56mb)  time: O(n * log n) | space: O(n)
    # Something doesn't presented in both strings.
    if set(word1) != set(word2):
        return False
    # Count every symbol occurrences for both.
    word1_occur: dict[str, int] = {}
    word2_occur: dict[str, int] = {}
    for sym in word1:
        if sym in word1_occur:
            word1_occur[sym] += 1
            continue
        word1_occur[sym] = 1
    for sym in word2:
        if sym in word2_occur:
            word2_occur[sym] += 1
            continue
        word2_occur[sym] = 1
    # If there's equal occurrences for the same amount of symbols,
    #  we can switch them for w.e times we need and build correct version of another string.
    # Cuz we're not limited and doesn't have any rules to do operation2.
    if sorted(word1_occur.values()) != sorted(word2_occur.values()):
        return False
    return True


# Time complexity: O(n * log n) -> creating two sets for word1, word2 => O(2n) -> counting all symbol occurrences for
# n - len of one of the input_array^^| both strings => O(2n) -> sorting and comparing both strings => O(n * log n).
# Auxiliary space: O(n) -> not saving, but still using space to compare 2 sets => O(2n) ->
#                         -> extra 2 dictionaries with same sizes => O(2n) -> and sorted versions to compare => O(2n).
# -------------------
# Ok. All is correct, but I was comparing values for being equal, and it's correct BUT I don't need to use set()
# cuz there can be presented more than 1 value with same time of occurrences.
# -------------------
# Well obviously check len() and set() of both strings to be equal.
# Only question is about second operation, does it mean we can just check occurrences of values and
# if set() of these occurrences are equal we can change them correctly?
# Like we're not blocked on what and when use one of the operations.
# So we can just switch symbols until we hit correct. If there's enough occurrences of them.
# Like ->        "cabbba" and "abbccc",
# a == 2, b == 3, a == 1 and a == 1, b == 2, c == 3 <- so we can just switch them between and get correct.


test_1: str = "abc"
test_2: str = "bca"
test_out: bool = True
assert test_out == close_strings(test_1, test_2)

test_1 = "a"
test_2 = "aa"
test_out = False
assert test_out == close_strings(test_1, test_2)

test_1 = "cabbba"
test_2 = "abbccc"
test_out = True
assert test_out == close_strings(test_1, test_2)

# test -> Failed -> I was using set(dict.values()) and it deletes equal occurrences. Just change it and correct.
test_1 = "aaabbbbccddeeeeefffff"
test_2 = "aaaaabbcccdddeeeeffff"
test_out = False
assert test_out == close_strings(test_1, test_2)
