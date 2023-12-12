# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane,
#  return the maximum number of points that lie on the same straight slope.
# -----------------------
# 1 <= points.length <= 300
# points[i].length == 2
# -10 ** 4 <= xi, yi <= 10 ** 4
# All the points are unique.


def max_points(points: list[list[int]]) -> int:
    # working_sol (92.92%, 90.30%) -> (64ms, 16.23mb)  time: O(n ** 2) | space: O(n)
    # 1 point == 1 line.
    # 2 points == 1 line.
    if len(points) <= 2:
        return len(points)

    def find_slope(point1: tuple[int, int], point2: tuple[int, int]) -> float | str:
        # slope = (rise / run) = (y2 - y1) / (x2 - x1) = (vertical change / horizontal change)
        # (x2 - x1)
        run: int = point2[0] - point1[0]
        # Vertical line == slope undefined.
        # We build from `point1_` to w.e others.
        # So, every undefined slope == +1 point on vertical line, which starts at `point1_`.
        if run == 0:
            return 'vertical'
        # (y2 - y1)
        rise: int = point2[1] - point1[1]
        # (x2 - x1) == 0 => x2 == x1 AND (y2 - y1) == 0 => y2 == y1
        # Same coordinates, so w.e the line we're going to build from `point1_` it will include all `duplicates`.
        if run == 0 and rise == 0:
            return 'duplicates'
        return rise / run

    max_on_line: int = 0
    # Start from every point possible.
    # But don't recheck previous points.
    # Because we already built line from previous -> current.
    # And if we build this line from current point again, we will simply get current -> previous.
    # Which is the same line, and we already checked this line slope.
    for x in range(len(points)):
        # (x, y)
        point1_: tuple[int, int] = (points[x][0], points[x][1])
        # All lines with `point1_` on them.
        # Same slope == same line.
        lines: dict[tuple[int, int] | str, int] = {
            'vertical': 1,
            'duplicates': 0,
        }
        for y in range(x + 1, len(points)):
            point2_: tuple[int, int] = (points[y][0], points[y][1])
            slope: float | str = find_slope(point1_, point2_)
            # Line already exist.
            if slope in lines:
                lines[slope] += 1
                continue
            # New line between 2 points == 2 points on it.
            lines[slope] = 2
        if lines:
            max_on_line = max(max_on_line, lines.pop('duplicates') + max(lines.values()))
    return max_on_line


# Time complexity: O(n ** 2) <- n - length of input array `points`.
# Inner loop iterates over the remaining points for every index(point) in `points`.
# And outer loop iterates for every point in `points` as well.
# Auxiliary space: O(n).
# We only store slopes we can build from one `point1_` to every other point in `points`.
# In the worst case we will have all unique slopes, so we will store only `n` slopes.


test: list[list[int]] = [[1, 1], [2, 2], [3, 3]]
test_out: int = 3
assert test_out == max_points(test)

test = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
test_out = 4
assert test_out == max_points(test)

test = [[2, 3], [1, 1]]
test_out = 2
assert test_out == max_points(test)

test = [[-6, -1], [3, 1], [12, 3]]
test_out = 3
assert test_out == max_points(test)

test = [[0, 0], [1, -1], [1, 1]]
test_out = 2
assert test_out == max_points(test)

test = [[2, 3], [3, 3], [-5, 3]]
test_out = 3
assert test_out == max_points(test)
