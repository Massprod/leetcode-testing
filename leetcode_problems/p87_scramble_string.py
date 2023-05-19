# We can scramble a string s to get a string t using the following algorithm:
#   If the length of the string is 1, stop.
#   If the length of the string is > 1, do the following:
#       1) Split the string into two non-empty substrings at a random index,
#       i.e., if the string is s, divide it to x and y where s = x + y.
#       2) Randomly decide to swap the two substrings or to keep them in the same order.
#       i.e., after this step, s may become s = x + y or s = y + x.
#       3) Apply step 1 recursively on each of the two substrings x and y.
# Given two strings s1 and s2 of the same length,
# return true if s2 is a scrambled string of s1, otherwise, return false.
# -----------------
# s1.length == s2.length  ,  1 <= s1.length <= 30
# s1 and s2 consist of lowercase English letters.


def is_scramble(s1: str, s2: str) -> bool:
    pass


test1_s1 = "great"
test1_s2 = "rgeat"
test1_out = True

test2_s1 = "abcde"
test2_s2 = "caebd"
test2_out = False

test3_s1 = "a"
test3_s2 = "a"
test3_out = True
