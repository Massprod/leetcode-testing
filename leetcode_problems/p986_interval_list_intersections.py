# You are given two lists of closed intervals, firstList and secondList,
#  where firstList[i] = [starti, endi] and secondList[j] = [startj, endj].
# Each list of intervals is pairwise disjoint and in sorted order.
# Return the intersection of these two interval lists.
# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
# The intersection of two closed intervals is a set of real numbers that are either empty
#  or represented as a closed interval.
# For example, the intersection of [1, 3] and [2, 4] is [2, 3].
# ---------------------
# 0 <= firstList.length, secondList.length <= 1000
# firstList.length + secondList.length >= 1
# 0 <= starti < endi <= 10 ** 9
# endi < starti+1
# 0 <= startj < endj <= 10 ** 9
# endj < startj+1


def interval_intersection(firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
    # working_sol (94.02%, 91.39%) -> (115ms, 17.46mb)  time: O(max(m, n)) | space: O(max(m, n))
    pos1: int = 0
    pos2: int = 0
    out: list[list[int]] = []
    while pos1 < len(firstList) and pos2 < len(secondList):
        start1, end1 = firstList[pos1]
        start2, end2 = secondList[pos2]
        # Second ends before reaching first interval.
        if end2 < start1:
            pos2 += 1
        # First ends before reaching second interval.
        elif end1 < start2:
            pos1 += 1
        # Otherwise, they will have intersection.
        else:
            out.append([max(start1, start2), min(end1, end2)])
            # We can have case like: f == [1, 4] , s == [2, 5]
            # We're given sorted in increasing order and disjoint intervals.
            # So, we can have interval [5, w.e] AFTER first, we need to check this.
            if end1 < end2:
                pos1 += 1
            elif end1 > end2:
                pos2 += 1
            # Or they can end at the same time,
            #  then there's no way they will intersect with sm1 else later.
            else:
                pos1 += 1
                pos2 += 1
    return out


# Time complexity: O(max(m, n)) <- m - length of input array `firstList`, n - length of input array `secondList`.
# Essentially we're just traversing both array, and only care about maximum sized.
# ---------------------
# Auxiliary space: O(max(m, n)).
# Worst case: [0, 100] and second is like [[0,1], [2, 3] etc. [99, 100]].
# `out` will be a size of this second array => O(max(m, n)).


test_1: list[list[int]] = [[0, 2], [5, 10], [13, 23], [24, 25]]
test_2: list[list[int]] = [[1, 5], [8, 12], [15, 24], [25, 26]]
test_out: list[list[int]] = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
assert test_out == interval_intersection(test_1, test_2)

test_1 = [[1, 3], [5, 9]]
test_2 = []
test_out = []
assert test_out == interval_intersection(test_1, test_2)
