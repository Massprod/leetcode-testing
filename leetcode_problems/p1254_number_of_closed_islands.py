# Given a 2D grid consists of 0s (land) and 1s (water).
# An island is a maximal 4-directionally connected group of 0s
#  and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.
# Return the number of closed islands.
# --- --- --- ---
# 1 <= grid.length, grid[0].length <= 100
# 0 <= grid[i][j] <=1
from collections import deque


def closed_island(grid: list[list[int]]) -> int:
    # working_solution: (93.92%, 94.91%) -> (11ms, 18.17mb)  Time: O(m * n) Space: O(1)
    # Any island will be correct, except the border ones.
    # Start BFS from any `0` except the border ones, and if they lead to 
    #  the boarder cell with `0` => incorrect.
    
    # [(dy, dx)] -> top, right, down, left
    directions: list[tuple[int, int]] = [
        (-1, 0), (0, 1), (1, 0), (0, -1)
    ]

    def bfs(cell: tuple[int, int], matrix: list[list[int]]) -> bool:
        nonlocal directions

        close_tag: bool = True
        que: deque[tuple[int, int]] = deque([cell])
        while que:
            cur_row, cur_col = que.popleft()
            for dy, dx in directions:
                new_row, new_col = cur_row + dy, cur_col + dx
                # Out ouf bounds => can't be surrounded by `1`s.
                if not (
                    0 <= new_row < len(matrix)
                    and
                    0 <= new_col < len(matrix[0])
                ):
                    close_tag = False
                    continue
                # Visited or water cell => both ignored.
                if -1 == matrix[new_row][new_col] or 1 == matrix[new_row][new_col]:
                    continue
                # Mark as visited.
                matrix[new_row][new_col] = -1
                que.append((new_row, new_col))
        
        return close_tag
    
    out: int = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if 0 != grid[row][col]:
                continue
            grid[row][col] = -1
            out += 1 if bfs((row, col), grid) else 0

    return out


# Time complexity: O(m * n) <- m - length of the input matrix `grid`,
#                              n - height of the input matrix `grid`.
# In the worst case, we're going to have `grid` with all `0` cells.
# Standard BFS traverse of every cell in the matrix `grid`, once => O(n * m).
# --- --- --- ---
# Space complexity: O(1)
# `directions` <- constant sized array => O(1).
# We reusing `grid` to mark visited => O(1).


test: list[list[int]] = [
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0]
]
test_out: int = 2
assert test_out == closed_island(test)

test = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0]
]
test_out = 1
assert test_out == closed_island(test)

test = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
]
test_out = 2
assert test_out == closed_island(test)
