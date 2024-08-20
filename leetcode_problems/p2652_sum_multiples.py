# Given a positive integer n, find the sum of all integers in the range [1, n]
#  inclusive that are divisible by 3, 5, or 7.
# Return an integer denoting the sum of all numbers in the given range satisfying the constraint.
# ------------------------
# 1 <= n <= 10 ** 3


def sum_of_multiples(n: int) -> int:
    # working_sol (84.91%, 80.56%) -> (56ms, 16.45mb)  time: O(n) | space: O(1)
    out: int = 0
    for val in range(3, n + 1):
        if ((not val % 3)
                or (not val % 5)
                or (not val % 7)):
            out += val
    return out


# Time complexity: O(n)
# Always traversing every value from `3` -> `n`, inclusive => O(n).
# ------------------------
# Auxiliary space: O(1)
# Only 1 constant INT is used => O(1).


test: int = 7
test_out: int = 21
assert test_out == sum_of_multiples(test)

test = 10
test_out = 40
assert test_out == sum_of_multiples(test)

test = 9
test_out = 30
assert test_out == sum_of_multiples(test)
