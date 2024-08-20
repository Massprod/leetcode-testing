# You are given a string s.
# Your task is to remove all digits by doing this operation repeatedly:
#  - Delete the first digit and the closest non-digit character to its left.
# Return the resulting string after removing all digits.
# ---------------------
# 1 <= s.length <= 100
# s consists only of lowercase English letters and digits.
# The input is generated such that it is possible to delete all digits.


def clear_digits(s: str) -> str:
    # working_sol (78.08%, 92.46%) -> (34ms, 16.34mb)  time: O(s) | space: O(s)
    stack: list[str] = []
    for char in s:
        if char.isdigit() and stack:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)


# Time complexity: O(s)
# Always traversing whole `s`, once => O(s).
# In the worst case there are no digits, we extra traverse all chars to join => O(2 * s).
# ---------------------
# Auxiliary space: O(s)
# `stack` <- allocates space for all chars from `s` => O(s).


test: str = "abc"
test_out: str = "abc"
assert test_out == clear_digits(test)

test = "cb34"
test_out = ""
assert test_out == clear_digits(test)
