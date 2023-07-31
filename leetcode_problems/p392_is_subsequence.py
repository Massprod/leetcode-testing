# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string
#   by deleting some (can be none) of the characters without disturbing the relative positions
#   of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
# --------------
# 0 <= s.length <= 100
# 0 <= t.length <= 10 ** 4
# s and t consist only of lowercase English letters.
# --------------
# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 10 ** 9,
#   and you want to check one by one to see if t has its subsequence.
# In this scenario, how would you change your code?
from string import ascii_lowercase
from random import choice


def is_subsequence(s: str, t: str) -> bool:
    # working_sol (98.3%, 91.54%) -> (35ms, 16.3mb)  time: O(n) | space: O(1)
    # Empty string is always correct.
    if len(s) == 0:
        return True
    # Empty string in which we search can't be empty.
    if len(t) == 0:
        return False
    # If symbols we need, more than we presented in T.
    if len(s) > len(t):
        return False
    # Symbol pointer.
    s_index: int = 0
    for _ in t:
        # If symbol is present, we can point to next.
        if s[s_index] == _:
            s_index += 1
        # If all symbols used -> correct
        if s_index == len(s):
            return True
    # Not all used -> incorrect.
    return False


# Time complexity: O(n) -> traversing whole input_T, once => O(n).
# n - len of input_T_array^^| Ω(log n) -> on media we will break at some point, cuz on average S is smaller than T.
# Auxiliary space: O(1) -> nothing extra, except one INT which doesnt depend on input => O(1).
# --------------
# Focused on follow_up too much, and missed that we have empty strings in constraints and failed commit...
# --------------
# Left to right for input_s and just check if everything present in input_t.
# For the follow_up -> we can just record everything, and insta return if same S is given.
# But for others, what can be done? Like we can't record semi_options, one I see for more is that
# count symbols in T and insta return if something isn't present from S. But it's still 1 traverse of S,
# and we could do the T traverse with it, not really faster.
# What if we store original S give, and save PREFIX + SUFFIX for it.
# Like dict[S] = [PREFIX(everything we met before first symbol) + S(itself) + SUFFIX(everything after last symbol)]
# Then we could check "gabc" after "abc" recorded, and we can drop everything from "gabc" which present in S.
# And just check "g" in prefix. But it's still traverse of whole input_S and after some part of input_T.
# Well at least its just part not whole. So we're basically deleting part of new S given and depending on where
# was that part we're trying to find in PREFIX or SUFFIX for this S deleted.
# But we need to find correct S in it, which is bad. So I guess it could work, but it's not really much faster
# than just standard check and fastest way is still to reuse duplicates.
# Extra we will need to use something like sliding_window to find stored data in dictionary,
# and maybe with very_large input_T, and small input_S it's faster but overall not much difference.
# Ok. I see, we're given constraint for T 10 ** 4 and 100 for S, so yeah. It should be faster to find
# already checked S in dictionary then recheck T. But still not building it for follow_up,
# it's some HARD problem and no reasons to, but it should work.


test1_s = "abc"
test1_t = "ahbgdc"
test1_out = True
assert test1_out == is_subsequence(test1_s, test1_t)

test2_s = "axc"
test2_t = "ahbgdc"
test2_out = False
assert test2_out == is_subsequence(test2_s, test2_t)

test_s: str = ""
test_t: str = ""
for _ in range(100):
    test_s += choice(ascii_lowercase)
for _ in range(10 ** 4):
    test_t += choice(ascii_lowercase)
print(test_s)
print("---------------------")
print(test_t)
