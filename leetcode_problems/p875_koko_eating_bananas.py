# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
# The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k.
# Each hour, she chooses some pile of bananas and eats k bananas from that pile.
# If the pile has less than k bananas, she eats all of them instead
#   and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.
# ----------------------
# 1 <= piles.length <= 10 ** 4
# piles.length <= h <= 10 ** 9
# 1 <= piles[i] <= 10 ** 9
from math import ceil
from random import randint


def min_eating_speed(piles: list[int], h: int) -> int:
    # working_sol (98.56%, 49.17%) -> (294ms, 18mb)  time: O((log m) * n) | space: O(1)
    # We can't eat 0 bananas :)
    left_l: int = 1
    # We can't eat faster than max_value in piles ->
    # -> cuz its == [max_pile] per 1 h, any lower is going to be eater in 1h as well.
    right_l: int = 10 ** 9
    min_speed: int = -1
    
    def speed_check(k: int) -> int:
        # Time taken to eat all piles.
        hours_taken: int = 0
        for pile in piles:
            # CEIL() -> cuz we can't instantly start eating other pile.
            # We need to wait for the end of the hour.
            hours_taken += ceil(pile / k)
        return hours_taken

    # Standard BinarySearch for maximum constraints.
    while left_l <= right_l:
        middle: int = (left_l + right_l) // 2
        time_taken: int = speed_check(middle)
        # We can slow down.
        if time_taken <= h:
            min_speed = middle
            right_l = middle - 1
            continue
        # We can speed up.
        left_l = middle + 1
    return min_speed


# Time complexity: O((log m) * n) -> standard BS for max_constraints is always => O(log m) ->
# m - speed limit == 10 ** 9^^| -> but for every BS speed_check we're traversing whole input_array => O((log m) * n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> only 6 constants used == 6 INTs, none of them depends on input => O(1).
# ----------------------
# Ok. Guess it's just binary search as previously. Like in p1870, just not trains.
# Working with max_constraints, let's fail.


test: list[int] = [3, 6, 7, 11]
test_h: int = 8
test_out: int = 4
assert test_out == min_eating_speed(test, test_h)

test = [30, 11, 23, 4, 20]
test_h = 5
test_out = 30
assert test_out == min_eating_speed(test, test_h)

test = [30, 11, 23, 4, 20]
test_h = 6
test_out = 23
assert test_out == min_eating_speed(test, test_h)

test = []
for _ in range(10 ** 4):
    test.append(randint(1, 10 ** 9))
test_h = randint(len(test), 10 ** 9)
# print(test)
# print(test_h)
