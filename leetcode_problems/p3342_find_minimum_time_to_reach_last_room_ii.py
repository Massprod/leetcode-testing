# There is a dungeon with n x m rooms arranged as a grid.
# You are given a 2D array moveTime of size n x m, where moveTime[i][j]
#  represents the minimum time in seconds when you can start moving to that room.
# You start from the room (0, 0) at time t = 0 and can move to an adjacent room.
# Moving between adjacent rooms takes exactly one second.
# Return the minimum time to reach the room (n - 1, m - 1).
# Two rooms are adjacent if they share a common wall,
#  either horizontally or vertically.
# ----------------------------
# 2 <= n == moveTime.length <= 50
# 2 <= m == moveTime[i].length <= 50
# 0 <= moveTime[i][j] <= 10 ** 9
import heapq


def min_time_to_reach(moveTime: list[list[int]]) -> int:
    # working_sol (98.28%, 99.14%) -> (298ms, 72.18mb)  time: O(n * m * log(n * m)) | space: O(n * m)
    # Standard Dijkstra.
    time: int
    alter: int
    row: int
    column: int
    # [(time, alter, row, column)] <- alter 0 == 1s, 1 == 2s
    # We use 0, 1 for alter. Because it will give us smallest cost option to move.
    que: list[tuple[int, int, int, int]] = [(0, 0, 0, 0)]
    heapq.heapify(que)
    target: tuple[int, int] = (len(moveTime) - 1, len(moveTime[0]) - 1)
    # [(dy, dx)] ->  (top, right, bot, left)
    options: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while que:
        time, alter, row, column = heapq.heappop(que)
        for dy, dx in options:
            new_row: int = row + dy
            new_column: int = column + dx
            if (not 0 <= new_row < len(moveTime)
                    or not 0 <= new_column < len(moveTime[0])):
                continue
            time_gate: int = moveTime[new_row][new_column]
            if -1 == time_gate:
                continue
            alter_shift: int = 2 if alter % 2 else 1
            new_time: int = max(time, time_gate) + alter_shift
            if target == (new_row, new_column):
                return new_time
            # We're not blocked on altering => save space for visited.
            moveTime[new_row][new_column] = -1
            new_alter: int = 1 if alter == 0 else 0
            heapq.heappush(
                que, (new_time, new_alter, new_row, new_column)
            )

    return -1


# Time complexity: O(n * m * log(n * m)) <- n - length of the input matrix `moveTime`,
#                                           h - height of the input matrix `moveTime`.
# Standard Dijkstra's with checking all of the cells => O(n * m * log(n * m)).
# ----------------------------
# Auxiliary space: O(n * m)
# `que` <- allocates space for each cell of the input matrix `moveTime`.


test: list[list[int]] = [[0, 4], [4, 4]]
test_out: int = 7
assert test_out == min_time_to_reach(test)

test = [[0, 0, 0], [0, 0, 0]]
test_out = 6
assert test_out == min_time_to_reach(test)

test = [[0, 1], [1, 2]]
test_out = 4
assert test_out == min_time_to_reach(test)
