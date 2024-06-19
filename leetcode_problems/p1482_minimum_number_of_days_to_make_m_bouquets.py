# You are given an integer array bloomDay, an integer m and an integer k.
# You want to make m bouquets. To make a bouquet,
#  you need to use k adjacent flowers from the garden.
# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i]
#  and then can be used in exactly one bouquet.
# Return the minimum number of days you need to wait to be able to make m bouquets from the garden.
# If it is impossible to make m bouquets return -1.
# -------------------
# bloomDay.length == n
# 1 <= n <= 10 ** 5
# 1 <= bloomDay[i] <= 10 ** 9
# 1 <= m <= 10 ** 6
# 1 <= k <= n
from random import randint


def min_days(bloom_day: list[int], m: int, k: int) -> int:
    # working_sol (50.35%, 75.28%) -> (839ms, 30.36mb)  time: O(n * (log max(n))) | space: O(1)
    # We don't have enough flowers in the Garden.
    if m * k > len(bloom_day):
        return -1

    def count_bouquets(reap_day: int) -> int:
        # We can only use `consecutive` flowers == k.
        # And we need to build `m`, `bouquets`.
        bouquets: int = 0
        streak: int = 0
        for day in bloom_day:
            if day <= reap_day:
                streak += 1
            else:
                streak = 0
            if streak == k:
                streak = 0
                bouquets += 1
        return bouquets

    left_l: int = 0
    right_l: int = max(bloom_day)
    while left_l <= right_l:
        middle: int = (left_l + right_l) // 2
        if m <= count_bouquets(middle):
            right_l = middle - 1
        else:
            left_l = middle + 1
    return left_l


# Time complexity: O(n * (log max(n))) <- n - length of the input array `bloom_day`.
# We always use BS in range (0 -> max(bloom_day)),
#  and for every BS check we traverse the whole array `bloom_day` => O(n * (log max(n)).
# -------------------
# Auxiliary space: O(1)
# We only use 5 constant INT's, none of them depend on input => O(1).


test: list[int] = [1, 10, 3, 10, 2]
test_m: int = 3
test_k: int = 1
test_out: int = 3
assert test_out == min_days(test, test_m, test_k)

test = [1, 10, 3, 10, 2]
test_m = 3
test_k = 2
test_out = -1
assert test_out == min_days(test, test_m, test_k)

test = [7, 7, 7, 7, 12, 7, 7]
test_m = 2
test_k = 3
test_out = 12
assert test_out == min_days(test, test_m, test_k)

test = [randint(1, 10 ** 9) for _ in range(10 ** 5)]
test_k = len(test) // randint(1, 100)
test_m = len(test) // test_k
print(test)
print(test_m)
print(test_k)
