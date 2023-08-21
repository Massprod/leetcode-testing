# There are some spherical balloons taped onto a flat wall that represents the XY-plane.
# The balloons are represented as a 2D integer array points where points[i] = [xstart, xend]
#   denotes a balloon whose horizontal diameter stretches between xstart and xend.
# You do not know the exact y-coordinates of the balloons.
# Arrows can be shot up directly vertically (in the positive y-direction)
#   from different points along the x-axis.
# A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend.
# There is no limit to the number of arrows that can be shot.
# A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
# --------------------
# 1 <= points.length <= 10 ** 5
# points[i].length == 2
# -2 ** 31 <= xstart < xend <= 2 ** 31 - 1


def find_min_arrow_shots(points: list[list[int]]) -> int:
    # working_sol (90.65%, 12.68%) -> (1104ms, 62.8mb)  time: O(n * log n) | space: O(1)
    # Sort by ENDs.
    points.sort(key=lambda x: x[1])
    # We essentially need a number of non overlapping intervals.
    # Everything overlapping can be destroyed with 1 arrow.
    break_end: int = points[0][1]
    arrows: int = 1
    for y in range(1, len(points)):
        # Overlapping sequence ends when:
        # newSTART is higher than minEND of current sequence.
        # Sorted byt ENDs, so we can use this END as minEND.
        if points[y][0] > break_end:
            # +1 For every non overlapping sequence,
            # and continue with new minEND of a new sequence.
            break_end = points[y][1]
            arrows += 1
    return arrows


# Time complexity: O(n * log n) -> sorting whole input_array in_place => O(n * log n) ->
# n - len of input_array^^| -> traversing whole input_array after sorting, once => O(n).
# Auxiliary space: O(1) -> only using 2 constant INTs, none of them depends on input => O(1).
# --------------------
# Find number of non overlapping intervals? Like we can shoot arrow and destroy everything which overlaps.
# So we just need to find breakpoints, where sequence isn't overlapping with others.
# Sort by ENDs and search for a breakpoints.
# These points are END <= START, otherwise it's starting somewhere behind and ending later.
# Even if we find something with start before this breakpoint later, it's still will take at least
# 1 arrow to destroy breakpoint and same arrow will destroy this overlapping interval later.
# Still +1 arrow anyway. Only question, can we destroy balloons at one point?
# Like END == 7, and other START == 7 shoot at 7 and destroy both, or we can't do this?
# Ok. Tested this, we can shoot at one point. So it's END < START, cuz equal will overlap.


test: list[list[int]] = [[10, 16], [2, 8], [1, 6], [7, 12]]
test_out: int = 2
assert test_out == find_min_arrow_shots(test)

test = [[1, 2], [3, 4], [5, 6], [7, 8]]
test_out = 4
assert test_out == find_min_arrow_shots(test)

test = [[1, 2], [2, 3], [3, 4], [4, 5]]
test_out = 2
assert test_out == find_min_arrow_shots(test)
