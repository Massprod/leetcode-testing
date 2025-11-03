# You are given a positive integer n.
# A positive integer is a base-10 component if it is the product of a single digit
#  from 1 to 9 and a non-negative power of 10.
# For example, 500, 30, and 7 are base-10 components, while 537, 102, and 11 are not.
# Express n as a sum of only base-10 components,
#  using the fewest base-10 components possible.
# Return an array containing these base-10 components in descending order.
# --- --- --- ---
# 1 <= n <= 10 ** 9


def decimal_representation(n: int) -> list[int]:
    # working_solution: (100%, 88.72%) -> (0ms, 17.68mb)  Time: O(n) Space: O(n)
    out: list[int] = []
    base: int = 1
    while n:
        digit: int = n % 10
        if 0 != digit:
            out.append(digit * base)
        base *= 10
        n //= 10

    return out[::-1]


# Time complexity: O(n)
# Using every digit of the `n`, once => O(n).
# --- --- --- ---
# Space complexity: O(n)
# In the worst case, every digit is non-zero.
# `out` <- allocates space for each digit of `n` => O(n).


test: int = 537
test_out: list[int] = [500, 30, 7]
assert test_out == decimal_representation(test)

test = 102
test_out = [100, 2]
assert test_out == decimal_representation(test)

test = 6
test_out = [6]
assert test_out == decimal_representation(test)
