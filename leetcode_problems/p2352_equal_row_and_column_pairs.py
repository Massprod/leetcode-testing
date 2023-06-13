# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj)
#       such that row ri and column cj are equal.
# A row and column pair is considered equal if they contain the same elements
#       in the same order (i.e., an equal array).
# ----------------
# n == grid.length == grid[i].length
# 1 <= n <= 200  ,  1 <= grid[i][j] <= 10 ** 5


def equal_pairs(grid: list[list[int]]) -> int:
    pass


test1 = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
test1_out = 1

test2 = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
test2_out = 3
