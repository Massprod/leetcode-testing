# Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.',
#  return the number of submatrices that contain:
#  - grid[0][0]
#  - an equal frequency of 'X' and 'Y'.
#  - at least one 'X'.
# --- --- --- ---
# 1 <= grid.length, grid[i].length <= 1000
# grid[i][j] is either 'X', 'Y', or '.'.


def number_of_submatrices(grid: list[list[str]]) -> int:
    # working_solution: (72.04%, 17.20%) -> (719ms, 169.73mb)  Time: O(m * n) Space: O(m * n)
    # grid[0][0] <- is it a symbol on this position.
    # Or an actual cell... Assume that an actual cell :)
    # X = 1, Y = -1, so we don't use extra space for counting.
    # Equal state is only `0`
    char_map: dict[str, int] = {
        'X': 1,
        'Y': -1,
    }
    # [ (char_val, X present) ]
    grid_int: list[list[tuple[int, bool]]] = [
        [(char_map.get(char, 0), True if char == 'X' else False) for char in row] for row in grid
    ]
    all_zeroes: bool = True
    for row in grid_int:
        if any(row):
            all_zeroes = False
            break
    out: int = 0
    if all_zeroes:
        return out
    
    # Essentially we're checkin 2 submatrices:
    # 1. Sub on top of the current cell.
    #    And because we need to include grid[0][0] it's always starts from it.
    # 2. Current row sub.
    # So, we need the row sub sum and top sum.
    for row in range(len(grid_int)):
        row_sum: int = 0
        row_x_present: bool = False
        for column in range(len(grid_int[0])):
            prefix_top, top_x_present = grid_int[row - 1][column] if 0 < row else (0, False)
            row_sum += grid_int[row][column][0]
            row_x_present = grid_int[row][column][1] | row_x_present
            sub_sum: int = row_sum + prefix_top
            sub_x_present: bool = top_x_present | grid_int[row][column][1] | row_x_present
            grid_int[row][column] = (sub_sum, sub_x_present)
            if sub_x_present and 0 == sub_sum:
                out += 1
    
    return out


# Time complexity: O(m * n)
# n - length of the input matrix `grid`,
# m - height of the input matrix `grid`.
# --- --- --- ---
# Space complexity: O(m * n)


test: list[list[str]] = [
    ["X", "Y", "."], ["Y", ".", "."]
]
test_out: int = 3
assert test_out == number_of_submatrices(test)

test = [
    ["X", "X"], ["X", "Y"]
]
test_out = 0
assert test_out == number_of_submatrices(test)

test = [
    [".", "."], [".", "."]
]
test_out = 0
assert test_out == number_of_submatrices(test)

test = [
    [".", ".", "."],
    [".", "X", "X"],
    ["Y", ".", "."],
    ["X", ".", "."],
]
test_out = 2
assert test_out == number_of_submatrices(test)
