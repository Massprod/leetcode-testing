# Given an input string s and a pattern p,
# implement regular expression matching with support for '.' and '*' where:
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).


def is_match(s: str, p: str) -> bool:


test0 = "aba"
ptest0 = "aa"
test1 = "aa"
ptest1 = "a"
test2 = "aa"
ptest2 = "a*"
test3 = "ab"
ptest3 = ".*"
test4 = "ab"
ptest4 = ".*c"
test5 = "aab"
ptest5 = "c*a*b"
test6 = "mississippi"
ptest6 = "mis*is*ip*."
# test6 fail:
# Forgot about last symbol in pattern can be ANY(.)
test7 = "aaa"
ptest7 = "a*a"
# test7 fail:
# Was thinking that we needed to MATCH everything in pattern if we have something left after .* - it's FALSE
# apparently we should stop and check for ALL
test8 = "mississippi"
ptest8 = "mis*is*p*."
# test8 fail:
# Was ignoring symbols if they are not in a pattern and continue counting
test9 = "aaa"
ptest9 = "ab*a*c*a"
test10 = "ab"
ptest10 = ".*.."
# After googling this task all I have done before is pointless cuz this Task is like INTRO for recursion
# and I can't solve it with just 1 loop
# print(is_match(test0, ptest0))  # false
# print(is_match(test1, ptest1))  # false
# print(is_match(test2, ptest2))  # true
# print(is_match(test3, ptest3))  # true
# print(is_match(test4, ptest4))  # false
# print(is_match(test5, ptest5))  # true
# print(is_match(test6, ptest6))  # true
# print(is_match(test7, ptest7))  # true
# print(is_match(test8, ptest8))  # false
# print(is_match(test9, ptest9))  # true
# print(is_match(test10, ptest10))  # true
