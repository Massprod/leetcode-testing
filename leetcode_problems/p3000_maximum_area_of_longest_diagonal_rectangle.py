# You are given a 2D 0-indexed integer array dimensions.
# For all indices i, 0 <= i < dimensions.length, dimensions[i][0]
#  represents the length and dimensions[i][1] represents the width of the rectangle i.
# Return the area of the rectangle having the longest diagonal.
# If there are multiple rectangles with the longest diagonal,
#  return the area of the rectangle having the maximum area.
# --- --- --- ---
# 1 <= dimensions.length <= 100
# dimensions[i].length == 2
# 1 <= dimensions[i][0], dimensions[i][1] <= 100
from math import sqrt


def area_of_max_diagonal(dimensions: list[list[int]]) -> int:
    # working_solution: (100%, 67.18%) -> (0ms, 17.77mb)  Time: O(n) Space: O(1)
    # area == length * width
    # diagonal = sqrt(length ** 2 + width ** 2)
    cur_diag: float = 0
    cur_area: int = 0
    for length, width in dimensions:
        diagonal: float = sqrt(
            length ** 2 + width ** 2
        )
        if cur_diag < diagonal:
            cur_diag, cur_area = diagonal, length * width
        elif cur_diag == diagonal:
            new_area: int = length * width
            if new_area <= cur_area:
                continue
            cur_area, cur_diag = new_area, diagonal
    
    return cur_area


# Time complexity: O(n) <- n - length of the input array `dimensions`
# Always traversing the whole input array `dimensions`, once => O(n).
# --- --- --- ---
# Space complexity: O(1)


test: list[list[int]] = [[9, 3], [8, 6]]
test_out: int = 48
assert test_out == area_of_max_diagonal(test)

test = [[3, 4], [4, 3]]
test_out = 12
assert test_out == area_of_max_diagonal(test)
