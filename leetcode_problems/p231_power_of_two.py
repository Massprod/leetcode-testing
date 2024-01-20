# Given an integer n, return true if it is a power of two.
# Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2 ** x.
# ---------------------------
# -2 ** 31 <= n <= 2 ** 31 - 1
# ---------------------------
# Follow up: Could you solve it without loops/recursion?


def is_power_of_two(n: int) -> bool:
    # working_sol (79.72%, 53.73%) -> (35ms, 16.54mb)  time: O(1) | space: O(1)
    # 0 - can't be a power of 2.
    if not n:
        return False
    # For any value of 2 ** X, we have only 1 bit set.
    # So, if change it by (-1) we will get set bit switched to 0, and everything else is 1,
    # None will be equally set and & returns 0.
    # Otherwise, we will get some number == not power of 2.
    return not n & n - 1


# Time complexity: O(1).
# Auxiliary space: O(1).


test: int = 1
test_out: bool = True
assert test_out == is_power_of_two(test)

test = 16
test_out = True
assert test_out == is_power_of_two(test)

test = 3
test_out = False
assert test_out == is_power_of_two(test)

test = 146
test_out = False
assert test_out == is_power_of_two(test)

test = 64
test_out = True
assert test_out == is_power_of_two(test)
