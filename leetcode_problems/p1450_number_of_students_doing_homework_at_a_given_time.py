# Given two integer arrays startTime and endTime and given an integer queryTime.
# The ith student started doing their homework at the time startTime[i]
#  and finished it at time endTime[i].
# Return the number of students doing their homework at time queryTime.
# More formally, return the number of students where queryTime
#  lays in the interval [startTime[i], endTime[i]] inclusive.
# ------------------
# startTime.length == endTime.length
# 1 <= startTime.length <= 100
# 1 <= startTime[i] <= endTime[i] <= 1000
# 1 <= queryTime <= 1000


def busy_students(start_time: list[int], end_time: list[int], query_time: int) -> int:
    # working_sol (96.90%, 80.75%) -> (30ms, 16.50mb)  time: O(n) | space: O(1)
    out: int = 0
    for index in range(len(start_time)):
        if start_time[index] <= query_time <= end_time[index]:
            out += 1
    return out


# Time complexity: O(n) <- n - length of the input array `start_time` and `end_time`.
# Always using all indexes of `start_time` => O(n).
# ------------------
# Auxiliary space: O(1)
# Only one constant INT used => O(1).


test_start: list[int] = [1, 2, 3]
test_end: list[int] = [3, 2, 7]
test_query: int = 4
test_out: int = 1
assert test_out == busy_students(test_start, test_end, test_query)

test_start = [4]
test_end = [4]
test_query = 4
test_out = 1
assert test_out == busy_students(test_start, test_end, test_query)
