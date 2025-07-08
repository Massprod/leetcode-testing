# A conveyor belt has packages that must be shipped from one port
#  to another within days days.
# The ith package on the conveyor belt has a weight of weights[i].
# Each day, we load the ship with packages on the conveyor belt
#  (in the order given by weights).
# We may not load more weight than the maximum weight capacity of the ship.
# Return the least weight capacity of the ship that will result in all the packages
#  on the conveyor belt being shipped within days days.
# ----------------------
# 1 <= days <= weights.length <= 5 * 10 ** 4
# 1 <= weights[i] <= 500
from random import randint

from pyperclip import copy


def ship_within_days(weights: list[int], days: int) -> int:
    # working_sol (91.83%, 89.70%) -> (142ms, 22.08mb)  time: O(n * log(sum(n))) | space: O(1)
    
    def check(check_array: list[int], day_limit: int, days: int) -> bool:
        run_sum: int = 0
        for value in check_array:
            run_sum += value
            if run_sum > day_limit:
                days -= 1
                run_sum = value
        # We good if we had enough, or leftovers. At least 1 day.
        return 1 <= days

    left: int = max(weights)  # At least 1 day & 1 cargo == min capacity
    right: int = sum(weights)
    while left < right:
        middle: int = (left + right) // 2
        if check(weights, middle, days):
            right = middle
            continue
        left = middle + 1
    
    return left


# Time complexity: O(n * log(sum(n))) <- n - input array `weights`.
# Standard binary search from `max(n)` to `sum(n)`.
# And for each check we're traversing whole input array `weights` => O(n * log(sum(n))).
# ----------------------
# Auxiliary space: O(1)


test: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_days: int = 5
test_out: int = 15
assert test_out == ship_within_days(test, test_days)

test = [3, 2, 2, 4, 1, 4]
test_days = 3
test_out = 6
assert test_out == ship_within_days(test, test_days)

test = [1, 2, 3, 1, 1]
test_days = 4
test_out = 3
assert test_out == ship_within_days(test, test_days)

test = [randint(1, 500) for _ in range(5 * 10 ** 4)]
copy(test)
