# Given an array of points on the X-Y plane points where points[i] = [xi, yi],
#  return the area of the largest triangle that can be formed
#  by any three different points.
# Answers within 10 ** -5 of the actual answer will be accepted.
# --- --- --- ---
# 3 <= points.length <= 50
# -50 <= xi, yi <= 50
# All the given points are unique.
import math


def largest_triangle_area(points: list[list[int]]) -> float:
    # working_solution: (13.14%, 73.42%) -> (143ms, 17.71mb)  Time: O(n ** 3) Space: O(1)
    def distance(point1: list[int], point2: list[int]) -> float:
        px1, py1 = point1
        px2, py2 = point2
        dist_x: int = px1 - px2
        dist_y: int =  py1 - py2
        
        dist: float = math.sqrt(dist_x ** 2 + dist_y ** 2)
        return dist
    
    out: float = 0.0
    for first in range(len(points)):
        for second in range(first + 1, len(points)):
            for third in range(second + 1, len(points)):
                side_a: float = distance(
                    points[first], points[second]
                )
                side_b: float = distance(
                    points[second], points[third]
                )
                side_c: float = distance(
                    points[third], points[first]
                )
                # semi_perimeter
                s: float = (side_a + side_b + side_c) / 2.0
                # Find terms <- using `0.0` in case we get a negative
                res: float = max(
                    s * (s - side_a) * (s - side_b) * (s - side_c),
                    0.0
                )
                # Get the area.
                area: float = math.sqrt(res)
                
                out = max(area, out)
    
    return out


# Time complexity: O(n ** 3) <- n - length of the input array `points`
# Triple nested loop with check of the every possible par we can use => O(n ** 3).
# --- --- --- ---
# Space complexity: O(1)


test: list[list[int]] = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
test_out: float = 2.00
print(largest_triangle_area(test))

test = [[1, 0], [0, 0], [0, 1]]
test_out = 0.50_000
print(largest_triangle_area(test))
