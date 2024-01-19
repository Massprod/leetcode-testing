# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
# A falling path starts at any element in the first row
#  and chooses the element in the next row that is either directly below
#  or diagonally left/right.
# Specifically, the next element from position (row, col) will be
#  (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
# -----------------
# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# -100 <= matrix[i][j] <= 100
from functools import cache


def min_falling_path_sum(matrix: list[list[int]]) -> int:
    # working_sol (21.61%, 17.00%) -> (167ms, 26.08mb)  time: O(m * n) | space: O(m * n)
    # ! (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1) !
    options: list[tuple[int, int]] = [(1, -1), (1, 0), (1, 1)]

    @cache
    def dfs(row: int, col: int) -> int:
        if row == len(matrix):
            return 0
        min_path: int = 100 * 1000
        # Check every option, and choose the smallest sum with backtrack.
        for dy, dx in options:
            new_col: int = col + dx
            if 0 <= new_col < len(matrix[0]):
                min_path = min(min_path, dfs(row + dy, new_col) + matrix[row][col])
        return min_path

    out: int = 100 * 1000
    for column in range(len(matrix[0])):
        out = min(out, dfs(0, column))
    return out


# Time complexity: O(m * n) <- m - rows of input matrix `matrix`, n - columns of input matrix `matrix`.
# Because we can have overlaps, like: start = [0] -> [1] or [0] and start = [1] -> [0] or [1].
# We can use backtrack and @cache result for [1].
# So, we always only calculate (m * n) states => O(m * n).
# -----------------
# Auxiliary space: O(m * n).
# We're caching all this states => O(m * n).
# Extra recursion stack can be of size `m + 1`, because we're always going until len(matrix).


test: list[list[int]] = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
test_out: int = 13
assert test_out == min_falling_path_sum(test)

test = [[-19, 57], [-40, -5]]
test_out = -59
assert test_out == min_falling_path_sum(test)
