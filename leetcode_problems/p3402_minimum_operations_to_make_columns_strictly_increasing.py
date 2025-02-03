# You are given a m x n matrix grid consisting of non-negative integers.
# In one operation, you can increment the value of any grid[i][j] by 1.
# Return the minimum number of operations needed to make all columns
#  of grid strictly increasing.
# ----------------------
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 0 <= grid[i][j] < 2500


def minimum_operations(grid: list[list[int]]) -> int:
    # working_sol (79.50%, 85.15%) -> (7ms, 17.97mb)  time: O(m * n) | space: O(1)
    out: int = 0

    for column in range(len(grid[0])):
        cur_val: int = grid[0][column]
        for row in range(1, len(grid)):
            if cur_val < grid[row][column]:
                cur_val = grid[row][column]
                continue
            diff: int = abs(
                grid[row][column] - cur_val
            ) + 1
            out += diff
            cur_val = diff + grid[row][column]
    
    return out

# Time complexity: O(m * n) <- m - length of the input array `grid`,
#                              n - length of the input array `grid`.
# Always traversing whole input matrix `grid`, once => O(m * n).
# ----------------------
# Auxiliary space: O(1)


test: list[list[int]] = [[3, 2], [1, 3], [3, 4],[0, 1]]
test_out: int = 15
assert test_out == minimum_operations(test)

test = [[3, 2, 1], [2, 1, 0], [1, 2, 3]]
test_out = 12
assert test_out == minimum_operations(test)
