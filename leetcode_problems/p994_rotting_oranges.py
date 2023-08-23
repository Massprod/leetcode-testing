# You are given an m x n grid where each cell can have one of three values:
#   0 representing an empty cell,
#   1 representing a fresh orange, or
#   2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.
# If this is impossible, return -1.
# ---------------
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.
from collections import deque


def rotting_oranges(grid: list[list[int]]) -> int:
    # working_sol (88.61%, 87.05%) -> (53ms, 16.2mb)  time: O(m * n) | space: O(m * n)
    # Standard BFS with delimiter for correct minutes count.
    rot_que: deque[tuple[int, int] | None] = deque()
    row: int = len(grid[0])
    column: int = len(grid)
    # Count every rotten orange for the First round|minute.
    for y_ in range(column):
        for x_ in range(row):
            if grid[y_][x_] == 2:
                rot_que.append((y_, x_))
    # Add delimiter to count as round|minute passed.
    rot_que.appendleft(None)
    minutes: int = 0
    # Take cells from right -> left.
    # When delimiter hit, count a passed minute.
    while any(rot_que):
        cur_cell: tuple[int, int] = rot_que.pop()
        if cur_cell is None:
            minutes += 1
            rot_que.appendleft(None)
            continue
        y: int = cur_cell[0]
        x: int = cur_cell[1]
        # ! any fresh orange that is 4-directionally adjacent
        #   to a rotten orange becomes rotten !
        # Check cells, if neighbour is fresh -> mark as rotten
        #  and add into a que to process later.
        if 0 <= y - 1:
            if grid[y - 1][x] == 1:
                grid[y - 1][x] = 2
                rot_que.appendleft((y - 1, x))
        if column > y + 1:
            if grid[y + 1][x] == 1:
                grid[y + 1][x] = 2
                rot_que.appendleft((y + 1, x))
        if 0 <= x - 1:
            if grid[y][x - 1] == 1:
                grid[y][x - 1] = 2
                rot_que.appendleft((y, x - 1))
        if row > x + 1:
            if grid[y][x + 1] == 1:
                grid[y][x + 1] = 2
                rot_que.appendleft((y, x + 1))
    # Extra check if there's some Fresh oranges left.
    for y_ in range(column):
        for x_ in range(row):
            if grid[y_][x_] == 1:
                # ! If this is impossible, return -1. !
                return -1
    # Otherwise, all rotten.
    return minutes


# Time complexity: O(m * n) -> traversing whole input_matrix once to get all rottens for the First minute => O(m * n)->
# m - input_matrix row length^^| -> worst case, everything is already rotten, so we will x4 check for every index =>
# n - input_matrix col length^^| => O(4 * (m * n)) -> extra traverse of input_matrix to check fresh ones => O(m * n).
# Auxiliary space: O(m * n) -> same worst case, everything is rotten so rot_que is equal to input_matrix size.
# ---------------
# Standard BFS with delimiter to count minutes.


test: list[list[int]] = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
test_out: int = 4
assert test_out == rotting_oranges(test)

test = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
test_out = -1
assert test_out == rotting_oranges(test)

test = [[0, 2]]
test_out = 0
assert test_out == rotting_oranges(test)

# test -> Failed -> Didn't notice that I was checking x > 0 when it's obviously x and y >= 0.
test = [[1, 2]]
test_out = 1
assert test_out == rotting_oranges(test)
