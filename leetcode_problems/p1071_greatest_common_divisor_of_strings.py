# For two strings s and t, we say "t divides s" if and only if s = t + ... + t
#   (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
# -------------------
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.
from string import ascii_uppercase
from random import choice


def gcd_of_strings(str1: str, str2: str) -> str:
    # working_sol (87.20%, 10.62%) -> (38ms, 16.4mb)  time: O(K * (m + n) | space: O(m + n + K)
    check_1: set[str] = set(str1)
    check_2: set[str] = set(str2)
    # Some symbols not presented in both strings.
    # We can't use them correctly in one of the strings.
    if check_1 != check_2:
        return ''
    # Taking smallest, and building from it.
    # Cuz it's either correct smallest of some part of it,
    # bigger one is just extra indexes to delete, and we don't need it.
    greatest: str = ""
    if len(str1) > len(str2):
        # We need to check str1|str2 for division,
        # so we need a deepcopy of one to build from.
        greatest = str2[::-1][::-1]
    else:
        greatest = str1[::-1][::-1]
    # Deleting symbols one by one.
    # So we're always going to have the greatest subarray possible.
    while len(greatest) != 0:
        # Current length of subarray.
        cur_len: int = len(greatest)
        # We can't divide them correctly for equal parts ->
        if len(str1) % cur_len != 0 or len(str2) % cur_len != 0:
            # -> skip and try smaller, symbols doesn't matter,
            # because we won't be able to build correct string from it anyway.
            greatest = greatest[:-1]
            continue
        correct: bool = True
        # Using slices instead of index_checks.
        # So we need to know FROM index and TO index.
        left_l: int = 0
        right_l: int = cur_len
        while right_l <= len(str1):
            if str1[left_l:right_l] == greatest:
                # Slicing SUB + SUB + SUB.
                # So we can just increment by SUB size.
                left_l += cur_len
                right_l += cur_len
                continue
            # If any slice isn't correct, we can't build correctly.
            correct = False
            break
        # Both should be correctly divisible by this sub.
        # So we can just ignore second string.
        if not correct:
            greatest = greatest[:-1]
            continue
        # Same approach for second string.
        left_l = 0
        right_l = cur_len
        while right_l <= len(str2):
            if str2[left_l:right_l] == greatest:
                left_l += cur_len
                right_l += cur_len
                continue
            correct = False
            break
        # If all were correct, it's the greatest SUB we need.
        # Because we're going backwards from max_len to 0.
        if correct:
            return greatest
        greatest = greatest[:-1]
    return greatest


# Time complexity: O(K * (m + n)) -> sets check for symbols is always => O(m + n) -> copying one string => O(n)|O(m) ->
# n - len of str1^^| -> we're filtering options with incorrect lengths and breaking after first incorrect encounter,
# m - len of str2^^| dunno how to calc correctly, but should be something like O(K * ???) <- where K is len(greatest) ->
# K - len of sub^^|  -> but how to calc inside loops, if it's correct loop then, it's even O(K * len(str1) / K +),
#                    if I understand correctly slicing and '==' still should check index by index, extra second string
#                    O(+ K * len(str2) / K) -> K is always changing by -1 if incorrect, how to implement it?
#                    O((K * len(str1) / K) + (K * len(str2) / K)) <- repeat from K to 0. Wait then it's just K ->
#                    O(K * ((K * len(str1) / K) + (K * len(str2) / K))) <- but how to do changed K for insides.
#                    Total lack of math on it, but maybe => O(K * (len(str1) + len(str2))) => O(K * (m + n)) ->
#                    -> actually seems correct, like for case with only last indexes being incorrect we're going to
#                    check every index of str1 and str2 for K times, where K is len(greatest) and we changing it by -1.
#                    Something like 'AAAAAAAAAABB' and 'AAA', every index of s1 will be checked 3 times. Only part
#                    which 99% incorrect is that we're breaking from loop without correct = False, so second string is
#                    going to be ignored but (m + n) still consider it. W.e leaving it like this.
# Auxiliary space: O(m + n + K) -> saving sets of m and n sizes => O(m + n) -> creating copy of smallest string,
#                    which is first subarray to check => O(K) -> and 4 extra constants => O(1).
# -------------------
# Ok. Working for max constraints and some test_cases, but it's faster to just fail and see tricky parts.
# Changed brute_force from checking index by index -> to slice check, and everything else is same.
# -------------------
# Brute force? With trying using whole smallest string, and decrease it symbol by symbol until correct hit?
# Should be correct for these constraints, let's try.


test_1: str = "ABCABC"
test_2: str = "ABC"
test_out: str = "ABC"
assert test_out == gcd_of_strings(test_1, test_2)

test_1 = "ABABAB"
test_2 = "ABAB"
test_out = "AB"
assert test_out == gcd_of_strings(test_1, test_2)

test_1 = "LEET"
test_2 = "CODE"
test_out = ""
assert test_out == gcd_of_strings(test_1, test_2)

test_1 = ""
test_2 = ""
for _ in range(100):
    test_1 += choice(ascii_uppercase)
    test_2 += choice(ascii_uppercase)
# print(test_1)
# print('------------')
# print(test_2)
