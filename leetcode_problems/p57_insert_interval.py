# You are given an array of non-overlapping interval where intervals[i] = [starti, endi]
# represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
# You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti
# and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.


def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    pass


test1_intervals = [[1, 3], [6, 9]]
test1_new_interval = [2, 5]
test1_out = [[1, 5], [6, 9]]

test2_intervals = [[1, 2], [3, 5], [6, 7], [8, 10]]
test2_new_interval = [4, 8]
test2_out = [[1, 2], [3, 10], [12, 16]]
