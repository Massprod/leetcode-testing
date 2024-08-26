# You are given a 0-indexed integer array batteryPercentages having length n,
#  denoting the battery percentages of n 0-indexed devices.
# Your task is to test each device i in order from 0 to n - 1,
#  by performing the following test operations:
#  - If batteryPercentages[i] is greater than 0:
#   - Increment the count of tested devices.
#   - Decrease the battery percentage of all devices with indices j in the range [i + 1, n - 1] by 1,
#     ensuring their battery percentage never goes below 0,
#     i.e, batteryPercentages[j] = max(0, batteryPercentages[j] - 1).
#   - Move to the next device.
#  - Otherwise, move to the next device without performing any test.
# Return an integer denoting the number of devices that will be tested after performing the test operations in order.
# ---------------------
# 1 <= n == batteryPercentages.length <= 100
# 0 <= batteryPercentages[i] <= 100
from random import randint


def count_tested_devices(battery_percentages: list[int]) -> int:
    # working_sol (85.64%, 90.73%) -> (50ms, 16.39mb)  time: O(n) | space: O(1)
    out: int = 0
    used: int = 0
    for percent in battery_percentages:
        if used < percent:
            out += 1
            used += 1
    return out


# Time complexity: O(n) <- n - length of the input array `battery_percentages`.
# Always traversing a whole input array `battery_percentages`, once => O(n).
# ---------------------
# Auxiliary space: O(1).


test: list[int] = [1, 1, 2, 1, 3]
test_out: int = 3
assert test_out == count_tested_devices(test)

test = [0, 1, 2]
test_out = 2
assert test_out == count_tested_devices(test)

test = [randint(1, 100) for _ in range(100)]
print(test)
