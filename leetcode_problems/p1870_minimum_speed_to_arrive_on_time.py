# You are given a floating-point number hour,
#   representing the amount of time you have to reach the office.
# To commute to the office, you must take n trains in sequential order.
# You are also given an integer array dist of length n,
#   where dist[i] describes the distance (in kilometers) of the ith train ride.
# Each train can only depart at an integer hour,
#   so you may need to wait in between each train ride.
# For example, if the 1st train ride takes 1.5 hours,
#   you must wait for an additional 0.5 hours before you can depart
#   on the 2nd train ride at the 2 hour mark.
# Return the minimum positive integer speed (in kilometers per hour)
#   that all the trains must travel at for you to reach the office on time,
#   or -1 if it is impossible to be on time.
# Tests are generated such that the answer will not exceed 10 ** 7
#   and hour will have at most two digits after the decimal point.
# -------------------------
# n == dist.length
# 1 <= n <= 10 ** 5
# 1 <= dist[i] <= 10 ** 5
# 1 <= hour <= 10 ** 9
# There will be at most two digits after the decimal point in hour.
from math import ceil
from random import randint, uniform


def min_speed_on_time(dist: list[int], hour: float) -> int:
    # working_sol (62.39%, 25.64%) -> (3153ms, 30.9mb)  time: O((log m) * n) | space: O(1)
    length: int = len(dist)

    def time_spend(speed: int):
        # Time spend for a WHOLE train trip
        # with given speed.
        time: float = 0.0
        for y in range(length - 1):
            # Everything, except last train having wait time
            # for a train to depart -> depart at integer hour.
            time += ceil(dist[y] / speed)
        # Last leading to a destination, there's no wait time after.
        time += dist[-1] / speed
        return time

    left_l: int = 1
    right_l: int = 10 ** 7
    min_speed: int = -1
    # Binary search for all values of constraint 10 ** 7.
    while left_l <= right_l:
        mid: int = (left_l + right_l) // 2
        if time_spend(mid) <= hour:
            min_speed = mid
            right_l = mid - 1
            continue
        left_l = mid + 1
    return min_speed


# Time complexity: O((log m) * n) -> standard binary search approach for a constraint limit of speed == 10 ** 7,
# m - speed limit 10 ** 7^^| for every middle check we're going to traverse whole input_array to find time
# n - len of input_array^^|  we need to spend for a full_trip -> O((log m) * n).
# Auxiliary space: O(1) -> 6 extra constants used, 5 INTS, 1 FLOAT none of them depends on input => O(1).
# -------------------------
# Made it working for case with length >= hour.
# We can find max_speed we can travel with taking 1h per train, then decrease it.
# Tried to make this be decreasing max_speed by 1 and checking for a correct time_gate.
# But it's TLE for limit_constraints. So taking a hint, cuz I don't get how we should search for this speed.
# Ok. It's the dumbest way I expected it to be. We can just make binary search for a correct time_gate for all
# speed options...from 1 to 10 ** 7. Expected some deep DP stuff or smth.
# If speed allows us correctly time_gate a trip -> sum(ceil(dist / speed)) except last,
#   cuz last doesn't need to have wait time for another train.
# Then we can try to decrease it and check again.
# If it's not then we need to speed up, increase and check again.


test1 = [1, 3, 2]
test1_hour = 6
test1_out = 1
assert test1_out == min_speed_on_time(test1, test1_hour)

test2 = [1, 3, 2]
test2_hour = 2.7
test2_out = 3
assert test2_out == min_speed_on_time(test2, test2_hour)

test3 = [1, 3, 2]
test3_hour = 1.9
test3_out = -1
assert test3_out == min_speed_on_time(test3, test3_hour)

test4 = [100, 2022, 21231, 12312, 12312, 12312, 12312, 12312, 999, 122, 3322, 123]
test4_hour = 11.5
test4_out = 21231
assert test4_out == min_speed_on_time(test4, test4_hour)

test: list[int] = []
for _ in range(10 ** 5):
    test.append(randint(1, 10 ** 5))
test_hour: float = uniform(1, 10 ** 9)
print(test)
print(test_hour)
print(min_speed_on_time(test, 862931601.51))
