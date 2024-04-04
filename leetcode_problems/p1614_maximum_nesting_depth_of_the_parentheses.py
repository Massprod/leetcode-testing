# A string is a valid parentheses string (denoted VPS) if it meets one of the following:
#   - It is an empty string "", or a single character not equal to "(" or ")",
#   - It can be written as AB (A concatenated with B), where A and B are VPS's, or
#   - It can be written as (A), where A is a VPS.
# We can similarly define the nesting depth depth(S) of any VPS S as follows:
#   - depth("") = 0
#   - depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
#   - depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
#   - depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
# For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2),
#  and ")(" and "(()" are not VPS's.
# Given a VPS represented as string s, return the nesting depth of s.
# ---------------------
# 1 <= s.length <= 100
# s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
# It is guaranteed that parentheses expression s is a VPS.


def max_depth(s: str) -> int:
    # working_sol (71.93%, 38.30%) -> (33ms, 16.57mb)  time: O(n) | space: O(1)
    # We only care about FREE opening brackets before any chars.
    # What we can potentially place after this opening brackets, before it's closed.
    open_br: str = '('
    closed_br: str = ')'
    open_count: int = 0
    out: int = 0
    for char in s:
        if open_br == char:
            open_count += 1
        elif closed_br == char:
            open_count -= 1
        out = max(out, open_count)
    return out


# Time complexity: O(s)
# Single traverse of the whole input array `s`.
# ---------------------
# Auxiliary space: O(1)
# Nothing extra which depends on input.


test: str = "(1+(2*3)+((8)/4))+1"
test_out: int = 3
assert test_out == max_depth(test)

test = "(1)+((2))+(((3)))"
test_out = 3
assert test_out == max_depth(test)

test = "((8+7)*(3+9)-0)*(1*6)"
test_out = 2
assert test_out == max_depth(test)
