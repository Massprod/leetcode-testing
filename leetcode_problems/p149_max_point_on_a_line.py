# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane,
# return the maximum number of points that lie on the same straight line.
# -----------------------
# 1 <= points.length <= 300  ,  points[i].length == 2  ,  -104 <= xi, yi <= 104
# All the points are unique.
import math


def max_points(points: list[list[int]]) -> int:
    # working_sol (66.22%, 29.41%) -> (92ms, 16.5mb)  time: O((n * n) * (log n)) | space: O(n)
    length: int = len(points)
    if length == 1:
        return 1
    if length == 2:
        return 2

    def normalize_float(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
        run: int = y[0] - x[0]
        if run == 0:
            return 1, 0
        if run < 0:
            x, y = y, x
            run = y[0] - x[0]
        rise: int = y[1] - x[1]
        greatest_common_div: int = math.gcd(abs(rise), abs(run))
        return rise // greatest_common_div, run // greatest_common_div

    max_on_line: int = 0
    for g in range(length):
        point: tuple = tuple(points[g])
        slopes: dict = {}
        for h in range(g + 1, length):
            pair: tuple = tuple(points[h])
            if point == pair:
                continue
            slope: tuple = normalize_float(point, pair)
            if slope in slopes:
                slopes[slope] += 1
                continue
            slopes[slope] = 2
        if slopes.values():
            max_on_line = max(max_on_line, max(slopes.values()))
    return max_on_line


# Time complexity: O((n * n) * (log n)) -> traversing whole input_list with nested loop => O(n * n) ->
# n - length of input_list^^   -> for every point we check, normalizing their slope(float),
#                                 constant actions with same input sizes => O(1) ->
#                              -> for every index g we're trying to check, creating dictionary and populating it
#                                 only with part of the input_list values => O(log n) ->
#                              -> choosing max_on_line between int and populated dictionary => O(1) <- hash table.
# Space complexity: O(n) -> creating extra dictionary, with size of input_list in the worst_case ->
# n - length of input_list^^ -> every point will have unique slope with our check_point(points[g]) => O(n)
# !
#   For each point p, calculate its slope with other points and use a map to record
#  how many points have same slope, by which we can find out how many points are on same line
#  with p as their one point. For each point keep doing the same thing and update
#  the maximum number of point count found so far.
#   To get rid of the precision problems, we treat slope as pair ((y2 – y1), (x2 – x1))
#  instead of ratio, and reduce pair by their gcd before inserting into map. !
#  No way to solve it without knowing this math ^^.
# I was trying to solve it, like queen problem...


test1 = [[1, 1], [2, 2], [3, 3]]
test1_out = 3
print(max_points(test1))

test2 = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
test2_out = 4
print(max_points(test2))

# test3 - failed -> failed to consider, that every 2 points can be a 1 line at any coordinates,
#                   so if we only have >= (2 points) -> it's by default 2 points_straight_line.
#                   And only after that we should count everything else.
test3 = [[2, 3], [1, 1]]
test3_out = 2
print(max_points(test3))

# test4 - failed -> not on diagonals and hor,vert. How can we make a line?
test4 = [[-6, -1], [3, 1], [12, 3]]
test4_out = 3
print(max_points(test4))
