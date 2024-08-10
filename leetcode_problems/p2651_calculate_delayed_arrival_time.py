# You are given a positive integer arrivalTime denoting the arrival time of a train in hours,
#  and another positive integer delayedTime denoting the amount of delay in hours.
# Return the time when the train will arrive at the station.
# Note that the time in this problem is in 24-hours format.
# ----------------------
# 1 <= arrivaltime < 24
# 1 <= delayedTime <= 24


def find_delayed_arrival_time(arrival_time: int, delayed_time: int) -> int:
    # working_sol (37.62%, 96.41%) -> (38ms, 16.39mb)  time: O(1) | space: O(1)
    return (arrival_time + delayed_time) % 24


# Time complexity: O(1)
# ----------------------
# Auxiliary space: O(1)


test: int = 15
test_delay: int = 5
test_out: int = 20
assert test_out == find_delayed_arrival_time(test, test_delay)

test = 13
test_delay = 11
test_out = 0
assert test_out == find_delayed_arrival_time(test, test_delay)
