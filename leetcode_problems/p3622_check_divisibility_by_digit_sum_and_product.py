# You are given a positive integer n. Determine whether n is divisible
#  by the sum of the following two values:
#  - The digit sum of n (the sum of its digits).
#  - The digit product of n (the product of its digits).
# Return true if n is divisible by this sum; otherwise, return false.
# --- --- --- ---
# 1 <= n <= 10 ** 6
from math import prod


def check_divisibility(n: int) -> bool:
    # working_solution: (100%, 54.72%) -> (0ms, 19.36mb)  Time: O(n) Space: O(n)
    t_n: int = n
    digits: list[int] = []
    while t_n:
        digit: int = t_n % 10
        digits.append(digit)
        t_n //= 10
    # ! The digit sum of n (the sum of its digits). !
    d_sum: int = sum(digits)
    # ! The digit product of n (the product of its digits). !
    d_prod: int = prod(digits)
    t_sum: int = d_sum + d_prod
    
    return 0 == (n % t_sum)


# Time complexity: O(n)
# --- --- --- ---
# Space complexity: O(n)


test: int = 99
test_out: bool = True
assert test_out == check_divisibility(test)

test = 23
test_out = False
assert test_out == check_divisibility(test)

test = 285
test_out = True
assert test_out == check_divisibility(test)
