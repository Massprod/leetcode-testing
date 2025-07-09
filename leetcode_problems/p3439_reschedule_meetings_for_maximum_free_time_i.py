# You are given an integer eventTime denoting the duration of an event,
#  where the event occurs from time t = 0 to time t = eventTime.
# You are also given two integer arrays startTime and endTime, each of length n.
# These represent the start and end time of n non-overlapping meetings,
#  where the ith meeting occurs during the time [startTime[i], endTime[i]].
# You can reschedule at most k meetings by moving their start time
#  while maintaining the same duration, to maximize the longest
#  continuous period of free time during the event.
# The relative order of all the meetings should stay the same
#  and they should remain non-overlapping.
# Return the maximum amount of free time possible after rearranging the meetings.
# Note that the meetings can not be rescheduled to a time outside the event.
# -----------------------------
# 1 <= eventTime <= 10 ** 9
# n == startTime.length == endTime.length
# 2 <= n <= 10 ** 5
# 1 <= k <= n
# 0 <= startTime[i] < endTime[i] <= eventTime
# endTime[i] <= startTime[i + 1] where i lies in the range [0, n - 2].


def max_free_time(
    eventTime: int, k: int, startTime: list[int], endTime: list[int]
) -> int:
    # working_sol (12.17%, 71.48%) -> (96ms, 36.13mb)  time: O(n) | space: O(1)
    out: int = 0
    window: int = 0
    for index in range(len(startTime)):
        window += endTime[index] - startTime[index]
        left: int = 0 if index <= k - 1 else endTime[index - k]
        right: int = eventTime if index == (len(startTime) - 1) else startTime[index + 1]
        out = max(out, right - left - window)
        if index >= k - 1:
            window -= endTime[index - k + 1] - startTime[index - k + 1]

    return out


# Time complexity: O(n) <- n - length of the input arrays `startTime`|`endTime`.
# Always traversing the whole input array `startTime`, once => O(n).
# -----------------------------
# Auxiliary space: O(1)


test_event: int = 5
test_k: int = 1
test_start_time: list[int] = [1, 3]
test_end_time: list[int] = [2, 5]
test_out: int = 2
assert test_out == max_free_time(test_event, test_k, test_start_time, test_end_time)

test_event = 10
test_k = 1
test_start_time = [0, 2, 9]
test_end_time = [1, 4, 10]
test_out = 6
assert test_out == max_free_time(test_event, test_k, test_start_time, test_end_time)

test_event = 5
test_k = 2
test_start_time = [0, 1, 2, 3, 4]
test_end_time = [1, 2, 3, 4, 5]
test_out = 0
assert test_out == max_free_time(test_event, test_k, test_start_time, test_end_time)
