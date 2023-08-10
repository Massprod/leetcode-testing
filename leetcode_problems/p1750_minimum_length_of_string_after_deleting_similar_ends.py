# Given a string s consisting only of characters 'a', 'b', and 'c'.
# You are asked to apply the following algorithm on the string any number of times:
#   Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
#   Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
#   The prefix and the suffix should not intersect at any index.
#   The characters from the prefix and suffix must be the same.
#   Delete both the prefix and the suffix.
# Return the minimum length of s after performing the above operation any number of times (possibly zero times).
# ----------------------
# 1 <= s.length <= 10 ** 5
# s only consists of characters 'a', 'b', and 'c'.
from random import choice


def minimum_length(s: str) -> int:
    # working_sol (98.62%, 78.62%) -> (74ms, 17.1mb)  time: O(n) | space: O(1)
    # Symbol to delete.
    symbol: str = ''
    # Pointers for prefix and suffix.
    left_l: int = 0
    right_l: int = len(s) - 1
    while left_l < right_l:
        # Equal symbol == we can delete.
        if s[left_l] == s[right_l]:
            symbol = s[left_l]
            # We only can delete without overlap.
            # So we need to break when index met.
            while s[left_l] == symbol and left_l < right_l:
                left_l += 1
            while s[right_l] == symbol and left_l < right_l:
                right_l -= 1
        else:
            # Zero indexed pointers, extra +1 for correct length.
            return (right_l - left_l) + 1
    # We're always breaking when prefix and suffix meet.
    # But they can meet on last symbol which is still can be deleted ->
    if s[left_l] == symbol:
        return 0
    # -> or it's different symbol, and we can't delete it.
    return 1


# Time complexity: O(n) -> in the worst case, we can delete everything, so it's traverse of whole input_array => O(n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> 2 constant INTs, and extra STR used -> STR can be counted as constant, because we're using
#                          only 1 symbol to store in it => O(1).
# ----------------------
# All easy, but is there better way to switch symbol?
# Like I want to save symbol and delete from both sides, and only after that -> switching it to another
# if left == right. No we can't get another symbol otherwise, cuz they could be not equal. If they're not equal
# we can't assign them and should break.


test: str = "ca"
test_out: int = 2
assert test_out == minimum_length(test)

test = "cabaabac"
test_out = 0
assert test_out == minimum_length(test)

test = "aabccabba"
test_out = 3
assert test_out == minimum_length(test)

test = ''
for _ in range(10 ** 5):
    test += choice(['a', 'b', 'c'])
# print(test)
