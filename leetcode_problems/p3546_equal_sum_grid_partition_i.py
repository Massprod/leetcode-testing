# You are given an m x n matrix grid of positive integers.
# Your task is to determine if it is possible to make either one horizontal
#  or one vertical cut on the grid such that:
# Each of the two resulting sections formed by the cut is non-empty.
# The sum of the elements in both sections is equal.
# Return true if such a partition exists; otherwise return false.
# --- --- --- ---
# 1 <= m == grid.length <= 10 ** 5
# 1 <= n == grid[i].length <= 10 ** 5
# 2 <= m * n <= 10 ** 5
# 1 <= grid[i][j] <= 10 ** 5


def can_partition_grid(grid: list[list[int]]) -> bool:
    # working_solution: (84.25%, 35.62%) -> (106ms, 47.02mb)  Time: O(n * m) Space: O(n + m)
    cur_dif: int

    sum_grid: int = 0
    # Horizontal slice.
    sum_rows: list[int] = []
    for row in grid:
        sum_row: int = sum(row)
        sum_rows.append(sum_row)
        sum_grid += sum_row
    # Check each row for horizontal slice.
    sum_horiz: int = 0
    for sum_row in sum_rows:
        sum_horiz += sum_row
        cur_dif = sum_grid - sum_horiz
        if cur_dif == sum_horiz:
            return True
        # Everything after this, will be lower.
        elif cur_dif < sum_horiz:
            break        
    # Vertical slice.
    sum_cols: list[int] = []
    for col in range(len(grid[0])):
        sum_col: int = 0
        for row in range(len(grid)):
            sum_col += grid[row][col]
        sum_cols.append(sum_col)
    # Check each column for vertical slice.
    sum_vert: int = 0
    for sum_col in sum_cols:
        sum_vert += sum_col
        cur_dif = sum_grid - sum_vert
        if cur_dif == sum_vert:
            return True
        elif cur_dif < sum_vert:
            break

    return False


# Time complexity: O(n * m)
# --- --- --- ---
# Space complexity: O(n + m)


test: list[list[int]] = [[1, 4], [2, 3]]
test_out: bool = True
assert test_out == can_partition_grid(test)

test = [[1, 3], [2, 4]]
test_out = False
assert test_out == can_partition_grid(test)
