# No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.
# Given an integer n, return a list of two integers [a, b] where:
#  - a and b are No-Zero integers.
#  - a + b = n
# The test cases are generated so that there is at least one valid solution.
# If there are many valid solutions, you can return any of them.
# --------------------
# 2 <= n <= 10 ** 4


def get_no_zero_integers(n: int) -> list[int]:
    # working_sol (96.63%, 12.42%) -> (26ms, 16.52mb)  time: O(n) | space: O(1)
    val1: int = 0
    val2: int = 0
    multiplier: int = 1
    while 0 < n:
        digit: int = n % 10
        n //= 10
        if 0 == digit:
            n -= 1
            val1 += 1 * multiplier
            val2 += 9 * multiplier
        elif 1 == digit and n > 0:
            n -= 1
            val1 += 2 * multiplier
            val2 += 9 * multiplier
        else:
            val1 += 1 * multiplier
            val2 += (digit - 1) * multiplier
        multiplier *= 10
    return [val1, val2]


# Time complexity: O(n)
# Always depleting `n` to 0 => O(n).
# --------------------
# Auxiliary space: O(1).
# Only 3 constant INT's none of them depends on input => O(1).


test: int = 2
test_out: list[int] = [1, 1]
assert test_out == get_no_zero_integers(test)

test = 11
test_out = [2, 9]
assert test_out == get_no_zero_integers(test)
