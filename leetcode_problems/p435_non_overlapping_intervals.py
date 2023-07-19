# Given an array of intervals intervals where intervals[i] = [starti, endi],
#   return the minimum number of intervals you need to remove to make
#   the rest of the intervals non-overlapping.
# ---------------
# 1 <= intervals.length <= 10 ** 5
# intervals[i].length == 2
# -5 * 10 ** 4 <= starti < endi <= 5 * 10 ** 4
from operator import itemgetter
from random import randint


def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    # working_sol (78.03%, 91.31%) -> (1328ms, 55.2mb)  time: O(n * log n) | space: O(1)
    if len(intervals) == 1:
        return 0
    # sort by END.
    intervals.sort(key=itemgetter(1))
    limit: int | None = None
    count: int = 0
    for x in range(len(intervals)):
        # First END is lowest of all intervals.
        # So it's either will be updated or
        # any START of other intervals is lower and overlapping.
        if limit is None:
            limit = intervals[x][1]
            continue
        # Intervals sorted in ascending by ENDs,
        # so if anything can't start from current HIGHEST
        # then it's overlapping cuz every interval is [start < end].
        # And no matter what start was before =>
        # => new_start is overlapping, cuz it's in range anySTART < HIGHEST.
        if limit > intervals[x][0]:
            count += 1
        # If it's correct interval sequence ->
        # -> we can just choose new HIGHEST(limit).
        elif limit <= intervals[x][0]:
            limit = intervals[x][1]
    return count

# Time complexity: O(n * log n) -> sorting everything by with set KEY == END => O(n * log n) ->
# n - len of input_array^^| -> traversing whole input_array, once => O(n) -> O(n * log n) + O(n) => O(n * log n).
# Auxiliary space: O(1) -> we're sorting in_place, so it's same input_array, but changed in ascending END's order ->
#                          -> using 2 extra constant INTs, doesn't depend on input => O(1).
# ---------------
# Most basic way is to just check every possible combination of end -> start.
# Where start is always higher or equal to end, because otherwise it's overlap, and we can't start from it.
# But it's O(n ** n), and not effective. Maybe binary search?
# Actually if we could sort this only on END's then we can just get hold of so far highest END and be sure, that's
# everything else behind -> is lower and if we're passing the check start > end(stored) it's not overlapping.
# Count everything that's not passing the check, and its should be correct.
# And update limit with correct interval, make it higher.


test1 = [[1, 2], [2, 3], [3, 4], [1, 3]]
test1_out = 1
assert test1_out == erase_overlap_intervals(test1)

test2 = [[1, 2], [1, 2], [1, 2]]
test2_out = 2
assert test2_out == erase_overlap_intervals(test2)

test3 = [[1, 2], [2, 3]]
test3_out = 0
assert test3_out == erase_overlap_intervals(test3)

test4 = [[0, 10], [1, 2], [2, 3], [3, 4], [1, 3], [5, 12]]
test4_out = 2
assert test4_out == erase_overlap_intervals(test4)

test5 = [[0, 0]]
test5_out = 0
assert test5_out == erase_overlap_intervals(test5)

# test6 -> failed -> Missed case with start being equal to limit(HIGHEST).
#                    Which is the most basic case, but I was thinking that we can't start from the same value.
#                    And it's in the test1, but there it wasn't critical, cuz it's only 1 value to delete.
test6 = [[18, 42], [-12, -3], [-83, 66], [4, 32], [0, 29], [62, 72], [-97, -14], [24, 87], [23, 56], [67, 97], [14, 48],
         [41, 48], [-59, 74], [-91, 50], [35, 97], [77, 83], [57, 68], [-99, 86], [-27, 16], [84, 94], [88, 90],
         [91, 93], [92, 96], [-78, -24], [32, 76], [-90, 7], [-78, -38], [-67, 30], [4, 58], [35, 36], [-47, -18],
         [-17, -7], [39, 70], [85, 86], [-28, -15], [91, 97], [-84, 1], [30, 71], [2, 93], [66, 97], [94, 97], [-7, 74],
         [-3, 26]]
test6_out = 31
assert test6_out == erase_overlap_intervals(test6)

test: list[list[int]] = []
test_interval: list[int] = []
for _ in range(10 ** 3):
    test_interval.clear()
    new_start: int = randint((-5 * 10 ** 4), (5 * 10 ** 4))
    new_end: int = randint((-5 * 10 ** 4), (5 * 10 ** 4))
    if new_start > new_end:
        test_interval.append(new_end)
        test_interval.append(new_start)
    if new_start < new_end:
        test_interval.append(new_start)
        test_interval.append(new_end)
    test.append(test_interval.copy())
print(test)
print(erase_overlap_intervals(test))
