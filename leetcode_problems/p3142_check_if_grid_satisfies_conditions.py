# You are given a 2D matrix grid of size m x n.
# You need to check if each cell grid[i][j] is:
# Equal to the cell below it, i.e. grid[i][j] == grid[i + 1][j] (if it exists).
# Different from the cell to its right, i.e. grid[i][j] != grid[i][j + 1] (if it exists).
# Return true if all the cells satisfy these conditions, otherwise, return false.
# -----------------------
# 1 <= n, m <= 10
# 0 <= grid[i][j] <= 9


def satisfies_conditions(grid: list[list[int]]) -> bool:
    # working_sol (78.77%, 35.93%) -> (70ms, 16.51mb)  time: O(n * m) | space: O(1)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if 0 <= row < len(grid) - 1:
                if grid[row][col] != grid[row + 1][col]:
                    return False
            if 0 <= col < len(grid[row]) - 1:
                if grid[row][col] == grid[row][col + 1]:
                    return False
    return True


# Time complexity: O(n * m) <- n - length of the input matrix `grid`, m - height of the input matrix `grid`.
# Always traversing whole input matrix `grid`, once => O(n * m).
# -----------------------
# Auxiliary space: O(1)
# Nothing extra is used.


test: list[list[int]] = [[1, 0, 2], [1, 0, 2]]
test_out: bool = True
assert test_out == satisfies_conditions(test)

test = [[1, 1, 1], [0, 0, 0]]
test_out = False
assert test_out == satisfies_conditions(test)

test = [[1], [2], [3]]
test_out = False
assert test_out == satisfies_conditions(test)
