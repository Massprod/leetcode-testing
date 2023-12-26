# You have n dice, and each die has k faces numbered from 1 to k.
# Given three integers n, k, and target, return the number of possible ways (out of the k ** n total ways)
#  to roll the dice, so the sum of the face-up numbers equals target.
# Since the answer may be too large, return it modulo 10 ** 9 + 7.
# ------------------
# 1 <= n, k <= 30
# 1 <= target <= 1000
from functools import cache


def num_rolls_to_target(n: int, k: int, target: int) -> int:
    # working_sol (80.10%, 6.87%) -> (205ms, 23.2mb)  time: O(target * n * k) | space: O(target * n)

    @cache
    def check(dices: int, path_sum: int) -> int:
        if path_sum > target:
            return 0
        # Bad wording in description.
        # We need to ROLL ALL DICES not just some part which can give us `target`.
        if not dices:
            if path_sum == target:
                return 1
            return 0
        paths: int = 0
        for roll in range(1, k + 1):
            paths += check(dices - 1, path_sum + roll)
        return paths

    return check(n, 0) % (10 ** 9 + 7)


# Time complexity: O(target * n * k) <- all input values with same names.
# We will have (target * n) states of recursion to memorise => O(target * n).
# And in each recursion call we have loop (1 -> k, inclusive) => O(target * n * k).
# ------------------
# Auxiliary space: O(target * n).
# We memorise every state of the recursion call.


test: int = 1
test_k: int = 6
test_target: int = 3
test_out: int = 1
assert test_out == num_rolls_to_target(test, test_k, test_target)

test = 2
test_k = 6
test_target = 7
test_out = 6
assert test_out == num_rolls_to_target(test, test_k, test_target)

test = 30
test_k = 30
test_target = 500
test_out = 222616187
assert test_out == num_rolls_to_target(test, test_k, test_target)
