# You are given an array of strings tokens that represents
# an arithmetic expression in a Reverse Polish Notation.
# Evaluate the expression. Return an integer that represents the value of the expression.
# Note that:
#   The valid operators are '+', '-', '*', and '/'.
#   Each operand may be an integer or another expression.
#   The division between two integers always truncates toward zero.
#   There will not be any division by zero.
#   The input represents a valid arithmetic expression in a reverse polish notation.
#   The answer and all the intermediate calculations can be represented in a 32-bit integer.
# -----------------------------
# 1 <= tokens.length <= 104
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].


def eval_rpn(tokens: list[str]) -> int:
    # working_sol (43.14%, 52.21%) -> (84ms, 16.6mb)  time: O(n) | space: O(log n)
    path: list[int] = []
    for x in range(len(tokens)):
        if tokens[x] == "+":
            new: int = path[-2] + path[-1]
            path.pop()
            path[-1] = new
            continue
        if tokens[x] == "-":
            new: int = path[-2] - path[-1]
            path.pop()
            path[-1] = new
            continue
        if tokens[x] == "*":
            new: int = int(path[-2] * path[-1])
            path.pop()
            path[-1] = new
            continue
        if tokens[x] == "/":
            new: int = int(path[-2] / path[-1])
            path.pop()
            path[-1] = new
            continue
        path.append(int(tokens[x]))
    return path[-1]


# Time complexity: O(n) -> traversing whole input once => O(n).
# n - length of input_list^^
# Space complexity: O(log n) -> only part with integers of input_list will be stored in path => O(log n)
# -----------------------------
# Wow, they didn't trick us in the description. Rare occasion.
# -----------------------------
# Should I check for errors?
# Because in the description => | The input represents a valid arithmetic expression in a reverse polish notation. | ->
# -> so inputs like this: ["1", "+", "-"] should be incorrect, and shouldn't be presented in test_cases.
# Guess I need to fail to check this, because if we trust in description it's ok.
# Otherwise, I need to check len of path, and ignore operands if there's less than 2 values inside
# -----------------------------
# !
#  In reverse Polish notation, the operators follow their operands. For example, to add 3 and 4 together,
# the expression is 3 4 + rather than 3 + 4. The expression 3 − 4 + 5 in conventional notation is 3 4 − 5 +
# in reverse Polish notation: 4 is first subtracted from 3, then 5 is added to it.
#  The concept of a stack, a last-in/first-out construct, is integral to the left-to-right evaluation of RPN.
# In the example 3 4 -, first the 3 is put onto the stack, then the 4; the 4 is now on top and the 3 below it.
# The subtraction operator removes the top two items from the stack, performs 3 - 4,
# and puts the result of -1 onto the stack. !
# Wiki page was given as a reference and I had no idea about this RPN, so it's correct to use this.


test1 = ["2", "1", "+", "3", "*"]
test1_out = 9
print(eval_rpn(test1))
assert test1_out == eval_rpn(test1)

test2 = ["4", "13", "5", "/", "+"]
test2_out = 6
print(eval_rpn(test2))
assert test2_out == eval_rpn(test2)

test3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
test3_out = 22
print(eval_rpn(test3))
assert test3_out == eval_rpn(test3)

test4 = ["1"]
test4_out = 1
print(eval_rpn(test4))
assert test4_out == eval_rpn(test4)

test5 = ["3", "4", "*", "5", "6", "*", "+"]
test5_out = 42
print(eval_rpn(test5))
assert test5_out == eval_rpn(test5)
