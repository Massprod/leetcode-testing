# Given a string s containing only three types of characters: '(', ')'
#  and '*', return true if s is valid.
# The following rules define a valid string:
#  - Any left parenthesis '(' must have a corresponding right parenthesis ')'.
#  - Any right parenthesis ')' must have a corresponding left parenthesis '('.
#  - Left parenthesis '(' must go before the corresponding right parenthesis ')'.
#  - '*' could be treated as a single right parenthesis ')' or a single left parenthesis '('
#    or an empty string "".
# -------------------------
# 1 <= s.length <= 100
# s[i] is '(', ')' or '*'.
from random import choice
from collections import deque


def check_valid_string(s: str) -> bool:
    # working_sol (74.42%, 50.32%) -> (33ms, 16.54mb)  time: O(s) | space: O(s)
    # [index of the '(' bracket]
    open_stack: deque[int] = deque([])
    # [index of the '*' wildcard]
    wild_stack: deque[int] = deque([])
    open_br: str = '('
    close_br: str = ')'
    wild_card: str = '*'
    # Best options is to use the closest open_brackets with close_brackets.
    # And to leave Furthest(from open_brackets) wildcards.
    for index, char in enumerate(s):
        if open_br == char:
            open_stack.append(index)
        elif close_br == char:
            if not open_stack:
                if wild_stack:
                    wild_stack.popleft()
                    continue
                else:
                    return False
            open_stack.pop()
        elif wild_card == char:
            wild_stack.append(index)
    # There's not enough `*` to close all the `(`.
    if len(open_stack) > len(wild_stack):
        return False
    while open_stack and wild_stack:
        if open_stack[0] < wild_stack[0]:
            open_stack.popleft()
            wild_stack.popleft()
            continue
        while wild_stack and open_stack[0] > wild_stack[0]:
            wild_stack.popleft()
    return 0 == len(open_stack)


# Time complexity: O(s)
# Standard stack problem with using of every index, at most 2 times => O(2s)
# -------------------------
# Auxiliary space: O(s)
# Worst case: we're only given `*` and `(`.
# So, we will store all of them in both stacks == 2 stacks with size of `s` => O(2s).


test: str = "()"
test_out: bool = True
assert test_out == check_valid_string(test)

test = "(*)"
test_out = True
assert test_out == check_valid_string(test)

test = "(*))"
test_out = True
assert test_out == check_valid_string(test)

test = "(*)()*)))**(()**)((())*(())*()(*))((()(*()*****)*()((**)*()*)**))()*)*)*))*(((***()()**)()(**)*))*))"
test_out = False
assert test_out == check_valid_string(test)

test = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
test_out = False
assert test_out == check_valid_string(test)

test = "*(*)(*))((*)*)))(*)())*())()(()*)*)****)())(()()*(*(*())()((())))*()****)(*(()))((*()*(**(*()*)*()"
test_out = True
assert test_out == check_valid_string(test)

test = "(*(()))((())())*(**(()))((*)()(()))*(())()(())(()"
test_out = False
assert test_out == check_valid_string(test)

test = ''.join([choice(['(', ')', '*']) for _ in range(100)])
print(test)
