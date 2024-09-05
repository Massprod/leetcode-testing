# You have observations of n + m 6-sided dice rolls with each face numbered from 1 to 6.
# n of the observations went missing, and you only have the observations of m rolls.
# Fortunately, you have also calculated the average value of the n + m rolls.
# You are given an integer array rolls of length m where rolls[i] is the value of the ith observation.
# You are also given the two integers mean and n.
# Return an array of length n containing the missing observations such that
#  the average value of the n + m rolls is exactly mean.
# If there are multiple valid answers, return any of them.
# If no such array exists, return an empty array.
# The average value of a set of k numbers is the sum of the numbers divided by k.
# Note that mean is an integer, so the sum of the n + m rolls should be divisible by n + m.
# ----------------------------
# m == rolls.length
# 1 <= n, m <= 10 ** 5
# 1 <= rolls[i], mean <= 6


def missing_rolls(rolls: list[int], mean: int, n: int) -> list[int]:
    # working_sol (27.27%, 93.32%) -> (1037ms, 26.07mb)  time: O(n + k) | space: O(n)
    # mean = (sum(n_rolls) + sum(m_rolls)) // (n + m)
    # We know sum(m_rolls) => sum(n_rolls) = (n + m) * mean - sum(m_rolls)
    out: list[int] = []
    sum_n_rolls: int = mean * (n + len(rolls)) - sum(rolls)
    # 1. We can't even use `1` as every roll value.
    # 2. We can't have more than `6` value on every roll, and we're given more than (6 * rolls)
    if sum_n_rolls < n or (6 * n) < sum_n_rolls:
        return out
    # Otherwise, we can take all full parts of `n` and spread the remainder.
    full_parts: int = sum_n_rolls // n
    remainder: int = sum_n_rolls % n
    for _ in range(n):
        out.append(full_parts)
    index: int = 0
    while remainder:
        out[index] += 1
        remainder -= 1
        index += 1
        if index == len(out):
            index = 0
    return out


# Time complexity: O(n + k) <- k - length of the input array `rolls`,
# Always traversing `rolls` to get `sum(rolls)` => O(k).
# Extra spreading `full_parts` for `n` values => O(n + k).
# `remainder` shouldn't be more than `n`, but I still did cycle check.
# Tho, it's never used in big test cases, so I guess we can call it `n` => O(2 * n + k).
# ----------------------------
# Auxiliary space: O(n).
# `out` <- always of the same size `n` => O(n).


test: list[int] = [3, 2, 4, 3]
test_mean: int = 4
test_n: int = 2
test_out: list[int] = [6, 6]
assert test_out == missing_rolls(test, test_mean, test_n)

test = [1, 5, 6]
test_mean = 3
test_n = 4
test_out = [3, 2, 2, 2]
assert test_out == missing_rolls(test, test_mean, test_n)

test = [1, 2, 3, 4]
test_mean = 6
test_n = 4
test_out = []
assert test_out == missing_rolls(test, test_mean, test_n)
