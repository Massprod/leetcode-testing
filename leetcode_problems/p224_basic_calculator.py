# Given a string s representing a valid expression,
#   implement a basic calculator to evaluate it, and return the result of the evaluation.
# Note: You are not allowed to use any built-in function which evaluates strings
#   as mathematical expressions, such as eval().
# ---------------------
# 1 <= s.length <= 3 * 10 ** 5
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
# '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
# There will be no two consecutive operators in the input.
# Every number and running calculation will fit in a signed 32-bit integer.


def calculate(s: str) -> int:
    # working_sol (43.67%, 89.34%) -> (108ms, 17.7mb)  time: O(n) | space: O(n)
    # Not using deque() it's overkill for this.
    list_que: list[int | str] = []
    # Set value to negative.
    negative: bool = False
    # Pointer in a string.
    point: int = 0
    while point < len(s):
        # Space is skipped no matter what.
        if s[point] == ' ':
            point += 1
            continue
        # Closing parenthesis ->
        elif s[point] == ')':
            point += 1
            # -> setting current value for these parentheses ->
            current: int = 0
            # -> que commands until open parenthesis->
            while list_que[-1] != '(':
                current += list_que.pop()
            # -> remove open parenthesis ->
            list_que.pop()
            # -> extra 'neg' trigger for negative values inside parentheses ->
            if len(list_que) != 0 and list_que[-1] == 'neg':
                # -> remove trigger ->
                list_que.pop()
                # -> add this parentheses value.
                list_que.append(current * -1)
                continue
            list_que.append(current)
        # Any value after this, should be negative.
        elif s[point] == '-':
            negative = True
            point += 1
        # Open parentheses ->
        elif s[point] == '(':
            # -> extra trigger for negative result.
            if negative:
                list_que.append('neg')
                # Reset, any negative values inside will be added separately.
                negative = False
            list_que.append('(')
            point += 1
        # Only symbol unchecked is '+' -> so it's actually digits.
        # And we can ignore any '+' anyway.
        elif s[point] != '+':
            # Current digit to combine with ->
            digits: str = s[point]
            point += 1
            # -> combining every other digits we meet ->
            while point != len(s) and s[point] != '+' and s[point] != '-'\
                    and s[point] != ')' and s[point] != '(':
                if s[point] != ' ':
                    digits += s[point]
                point += 1
            # -> make it negative if flagged.
            if negative:
                list_que.append(int(digits) * - 1)
                negative = False
                continue
            list_que.append(int(digits))
        # If it's '+' skip. Just without check for '+'.
        else:
            point += 1
    # We count everything inside parentheses and add every value outside of them.
    # Everything is having correctly set signs, so we can just summarize after.
    return sum(list_que)


# Time complexity: O(n) -> traversing whole input_array, once -> but for every parentheses we're going to
# n - len of input_array^^| extra use stored values, to calculate these parentheses value ->
#                           -> in the worst case like (((1+1)+(1+1)-(1+1))), we're going to use every index twice,
#                           so it should be O(2n), cuz we're using either whole value or single digits if it's only
#                           digits then we're traversing whole array again to calculate parentheses, otherwise
#                           only a part => O(n).
# Auxiliary space: O(n) -> worst case (1+1+1+1..etc) -> every index will be stored into a list_que => O(n) ->
#                       -> actually even more than n indexes will be stored, because for every '-' before open_bracket
#                       we're adding 'neg' which is extra, but we can't use more than 1 operator consecutive.
#                       So it's only one 'neg' per open_bracket only if it's before it. Other indexes will dominate.
# ---------------------
# So basically deque() or just a list with commands, and only tricky part I see is that we need to reverse
# sign of parentheses if there's '-' before it.
# Ok. Seems working, but I need test_cases.
# A lot can be rebuilt, but not today. Maybe after revisiting. Normal results anyway.


test: str = "1 + 1"
test_out: int = 2
assert test_out == calculate(test)

test = " 2-1 + 2 "
test_out = 3
assert test_out == calculate(test)

test = "(1+(4+5+2)-3)+(6+8)"
test_out = 23
assert test_out == calculate(test)

test = "   ((((1 + 1 - 22 - 34 +(-10+24)) -122-123     )-(-23)-99+12+100+9999)-123)-10000        "
test_out = -373
assert test_out == calculate(test)

test = "-(-10-9-1+1)-(-23-23+(-1)+(-120)+(-1)-(-100)-(15)+109)"
test_out = -7
assert test_out == calculate(test)
