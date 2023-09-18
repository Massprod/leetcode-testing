# You are given an n x n binary matrix grid where 1 represents land and 0 represents water.
# An island is a 4-directionally connected group of 1's not connected to any other 1's.
# There are exactly two islands in grid.
# You may change 0's to 1's to connect the two islands to form one island.
# Return the smallest number of 0's you must flip to connect the two islands.
# -------------------
# n == grid.length == grid[i].length
# 2 <= n <= 100
# grid[i][j] is either 0 or 1.
# There are exactly two islands in grid.
from collections import deque


def shortest_bridge(grid: list[list[int]]) -> int:
    # working_sol (99.11%, 100%) -> (296ms, 16.70mb)  time: O(n * n) | space: O(n * n)
    min_bridge: int = 0
    row_len: int = len(grid[0])
    col_len: int = len(grid)
    # All cells of First island.
    que: deque[tuple[int, int] | None] = deque()
    # Only cells with water around, skipping inland.
    bridge_que: deque[tuple[int, int] | None] = deque()
    # W.e sign to mark != 0.
    mark: int = 3
    # Find every cell of the First island.
    for y_ in range(col_len):
        if bridge_que:
            break
        for x_ in range(row_len):
            if grid[y_][x_]:
                grid[y_][x_] = mark
                que.append((y_, x_))
                while que:
                    cell: tuple[int, int] = que.popleft()
                    row: int = cell[0]
                    col: int = cell[1]
                    if 0 <= row - 1 < row_len:
                        if not grid[row - 1][col]:
                            bridge_que.append((row, col))
                        if grid[row - 1][col] == 1:
                            que.append((row - 1, col))
                            grid[row - 1][col] = mark
                    if 0 <= row + 1 < row_len:
                        if not grid[row + 1][col]:
                            bridge_que.append((row, col))
                        if grid[row + 1][col] == 1:
                            que.append((row + 1, col))
                            grid[row + 1][col] = mark
                    if 0 <= col - 1 < col_len:
                        if not grid[row][col - 1]:
                            bridge_que.append((row, col))
                        if grid[row][col - 1] == 1:
                            que.append((row, col - 1))
                            grid[row][col - 1] = mark
                    if 0 <= col + 1 < col_len:
                        if not grid[row][col + 1]:
                            bridge_que.append((row, col))
                        if grid[row][col + 1] == 1:
                            que.append((row, col + 1))
                            grid[row][col + 1] = mark
                break

    bridge_que.append(None)
    # BFS with delimiter to find the shortest path,
    #  from First -> Second island. (check -> not named)
    while bridge_que:
        cell = bridge_que.popleft()
        if cell is None:
            if bridge_que:
                bridge_que.append(None)
            min_bridge += 1
            continue
        row = cell[0]
        col = cell[1]
        if 0 <= row - 1 < row_len:
            if grid[row - 1][col] == 1:
                break
            if not grid[row - 1][col]:
                bridge_que.append((row - 1, col))
                grid[row - 1][col] = mark
        if 0 <= row + 1 < row_len:
            if grid[row + 1][col] == 1:
                break
            if not grid[row + 1][col]:
                bridge_que.append((row + 1, col))
                grid[row + 1][col] = mark
        if 0 <= col - 1 < col_len:
            if grid[row][col - 1] == 1:
                break
            if not grid[row][col - 1]:
                bridge_que.append((row, col - 1))
                grid[row][col - 1] = mark
        if 0 <= col + 1 < col_len:
            if grid[row][col + 1] == 1:
                break
            if not grid[row][col + 1]:
                bridge_que.append((row, col + 1))
                grid[row][col + 1] = mark
    return min_bridge


# Time complexity: O(n * n) -> in the worst case we will use every index of the matrix once => O(n * n).
# n - len of input square matrix^^|
# Auxiliary space: O(n * n) -> sticking to complexity as before O(n * n), every cell in a  que.
# -------------------
# Ok. Idea was correct, failed in 2 things:
#  - Didn't use visited set for the first island correctly,
#    built it fast and didn't even bother to return and see it again.
#    Too much focus on second one, while first was unfinished.
#  - Failed to see that we don't need to use every possible point to build a bridge.
#    Cuz it can be done with round based BFS like in rotten_tomatoes.
# -------------------
# Used correct BFS idea, but I was trying to build bridge from EVERY cell of the island.
# When I could have used approach with delimiter and just count rounds.
# Otherwise, it's TLE. But correct.


test: list[list[int]] = [[0, 1], [1, 0]]
test_out: int = 1
assert test_out == shortest_bridge(test)

test = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
test_out = 2
assert test_out == shortest_bridge(test)

test = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
test_out = 1
assert test_out == shortest_bridge(test)

test = [[0, 1, 0, 0, 0], [0, 1, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
test_out = 1
assert test_out == shortest_bridge(test)
