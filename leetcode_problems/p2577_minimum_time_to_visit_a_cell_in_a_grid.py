# You are given a m x n matrix grid consisting of non-negative integers where grid[row][col]
#  represents the minimum time required to be able to visit the cell (row, col),
#  which means you can visit the cell (row, col) only when the time you visit
#   it is greater than or equal to grid[row][col].
# You are standing in the top-left cell of the matrix in the 0th second,
#  and you must move to any adjacent cell in the four directions: up, down, left, and right.
# Each move you make takes 1 second.
# Return the minimum time required in which you can visit the bottom-right cell of the matrix.
# If you cannot visit the bottom-right cell, then return -1
# ------------------------
# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 1000
# 4 <= m * n <= 10 ** 5
# 0 <= grid[i][j] <= 10 ** 5
# grid[0][0] == 0
import heapq


def minimum_time(grid: list[list[int]]) -> int:
    # working_sol (86.28%, 98.91%) -> (669ms, 27.58mb)  time: O(n * m * log (m * n)) | space: O(n * m)
    cost: int
    row: int
    col: int
    # We can't even start
    if 1 < grid[0][1] and 1 < grid[1][0]:
        return -1
    target_row: int = len(grid) - 1
    target_col: int = len(grid[0]) - 1
    # [ top, right, bot, left ]
    directions: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    # [ (cost, row, col) ]
    que: list[tuple[int, int, int]] = [(0, 0, 0)]
    heapq.heapify(que)
    while que:
        cost, row, col = heapq.heappop(que)
        for dy, dx in directions:
            new_row: int = row + dy
            new_col: int = col + dx
            if (not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]))
                    or -1 == grid[new_row][new_col]):
                continue
            new_cost: int = cost + 1
            if new_cost < grid[new_row][new_col]:
                # If we need to wait and move back-forth to waste time.
                # We will either make `odd` steps and enter the desired cell.
                # Or we're going to make `even` steps and enter the desired cell with delay.
                # Depends on the difference between a current_cell and desired cell.
                wait_time: int = 0 if (grid[new_row][new_col] - cost) % 2 else 1
                new_cost = max(
                    new_cost,  # we can just continue and step into the next cell
                    wait_time + grid[new_row][new_col]  # we need to make some back-forth moves
                )
            if new_row == target_row and new_col == target_col:
                return new_cost
            heapq.heappush(
                que,
                (new_cost, new_row, new_col)
            )
            grid[new_row][new_col] = -1
    return -1


# Time complexity: O(n * m * log (n * m)) <- n - height of the input matrix `grid`,
#                                            m - length of the input matrix `grid`.
# Standard Dijksta with using every cell of the matrix, and pop(), push() them in `que` => O(n * m * log (n * m))
# ------------------------
# Auxiliary space: O(n * m)
# `que` <- allocates space for each cell of the matrix `grid` => O(n * m).


test: list[list[int]] = [[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]]
test_out: int = 7
assert test_out == minimum_time(test)

test = [[0, 2, 4], [3, 2, 1], [1, 0, 4]]
test_out = -1
assert test_out == minimum_time(test)
