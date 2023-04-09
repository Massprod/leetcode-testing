# Given an input string s and a pattern p,
# implement regular expression matching with support for '.' and '*' where:
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

def is_match(s: str, p: str) -> bool:
    to_check = s
    pattern = p
    any_sign = "."
    wild = "*"
    if not pattern:  # every time we call recurs, checking for string to be more than 1 symbol
        if not to_check:  # same with pattern
            return True  # if string 0 and pattern 0 symbols left. We can assume that's all checked
        return False  # otherwise string is exhausted and pattern NOT, something unchecked
    elif not to_check:  # if no symbols left in string
        if len(pattern) > 1 and pattern[1] == wild:  # and pattern still have wildcard
            return is_match(to_check, pattern[2:])  # we call it with slice from wildcard
        return False  # otherwise same break as before
    elif len(pattern) == 1:  # if only 1 symbol is left to check
        if len(to_check) == 1 and (pattern[0] == any_sign or pattern[0] == to_check[0]):  # we checking it for correct pattern or any_sign
            return True  # if it's correct, it's means all symbols in pattern and original string is checked
        return False  # otherwise  some symbols unchecked and len's is 0
    elif pattern[1] != wild:  # checking second symbol in pattern to be NOT wildcard
        if pattern[0] == any_sign or pattern[0] == to_check[0]:  # if it's not wildcard we can just compare them
            return is_match(to_check[1:], pattern[1:])  # and if they're checked, we can slice from them and check again
        return False  # otherwise we have a pair which can't be resolved, so it's False
    elif len(pattern) > 3 and pattern[3] == "*" and pattern[0] == pattern[2]:  # if we have 2 wildcards in a row
        return is_match(to_check, pattern[2:])  # we just slice one of them OFF, and check again
    elif to_check[0] != pattern[0] and pattern[0] != any_sign:  # checking 0 symbols, if they're not equal
        return is_match(to_check, pattern[2:])  # even if there's [1] and it's wildcard we still slice it from [2] and removing [0][1] because they can't be used
    return is_match(to_check[1:], pattern) or is_match(to_check, pattern[2:]) or is_match(to_check[1:], pattern[2:])  # left options
    # 1option: to_check[0] == pattern[0] and pattern[1] == wildcard . we slicing element from string and check next symbol to be equal to wildcard
    # 2option: to_check[0] != pattern[0] and pattern[1] == wildcard . we slicing from wildcard and string unchanged
    # 3option: to_check[0] == pattern[0] and pattern[1] == wildcard . we slicing element from string and next symbol is not equal to wildcard

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
print(is_match(test0, ptest0))  # false
print(is_match(test1, ptest1))  # false
print(is_match(test2, ptest2))  # true
print(is_match(test3, ptest3))  # true
print(is_match(test4, ptest4))  # false
print(is_match(test5, ptest5))  # true
print(is_match(test6, ptest6))  # true
print(is_match(test7, ptest7))  # true
print(is_match(test8, ptest8))  # false
print(is_match(test9, ptest9))  # true
print(is_match(test10, ptest10))  # true
