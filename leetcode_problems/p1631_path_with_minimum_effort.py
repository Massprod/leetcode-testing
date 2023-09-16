# You are a hiker preparing for an upcoming hike.
# You are given heights, a 2D array of size rows x columns, where heights[row][col]
#  represents the height of cell (row, col). You are situated in the top-left cell, (0, 0),
#  and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed).
# You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
# -----------------------
# rows == heights.length
# columns == heights[i].length
# 1 <= rows, columns <= 100
# 1 <= heights[i][j] <= 10 ** 6
import heapq
from random import randint


def minimum_effort_path(heights: list[list[int]]) -> int:
    # working_sol (99.74%, 95.34%) -> (471ms, 17.57mb)  time: O(m * n * log(m * n)) | space: O(m * n)
    row_len: int = len(heights[0])
    col_len: int = len(heights)
    if row_len == 1 and col_len == 1:
        return 0
    que: list[tuple[int, int, int]] = []
    heapq.heapify(que)
    # (effort, row_number, col_number)
    heapq.heappush(que, (0, 0, 0))
    max_effort: int = 0
    # ! 1 <= heights[i][j] <= 10 ** 6 !
    # Use anything as a mark, but if it's INT stay out of constraint range.
    mark: int = 0
    while que:
        # Cell with minimum step effort.
        cur_cell: tuple[int, int, int] = heapq.heappop(que)
        cur_dist: int = cur_cell[0]
        y: int = cur_cell[1]  # row
        x: int = cur_cell[2]  # col
        # Because we're using same input_list to save space,
        #  we can add same cells into a que twice.
        # And it will be marked only after processing this cell ->
        # -> in case if distance to it will be a minimum at some time.
        if not heights[y][x]:
            continue
        max_effort = max(max_effort, cur_dist)
        if (y, x) == (col_len - 1, row_len - 1):
            break
        if 0 <= y - 1 < col_len and heights[y - 1][x] != mark:
            effort: int = abs(heights[y - 1][x] - heights[y][x])
            heapq.heappush(que, (effort, y - 1, x))
        if 0 <= y + 1 < col_len and heights[y + 1][x] != mark:
            effort = abs(heights[y + 1][x] - heights[y][x])
            heapq.heappush(que, (effort, y + 1, x))
        if 0 <= x - 1 < row_len and heights[y][x - 1] != mark:
            effort = abs(heights[y][x - 1] - heights[y][x])
            heapq.heappush(que, (effort, y, x - 1))
        if 0 <= x + 1 < row_len and heights[y][x + 1] != mark:
            effort = abs(heights[y][x + 1] - heights[y][x])
            heapq.heappush(que, (effort, y, x + 1))
        # Mark as visited.
        heights[y][x] = mark
    return max_effort


# Time complexity: O(m * n * log(m * n)) -> for each cell we traverse all it's adjacent neighbours => O(m * n)
# n - row length of input_matrix^^| and insert them into a heapq => O(log(m * n)) => O(m * n * log (m * n)).
# m - col length of input_matrix^^| In the worst case there's every cell in a heap.
# Auxiliary space: O(m * n) -> worst case == one cell -> one heap entry per cell => O(m * n).
# -----------------------
# Can we ignore BinarySearch?
# Like first idea was just use BFS to choose minimum resistance path and walk it, with remembering of maximum
#  effort we used. But we can't do this with just 4 neighbours, cuz then we need to traverse ALL paths possible.
# And my solution from Hints is very slow and Higher once's actually just using same ides with only BFS.
# But with choosing Minimum option not just from 4 neighbours but ALL the cells we added into a que so far.
# Which can be done with heapq(). Rebuild time.
# -----------------------
# First idea is use BFS, but we need only one size of step. And how we can find this step?
# Hint:
# !
# If you are given threshold k, check if it is possible
#  to go from (0, 0) to (n-1, m-1) using only edges of ≤ k cost.
# !
# Ok. Binary search for this K and BFS with this value, or DFS, but we still need to check all paths.
# Min_value == 0, Max_value == (max_in_matrix - min_in_matrix) <- BS limits.
# Well BFS can be done with just a matrix, but we need to find Max_value or use Max_constraint which is extra checks.
# Guess it's better to create Graph with all cells and their edges, like:
# {cell: {cell: edge_weight}}
# BFS on (0, 0) to check all paths to expand wih standard maintain of visited, and only add node if
# edge connecting it (edge <= K). If at any time we added last cell we need (n - 1, m - 1) we can return True.
# And try to make BS_check value Lower, if we can't get to this than we need Higher K.
# Should be correct. Working with random max_constraints, let's test.


test: list[list[int]] = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
test_out: int = 2
assert test_out == minimum_effort_path(test)

test = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
test_out = 1
assert test_out == minimum_effort_path(test)

test = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
test_out = 0
assert test_out == minimum_effort_path(test)

test = [[1]]
test_out = 0
assert test_out == minimum_effort_path(test)

test = [[1, 2]]
test_out = 1
assert test_out == minimum_effort_path(test)

test = [
    [4, 3, 4, 10, 5, 5, 9, 2], [10, 8, 2, 10, 9, 7, 5, 6], [5, 8, 10, 10, 10, 7, 4, 2],
    [5, 1, 3, 1, 1, 3, 1, 9], [6, 4, 10, 6, 10, 9, 4, 6]
]
test_out = 5
assert test_out == minimum_effort_path(test)

test = [[1, 2, 7], [3, 1, 7]]
test_out = 5
assert test_out == minimum_effort_path(test)

test = [[7, 9], [3, 6], [6, 9], [3, 6]]
test_out = 3
assert test_out == minimum_effort_path(test)

test = [[randint(1, 10 ** 6) for _ in range(100)] for _ in range(100)]
print(test)
