# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane,
# return the maximum number of points that lie on the same straight line.
# -----------------------
# 1 <= points.length <= 300  ,  points[i].length == 2  ,  -104 <= xi, yi <= 104
# All the points are unique.


def max_points(points: list[list[int]]) -> int:
    length: int = len(points)
    if length == 1:
        return 1
    used_horizont: set[int] = set()
    used_vertical: set[int] = set()
    used_ascending: set[int] = set()
    used_descending: set[int] = set()
    vertical_line: int = 1
    horizontal_line: int = 1
    ascending_diag: int = 1
    descending_diag: int = 1
    lines: set[int] = set()
    for point in points:
        point_x: int = point[0]
        point_y: int = point[1]
        if point_x in used_vertical:
            continue
        if point_y in used_horizont:
            continue
        if abs(point_x + point_y) in used_descending:
            continue
        if abs(point_x - point_y) in used_ascending:
            continue
        for g in range(length):
            if points[g] == point:
                continue
            check_x: int = points[g][0]
            check_y: int = points[g][1]
            if check_y == point_y:
                horizontal_line += 1
            if check_x == point_x:
                vertical_line += 1
            if (check_x + check_y) == (point_x + point_y):
                descending_diag += 1
            if abs(check_x - check_y) == abs(point_x - point_y):
                ascending_diag += 1
        used_horizont.add(point_y)
        used_vertical.add(point_x)
        used_ascending.add(abs(point_x - point_y))
        used_descending.add(abs(point_x + point_y))
        lines.add(vertical_line), lines.add(horizontal_line)
        lines.add(ascending_diag), lines.add(descending_diag)
        vertical_line = 1
        horizontal_line = 1
        ascending_diag = 1
        descending_diag = 1
    return max(lines)


# Ascending diag: x1 - y1 == xk - yk
# Descending diag: x1 + y1 == xk + yk
# Horizont: y1 = y2 = yk
# Vertical: x1 = x2 = xk
# -----------------------
# If we don't care about speed we can check every index one by one and count their lines,
# but it's going to be O(n ** n) and I fear with 300 points it will hit time_limit.
# How we can avoid it?
# 1) Delete every index with 0? If we check point and find there's no other points on her lines.
# Ok. But still need's to be checked and if there's none like this?
# 2) Remember lines? We check x = 2, for every index, and if we met another point with x == 2
# just ignore it or at least ignore horizontal calc.
# Ok. 2 might be enough, don't see other options for now.


test1 = [[1, 1], [2, 2], [3, 3]]
test1_out = 3
print(max_points(test1))

test2 = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
test2_out = 4
print(max_points(test2))
