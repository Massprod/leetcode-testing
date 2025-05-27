# You are given an m x n integer matrix grid, and three integers row, col, and color.
# Each value in the grid represents the color of the grid square at that location.
# Two squares are called adjacent if they are next to each other in any of the 4 directions.
# Two squares belong to the same connected component
#  if they have the same color and they are adjacent.
# The border of a connected component is all the squares in the connected component
#  that are either adjacent to (at least) a square not in the component,
#  or on the boundary of the grid (the first or last row or column).
# You should color the border of the connected component
#  that contains the square grid[row][col] with color.
# Return the final grid.
# -----------------------
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 1 <= grid[i][j], color <= 1000
# 0 <= row < m
# 0 <= col < n
from collections import deque


def color_border(grid: list[list[int]], row: int, col: int, color: int) -> list[list[int]]:
    # working_sol (100.00%, 89.49%) -> (0ms, 17.91mb)  time: O(m * n) | space: O(m * n)
    cur_row: int
    cur_col: int
    # Standard BFS with edge elements.
    que: deque[tuple[int, int]] = deque([(row, col)])
    # We can't alter original matrix => save in `visited`.
    visited: set[tuple[int, int]] = {(row, col)}
    # top, right, bot, left
    directions: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    # [(row, col)] <- all border cells
    border_elements: list[tuple[int, int]] = []
    row_limit: int = len(grid)
    col_limit: int = len(grid[0])
    init_color: int = grid[row][col]
    while que:
        cur_row, cur_col = que.popleft()
        # Surrounded by 4 component elements.
        component_neighbours: bool = True
        for dy, dx in directions:
            new_row: int = cur_row + dy
            new_col: int = cur_col + dx
            new_coord: tuple[int, int] = (new_row, new_col)
            if new_coord in visited:
                continue
            if (not (0 <= new_row < row_limit)
                or not (0 <= new_col < col_limit)):
                component_neighbours = False
                continue
            if init_color != grid[new_row][new_col]:
                component_neighbours = False
                continue
            que.append(new_coord)
            visited.add(new_coord)
        # One of the adjacent elements are not in the component
        #  or it's on the border matrix.
        if not component_neighbours:
            border_elements.append(
                (cur_row, cur_col)
            )
    for cell in border_elements:
        grid[cell[0]][cell[1]] = color

    return grid


# Time complexity: O(m * n) <- m - height of the input matrix `grid`,
#                              n - length of the input matrix `grid`.
# In the worst case, we're going to have a matrix of 2x2 size, with 1 component.
# BFS will traverse whole matrix, once => O(m * n)
# And we extra traverse whole matrix to change the color,
#  because every element is border element => O(2 * m * n).
# -----------------------
# Auxiliary space: O(m * n)
# `que` <- allocates space for each cell of the matrix `grid` => O(m * n).
# `visited` <- allocates space for each cell of the matrig `grid` => O(2 * m * n).


test: list[list[int]] = [[1, 1], [1, 2]]
test_row: int = 0
test_col: int = 0
test_color: int = 3
test_out: list[list[int]] = [[3, 3], [3, 2]]
assert test_out == color_border(test, test_row, test_col, test_color)

test = [[1, 2, 2], [2, 3, 2]]
test_row = 0
test_col = 1
test_color = 3
test_out = [[1, 3, 3], [2, 3, 3]]
assert test_out == color_border(test, test_row, test_col, test_color)

test = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
test_row = 1
test_col = 1
test_color = 2
test_out = [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
assert test_out == color_border(test, test_row, test_col, test_color)
