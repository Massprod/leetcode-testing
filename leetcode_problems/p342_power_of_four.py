# Given an integer n, return true if it is a power of four.
# Otherwise, return false.
# An integer n is a power of four, if there exists an integer x such that n == 4 ** x.
# ----------------
# -2 ** 31 <= n <= 2 ** 31 - 1


def is_power_of_four(n: int) -> bool:
    # working_sol (62.89%, 99.16%) -> (39ms, 16mb)  time: O(n) | space: O(1)
    if n == 1:
        return True
    while n > 4:
        n /= 4
    return n == 4


# Time complexity: O(n) -> linear grow with input size, higher => more divisions => O(n).
# Auxiliary space: O(1) -> nothing extra.


test: int = 16
test_out: bool = True
assert test_out == is_power_of_four(test)

test = 5
test_out = False
assert test_out == is_power_of_four(test)

test = 1
test_out = True
assert test_out == is_power_of_four(test)
