# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
#  determine if the input string is valid.
# An input string is valid if:
#   - Open brackets must be closed by the same type of brackets.
#   - Open brackets must be closed in the correct order.
#   - Every close bracket has a corresponding open bracket of the same type.
# -------------------
# 1 <= s.length <= 10 ** 4
# s consists of parentheses only '()[]{}'.


def is_valid(s: str) -> bool:
    # working_sol (91.10%, 93.85%) -> (32ms, 16.1mb)  time: O(n) | space: O(n)
    stack: list[str] = []
    # (close, open)
    valid: dict[str, str] = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    for bracket in s:
        # Opener.
        if bracket not in valid:
            stack.append(bracket)
        # Close bracket, with opener.
        elif stack:
            # Correct pair.
            if stack[-1] == valid[bracket]:
                stack.pop()
            # Incorrect.
            else:
                return False
        # Close bracket, but no openers.
        else:
            return False
    # Something unclosed.
    if stack:
        return False
    return True


# Time complexity: O(n) -> worst case == half of indexes will be openers and other half is closers ->
# n - len of input string^^| -> then we will add openers in a stack and close them after, using half indexes twice =>
#                            => O(n).
# Auxiliary space: O(n) -> worst case == everything is openers -> our stack will store every symbol of input => O(n).


test: str = "()"
test_out: bool = True
assert test_out == is_valid(test)

test = "()[]{}"
test_out = True
assert test_out == is_valid(test)

test = "(]"
test_out = False
assert test_out == is_valid(test)

test = "()[]{)}["
test_out = False
assert test_out == is_valid(test)

test = "]}()[]{}"
test_out = False
assert test_out == is_valid(test)

test = "([})((][{}))[{())]}]"
test_out = False
assert test_out == is_valid(test)

test = "{[((()))]}"
test_out = True
assert test_out == is_valid(test)

test = "[([{}()]))]"
test_out = False
assert test_out == is_valid(test)
