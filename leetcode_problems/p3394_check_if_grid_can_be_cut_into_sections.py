# You are given an integer n representing the dimensions of an n x n grid,
#  with the origin at the bottom-left corner of the grid.
# You are also given a 2D array of coordinates rectangles,
#  where rectangles[i] is in the form [startx, starty, endx, endy],
#  representing a rectangle on the grid.
# Each rectangle is defined as follows:
#  - (startx, starty): The bottom-left corner of the rectangle.
#  - (endx, endy): The top-right corner of the rectangle.
# Note that the rectangles do not overlap.
# Your task is to determine if it is possible to make either two horizontal
#  or two vertical cuts on the grid such that:
#  - Each of the three resulting sections formed by the cuts
#    contains at least one rectangle.
#  - Every rectangle belongs to exactly one section.
# Return true if such cuts can be made; otherwise, return false.
# ----------------------------
# 3 <= n <= 10 ** 9
# 3 <= rectangles.length <= 10 ** 5
# 0 <= rectangles[i][0] < rectangles[i][2] <= n
# 0 <= rectangles[i][1] < rectangles[i][3] <= n
# No two rectangles overlap.


def check_valid_cuts(n: int, rectangles: list[list[int]]) -> bool:
    # working_sol (28.60%, 88.51%) -> (603ms, 83.36mb)  time: O(n * log n) | space: O(n)
    # Essentially we only care about having 3 separated ranges,
    #  we don't care about anything else.
    # So, just check for ranges on Y and X axis.
    # And if there's 3 distinct ranges on one of them => we can split correctly.
    prev_start: int
    prev_end: int
    # Sort and check Y-axis first.
    rectangles.sort(key=lambda x: [x[1], x[3]])
    # ! 3 <= rectangles.length <= 10 ** 5 !
    check_ranges: list[list[int, int]] = [ [rectangles[0][1], rectangles[0][3]] ]
    for _, start_y, _, end_y in rectangles[1:]:
        prev_start, prev_end = check_ranges[-1]
        # Merge if we can.
        if prev_start <= start_y < prev_end:
            check_ranges[-1] = [prev_start, max(prev_end, end_y)]
        # Or it's a new range.
        else:
            check_ranges.append([start_y, end_y])
    if 3 <= len(check_ranges):
        return True
    # Sort and check X-axis if we can't slice horizontally.
    rectangles.sort(key=lambda x: [x[0], x[2]])
    # Repeating, but w.e. No reasons to bother with uniFunc.
    check_ranges = [ [rectangles[0][0], rectangles[0][2]] ]
    for start_x, _, end_x, _ in rectangles[1:]:
        prev_start, prev_end = check_ranges[-1]
        if prev_start <= start_x < prev_end:
            check_ranges[-1] = [prev_start, max(prev_end, end_x)]
        else:
            check_ranges.append([start_x, end_x])

    return 3 <= len(check_ranges)


# Time complexity: O(n * log n) <- n - length of the input array `rectangles`.
# Sorting and traversing the input array `rectangles`, twice => O(2 * n * log n).
# ----------------------------
# Auxiliary space: O(n)
# `sort` <- takes O(n) => O(2 * n).
# In the worst case, there's no overlapping ranges.
# And we will allocates space for each range in `check_ranges` => O(3 * n).


test: int = 5
test_rectangles: list[list[int]] = [
    [1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]
]
test_out: bool = True
assert test_out == check_valid_cuts(test, test_rectangles)

test = 4
test_rectangles = [
    [0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]
]
test_out = True
assert test_out == check_valid_cuts(test, test_rectangles)

test = 4
test_rectangles = [
    [0, 2, 2, 4], [1, 0, 3, 2], [2, 2, 3, 4], [3, 0, 4, 2], [3, 2, 4, 4]
]
test_out = False
assert test_out == check_valid_cuts(test, test_rectangles)
