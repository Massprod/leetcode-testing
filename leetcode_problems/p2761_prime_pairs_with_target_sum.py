# You are given an integer n. We say that two integers x and y form a prime number pair if:
#   1 <= x <= y <= n
#   x + y == n
#   x and y are prime numbers
# Return the 2D sorted list of prime number pairs [xi, yi].
# The list should be sorted in increasing order of xi.
# If there are no prime number pairs at all, return an empty array.
# Note: A prime number is a natural number greater than 1 with only two factors, itself and 1.
# ---------------------
# 1 <= n <= 10 ** 6
from math import isqrt


def find_prime_pairs(n: int) -> list[list[int]]:
    # working_sol (82.58%, 30.69%) -> (3896ms, 34.4mb)  time: O(n * log(log(n))) | space: O(n + log n)
    if n <= 3:
        return []
    # Every index is integer in range 0 -> n (inclusive).
    # 0, 1 -> Not primes.
    is_prime: list[int] = [True for _ in range(n + 1)]
    is_prime[0], is_prime[1] = False, False
    # Sieve of Eratosthenes algorithm.
    for num in range(2, int(n ** 0.5) + 1):
        if is_prime[num]:
            for val in range(num * num, n + 1, num):
                is_prime[val] = False
    correct_primes: list[list[int]] = []
    # We only need values y > x and x + y == n ->
    # -> so we can use only half, otherwise it's x + y > n.
    # 0, 1 -> Not primes, and n should be inclusive.
    for x in range(2, n // 2 + 1):
        y: int = n - x
        if is_prime[x] and is_prime[y]:
            correct_primes.append([x, y])
    return correct_primes


# Time complexity: O(n * log(log(n))) -> ! the inner loop runs at most n/p times for each prime number p,
# n - input value^^|                       so it has a time complexity of O(n/2 + n/3 + n/5 + …),
#                                          which is approximately O(n * log(log(n))). ! ->
#                                          -> and final loop to get correct primes, is O(n // 2) => O(n * log(log(n))).
# Auxiliary space: O(n + log n) -> storing all not/primes for n, every index is value from 0 -> n (inclusive) => O(n) ->
#                          -> extra we're creating another array to store correct combinations ->
#                          -> dunno what worst case can be here, but obviously they can't be all primes to use,
#                          so it's some part of (n // 2) used for x, and y O(2 * log (n // 2)) ?? ->
#                          -> only using half of values from 2 -> n (inclusive) to get x and same for y =>
#                          => so it should take double space for some correct part of half_n == log(n // 2) =>
#                          => O(n + 2 * log n) => O(n + log n).
# ---------------------
# Ok. Was slow, cuz I used dictionary which is slower to populate then list.
# And I used indexes as values to get primes, but then brain-lagged and rebuild it into
# dictionary to get them in O(1), but it's already index == value.
# So we can just loop through indexes.
# ---------------------
# Pure math problem, unsolvable without knowing -> Sieve of Eratosthenes Algorithm.
# Cuz strict TimeLimit.


test_n: int = 10
test_out = [[3, 7], [5, 5]]
assert test_out == find_prime_pairs(test_n)

test_n = 2
test_out = []
assert test_out == find_prime_pairs(test_n)
