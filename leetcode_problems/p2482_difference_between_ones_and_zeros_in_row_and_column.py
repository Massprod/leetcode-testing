# You are given a 0-indexed m x n binary matrix grid.
# A 0-indexed m x n difference matrix diff is created with the following procedure:
#   - Let the number of ones in the ith row be onesRowi.
#   - Let the number of ones in the jth column be onesColj.
#   - Let the number of zeros in the ith row be zerosRowi.
#   - Let the number of zeros in the jth column be zerosColj.
#   - diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
# Return the difference matrix diff.
# --------------------------
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10 ** 5
# 1 <= m * n <= 10 ** 5
# grid[i][j] is either 0 or 1.
from random import randint


def ones_minus_zeros(grid: list[list[int]]) -> list[list[int]]:
    # working_sol (88.93%, 70.36%) -> (1340ms, 51.28mb)  time: O(m * n) | space: O(m + n)
    # {row: ones - zeros}
    rows: dict[int, int] = {row: 0 for row in range(len(grid))}
    # {col: ones - zeros}
    cols: dict[int, int] = {col: 0 for col in range(len(grid[0]))}
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]:
                rows[row] += 1
                cols[col] += 1
            else:
                rows[row] -= 1
                cols[col] -= 1
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # ! diff[i][j] = onesRowi - zerosRowi + onesColj - zerosColj !
            grid[row][col] = rows[row] + cols[col]
    return grid


# Time complexity: O(m * n) <- m - length of input matrix `grid`, n - height of input matrix `grid`.
# Creating `rows` and `cols` with (row: int), (col: int) pairs => O(m + n).
# Fully traversing input matrix `grid` to get all (ones - zeros) for rows and cols => O(m * n).
# Another traverse of full matrix `grid` to reassign differences => O(m * n).
# --------------------------
# Auxiliary space: O(m + n)
# Two dictionaries `rows` and `cols` with all rows and cols stores in them => O(m + n).


test: list[list[int]] = [[0, 1, 1], [1, 0, 1], [0, 0, 1]]
test_out: list[list[int]] = [[0, 0, 4], [0, 0, 4], [-2, -2, 2]]
assert test_out == ones_minus_zeros(test)

test = [[1, 1, 1], [1, 1, 1]]
test_out = [[5, 5, 5], [5, 5, 5]]
assert test_out == ones_minus_zeros(test)

test = [[randint(0, 1) for col in range(10 ** 3)] for _ in range(10 ** 2)]
print(test)
