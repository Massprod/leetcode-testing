# Given a balanced parentheses string s, return the score of the string.
# The score of a balanced parentheses string is based on the following rule:
#  - "()" has score 1.
#  - AB has score A + B, where A and B are balanced parentheses strings.
#  - (A) has score 2 * A, where A is a balanced parentheses string.
# -----------------------
# 2 <= s.length <= 50
# s consists of only '(' and ')'.
# s is a balanced parentheses string.


def score_of_parentheses(s: str) -> int:
    # working_sol (100.00%, 46.62%) -> (0ms, 17.76mb)  time: O(s) | space: O(s)
    stack: list[int] = []

    for char in s:
        if '(' == char:
            stack.append(0)
        else:
            val: int = stack.pop()
            # Close single bracket.
            if 0 == val:
                stack.append(1)
            # Gather the whole sequence.
            else:
                subscore: int = val
                while 0 != stack[-1]:
                    subscore += stack.pop()
                stack.pop()
                stack.append(subscore * 2)
    
    return sum(stack)


# Time complexity: O(s)
# Always traversing each char of the input string `s` => O(s).
# -----------------------
# Auxiliary space: O(s)
# Because the `s` is balanced, in the worst case `stack` holds half of the `s` => O(s).


test: str = '()'
test_out: int = 1
assert test_out == score_of_parentheses(test)

test = '(())'
test_out = 2
assert test_out == score_of_parentheses(test)

test = '()()'
test_out = 2
assert test_out == score_of_parentheses(test)

test = '(()(()))'
test_out = 6
assert test_out == score_of_parentheses(test)
