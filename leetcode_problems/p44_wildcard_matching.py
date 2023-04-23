# Given an input string (s) and a pattern (p), implement wildcard pattern matching
# with support for '?' and '*' where:
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

def wildcard_match(s: str, p: str) -> bool:
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
        if pat_cursor < pat_len and s[str_cursor] == p[pat_cursor] and p[pat_cursor] == any_sign:
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
