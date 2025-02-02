# Given an m x n grid. Each cell of the grid has a sign pointing to the next cell
#  you should visit if you are currently in this cell. The sign of grid[i][j] can be:
#  - 1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
#  - 2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
#  - 3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
#  - 4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
# Notice that there could be some signs on the cells
#  of the grid that point outside the grid.
# You will initially start at the upper left cell (0, 0).
# A valid path in the grid is a path that starts from the upper left cell (0, 0)
#  and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid.
# The valid path does not have to be the shortest.
# You can modify the sign on a cell with cost = 1.
# You can modify the sign on a cell one time only.
# Return the minimum cost to make the grid have at least one valid path.
# ------------------------
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# 1 <= grid[i][j] <= 4
from collections import deque


def min_cost(grid: list[list[int]]) -> int:
    # working_sol (69.87%, 63.98%) -> (104ms, 19.07mb)  time: O(m * n) | space: O(m * n)
    cell_row: int
    cell_column: int
    new_row: int
    new_column: int

    # [ right, left, bot, top ] <= (dy, dx)
    dirs: list[tuple[int, int]] = [
        (0, 1), (0, -1), (1, 0), (-1, 0), 
    ]
    # max_cost we could have is when we turn every cell on a path == m * n
    max_cost: int = len(grid) * len(grid[0]) + 100
    costs: list[list[int]] = [
        [max_cost for _ in range(len(grid[0]))] for _ in range(len(grid))
    ]
    costs[0][0] = 0  # start point
    # [ (row, column) ]
    que: deque[tuple[int, int]] = deque([(0, 0)])
    while que:
        cell_row, cell_column = que.popleft()
        for dir_index, (dy, dx) in enumerate(dirs):
            new_row, new_column = cell_row + dy, cell_column + dx
            # We don't need to turn arrow, if it's already facing check direction.
            turn_cost: int = 0 if (dir_index + 1) == grid[cell_row][cell_column] else 1
            # Correct cell and current path is less costly than a stored one.
            path_cost: int = costs[cell_row][cell_column] + turn_cost
            if (0 <= new_row < len(grid)
                 and 0 <= new_column < len(grid[0])
                 and costs[new_row][new_column] > path_cost):
                costs[new_row][new_column] = path_cost
                # Less effective => check last
                if 1 == turn_cost:
                    que.append(
                        (new_row, new_column)
                    )
                # More effective => check first
                else:
                    que.appendleft(
                        (new_row, new_column)
                    )

    return costs[-1][-1]
 

# Time complexity: O(m * n) <- m - length of the input matrix `grid`,
#                              n - length of the input matrix `grid`.
# Always traversing whole input matrix `grid`, once => O(m * n).
# ------------------------
# Auxiliary space: O(m * n)
# `que` <- allocates space for each cell of the `grid` => O(m * n).
# `costs` <- allocates space for each cell of the `grid` => O(2 * m * n).


test: list[list[int]] = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]
test_out: int = 3
assert test_out == min_cost(test)

test = [[1, 1, 3], [3, 2, 2], [1, 1, 4]]
test_out = 0
assert test_out == min_cost(test)

test = [[1, 2], [4, 3]]
test_out = 1
assert test_out == min_cost(test)
