# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.
# ---------------------
# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.
from random import choice, randint
from string import ascii_lowercase


def merge_alternately(word1: str, word2: str) -> str:
    # working_sol (98.14%, 73.10%) -> (33ms, 16.2mb)  time: O(n) | space: O(n + m)
    # word1, word2 pointers.
    point1: int = 0
    point2: int = 0
    # We can't manipulate indexes within a string, so it's mandatory.
    merged: str = ""
    # Didn't want to extra check on every index ->
    # -> if pointer >= len(word1/word2), so now it's just breaking
    # only when out of bounds, should be faster.
    while True:
        try:
            merged += word1[point1]
            point1 += 1
        except IndexError:
            merged += word2[point2:]
            break
        try:
            merged += word2[point2]
            point2 += 1
        except IndexError:
            merged += word1[point1:]
            break
    return merged


# Time complexity: O(n) -> always traversing indexes equal to shortest_input, and same indexes in other ->
# n - len of longest_input_string^^| -> extra just assign everything what's left in longer_string ->
#                                    -> but it's actually still use of those indexes,
#                                    so it's should be => O(n) <- where n is len(longest_string).
# Auxiliary space: O(m + n) -> 2 extra INTs, which doesn't depend on input -> extra creating a new string
# m - len of shortest_input_string^^| with a size of both inputs summarized == (m + n) => O(m + n).
# ---------------------
# Want to try this with breaking from loop with RAISING error not just checking pointer.
# Cuz if we're checking pointer for every symbol it's extra time, and it should be faster to just
# get index_error break.


# Time to change design for tests, cuz test1 without type annotation is not actually good.
test_w1: str = "abc"
test_w2: str = "pqr"
test_out: str = "apbqcr"
assert test_out == merge_alternately(test_w1, test_w2)

test_w1 = "ab"
test_w2 = "pqrs"
test_out = "apbqrs"
assert test_out == merge_alternately(test_w1, test_w2)

test_w1 = "abcd"
test_w2 = "pq"
test_out = "apbqcd"
assert test_out == merge_alternately(test_w1, test_w2)

test_w1 = ""
test_w2 = ""
for _ in range(randint(20, 100)):
    test_w1 += choice(ascii_lowercase)
for _ in range(randint(20, 100)):
    test_w2 += choice(ascii_lowercase)
print(test_w1)
print("-----BREAK-----")
print(test_w2)
