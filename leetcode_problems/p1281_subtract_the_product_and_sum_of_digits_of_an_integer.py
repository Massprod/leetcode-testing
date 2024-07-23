# Given an integer number n,
#  return the difference between the product of its digits and the sum of its digits.
# ---------------------
# 1 <= n <= 10 ** 5


def subtract_product_and_sum(n: int) -> int:
    # working_sol (80.74%, 16.94) -> (31ms, 16.52mb)  time: O(n) | space: O(1)
    _sum: int = 0
    _prod: int = 1
    while n:
        digit: int = n % 10
        _sum += digit
        _prod *= digit
        n //= 10
    return _prod - _sum


# Time complexity O(n).
# Always depleting `n` to 0 => O(n).
# ---------------------
# Auxiliary space: O(1).
# Only 3 constant INT's used, none of them depends on input => O(1).


test: int = 234
test_out: int = 15
assert test_out == subtract_product_and_sum(test)

test = 4421
test_out = 21
assert test_out == subtract_product_and_sum(test)
