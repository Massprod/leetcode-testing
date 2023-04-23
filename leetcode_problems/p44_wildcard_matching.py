# Given an input string (s) and a pattern (p), implement wildcard pattern matching
# with support for '?' and '*' where:
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

def wildcard_match(s: str, p: str) -> bool:
    # working_sol (87.71%, 95.3%) -> (54ms, 13.9mb)  time: O(n) | space: O(1)
    str_cursor = 0
    str_len = len(s)
    pat_cursor = 0
    pat_len = len(p)
    wild_sign = "*"
    any_sign = "?"
    last_index = 0
    wildcard = -1
    while str_cursor < str_len:
        if pat_cursor < pat_len and s[str_cursor] == p[pat_cursor]:
            str_cursor += 1
            pat_cursor += 1
            continue
        if pat_cursor < pat_len and p[pat_cursor] == any_sign and s[str_cursor] != p[pat_cursor]:
            str_cursor += 1
            pat_cursor += 1
            continue
        if pat_cursor < pat_len and p[pat_cursor] == wild_sign:
            last_index = str_cursor
            wildcard = pat_cursor
            pat_cursor += 1
            continue
        if wildcard != -1:
            pat_cursor = wildcard + 1
            str_cursor = last_index + 1
            last_index += 1
            continue
        return False
    while pat_cursor < len(p):
        if p[pat_cursor] == wild_sign:
            pat_cursor += 1
            continue
        return False
    return True

# Time complexity: O(n) -> looping once through whole input (pattern + string -> 1n + 1n), linear scale with input.
# Space complexity: O(1) -> no matter what input size, we're using same constants.

# Most tricky part of this task, is to skip WILDCARD and check for a left available options.
# Because we can skip WILDCARDS, we're just ignoring them and looping through a left options with a pat_cursor.


test1 = "aa"
test1_pattern = "a"
test1_out = False
print(wildcard_match(test1, test1_pattern))
assert wildcard_match(test1, test1_pattern) == test1_out

test2 = "aa"
test2_pattern = "*"
test2_out = True
print(wildcard_match(test2, test2_pattern))
assert wildcard_match(test2, test2_pattern) == test2_out

test3 = "cb"
test3_pattern = "?a"
test3_out = False
print(wildcard_match(test3, test3_pattern))
assert wildcard_match(test3, test3_pattern) == test3_out

test4 = "aa"
test4_pattern = "*a"
test4_out = True
print(wildcard_match(test4, test4_pattern))
assert wildcard_match(test4, test4_pattern) == test4_out

# test5 - failed -> cursor value in pattern shouldn't be equal to string cursor, but can be any_sign,
#                   and I was checking for equality.
test5 = "ab"
test5_pattern = "?*"
test5_out = True
print(wildcard_match(test5, test5_pattern))
assert wildcard_match(test5, test5_pattern) == test5_out


test6 = "abcd"
test6_pattern = "ab*cd*"
test6_out = True
print(wildcard_match(test6, test6_pattern))
