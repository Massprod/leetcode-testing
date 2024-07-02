# Alice has n candies, where the ith candy is of type candyType[i].
# Alice noticed that she started to gain weight, so she visited a doctor.
# The doctor advised Alice to only eat n / 2 of the candies she has (n is always even).
# Alice likes her candies very much, and she wants to eat the maximum number
#  of different types of candies while still following the doctor's advice.
# Given the integer array candyType of length n,
#  return the maximum number of different types of candies she can eat if she only eats n / 2 of them.
# ---------------------
# n == candyType.length
# 2 <= n <= 10 ** 4
# n is even.
# -10 ** 5 <= candyType[i] <= 10 ** 5
from random import randint


def distribute_candies(candies: list[int]) -> int:
    # working_sol (78.07%, 56.31%) -> (595ms, 18.71mb)  time: O(n) | space: O(n)
    max_candies: int = len(candies) // 2
    types: set[int] = set(candies)
    return len(types) if len(types) <= max_candies else max_candies


# Time complexity: O(n) <- n - length of the input array `candies`.
# Always traversing the input array `candies`, once => O(n).
# ---------------------
# Auxiliary space: O(n).
# The worst case: every value in `candies` are unique, so we will store all of them in `types` => O(n).


test: list[int] = [1, 1, 2, 2, 3, 3]
test_out: int = 3
assert test_out == distribute_candies(test)

test = [1, 1, 2, 3]
test_out = 2
assert test_out == distribute_candies(test)

test = [6, 6, 6, 6]
test_out = 1
assert test_out == distribute_candies(test)

test = [randint(-10 ** 5, 10 ** 5) for _ in range(10 ** 4)]
print(test)
