# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


def isValid(s: str) -> bool:
    chars = []
    valid = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    check = list(s)
    for _ in check:
        chars.append(_)
        if _ in valid.keys() and len(chars) == 1:  # check if added element is END
            return False
        if _ in valid.keys() and valid[_] == chars[-2]:  # check if added element is  END, but we have START unclosed
            chars.pop()
            chars.pop()
        elif _ in valid.values():  # check if added element is START
            continue
        else:
            return False
    if len(chars) == 0:
        return True
    return False


# print(isValid("()"))
# print(isValid("()[]{}"))
# print(isValid("()[]{)}["))
# print(isValid("]}()[]{}"))
# print(isValid("(]"))
# print(isValid("([})((][{}))[{())]}]"))
# print(isValid("([)]"))
# print(isValid("()]"))
# print(isValid("()[]{})"))
# print(isValid("{[((()))]}"))
print(isValid("[([{}()]))]"))