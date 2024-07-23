# Given an integer n, return any array containing n unique integers such that they add up to 0.
# -----------------------
# 1 <= n <= 1000


def sum_zero(n: int) -> list[int]:
    # working_sol (88.79%, 50.04%) -> (31ms, 16.66mb)  time: O(n) | space: O(n)
    out: list[int] = []
    cur_val: int = 1
    if n % 2:
        out.append(0)
        n -= 1
    while n:
        out.append(cur_val)
        out.append(cur_val * -1)
        cur_val += 1
        n -= 2
    return out


# Time complexity: O(n)
# Always depleting `n` to 0 => O(n).
# -----------------------
# Auxiliary space: O(n)
# `out` is always of size `n` => O(n).


test: int = 5
test_out: list[int] = [0, 1, -1, 2, -2]
assert test_out == sum_zero(test)

test = 3
test_out = [0, 1, -1]
assert test_out == sum_zero(test)

test = 1
test_out = [0]
assert test_out == sum_zero(test)
