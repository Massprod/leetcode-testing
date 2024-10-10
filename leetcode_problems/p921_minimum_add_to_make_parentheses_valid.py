# A parentheses string is valid if and only if:
#  - It is the empty string,
#  - It can be written as AB (A concatenated with B), where A and B are valid strings, or
#  - It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.
#  - For example, if s = "()))", you can insert an opening parenthesis to be "(()))"
#    or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.
# ----------------------------
# 1 <= s.length <= 1000
# s[i] is either '(' or ')'.
from random import choice


def min_add_to_make_valid(s: str) -> int:
    # working_sol (80.00%, 30.64%) -> (31ms, 16.54mb)  time: O(s) | space: O(s)
    stack: list[str] = []
    # If we have `opened` => 100% needs to have `closed` after it.
    # If we can't close it with anything after => we need to insert `closed`.
    # And if we got `closed` without any `opened` => we need to insert `opened`.
    out: int = 0
    for char in s:
        if '(' == char:
            stack.append(char)
        elif stack and '(' == stack[-1]:
            stack.pop()
        else:
            out += 1
    return out + len(stack)


# Time complexity: O(s).
# Always traversing whole input string `s`, once => O(s).
# ----------------------------
# Auxiliary space: O(s)
# In the worst case, there's only `opened` brackets.
# `stack` <- allocates space for each char from `s` => O(s).


test: str = "())"
test_out: int = 1
assert test_out == min_add_to_make_valid(test)

test = "((("
test_out = 3
assert test_out == min_add_to_make_valid(test)

test = ''.join([choice(['(', ')']) for _ in range(1000)])
print(test)
