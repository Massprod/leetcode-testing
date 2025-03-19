# You are given an n x n square matrix of integers grid.
# Return the matrix such that:
#  - The diagonals in the bottom-left triangle (including the middle diagonal)
#    are sorted in non-increasing order.
#  - The diagonals in the top-right triangle are sorted in non-decreasing order.
# ---------------------------
# grid.length == grid[i].length == n
# 1 <= n <= 10
# -10 ** 5 <= grid[i][j] <= 10 ** 5


def sort_matrix(grid: list[list[int]]) -> list[list[int]]:
    # working_sol (34.97%, 81.48%) -> (14ms, 17.72mb)  time: O(m * n * log(m * n))
    #                                                 space: O(sqr(m ** 2 + n ** 2))

    def sort_diag(
        start_y: int,
        start_x: int,
        matrix: list[list[int]],
        reverse: bool = False,
    ) -> None:
        values: list[int] = []
        populate: bool = False
        index: int = 0
        for step in range(2):
            if 1 == step:
                populate = True
                values.sort(reverse=reverse)
            row: int = start_y
            column: int = start_x
            while (0 <= row < len(matrix)
                and 0 <= column < len(matrix[0])):
                if not populate:
                    values.append(matrix[row][column])
                else:
                    matrix[row][column] = values[index]
                    index += 1
                row += 1
                column += 1

    for column in range(1, len(grid[0])):
        sort_diag(0, column, grid, False)
    for row in range(len(grid)):
        sort_diag(row, 0, grid, True)

    return grid


# Time complexity: O(m * n * log(m * n)) <- m - length of the input matrix `grid`,
#                                           n - height of the input matrix `grid`.
# Essentially we're sorting whole matrix anyway => O(m * n * log(m * n)).
# ---------------------------
# Auxiliary space: O(sqr(m ** 2 + n ** 2))
# `values` <- allocates space for all diagonals.
# diag of rectangle == sqr(m ** 2 + n ** 2).


test: list[list[int]] = [[1, 7, 3], [9, 8, 2], [4, 5, 6]]
test_out: list[list[int]] = [[8, 2, 3], [9, 6, 7], [4, 5, 1]]
assert test_out == sort_matrix(test)

test = [[0, 1], [1, 2]]
test_out = [[2, 1], [1, 0]]
assert test_out == sort_matrix(test)

test = [[1]]
test_out = [[1]]
assert test_out == sort_matrix(test)
