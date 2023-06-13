# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj)
#       such that row ri and column cj are equal.
# A row and column pair is considered equal if they contain the same elements
#       in the same order (i.e., an equal array).
# ----------------
# n == grid.length == grid[i].length
# 1 <= n <= 200  ,  1 <= grid[i][j] <= 10 ** 5


def equal_pairs(grid: list[list[int]]) -> int:
    # working_sol (14.93%, 56.95%) -> (800ms, 21.5mb)  time: O(m * n) | space: O(m * n)
    column_length: int = len(grid)
    row_length: int = len(grid[0])
    rows: dict[int, list[int]] = {}
    columns: dict[int, list[int]] = {}
    for y in range(column_length):
        for x in range(row_length):
            value: int = grid[y][x]
            if x not in columns:
                columns[x] = [value]
            else:
                columns[x].append(value)
            if y not in rows:
                rows[y] = [value]
            else:
                rows[y].append(value)
    pairs: int = 0
    for row in rows.values():
        for column in columns.values():
            if row == column:
                pairs += 1
    return pairs


# Time complexity: O(m * n) -> traversing input_matrix once to create all rows, columns and store them => O(m * n) ->
# m - len of matrix_column^^| -> traversing created dictionaries with stored values, to find duplicates => O(m * n) ->
# n - len of matrix_row^^|    -> O(2 * (m * n)) => O(m * n).
# Auxiliary space: O(m * n) -> creating dictionary with keys equal to m and values equal to rows => O(m * n) ->
#                             -> creating second dictionary with keys equal to n and values equal to columns =>
#                             => O(n * m) -> O(2 * (m * n)) => O(m * n).
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
