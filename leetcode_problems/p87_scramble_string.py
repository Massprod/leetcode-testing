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
import random
from string import ascii_lowercase


def is_scramble(s1: str, s2: str) -> bool:
    if len(s1) == 1 and s1 == s2:
        return True
    if len(s1) == 1 and s1 != s2:
        return False
    storage: dict = {}

    def slice_search(string: str, check: str) -> bool:
        if string == check:
            return True
        if not len(string):
            return True
        if sorted(string) != sorted(check):
            return False
        if len(string) != len(check):
            return False
        added: str = string + " " + check
        if added in storage:
            return storage[added]
        flag: bool = False
        for index in range(1, len(string)):
            left: str = string[:index]
            left_check: str = check[:index]
            right: str = string[index:]
            right_check: str = check[index:]
            if slice_search(left, left_check) and slice_search(right, right_check):
                flag = True
                storage[added] = flag
                return True
            reverse_left: str = string[-index:]
            reverse_right: str = string[:-index]
            if slice_search(reverse_left, left_check) and slice_search(reverse_right, right_check):
                flag = True
                storage[added] = flag
                return True
        storage[added] = flag
        return False
    if slice_search(s1, s2):
        return True
    return False

# This is some combination stuff, but with changing slices?
# For every index in s1 slice it call recursion with resulted 2 slices: swapped, un_swapped.
# repeat and give input of slice index?
# x + 1 - right slice start -> s[x + 1:]
# x - left slice end -> s[:x]


test1_s1 = "great"
test1_s2 = "rgeat"
test1_out = True
assert test1_out is is_scramble(test1_s1, test1_s2)
print(is_scramble(test1_s1, test1_s2))

test2_s1 = "abcde"
test2_s2 = "caebd"
test2_out = False
assert test2_out is is_scramble(test2_s1, test2_s2)
print(is_scramble(test2_s1, test2_s2))

test3_s1 = "a"
test3_s2 = "a"
test3_out = True
assert test3_out is is_scramble(test3_s1, test3_s2)
print(is_scramble(test3_s1, test3_s2))

test4_s1 = "abcdefgth"
test4_s2 = "gfedcbath"
test4_out = True
assert test4_out is is_scramble(test4_s1, test4_s2)
print(is_scramble(test4_s1, test4_s2))

test5_s1 = "abcdefghijklmnopq"
test5_s2 = "efghijklmnopqcadb"
test5_out = False
assert test5_out is is_scramble(test5_s1, test5_s2)
print(is_scramble(test5_s1, test5_s2))
