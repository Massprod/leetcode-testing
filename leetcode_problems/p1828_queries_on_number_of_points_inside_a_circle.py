# You are given an array points where points[i] = [xi, yi]
#  is the coordinates of the ith point on a 2D plane.
# Multiple points can have the same coordinates.
# You are also given an array queries where queries[j] = [xj, yj, rj]
#  describes a circle centered at (xj, yj) with a radius of rj.
# For each query queries[j], compute the number of points inside the jth circle.
# Points on the border of the circle are considered inside.
# Return an array answer, where answer[j] is the answer to the jth query.
# --------------------------
# 1 <= points.length <= 500
# points[i].length == 2
# 0 <= x​​​​​​i, y​​​​​​i <= 500
# 1 <= queries.length <= 500
# queries[j].length == 3
# 0 <= xj, yj <= 500
# 1 <= rj <= 500
# All coordinates are integers.


def  count_poins(points: list[list[int]], queries: list[list[int]]) -> list[int]:
    
    out: list[int] = []
    for circle_x, circle_y , circle_r in queries:
        square_r: int = circle_r ** 2
        points_inside: int = 0
        for point_x, point_y in points:
            center_distance: int = (point_x - circle_x) ** 2 + (point_y - circle_y) ** 2
            if center_distance <= square_r:
                points_inside += 1
        out.append(points_inside)
    
    return out


test_points: list[list[int]] = [[1, 3], [3, 3], [5, 3], [2, 2]]
test_queries: list[list[int]] = [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
test_out: list[int] = [3, 2, 2]
assert test_out == count_poins(test_points, test_queries)

test_points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
test_queries = [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]
test_out = [2, 3, 2, 4]
assert test_out == count_poins(test_points, test_queries)
