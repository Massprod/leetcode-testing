# Run-length encoding is a string compression method that works by replacing
#  consecutive identical characters (repeated 2 or more times) with the concatenation of the character
#  and the number marking the count of the characters (length of the run).
# For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3".
# Thus the compressed string becomes "a2bc3".
# Notice that in this problem, we are not adding '1' after single characters.
# Given a string s and an integer k.
# You need to delete at most k characters from s such that the run-length encoded version
#  of s has minimum length.
# Find the minimum length of the run-length encoded version of s after deleting at most k characters.
# -------------------
# 1 <= s.length <= 100
# 0 <= k <= s.length
# s contains only lowercase English letters.
from functools import cache
from random import choice
from string import ascii_lowercase


def get_length_of_optim_compression(s: str, k: int) -> int:
    # working_sol (97%, 91%) -> (1197ms, 20.9mb)  time: O(n ** 2 * k) | space: O(n * k)

    @cache
    def check(index: int, deletions: int) -> int:
        if index == -1:
            return 0
        out: int = 10000
        # Delete any single symbol, if we can.
        if deletions > 0:
            out = check(index - 1, deletions - 1)
        symbol: str = s[index]
        streak: int = 0
        deleted: int = 0
        # Or try to continue streak(sequence) with that symbol as far as we can.
        # Until we hit another symbol, delete other symbols while we can delete them.
        # And find maximum sequence we can have with that `s[index]` symbol.
        # To cover cases like: 'aaabcdaaa', we can continue 'a3' as 'a6' with deletion of 'bcd'.
        for x in range(index, -1, - 1):
            if symbol == s[x]:
                streak += 1
            else:
                deleted += 1
            # We can't delete more than 'k' times, or what's left of it == 'deletions'.
            if deleted > deletions:
                break
            if streak == 1:
                streak_length: int = 0
            else:
                streak_length = len(str(streak))
            # +1 - for symbol itself  ,  +streak_length - size of compression number.
            out = min(out, check(x - 1, deletions - deleted) + 1 + streak_length)
        return out

    return check(len(s) - 1, k)


# Time complexity: O(n ** 2 * k) <- n - length of input string `s`.
# We will check all (n * k) states => O(n * k).
# And for every state we will traverse some part of the string, for 0 it's all string => O(n * k * n).
# -------------------
# Auxiliary space: O(n * k)
# Using @cache to store all the (n * k) states => O(n * k).
# -------------------
# We have 2 options:
# delete any symbol and try to build from another
# OR
# use current symbol and try to build maximum sequence with it.
# Because we need to continue sequence like: 'aabaa', in this case best way is to delete 'b' and use 'a4' as compress.
# So, we can just continue building 'a' sequence from [0] OR [1]. How to calc compress number?
# Store how many 'a' we meet with INT and convert to STR when needed? Extra case with 'a1' => 'a'.
# Base end case for backtrack? 0? Yep '0' and choose minimum options from backtrack.


test: str = "aaabcccd"
test_k: int = 2
test_out: int = 4
assert test_out == get_length_of_optim_compression(test, test_k)

test = "aabbaa"
test_k = 2
test_out = 2
assert test_out == get_length_of_optim_compression(test, test_k)

test = "aaaaaaaaaaa"
test_k = 0
test_out = 3
assert test_out == get_length_of_optim_compression(test, test_k)

test = ''.join([choice(ascii_lowercase) for _ in range(100)])
print(test)
