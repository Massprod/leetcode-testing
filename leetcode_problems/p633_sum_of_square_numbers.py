# Given a non-negative integer c,
#  decide whether there're two integers a and b such that a2 + b2 = c.
# ------------------------
# 0 <= c <= 2 ** 31 - 1
import math


def judge_square_sum(c: int) -> bool:
    # working_sol (46.65%, 79.87%) -> (102ms, 16.43mb)  time: O(sqrt(c) * log c) space: O(1)
    a: int = 0
    while a * a <= c:
        b: float = math.sqrt(c - a * a)
        if b.is_integer():
            return True
        a += 1
    return False


# Time complexity: O(sqrt(c) * log c)
# We always check `sqrt(c)` value and for each value we search `sqrt(c - a * a)` => O(sqrt(c) * log c).
# ------------------------
# Auxiliary space: O(1)
# Only two constants used `a`, `b` - none of them depends on input => O(1)


test: int = 5
test_out: bool = True
assert test_out == judge_square_sum(test)

test = 3
test_out = False
assert test_out == judge_square_sum(test)
