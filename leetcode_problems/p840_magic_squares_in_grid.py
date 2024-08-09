# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9
#  such that each row, column, and both diagonals all have the same sum.
# Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?
# Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.
# --------------------------
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 10
# 0 <= grid[i][j] <= 15


def num_magic_squares_inside(grid: list[list[int]]) -> int:
    # working_sol (81.03%, 53.33%) -> (37ms, 16.60mb)  time: O(m * n) | space: O(1)

    def magic_check(start_row: int, start_col: int) -> bool:
        # We always should have 1-9 unique values in 3x3, inclusive.
        used_values: set[int] = {val for val in range(1, 10)}
        for _row in range(start_row, start_row + 3):
            for _col in range(start_col, start_col + 3):
                value: int = grid[_row][_col]
                if value not in used_values:
                    return False
                used_values.remove(value)
        # And w.e the combination of values we use, it's going to be 15.
        # On every row, column and diagonal
        over_all_sum: int = 15
        # rows check
        for _row in range(start_row, start_row + 3):
            cur_row_sum: int = 0
            for _col in range(start_col, start_col + 3):
                cur_row_sum += grid[_row][_col]
            if over_all_sum != cur_row_sum:
                return False
        # col's check
        cols_sum: int = 0
        for _col in range(start_col, start_col + 3):
            cur_col_sum: int = 0
            for _row in range(start_row, start_row + 3):
                cur_col_sum += grid[_row][_col]
            if over_all_sum != cur_col_sum:
                return False
        # diag's check
        desc_diag_y: int = start_row
        desc_diag_x: int = start_col
        cur_diag_sum: int = grid[desc_diag_y][desc_diag_x]
        for _ in range(2):
            desc_diag_y += 1
            desc_diag_x += 1
            cur_diag_sum += grid[desc_diag_y][desc_diag_x]
        if over_all_sum != cur_diag_sum:
            return False
        asc_diag_y: int = start_row + 2
        asc_diag_x: int = start_col
        cur_diag_sum = grid[asc_diag_y][asc_diag_x]
        for _ in range(2):
            asc_diag_y -= 1
            asc_diag_x += 1
            cur_diag_sum += grid[asc_diag_y][asc_diag_x]
        if over_all_sum != cur_diag_sum:
            return False
        return True

    out: int = 0
    for row in range(len(grid) - 2):
        for col in range(len(grid[0]) - 2):
            if magic_check(row, col):
                out += 1
    return out


# Time complexity: O(m * n) <- m - height of the input matrix `grid`, n - length of the input matrix `grid`.
# Always using `m - 2` rows and `n - 2` columns to start `magic_check`.
# And because `magic_check` is always performs the same actions, we can count it as constant => O(m * n).
# --------------------------
# Auxiliary space: O(1)
# `used_values` <- always of the same size `9` => O(1).
# All the INT's used, always present, nothing depends on input => O(1).


test: list[list[int]] = [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]
test_out: int = 1
assert test_out == num_magic_squares_inside(test)

test = [[8]]
test_out = 0
assert test_out == num_magic_squares_inside(test)

test = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
test_out = 0
assert test_out == num_magic_squares_inside(test)

test = [
    [9, 9, 5, 1, 9, 5, 5, 7, 2, 5], [9, 1, 8, 3, 4, 6, 7, 2, 8, 9], [4, 1, 1, 5, 9, 1, 5, 9, 6, 4],
    [5, 5, 6, 7, 2, 8, 3, 4, 0, 6], [1, 9, 1, 8, 3, 1, 4, 2, 9, 4], [2, 8, 6, 4, 2, 7, 3, 2, 7, 6],
    [9, 2, 5, 0, 7, 8, 2, 9, 5, 1], [2, 1, 4, 4, 7, 6, 2, 4, 3, 8], [1, 2, 5, 3, 0, 5, 10, 8, 5, 2],
    [6, 9, 6, 8, 8, 4, 3, 6, 0, 9]
]
test_out = 3
assert test_out == num_magic_squares_inside(test)
