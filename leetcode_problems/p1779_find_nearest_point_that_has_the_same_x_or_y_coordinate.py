# You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y).
# You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi).
# A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.
# Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location.
# If there are multiple, return the valid point with the smallest index.
# If there are no valid points, return -1.
# The Manhattan distance between two points (x1, y1) and (x2, y2)
#  is abs(x1 - x2) + abs(y1 - y2).
# ---------------------------
# 1 <= points.length <= 10 ** 4
# points[i].length == 2
# 1 <= x, y, ai, bi <= 10 ** 4


def nearest_valid_point(x: int, y: int, points: list[list[int]]) -> int:
    # working_sol (97.66%, 69.92%) -> (572ms, 21.72mb)  time: O(n) | space: O(1)
    out: int = -1
    cur_dist: int | float = float('inf')
    for index in range(len(points)):
        _x: int = points[index][0]
        _y: int = points[index][1]
        if _x == x or _y == y:
            manh_dist: int = abs(_y - y) + abs(_x - x)
            if manh_dist < cur_dist:
                cur_dist, out = manh_dist, index
    return out


test_x: int = 3
test_y: int = 4
test_points: list[list[int]] = [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]
test_out: int = 2
assert test_out == nearest_valid_point(test_x, test_y, test_points)

test_x = 3
test_y = 4
test_points = [[3, 4]]
test_out = 0
assert test_out == nearest_valid_point(test_x, test_y, test_points)

test_x = 3
test_y = 4
test_points = [[2, 3]]
test_out = -1
assert test_out == nearest_valid_point(test_x, test_y, test_points)
