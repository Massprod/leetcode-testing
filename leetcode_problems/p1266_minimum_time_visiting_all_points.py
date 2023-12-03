# On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi].
# Return the minimum time in seconds to visit all the points in the order given by points.
# You can move according to these rules:
#  In 1 second, you can either:
#   - move vertically by one unit,
#   - move horizontally by one unit, or
#   - 0 move diagonally sqrt(2) units (in other words, move one unit vertically
#      then one unit horizontally in 1 second).
#   - You have to visit the points in the same order as they appear in the array.
#   - You are allowed to pass through points that appear later in the order, but these do not count as visits.
# ------------------
# points.length == n
# 1 <= n <= 100
# points[i].length == 2
# -1000 <= points[i][0], points[i][1] <= 1000


def min_time_to_visit_all_points(points: list[list[int]]) -> int:
    # working_sol (92.30%, 30.54%) -> (57ms, 16.4mb)  time: O(n) | space: O(1)
    # Can travel only horizontal + vertical == Manhattan distance.
    # If we can extra travel on diagonal == Chebyshev distance.
    out: int = 0
    for x in range(1, len(points)):
        out += max(
            abs(points[x][0] - points[x - 1][0]),  # abs(x2 - x1)
            abs(points[x][1] - points[x - 1][1]),  # abs(y2 - y1)
        )
    return out


# Time complexity: O(n) <- n - length of input array 'points'.
# Single traverse of the whole input array 'points'.
# ------------------
# Auxiliary space: O(1)
# Only using 1 extra INT no matter the input.


test: list[list[int]] = [[1, 1], [3, 4], [-1, 0]]
test_out: int = 7
assert test_out == min_time_to_visit_all_points(test)

test = [[3, 2], [-2, 2]]
test_out = 5
assert test_out == min_time_to_visit_all_points(test)
