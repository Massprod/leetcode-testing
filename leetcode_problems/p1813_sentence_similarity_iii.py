# You are given two strings sentence1 and sentence2, each representing a sentence composed of words.
# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
# Each word consists of only uppercase and lowercase English characters.
# Two sentences s1 and s2 are considered similar if it is possible to insert an arbitrary sentence (possibly empty)
#  inside one of these sentences such that the two sentences become equal.
# Note that the inserted sentence must be separated from existing words by spaces.
# For example,
#  - s1 = "Hello Jane" and s2 = "Hello my name is Jane" can be made equal by inserting
#    "my name is" between "Hello" and "Jane" in s1.
#  - s1 = "Frog cool" and s2 = "Frogs are cool" are not similar, since although there is a sentence
#    "s are" inserted into s1, it is not separated from "Frog" by a space.
# Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar.
# Otherwise, return false.
# ------------------
# 1 <= sentence1.length, sentence2.length <= 100
# sentence1 and sentence2 consist of lowercase and uppercase English letters and spaces.
# The words in sentence1 and sentence2 are separated by a single space.


def are_sentences_similar(s1: str, s2: str) -> bool:
    # working_sol (86.88%, 96.88%) -> (30ms, 16.38mb)  time: O(s1 + s2) | space: O(s1 + s2)
    # We need to check the shortest option for `left`
    # And the shortest option for `right_1`.
    if len(s1) > len(s2):
        return are_sentences_similar(s2, s1)
    words_1: list[str] = s1.split(' ')
    words_2: list[str] = s2.split(' ')
    left: int = 0
    right_1: int = len(words_1) - 1
    right_2: int = len(words_2) - 1
    while left < len(words_1) and words_1[left] == words_2[left]:
        left += 1
    while 0 <= right_1 and words_1[right_1] == words_2[right_2]:
        right_1 -= 1
        right_2 -= 1
    # Either we used everything or some word wasn't equal == we can't use it.
    return right_1 < left


# Time complexity: O(s1 + s2)
# Splitting both input strings `s1` and `s2` to get all the words => O(s1 + s2).
# Extra traversing all these words, twice == checking all `s1` + `s2` chars => O(3 * (s1 + s2)).
# ------------------
# Auxiliary space: O(s1 + s2)
# `words_1` <- allocates space for each char from `s1` => O(s1).
# `words_2` <- allocates space for each char from `s2` => O(s1 + s2).


test_s1: str = "My name is Haley"
test_s2: str = "My Haley"
test_out: bool = True
assert test_out == are_sentences_similar(test_s1, test_s2)

test_s1 = "of"
test_s2 = "A lot of words"
test_out = False
assert test_out == are_sentences_similar(test_s1, test_s2)

test_s1 = "Eating right now"
test_s2 = "Eating"
test_out = True
assert test_out == are_sentences_similar(test_s1, test_s2)
