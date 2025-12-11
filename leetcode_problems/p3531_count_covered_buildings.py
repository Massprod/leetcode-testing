# You are given a positive integer n, representing an n x n city.
# You are also given a 2D grid buildings, where buildings[i] = [x, y]
#  denotes a unique building located at coordinates [x, y].
# A building is covered if there is at least one building
#  in all four directions: left, right, above, and below.
# Return the number of covered buildings.
# --- --- --- ---
# 2 <= n <= 10 ** 5
# 1 <= buildings.length <= 10 ** 5
# buildings[i] = [x, y]
# 1 <= x, y <= n
# All coordinates of buildings are unique.


def count_covered_buildings(n: int, buildings: list[list[int]]) -> int:
    # working_solution: (85.71%, 100%) -> (423ms, 54.04mb)  Time: O(n + m) Space: O(n)
    # fc - first cell
    # lc - last cell
    max_val: int = n + 1
    min_val: int = 0
    min_rows: list[int] = [max_val for _ in range(max_val)]
    max_rows: list[int] = [min_val for _ in range(max_val)]
    min_cols: list[int] = [max_val for _ in range(max_val)]
    max_cols: list[int] = [min_val for _ in range(max_val)]
    for col, row in buildings:
        min_rows[row] = min(min_rows[row], col)
        max_rows[row] = max(max_rows[row], col)
        min_cols[col] = min(min_cols[col], row)
        max_cols[col] = max(max_cols[col], row)
    
    out: int = 0
    for col, row in buildings:
        if (
            col > min_rows[row] and col < max_rows[row]
            and
            row > min_cols[col] and row < max_cols[col]
        ):
            out +=1
    
    return out


# Time complexity: O(n + m)
# m - length of the input array `buildings`
# Building all of the cells to use => O(4 * n).
# Traversing every building in buildings, twice => O(4 * n + 2 * m).
# --- --- --- ---
# Space complexity: O(n)


test_n: int = 3
test: list[list[int]]  = [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]]
test_out: int = 1
assert test_out == count_covered_buildings(test_n, test)

test_n = 3
test = [[1, 1], [1, 2], [2, 1], [2, 2]]
test_out = 0
assert test_out == count_covered_buildings(test_n, test)

test_n = 5
test = [[1, 3], [3, 2], [3, 3], [3, 5], [5, 3]]
test_out = 1
assert test_out == count_covered_buildings(test_n, test)
