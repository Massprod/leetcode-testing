# You are given an m x n binary matrix grid,
#  where 0 represents a sea cell and 1 represents a land cell.
# A move consists of walking from one land cell to another adjacent (4-directionally)
#  land cell or walking off the boundary of the grid.
# Return the number of land cells in grid for which we cannot walk off the boundary
#  of the grid in any number of moves.
# --------------------------
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] is either 0 or 1.
from collections import deque

from random import randint

from pyperclip import copy


def num_enclaves(grid: list[list[int]]) -> int:
    # working_sol (20.63%, 89.78%) -> (155ms, 19.89mb)  time: O(m * n) | space: O(m * n)

    def bfs(row: int, col: int, matrix: list[list[int]]) -> int:
        cur_row: int
        cur_col: int
        enclaves: int = 1
        board_hit: bool = False
        # -1 == visited.
        # [(row, col)]
        que: deque[tuple[int, int]] = deque([(row, col)])
        # [top, right, bot, left] <- (dy, dx)
        directions: list[tuple[int, int]] = [
            (-1, 0), (0, 1), (1, 0), (0, -1)
        ]
        while que:
            cur_row, cur_col = que.popleft()
            for dy, dx in directions:
                next_row, next_col = cur_row + dy, cur_col + dx
                if (not (0 <= next_row < len(matrix))
                    or not (0 <= next_col < len(matrix[0]))):
                    board_hit = True
                    matrix[cur_row][cur_col] = -2
                    enclaves = 0
                    continue
                if -2 == matrix[next_row][next_col]:
                    board_hit = True
                    matrix[cur_row][cur_col] = -2
                    enclaves = 0
                elif 1 == matrix[next_row][next_col]:
                    if board_hit:
                        matrix[next_row][next_col] = -2
                        enclaves = 0
                    else:
                        matrix[next_row][next_col] = -1
                        enclaves += 1
                    que.append((next_row, next_col))
        
        return enclaves

    out: int = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if 1 == grid[row][col]:
                grid[row][col] = -1
                out += bfs(row, col, grid)

    return out


# Time complexity: O(m * n) <- m - length of the input matrix `grid`,
#                              n - height of the input matrix `grid`.
# Always traversing the whole input matrix `grid`, once => O(m * n).
# --------------------------
# Auxiliary space: O(m * n)
# In the worst case all cells are `1`.
# `que` <- allocates space for each cell of the the input matrix `grid` => O(m * n).


test: list[list[int]] = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
test_out: int = 3
assert test_out == num_enclaves(test)

test = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
test_out = 0
assert test_out == num_enclaves(test)

test = [[randint(0, 1) for _ in range(500)] for _ in range(500)]
copy(test) # type: ignore
