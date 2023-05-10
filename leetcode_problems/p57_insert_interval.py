# You are given an array of non-overlapping interval where intervals[i] = [starti, endi]
# represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
# You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti
# and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.


def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    def place(to_place: list[list[int]], new_interval: list[int]) -> int:
        start: int = new_interval[0]
        end: int = new_interval[1]
        for g in range(len(to_place)):
            check_start: int = to_place[g][0]
            check_end: int = to_place[g][1]
            if end < check_start and start > to_place[g - 1][1]:  # place inside
                to_place.insert(g, [start, end])
                return -1
            if start <= check_start <= end <= check_end:
                start = min(start, check_start)
                end = max(end, check_end)
                to_place[g] = [start, end]
                return g
            elif check_start <= start <= check_end <= end:
                start = min(start, check_start)
                end = max(end, check_end)
                to_place[g] = [start, end]
                return g
            elif start <= check_start <= check_end <= end:
                start = min(start, check_start)
                end = max(end, check_end)
                to_place[g] = [start, end]
                return g
            elif check_start <= start <= end <= check_end:
                start = min(start, check_start)
                end = max(end, check_end)
                to_place[g] = [start, end]
                return g
        return -1

    def can_merge(to_merge: list[list[int]], start_index: int) -> None:
        start: int = to_merge[start_index][0]
        end: int = to_merge[start_index][1]
        y: int = start_index + 1
        while y < len(to_merge):
            check_start: int = to_merge[y][0]
            check_end: int = to_merge[y][1]
            if start <= check_start <= end <= check_end:
                start = min(start, check_start)
                end = max(end, check_end)
                to_merge.pop(y)
                to_merge[start_index] = [start, end]
                continue
            elif check_start <= start <= check_end <= end:
                start = min(start, check_start)
                end = max(end, check_end)
                to_merge.pop(y)
                to_merge[start_index] = [start, end]
                continue
            elif start <= check_start <= check_end <= end:
                start = min(start, check_start)
                end = max(end, check_end)
                to_merge.pop(y)
                to_merge[start_index] = [start, end]
                continue
            elif check_start <= start <= end <= check_end:
                start = min(start, check_start)
                end = max(end, check_end)
                to_merge.pop(y)
                to_merge[start_index] = [start, end]
                continue
            return

    if len(intervals) == 0:
        intervals.append(newInterval)
        return intervals
    new_start = newInterval[0]
    new_end = newInterval[1]
    if new_end < intervals[0][0]:  # place before
        intervals.insert(0, newInterval)
        return intervals
    if new_start > intervals[-1][1]:  # place after
        intervals.append(newInterval)
        return intervals
    if (place_index := place(intervals, newInterval)) >= 0:  # place inside or merge_walk
        can_merge(intervals, place_index)
        return intervals
    return intervals


# place() -> searching for a index where we can insert new_interval.
# can_merge() -> simple merging every value until we hit something we can't merge into.
#  Guess trick in this task is to place new_interval in the start or end of intervals,
#  because it's not corresponds with values inside intervals.
# There's only one NEW_INTERVAL and 3 ways to place it: before [0], after [-1], somewhere between [0] - [-1].
# ------------------------------------
# Mirror for p56, but now we first need to find place from where to start merging.
# Going from left_to_right (ascending) and first time we encounter something we can merge new_interval with,
# just call ! can_merge() ! from p56 with this start index.


test1_intervals = [[1, 3], [6, 9]]
test1_new_interval = [2, 5]
test1_out = [[1, 5], [6, 9]]
print(insert(test1_intervals, test1_new_interval))

test2_intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
test2_new_interval = [4, 8]
test2_out = [[1, 2], [3, 10], [12, 16]]
print(insert(test2_intervals, test2_new_interval))

test3_intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
test3_new_interval = [17, 18]
test3_out = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16], [17, 18]]
print(insert(test3_intervals, test3_new_interval))

# test4 - failed -> because I consider less than [0] or more than [-1] values, but didn't think about empty intervals,
#                 ! 0 <= intervals.length <= 104
#                   newInterval.length == 2 ! <- always CHECK constraints...
test4_intervals = []
test4_new_interval = [5, 7]
test4_out = [[5, 7]]
print(insert(test4_intervals, test4_new_interval))

# test5 - failed -> bruh. I used walrus_sign to assign place_index and forgot about index == 0 case,
#                   and 0 is always FALSE, we're getting index = 0 and instantly skipping IF statement.
#                   Walrus is a tricky_one in these situations, I should remember it.
test5_intervals = [[1, 5], [6, 8]]
test5_new_interval = [5, 6]
test5_out = [1, 8]
print(insert(test5_intervals, test5_new_interval))

# test6 - failed -> fail to see case where's new_interval can't be merged and not going to be a new [0] or [-1]
#                   but somewhere between.
test6_intervals = [[3, 5], [12, 15]]
test6_new_interval = [6, 6]
test6_out = [[3, 5], [6, 6], [12, 15]]
print(insert(test6_intervals, test6_new_interval))
