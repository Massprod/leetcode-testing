# Given a string s which represents an expression, evaluate this expression and return its value.
# The integer division should truncate toward zero.
# You may assume that the given expression is always valid.
# All intermediate results will be in the range of [-2 ** 31, 2 ** 31 - 1].
# Note: You are not allowed to use any built-in function which evaluates
#  strings as mathematical expressions, such as eval().
# -------------------------
# 1 <= s.length <= 3 * 10 ** 5
# s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range [0, 2 ** 31 - 1].
# The answer is guaranteed to fit in a 32-bit integer.


def calculate(s: str) -> int:
    # working_sol (39.97%, 9.30%) -> (118ms, 22.90mb)  time: O(s) | space: O(s)
    cur_num: int
    stack: list[int | str] = []
    cur_int: list[str] = []
    # There's always some operand between numbers.
    # We can't have cases like: "3  2 + 2 * 2".
    for char in s:
        if ' ' == char:
            continue
        if char.isdigit():
            cur_int.append(char)
        else:
            if stack and stack[-1] == '*':
                cur_num = int(''.join(cur_int))
                cur_int = []
                stack.pop()
                stack.append(stack.pop() * cur_num)
                stack.append(char)
            elif stack and stack[-1] == '/':
                cur_num = int(''.join(cur_int))
                cur_int = []
                stack.pop()
                stack.append(stack.pop() // cur_num)
                stack.append(char)
            else:
                stack.append(int(''.join(cur_int)))
                cur_int = []
                stack.append(char)
    if cur_int:
        cur_num = int(''.join(cur_int))
        if stack:
            if stack[-1] == '*':
                stack.pop()
                stack.append(stack.pop() * cur_num)
            elif stack[-1] == '/':
                stack.pop()
                stack.append(stack.pop() // cur_num)
            else:
                stack.append(cur_num)
        else:
            stack.append(cur_num)
    out: int = stack[0]
    for index in range(1, len(stack)):
        if stack[index] == "+":
            out += stack[index + 1]
        elif stack[index] == "-":
            out -= stack[index + 1]
    return out


# Time complexity: O(s)
# Always traversing whole `s` => O(s).
# Extra traversing `stack` which is going to store every num from `s` => O(2 * s).
# -------------------------
# Auxiliary space: O(s)
# `cur_int` <- in the worst case, can be of size `s` if there's only 1 number in `s` => O(s).
# `stack` <- will store every num from `s` => O(s).
# !
# TODO:
#  Not completely correct, but im done for today, maybe change it to a normal description later.
#  It's still linear, so it's not a big deal.
# !


test: str = "3+2*2"
test_out: int = 7
assert test_out == calculate(test)

test = " 3/2 "
test_out = 1
assert test_out == calculate(test)

test = " 3+5 / 2 "
test_out = 5
assert test_out == calculate(test)

test = " 3 + 5/ 2/ 3 * 4"
test_out = 3
assert test_out == calculate(test)

test = "1 + 1"
test_out = 2
assert test_out == calculate(test)
