# You are given two integers n and m representing the number
#  of rows and columns of a grid, respectively.
# You are also given a 2D integer array sources, where sources[i] = [ri, ci, color​​​​​​​i]
#  indicates that the cell (ri, ci) is initially colored with colori.
# All other cells are initially uncolored and represented as 0.
# At each time step, every currently colored cell spreads its color
#  to all adjacent uncolored cells in the four directions: up, down, left, and right.
# All spreads happen simultaneously.
# If multiple colors reach the same uncolored cell at the same time step,
#  the cell takes the color with the maximum value.
# The process continues until no more cells can be colored.
# Return a 2D integer array representing the final state of the grid,
#  where each cell contains its final color.
# --- --- --- ---
# 1 <= n, m <= 10 ** 5
# 1 <= n * m <= 10 ** 5
# 1 <= sources.length <= n * m
# sources[i] = [ri, ci, colori]
# 0 <= ri <= n - 1
# 0 <= ci <= m - 1
# 1 <= colori <= 10 ** 6​​​​​​​
# All (ri, ci​​​​​​​) in sources are distinct.
from collections import deque


def color_grid(n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
    # working_solution: (14.94%, 5.64%) -> (1404ms, 53.92mb)  Time: O(m * n) Space: O(m * n)
    # [up, right, bot, left] - (row, column)
    directions: list[tuple[int, int]] = [
        (-1, 0), (0, 1), (1, 0), (0, -1)
    ]
    grid: list[list[int]] = [
        [0 for _ in range(m)] for _ in range(n)
    ]
    que: deque = deque([])
    # We only care about conflict when colours meet at the same round.
    round: int = 0
    # (row, column, round)
    visited: dict[tuple[int, int], int] = {}
    for row, column, colour in sources:
        grid[row][column] = colour
        que.append((row, column, colour))
        # We shouldn't touch initial cells.
        visited[(row, column)] = -1
    # Round break.
    round_breaker = None
    que.append(round_breaker)
    while que:
        if que[0] is round_breaker:
            que.popleft()
            if que:
                que.append(round_breaker)
                round += 1
            continue
        row, column, colour = que.popleft()
        for drow, dcol in directions:
            new_row: int = row + drow
            new_col: int = column + dcol
            if not (0 <= new_row < n) or not (0 <= new_col < m):
                continue
            # Same time => check colour weight.
            if (
                (new_row, new_col) in visited
                and
                visited[(new_row, new_col)] == round
                and
                grid[new_row][new_col] < colour
            ):
                grid[new_row][new_col] = colour
                que.append((new_row, new_col, colour))
                continue
            # Time is different and cell is already coloured.
            if 0 != grid[new_row][new_col]:
                continue
            grid[new_row][new_col] = colour
            visited[(new_row, new_col)] =  round
            que.append((new_row, new_col, colour))
    
    return grid


# Time complexity: O(m * n)
# --- --- --- ---
# Space complexity: O(m * n)


test_n: int = 3
test_m: int = 3
test_sources: list[list[int]] = [
    [0, 0, 1], [2, 2, 2]
]
test_out: list[list[int]] = [
    [1, 1, 2], [1, 2, 2], [2, 2, 2]
]
assert test_out == color_grid(test_n, test_m, test_sources)

test_n = 3
test_m = 3
test_sources = [
    [0, 1, 3], [1, 1, 5]
]
test_out = [
    [3, 3, 3], [5, 5, 5], [5, 5, 5]
]
assert test_out == color_grid(test_n, test_m, test_sources)

test_n = 2
test_m = 2
test_sources = [
    [1, 1, 5]
]
test_out = [
    [5, 5], [5, 5]
]
assert test_out == color_grid(test_n, test_m, test_sources)
