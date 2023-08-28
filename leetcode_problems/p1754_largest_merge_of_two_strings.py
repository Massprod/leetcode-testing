# You are given two strings word1 and word2.
# You want to construct a string merge in the following way:
#  while either word1 or word2 are non-empty, choose one of the following options:
#   - If word1 is non-empty, append the first character in word1 to merge and delete it from word1.
#    - For example, if word1 = "abc" and merge = "dv", then after choosing this operation,
#      word1 = "bc" and merge = "dva".
#   - If word2 is non-empty, append the first character in word2 to merge and delete it from word2.
#    - For example, if word2 = "abc" and merge = "", then after choosing this operation,
#      word2 = "bc" and merge = "a".
# Return the lexicographically largest merge you can construct.
# ---------------
# 1 <= word1.length, word2.length <= 3000
# word1 and word2 consist only of lowercase English letters.
from string import ascii_lowercase
from random import choice


def largest_merge(word1: str, word2: str) -> str:
    # working_sol (83.13%, 57.50%) -> (83ms, 16.52mb)  time: O(n * log n) | space: O(n + m)
    w1_index: int = 0
    w2_index: int = 0
    merged: str = ''
    while w1_index != len(word1) and w2_index != len(word2):
        # Built in Python checks is a lot Faster, than
        #  rebuilding it on your own.
        if word1[w1_index] > word2[w2_index]:
            merged += word1[w1_index]
            w1_index += 1
            continue
        # If both are equal, take from LexicoHigher string.
        if word1[w1_index] == word2[w2_index]:
            # ! You should choose the next character from the larger string. !
            if word1[w1_index + 1:] > word2[w2_index + 1:]:
                merged += word1[w1_index]
                w1_index += 1
                continue
        merged += word2[w2_index]
        w2_index += 1

    merged += word1[w1_index:] + word2[w2_index:]
    return merged


# Time complexity: O(n * log n) -> for every index checking for LexicoHigher string => O(n * log n) ->
# n - len of longest input_string^^| -> worst case, everything is duplicates and strings are equal,
#                                    so for every index step we will recheck n - 1, n - 2, n - 3 etc. strings
#                                    to decide which is LexicoHigher.
# Auxiliary space: O(n + m) -> merging both input string into one => O(n + m) ->
# n - len of word1^^|  -> slicing never taking more space than input_string, so it's still (n + m) extra.
# m - len of word2^^|
# ---------------
# Ok. Working with big constraints but failed 105 test_case.
# Don't see any mistake and with such big values, it's hard to see. Guess I'm failing to find LexicoLarger string.
# Which is strange, cuz I'm doing standard search for a first difference and saving this index, then appending
#  everything from a Higher string until this index is reached.
# W.e there's actually faster way with Python we can just check string > string, will do it automatically.
# But I guess point was to make your own check for LexicoLarger part of string left.
# And I don't see how it's failing. Even worked with 10+ random cases with 3000length.
# So I guess it's better to stick with Python standard and do not reinvent the wheel.
# Well my Wheel is obviously working, but with every equal symbol check for LexicoHigher.
# And I'm failing to make it slicing correctly, w.e. It's always best to stick with already built in methods.
# Or we can't actually SLICE part of the string from equal symbol -> higher symbol.
# And we need to recheck it anyway. Cuz in this case it's working correctly.
# ---------------
# Guess it can be done with recursion and when merge fully build, check with already saved and decide what's higher.
# But it's slow and hint ->
# -> ! If both are equal, think of a criteria that lets you decide which string to consume the next character from. !
# -> ! You should choose the next character from the larger string. !
# Let's try to just build like this^^.


test_1: str = "cabaa"
test_2: str = "bcaaa"
test_out: str = "cbcabaaaaa"
assert test_out == largest_merge(test_1, test_2)

test_1 = "abcabc"
test_2 = "abdcaba"
test_out = "abdcabcabcaba"
assert test_out == largest_merge(test_1, test_2)

test_1 = ''
test_2 = ''
for _ in range(3000):
    test_1 += choice(ascii_lowercase)
    test_2 += choice(ascii_lowercase)
# print(test_1)
# print('-----')
# print(test_2)
