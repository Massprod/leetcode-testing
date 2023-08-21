# Given two strings word1 and word2,
#   return the minimum number of operations required to convert word1 to word2.
# You have the following three operations permitted on a word:
#   - Insert a character
#   - Delete a character
#   - Replace a character
# --------------
# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.
from string import ascii_lowercase
from random import choice


def min_distance(word1: str, word2: str) -> int:
    # working_sol (46.69%, 83.92%) -> (147ms, 18.9mb)  time: O(m * n) | space: O(m * n)
    recur_cache: dict[tuple[int, int]: int] = {}

    def do_option(index_1: int, index_2: int) -> int:
        if (index_1, index_2) in recur_cache:
            return recur_cache[index_1, index_2]
        # We can't delete or replace when word1 exhausted,
        # so only option left is to Insert.
        # Assume we build correct string so far,
        # so we need to Insert everything what's left in word2
        # into word1 -> len(word2) - index_2.
        # Extra we need to include Index from what we called,
        # so we don't need to zero_index len().
        if index_1 == len(word1):
            return len(word2) - index_2
        # Same approach, but we Delete everything what's left in word1.
        if index_2 == len(word2):
            return len(word1) - index_1
        # If symbols are equal, then we have correct pair set,
        # don't need to do anything. Skipping both indexes.
        if word1[index_1] == word2[index_2]:
            return do_option(index_1 + 1, index_2 + 1)
        # We check strings symbol by symbol, and choose every possible option.
        recur_cache[index_1, index_2] = min(
            1 + do_option(index_1 + 1, index_2),  # Delete symbol from word1
            1 + do_option(index_1, index_2 + 1),  # Insert symbol in word1
            1 + do_option(index_1 + 1, index_2 + 1),  # Replace symbol in word1
        )
        return recur_cache[index_1, index_2]

    return do_option(0, 0)


# Time complexity: O(m * n) -> standard recursion with 3 options is O(3 ** k), where k is min(len(word1), len(word2) ->
# n - len of word1^^|  -> but we're using memorization, so it's should be O(m * n), cuz all combinations of indexes
# m - len of word2^^|  will be used only once.
# Auxiliary space: O(m * n) -> every index combination will be stored in cache dictionary => O(m * n) ->
#                           -> extra recursion stack will be either m or n size at max, so it's dominated|ignored.
# --------------
# Returning to this after a long time, but still confused.
# Like it should be just a recursion with 3 options:
#   - delete any symbol
#   - insert any symbol
#   - replace any symbol
# But how? Like obviously we need to save symbols which already correctly set.
# But how we can decide on which to delete or replace?
# Ok. We don't need to decide anything, we can just use every index and do any of these options.
# Choose minimum counter and return it.
# Delete -> just deleting index from word1 and trying to check other indexes.
# Insert -> we assume that we inserted some symbol on w.e place we wanted, so it's correctly set
#           symbol from word2, skipping index from word2.
# Replace -> same as Insert, but we're skipping both indexes, cuz we replaced symbol from word2 -> word1,
#            and now symbols on this index correctly set.


test_1: str = "horse"
test_2: str = "ros"
test_out: int = 3
assert test_out == min_distance(test_1, test_2)

test_1 = "intention"
test_2 = "execution"
test_out = 5
assert test_out == min_distance(test_1, test_2)

test_1 = ''
test_2 = ''
for _ in range(500):
    test_1 += choice(ascii_lowercase)
    test_2 += choice(ascii_lowercase)
print(test_1)
print('------------------')
print(test_2)
