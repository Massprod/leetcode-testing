# Given an array of integers temperatures represents the daily temperatures,
#   return an array answer such that answer[i] is the number of days you have to wait
#   after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.
# ---------------------
# 1 <= temperatures.length <= 10 ** 5
# 30 <= temperatures[i] <= 100


def daily_temps(temperatures: list[int]) -> list[int]:
    # working_sol (97.56%, 99.93%) -> (858ms, 29.08mb)  time: O(n) | space: O(n)
    # [indexes of days with lower temperature]
    list_stack: list[int] = []
    for day, temperature in enumerate(temperatures):
        # Delete everything lower, and because we store day indexes we can find distance.
        while list_stack and temperatures[list_stack[-1]] < temperature:
            lower_day: int = list_stack.pop()
            temperatures[lower_day] = day - lower_day
        list_stack.append(day)
    # Annul days which didn't meet higher Temperature days.
    for day in list_stack:
        temperatures[day] = 0
    return temperatures


# Time complexity: O(n) <- n - length of input array `temperatures`.
# Worst case: everything is lower except last value.
# Then we will traverse input once, to add everything in a stack => O(n).
# And extra traverse stack to get distances => O(n - 1).
# ---------------------
# Auxiliary space: O(n).
# Changing temperatures inplace, but still stack can be a size of input == `n` => O(n).
# -------------
# Standard mono stack with deleting everything lower. Store every index so far and find distance, between
# stored index and index on which Higher temperature was met.


test: list[int] = [73, 74, 75, 71, 69, 72, 76, 73]
test_out: list[int] = [1, 1, 4, 2, 1, 1, 0, 0]
assert test_out == daily_temps(test)

test = [30, 40, 50, 60]
test_out = [1, 1, 1, 0]
assert test_out == daily_temps(test)

test = [30, 60, 90]
test_out = [1, 1, 0]
assert test_out == daily_temps(test)

test = [50, 50, 50, 50, 50]
test_out = [0, 0, 0, 0, 0]
assert test_out == daily_temps(test)

test = [50, 50, 50, 50, 50, 51]
test_out = [5, 4, 3, 2, 1, 0]
assert test_out == daily_temps(test)
