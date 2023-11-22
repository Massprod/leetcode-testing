# Given an integer x, return true if x is a palindrome, and false otherwise.
#
# Follow up: Could you solve it without converting the integer to a string?
# ------------------------
# -2 ** 31 <= x <= 2 ** 31 - 1


def is_palindrome(x: int) -> bool:
    # working_sol (66.92%, 43.50%) -> (58ms, 16.2mb)  time: O(log x) | space: O(1)
    # '-' no way around negative sign.
    if x < 0:
        return False
    # (10 ** w.e) no way around first 1. Except 0.
    if x % 10 == 0 and x > 0:
        return False
    # Deconstruct by taking last digits of 'x', one by one.
    half: int = 0
    while x > half:
        half = half * 10 + x % 10
        x //= 10
    # Even or Odd palindrome.
    # In both cases 'half' will be higher|equal than original 'x' and we need extra check.
    return x == half or x == half // 10


# Time complexity: O(log x) -> essentially we will check only part of the input 'x' => O(log x).
# Auxiliary space: O(1) -> only 1 constant INT => O(1).


test: int = 121
test_out: bool = True
assert test_out == is_palindrome(test)

test = -121
test_out = False
assert test_out == is_palindrome(test)

test = 10
test_out = False
assert test_out == is_palindrome(test)
