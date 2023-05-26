# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane,
# return the maximum number of points that lie on the same straight line.
# -----------------------
# 1 <= points.length <= 300  ,  points[i].length == 2  ,  -104 <= xi, yi <= 104
# All the points are unique.


def max_pointa(points: list[list[int]]) -> int:
    pass


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

test2 = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
test2_out = 4
