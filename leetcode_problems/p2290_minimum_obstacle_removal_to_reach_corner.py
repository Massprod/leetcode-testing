# You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:
#  - 0 represents an empty cell,
#  - 1 represents an obstacle that may be removed.
# You can move up, down, left, or right from and to an empty cell.
# Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0)
#  to the lower right corner (m - 1, n - 1).
# -------------------------
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10 ** 5
# 2 <= m * n <= 10 ** 5
# grid[i][j] is either 0 or 1.
# grid[0][0] == grid[m - 1][n - 1] == 0
import heapq


def minimum_obstacle(grid: list[list[int]]) -> int:
    # working_sol (50.62%, 26.32%) -> (1569ms, 47.34mb)  time: O(m * n * log n) | space: O(m * n)
    cost: int
    row: int
    col: int
    target_row: int = len(grid) - 1
    target_col: int = len(grid[0]) - 1
    # [ top, right, bot, left ]
    directions: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    # ( cost, row, col )
    que: list[tuple[int, int, int]] = [(0, 0, 0)]
    heapq.heapify(que)
    visited: set[tuple[int, int]] = {(0, 0)}
    # Standard Dijkstra
    while que:
        cost, row, col = heapq.heappop(que)
        for dy, dx in directions:
            new_row: int = row + dy
            new_col: int = col + dx
            if not (0 <= new_row < len(grid)
                    and 0 <= new_col < len(grid[0])
                    and (new_row, new_col) not in visited):
                continue
            if new_row == target_row and new_col == target_col:
                return cost
            new_cost: int = cost + grid[new_row][new_col]
            heapq.heappush(
                que,
                (new_cost, new_row, new_col)
            )
            visited.add(
                (new_row, new_col)
            )
    return -1


# Time complexity: O(m * n * log (m * n)) <- m - height of the input matrix `grid`,
#                                            n - length of the input matrix `grid`.
# Standard Dijkstra uses (m * n) cells as default BFS, and we're using `heap` to push and pop values.
# Every cell will be pushed and popped from `heap` => O(m * n * log (m * n)).
# -------------------------
# Auxiliary space: O(m * n)
# `que` <- allocates space for each visited cell => O(m * n).
# `visited` <- allocates space for each visited cell => O((m * n) * 2).


test: list[list[int]] = [[0, 1, 1], [1, 1, 0], [1, 1, 0]]
test_out: int = 2
assert test_out == minimum_obstacle(test)

test = [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]
test_out = 0
assert test_out == minimum_obstacle(test)
