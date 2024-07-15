# A valid parentheses string is either empty "", "(" + A + ")",
#  or A + B, where A and B are valid parentheses strings, and + represents string concatenation.
#  - For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty,
#  and there does not exist a way to split it into s = A + B,
#  with A and B nonempty valid parentheses strings.
# Given a valid parentheses string s,
#  consider its primitive decomposition: s = P1 + P2 + ... + Pk,
#  where Pi are primitive valid parentheses strings.
# Return s after removing the outermost parentheses
#  of every primitive string in the primitive decomposition of s.
# ------------------------
# 1 <= s.length <= 10 ** 5
# s[i] is either '(' or ')'.
# s is a valid parentheses string.

def remove_outermost_parentheses(s: str) -> str:
    # working_sol (80.87%, 98.23%) -> (35ms, 16.47mb)  time: O(s) | space: O(s)
    out: list[str] = []
    openers: int = 0
    closers: int = 0
    stack: list[str] = []
    # ! s is a valid parentheses string. !
    # So, we don't care about anything, except deleting [0] and [-1] from `stack`.
    for char in s:
        if '(' == char:
            openers += 1
        elif ')' == char:
            closers += 1
        stack.append(char)
        if openers == closers:
            out += stack[1:len(stack)-1]
            stack = []
            openers, closers = 0, 0
    return ''.join(out)


# Time complexity: O(s)
# Always traversing whole input string `s`, twice to add value into stack and slice it after => O(2s).
# Extra joining them after, in the worst-case, we should delete only 2 elements => O(2s + (s - 2))
# ------------------------
# Auxiliary space: O(s).
# `stack` will allocate space for every symbol from `s` => O(s).
# `out` is going to be of size == `s - 2` => O(s + (s - 2)).


test: str = "(()())(())"
test_out: str = "()()()"
assert test_out == remove_outermost_parentheses(test)

test = "(()())(())(()(()))"
test_out = "()()()()(())"
assert test_out == remove_outermost_parentheses(test)

test = "()()"
test_out = ""
assert test_out == remove_outermost_parentheses(test)
