# Given n points on a 2D plane where points[i] = [xi, yi],
#  Return the widest vertical area between two points such that no points are inside the area.
# A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height).
# The widest vertical area is the one with the maximum width.
# Note that points on the edge of a vertical area are not considered included in the area.
# -----------------------
# n == points.length
# 2 <= n <= 10 ** 5
# points[i].length == 2
# 0 <= xi, yi <= 10 ** 9
from random import randint


def max_width_of_vert_area(points: list[list[int]]) -> int:
    # working_sol (97.91%, 6.69%) -> (714ms, 60.1mb)  time: O(n * log n) | space: O(n)
    # We don't care about `Y` at all.
    # All we care is difference  in `X` and because we shouldn't have anything between 2 points,
    #  it's just a maximum difference of `X` coordinates between any 2 points after sorting.
    points.sort(key=lambda y: y[0])
    out: int = 0
    for x in range(1, len(points)):
        out = max(out, points[x][0] - points[x - 1][0])
    return out


# Time complexity: O(n * log n) <- n - length of input array `points`.
# Standard builtin sort() takes O(n * log n) + O(n) space.
# Extra traverse to get maximum difference => O(n).
# Auxiliary space: O(n).


test: list[list[int]] = [[8, 7], [9, 9], [7, 4], [9, 7]]
test_out: int = 1
assert test_out == max_width_of_vert_area(test)

test = [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]
test_out = 3
assert test_out == max_width_of_vert_area(test)

test = [[randint(0, 10 ** 9), randint(0, 10 ** 9)] for _ in range(10 ** 4)]
print(test)
