# Given a positive integer num, return true if num is a perfect square or false otherwise.
# A perfect square is an integer that is the square of an integer.
# In other words, it is the product of some integer with itself.
# You must not use any built-in library function, such as sqrt.
# ------------------
# 1 <= num <= 2 ** 31 - 1


def is_perfect_square(num: int) -> bool:
    # working_sol (95.00%, 54.56%) -> (29ms, 16.58mb)  time: O(log num) | space: O(1)
    left: int = 1
    # There's no perfect square with: n * n when n > (n // 2)
    right: int = num // 2
    while left <= right:
        middle: int = (left + right) // 2
        if (middle * middle) < num:
            left = middle + 1
        else:
            right = middle - 1
    return (left * left) == num


# Standard BS algo.
# Time complexity: O(log num).
# Auxiliary space: O(1).


test: int = 16
test_out: bool = True
assert test_out == is_perfect_square(test)

test = 14
test_out = False
assert test_out == is_perfect_square(test)

test = 333
test_out = False
assert test_out == is_perfect_square(test)

test = 121
test_out = True
assert test_out == is_perfect_square(test)
