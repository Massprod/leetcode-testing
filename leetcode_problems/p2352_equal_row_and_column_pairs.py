# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj)
#       such that row ri and column cj are equal.
# A row and column pair is considered equal if they contain the same elements
#       in the same order (i.e., an equal array).
# ----------------
# n == grid.length == grid[i].length
# 1 <= n <= 200  ,  1 <= grid[i][j] <= 10 ** 5


def equal_pairs(grid: list[list[int]]) -> int:
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
        if row in columns.values():
            pairs += 1
    return pairs


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

test2 = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
test2_out = 3
print(equal_pairs(test2))
