# The Tribonacci sequence Tn is defined as follows:
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.
# --------------
# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2 ** 31 - 1.


def tribonacci(n: int) -> int:
    # working_sol (92.15%, 67.36%) -> (39ms, 16.27mb)  time: O(n) | space: O(n)
    # T0,T1,T2 by default + values to n, included
    tribo: list[int] = [0, 1, 1] + [0 for _ in range(n - 2)]
    # n -> inclusive.
    for x in range(3, n + 1):
        tribo[x] = tribo[x - 3] + tribo[x - 2] + tribo[x - 1]
    return tribo[n]


# Time complexity: O(n) -> creating array of n size, and traversing it from 3 to n indexes => O(n).
# n - input value ^^|
# Auxiliary space: O(n) -> array of n size => O(n) -> could be done with O(1), with just saving last 3 values we need.
# --------------
# So in other words Tn = Tn-3 + Tn-2 + Tn-1 ?


test: int = 4
test_out: int = 4
assert test_out == tribonacci(test)

test = 25
test_out = 1389537
assert test_out == tribonacci(test)
