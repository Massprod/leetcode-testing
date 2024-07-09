# There is a restaurant with a single chef.
# You are given an array customers, where customers[i] = [arrival_i, time_i]:
#   - arrival_i is the arrival time of the ith customer.
#     The arrival times are sorted in non-decreasing order.
#   - time_i is the time needed to prepare the order of the ith customer.
# When a customer arrives, he gives the chef his order,
#  and the chef starts preparing it once he is idle.
# The customer waits till the chef finishes preparing his order.
# The chef does not prepare food for more than one customer at a time.
# The chef prepares food for customers in the order they were given in the input.
# Return the average waiting time of all customers.
# Solutions within 10 ** -5 from the actual answer are considered accepted.
# --------------------
# 1 <= customers.length <= 10 ** 5
# 1 <= arrival_i, time_i <= 10 ** 4
# arrival_i <= arrival_i+1
from random import randint


def average_waiting_time(customers: list[list[int]]) -> float:
    # working_sol (62.89%, 45.36%) -> (746ms, 57.13mb)  time: O(n) | space: O(1)
    start: int
    cook_time: int
    out: int = 0
    prev_end: int = 0
    for start, cook_time in customers:
        # If we have some positive gap between clients,
        #  we should always treat this client as a new sequence.
        if prev_end < start:
            prev_end = start
        # Otherwise we need (prev_end - start),
        #  to know how much this client is going to wait.
        out += prev_end - start + cook_time
        prev_end += cook_time
    return out / len(customers)


# Time complexity: O(n) <- n - length of the input array `customers`.
# Always traversing whole input array `customers`, once => O(n).
# --------------------
# Auxiliary space: O(1)
# Only constant INT's used, none of them depends on input => O(1)


test: list[list[int]] = [[1, 2], [2, 5], [4, 3]]
test_out: float = 5.0
assert test_out == average_waiting_time(test)

test = [[5, 2], [5, 4], [10, 3], [20, 1]]
test_out = 3.25
assert test_out == average_waiting_time(test)

test = [[randint(1, 10 ** 4), randint(1, 10 ** 4)] for _ in range(10 ** 3)]
test.sort(key=lambda x: x[0])
print(test)
