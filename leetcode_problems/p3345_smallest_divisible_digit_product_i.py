# You are given two integers n and t.
# Return the smallest number greater than or equal to n such that the product of its digits is divisible by t.
# ----------------------
# 1 <= n <= 100
# 1 <= t <= 10


def smallest_number(n: int, t: int) -> int:
    # working_sol (100.00%, 5.43%) -> (0ms, 17.34mb)  time: O(k * d) | space: O(1)
    if 0 == t:
        return -1

    def digit_prod(value: int) -> int:
        out: int = 1
        while value:
            digit: int = value % 10
            out *= digit
            if 0 == out:
                return 0
            value //= 10
        return out

    while 0 != (digit_prod(n) % t):
        n += 1
    return n


# Time complexity: O(k * d) <- k - number of increments, d - average digits in used values.
# Increment value until we hit a target => O(k * d).
# ----------------------
# Auxiliary space: O(1)
# Only 2 extra INTs used, and we're not stacking calls on `digit_prod` => O(1).


test_n: int = 10
test_t: int = 2
test_out: int = 10
assert test_out == smallest_number(test_n, test_t)

test_n = 15
test_t = 3
test_out = 16
assert test_out == smallest_number(test_n, test_t)
