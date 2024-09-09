# Given two integers, num and t.
# A number is achievable if it can become equal to num after applying the following operation:
# Increase or decrease the number by 1, and simultaneously increase or decrease num by 1.
# Return the maximum achievable number after applying the operation at most t times.
# ----------------------
# 1 <= num, t <= 50
from random import randint


def the_maximum_achievable_x(num: int, t: int) -> int:
    # working_sol (32.86%, 66.40%) -> (42ms, 16.41mb)  time: O(1) | space: O(1)
    # We don't care about anything, except `t`.
    # Because w.e the number `target` we choose, we still need to get to `num`.
    # And the best option is to REDUCE it by 1 and instantly add 1 to `num`.
    # And because we're limited by `t`, we can make only `t` * 2 moves.
    # So, our `target` is always == `num` + `t` * 2.
    return num + t * 2


# Time complexity: O(1)
# ----------------------
# Auxiliary space: O(1)


test: int = 4
test_t: int = 1
test_out: int = 6
assert test_out == the_maximum_achievable_x(test, test_t)

test = 3
test_t = 2
test_out = 7
assert test_out == the_maximum_achievable_x(test, test_t)

test = randint(1, 50)
test_t = randint(1, 50)
print(f'`num`: {test}\n`t`: {test_t}')
