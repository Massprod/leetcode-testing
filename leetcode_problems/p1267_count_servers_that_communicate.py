# You are given a map of a server center, represented as a m * n integer matrix grid,
#  where 1 means that on that cell there is a server and 0 means that it is no server.
# Two servers are said to communicate if they are on the same row or on the same column.
# Return the number of servers that communicate with any other server.
# ----------------------
# m == grid.length
# n == grid[i].length
# 1 <= m <= 250
# 1 <= n <= 250
# grid[i][j] == 0 or 1
from collections import defaultdict


def count_servers(grid: list[list[int]]) -> int:
    # working_sol (18.73%, 22.47%) -> (34ms, 19.76mb)  time: O(m * n) | space: O(m + n)
    # { row: 1 on this row }
    rows: dict[int, int] = {
        index: row.count(1) for index, row in enumerate(grid)
    }
    # { col: 1 on this column }
    cols: dict[int, int] = defaultdict(int)
    for column in range(len(grid[0])):
        for row in range(len(grid)):
            cols[column] += grid[row][column]
    out: int = 0
    # Visit every cell, once.
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if not grid[row][col]:
                continue
            if 1 < rows[row] or 1 < cols[col]:
                out += 1
            
    return out


# Time complexity: O(m * n) <- m - length of the input array `grid`,
#                              n - height of the input array `grid`
# Always traversing whole input array, 3 times => O(3 * m * n).
# ----------------------
# Auxiliary space: O(m + n)
# `rows` <- allocates space for each row in `grid` => O(n).
# `cols` <- allocates space for each column in `grid` => O(m).


test: list[list[int]] = [[1,0],[0,1]]
test_out: int = 0
assert test_out == count_servers(test)

test = [[1,0],[1,1]]
test_out = 3
assert test_out == count_servers(test)

test = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
test_out = 4
assert test_out == count_servers(test)
