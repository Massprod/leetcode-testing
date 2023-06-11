# Given an integer n, return the number of prime numbers that are strictly less than n.
# --------------
# 0 <= n <= 5 * 10 ** 6
from math import sqrt, ceil


def count_primes(n: int) -> int:
    # working_sol (27.75%, 5.25%) -> (5149ms, 107.5mb)  time: O(n * log log n) | space: O(n)
    if n <= 2:
        return 0
    all_values: list[int] = [False, False] + [True for _ in range(2, n)]
    square: int = ceil(sqrt(n))
    for p in range(2, square):
        if all_values[p]:
            j: int = p * p
            while j < n:
                all_values[j] = False
                j += p
    primes: int = 0
    for _ in all_values:
        if _:
            primes += 1
    return primes


# Time complexity: O(n * log log n)
# n - input value^^|
# Auxiliary space: O(n) -> creating list of input_n size + 2 => O(n).
# --------------
# No way without extra info -> https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes


test1 = 10
test1_out = 4
assert test1_out == count_primes(test1)

test2 = 0
test2_out = 0
assert test2_out == count_primes(test2)

test3 = 1
test3_out = 0
assert test3_out == count_primes(test3)

test4 = 4000001
test4_out = 283146
assert test4_out == count_primes(test4)
