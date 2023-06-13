# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj)
#       such that row ri and column cj are equal.
# A row and column pair is considered equal if they contain the same elements
#       in the same order (i.e., an equal array).
# ----------------
# n == grid.length == grid[i].length
# 1 <= n <= 200  ,  1 <= grid[i][j] <= 10 ** 5


def equal_pairs(grid: list[list[int]]) -> int:
    # working_sol (72.9%, 56.95%) -> (496ms, 21.6mb)  time: O(m * n) | space: O(m * n)
    column_length: int = len(grid)
    row_length: int = len(grid[0])
    rows: dict[tuple[int], int] = {}
    pairs: int = 0
    for row in grid:
        t_row: tuple[int] = tuple(row)
        # counting rows and their duplicates
        if t_row not in rows:
            rows[t_row] = 1
            continue
        rows[t_row] += 1
    for x in range(row_length):
        column: list[int] = []
        for y in range(column_length):
            column.append(grid[y][x])
        t_column: tuple[int] = tuple(column)
        # adding number of rows with duplicates, to ignore looping through all rows
        if t_column in rows:
            pairs += rows[t_column]
    return pairs


# Time complexity: O(m * n) -> traversing input_matrix once to store all presented rows => O(m) ->
# m - len of matrix_column^^| -> traversing input_matrix once again to count every column which equal to a row =>
# n - len of matrix_row^^|       => O(m * n) -> O(m + (m * n)) => O(m * n).
# Auxiliary space: O(m * n) -> creating dictionary with keys equal to tuple(row) for every row in input_matrix,
#                              and values equal to their occurrences(counting duplicates) => O(m * n) ->
#                              -> creating/changing one list(column) for every column in input_matrix => O(m) ->
#                              -> creating/changing one tuple(column) for every column in input_matrix => O(m) ->
#                              -> O(m + m + m * n) => O(m * n).
# ----------------
# Rebuild solution is faster, because now we're not checking every row for a column in dictionaries,
# but simply checking if at least one column is IN rows which is O(1) instead of O(m) before.
# ----------------
# Don't why this task is marked Medium, but there's some tricky_part I don't see.
# Either it's TimeLimit and I need to find better searching way, or it's some reading of columns, rows.
# Otherwise, it's just too easy, which is fishy.
# ----------------
# Guess there's no reason to care about how we read the columns, rows.
# Because there's always 1 connected value in them, and it should be correctly placed for every pair ->
# -> so we're just reading rows as LEFT->RIGHT, columns as TOP->BOTTOM.
# At least for now, I don't see how reading backwards can be correct ->
# -> because we're reading either left->right + top->bottom or bottom->top + right->left,
# otherwise they're incorrect arrays. Will stick to a first option.


test1 = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
test1_out = 1
print(equal_pairs(test1))
assert test1_out == equal_pairs(test1)

test2 = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
test2_out = 3
print(equal_pairs(test2))
assert test2_out == equal_pairs(test2)

# test3 - failed -> I was counting only rows to columns, needed both.
test3 = [[3, 1, 2, 2], [1, 4, 4, 4], [2, 4, 2, 2], [2, 5, 2, 2]]
test3_out = 3
print(equal_pairs(test3))
assert test3_out == equal_pairs(test3)
