# You are given a 0-indexed n x n grid where n is odd, and grid[r][c] is 0, 1, or 2.
# We say that a cell belongs to the Letter Y if it belongs to one of the following:
#  - The diagonal starting at the top-left cell and ending at the center cell of the grid.
#  - The diagonal starting at the top-right cell and ending at the center cell of the grid.
#  - The vertical line starting at the center cell and ending at the bottom border of the grid.
# The Letter Y is written on the grid if and only if:
#  - All values at cells belonging to the Y are equal.
#  - All values at cells not belonging to the Y are equal.
#  - The values at cells belonging to the Y are different
#     from the values at cells not belonging to the Y.
# Return the minimum number of operations needed to write the letter Y
#  on the grid given that in one operation you can change the value at any cell to 0, 1, or 2.
# --- --- --- ---
# 3 <= n <= 49 
# n == grid.length == grid[i].length
# 0 <= grid[i][j] <= 2
# n is odd.


def minimum_operations_to_write_y(grid: list[list[int]]) -> int:
    # working_solution: (94.37%, 9.72%) -> (19ms, 18.23mb)  Time: O(n * n) Space: O(n * n)
    # ! n is odd !
    middle: int = len(grid) // 2

    inside_symbol: list[list[bool]] = [
        [False for _ in range(len(grid[0]))] for _ in range(len(grid))
    ]
    # Mark insides and outsides.
    for row in range(middle + 1):
        inside_symbol[row][row] = True                  # top-left -> center
        inside_symbol[row][len(grid) - 1 - row] = True  # top-right -> center
    for row in range(middle, len(grid)):                # center -> bottom
        inside_symbol[row][middle] = True
    # Count occurrences inside/outside [`0`, `1`, `2`]
    inside_count: list[int] = [0, 0, 0]
    outside_count: list[int] = [0, 0, 0]
    symbol_size: int = 0
    outside_size: int = 0
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            value: int = grid[row][column]
            if inside_symbol[row][column]:
                inside_count[value] += 1
                symbol_size += 1
            else:
                outside_count[value] += 1
                outside_size += 1

    out: int = len(grid) * len(grid)
    options: tuple[int, int, int] = (0, 1 , 2)
    # Try out every possible switch option we have.
    for a in options:
        for b in options:
            if a == b:
                continue
            # (switches inside the symbol) + (switched outside the symbol)
            switch_cost: int = (
                (symbol_size - inside_count[a]) + (outside_size - outside_count[b])
            )
            out = min(out, switch_cost)

    return out


# # Time complexity: O(n * n) <- n - length | height of the input square matrix `grid`.
# Always traversing whole matrix to get inside & outside coordinates, once => O(n * n).
# Extra traversing whole matrix to get count of the values inside & outside, once => O(2 * n * n).
# And options check is always constant, because we're always using the same options.
# --- --- --- ---
# Space complexity: O(n * n)
# `inside_symbol` <- allocates space for each cell of the input square matrix `grid`.


test: list[list[int]] = [[1, 2, 2], [1, 1, 0], [0, 1, 0]]
test_out: int = 3
assert test_out == minimum_operations_to_write_y(test)

test = [
    [0, 1, 0, 1, 0], [2, 1, 0, 1, 2], [2, 2, 2, 0, 1], [2, 2, 2, 2, 2], [2, 1, 2, 2, 2]
]
test_out = 12
assert test_out == minimum_operations_to_write_y(test)
