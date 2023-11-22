# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.
#   0 <= x <= 2 ** 31 - 1
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
# ---------------
# 0 <= x <= 2 ** 31 - 1

def my_sqrt(x: int) -> int:
    # working_sol (94.81%, 65.86%) -> (39ms, 16.2mb)  time: O(log (x // 2)) | space: O(1)
    if x <= 1:
        return x
    # Standard BinarySearch.
    left_l: int = 1
    # If it's perfect square then it's at max (x // 2) <- sqr(4) == 2.
    # Otherwise, it's lower. Assume maximum square limit == (x // 2).
    right_l: int = x // 2
    while left_l < right_l:
        middle: int = (left_l + right_l) // 2 + 1
        if middle * middle <= x:
            left_l = middle
        else:
            right_l = middle - 1
    return left_l


# Time complexity: O(log (x // 2)) -> standard BS from 1 -> (x // 2) inclusive => O(log (x //2 )).
# Auxiliary space: O(1) -> only 3 constant INTs use, none of them depends on input => O(1).


test: int = 4
test_out: int = 2
assert test_out == my_sqrt(test)

test = 8
test_out = 2
assert test_out == my_sqrt(test)

test = 2 ** 31 - 1
test_out = 46340
assert test_out == my_sqrt(test)

test = 1
test_out = 1
assert test_out == my_sqrt(test)
