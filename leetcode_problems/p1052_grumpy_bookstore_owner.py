# There is a bookstore owner that has a store open for n minutes.
# Every minute, some number of customers enter the store.
# You are given an integer array customers of length n where customers[i] is the number
#  of the customer that enters the store at the start of the ith minute
#  and all those customers leave after the end of that minute.
# On some minutes, the bookstore owner is grumpy.
# You are given a binary array grumpy where grumpy[i] is 1
#  if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.
# When the bookstore owner is grumpy, the customers of that minute are not satisfied,
#  otherwise, they are satisfied.
# The bookstore owner knows a secret technique to keep themselves not grumpy
#  for minutes consecutive minutes, but can only use it once.
# Return the maximum number of customers that can be satisfied throughout the day.
# ---------------------------
# n == customers.length == grumpy.length
# 1 <= minutes <= n <= 2 * 10 ** 4
# 0 <= customers[i] <= 1000
# grumpy[i] is either 0 or 1.
from random import randint


def max_satisfied(customers: list[int], grumpy: list[int], minutes: int) -> int:
    # working_sol (99.65%, 38.37%) -> (196ms, 18.91mb)  time: O(n + k) | space: O(1)
    # Standard sliding window.
    all_satisfied: int = 0
    # First, we care about how many we can satisfy without changes.
    for index in range(len(customers)):
        all_satisfied += customers[index] if not grumpy[index] else 0
    # Then a first window we can change.
    for index in range(minutes):
        all_satisfied += customers[index] if grumpy[index] else 0
    out: int = all_satisfied
    left_l: int = 0
    # And all other window placements.
    for index in range(minutes, len(customers)):
        # We change the mood from 0 -> 1, so we need to reduce.
        all_satisfied -= customers[left_l] if grumpy[left_l] else 0
        left_l += 1
        # We change the mood from 1 -> 0, so we need to increase.
        all_satisfied += customers[index] if grumpy[index] else 0
        out = max(out, all_satisfied)
    return out


# Time complexity: O(n + k) <- n - length of the input arrays `customers` or `grumpy`,
#                              k - input value `minutes`.
# We're always traversing whole input array `customers` once,
#  to get `all_satisfied` customers before any changes => O(n).
# Then we're traversing `minutes` range of indexes to get changes made by the first window => O(k).
# In the worst case, we're going to have `minutes` == 1.
# In this case, we're traversing (n - 1) indexes of `customers` again => O(n - 1 + n + k).
# ---------------------------
# Auxiliary space: O(1)
# Only 3 constant INT's used, none of them depends on the input => O(1).


test: list[int] = [1, 0, 1, 2, 1, 1, 7, 5]
test_grumpy: list[int] = [0, 1, 0, 1, 0, 1, 0, 1]
test_minutes: int = 3
test_out: int = 16
assert test_out == max_satisfied(test, test_grumpy, test_minutes)

test = [1]
test_grumpy = [0]
test_minutes = 1
test_out = 1
assert test_out == max_satisfied(test, test_grumpy, test_minutes)

test = [randint(0, 1000) for _ in range(2 * 10 ** 4)]
test_grumpy = [randint(0, 1) for _ in range(2 * 10 ** 4)]
test_minutes = randint(1, len(test))
print(test, '\n\n')
print(test_grumpy, '\n\n')
print(test_minutes)
