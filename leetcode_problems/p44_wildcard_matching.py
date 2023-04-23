# Given an input string (s) and a pattern (p), implement wildcard pattern matching
# with support for '?' and '*' where:
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

def wildcard_match(s: str, p: str) -> bool:
    pass


test1 = "aa"
test1_pattern = "a"
test1_out = False

test2 = "aa"
test2_pattern = "*"
test2_out = True

test3 = "cb"
test3_pattern = "?a"
test3_out = False

test4 = "aa"
test4_pattern = "*a"
test4_out = True
