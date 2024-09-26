# You are given a 0-indexed string word, consisting of lowercase English letters.
# You need to select one index and remove the letter at that index from word
#  so that the frequency of every letter present in word is equal.
# Return true if it is possible to remove one letter so that the frequency of all letters in word are equal,
#  and false otherwise.
# Note:
#  - The frequency of a letter x is the number of times it occurs in the string.
#  - You must remove exactly one letter and cannot choose to do nothing.
# --------------------------
# 2 <= word.length <= 100
# word consists of lowercase English letters only.
from random import choice
from collections import Counter
from string import ascii_lowercase


def equal_frequency(word: str) -> bool:
    # working_sol (70.89%, 7.93%) -> (33ms, 16.63mb)  time: O(n) | space: O(n)
    # { char: occurrences }
    occurrences: dict[str, int] = Counter(word)
    if 1 == len(occurrences):
        return True
    rem_used: bool = False
    min_occur: int = 110
    char_to_rem: str = ''
    for char, occurs in occurrences.items():
        # We can have multiple `1` occurs, and we can either delete whole `char`.
        # Or leave it, and it will be ok with another `1` occur chars.
        # Because `min_occur` is still going to be `1`.
        if not char_to_rem and 1 == occurs:
            char_to_rem = char
            continue
        min_occur = min(min_occur, occurs)
    if char_to_rem:
        occurrences.pop(char_to_rem)
    # If only 1 char left == we got what we need.
    if 1 == len(occurrences):
        return True
    for value in occurrences.values():
        # We can take only 1 char.
        # And we either already took it before with `1 == occurs`
        # Or we will delete another one with value difference.
        if value != min_occur:
            # We need to delete more than 1.
            if rem_used:
                return False
            # We can decrement only by 1.
            if 1 != (value - min_occur):
                return False
            rem_used = True
    # `1 != min_occur and char_to_rem` <- means we only have one char with occur == 1.
    # And if we also deleted another char, we can't balance it.
    if 1 != min_occur and rem_used and char_to_rem:
        return False
    # `1 == min_occur and char_to_rem` <- means we have more than one char with occur == 1.
    # And we already got it in balance with deleted `char_to_rem`, but we still can delete another `char`.
    if 1 == min_occur and rem_used and char_to_rem:
        return True
    # We just deleted one char occurrence.
    if rem_used and not char_to_rem:
        return True
    # We don't need to delete anything extra, and had some char with occur == 1.
    if not rem_used and char_to_rem:
        return True
    # We can't balance in other cases.
    return False


# Time complexity: O(n) <- n - length of the input string `word`.
# In the worst case every char in `word` is unique.
# Always traversing it once to get all unique values occurrences => O(n).
# Extra traversing `occurrences.values() == n` to get single occurrence char and `min_occur` => O(2 * n).
# Another traverse of every value to get how many occurrences we need to remove => O(3 * n).
# --------------------------
# Auxiliary space: O(n)
# `occurrences` <- allocates space for each unique char from `word` => O(n).


test: str = "abcc"
test_out: bool = True
assert test_out == equal_frequency(test)

test = "bac"
test_out = True
assert test_out == equal_frequency(test)

test = "aazz"
test_out = False
assert test_out == equal_frequency(test)

test = "ceeeec"
test_out = False
assert test_out == equal_frequency(test)

test = ''.join([choice(ascii_lowercase) for _ in range(100)])
print(test)
