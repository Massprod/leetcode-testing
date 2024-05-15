# You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:
#  - A cell containing a thief if grid[r][c] = 1
#  - An empty cell if grid[r][c] = 0
# You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid,
#  including cells containing thieves.
# The safeness factor of a path on the grid is defined as the minimum manhattan distance
#  from any cell in the path to any thief in the grid.
# Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).
# An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c)
#  and (r - 1, c) if it exists.
# The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|,
#  where |val| denotes the absolute value of val.
# -------------------------------
# 1 <= grid.length == n <= 400
# grid[i].length == n
# grid[i][j] is either 0 or 1.
# There is at least one thief in the grid.
import heapq
from random import randint
from collections import deque


def maximum_safeness_factor(grid: list[list[int]]) -> int:
    # working_sol (75.34%, 29.68%) -> (3252ms, 52.9mb)  time: O(m * n * log(m * n)) | space: O(m * n)
    cur_min_distance: int
    cell_row: int
    cell_col: int
    new_row: int
    new_col: int
    cur_safe_distance: int
    # W.e the path, we choose minManh will be a 0 === 0 safest.
    if grid[0][0] or grid[len(grid) - 1][len(grid[0]) - 1]:
        return 0
    que: deque[tuple[int, int]] = deque([])
    visited: set[tuple[int, int]] = set()
    # ! 1 <= grid.length == n <= 400 ! <- max dist ~~ 399 + 399 = 798
    min_manh_distances: list[list[int]] = [[1500 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    # Mark every Thief we have in a `grid`.
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if 1 == grid[row][col]:
                que.append((row, col))
                min_manh_distances[row][col] = 0
                visited.add((row, col))
    # [top, right, bot, left]
    options: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    # BFS - to get all minimum distances from all the Thieves to every empty cell in a `grid`.
    while que:
        cell_row, cell_col = que.popleft()
        for step_row, step_col in options:
            new_row = cell_row + step_row
            new_col = cell_col + step_col
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and (new_row, new_col) not in visited:
                # We're always stepping by 1 cell, which is equal to a change of Manhattan distance for an +1.
                cur_min_distance = min_manh_distances[new_row][new_col]
                min_manh_distances[new_row][new_col] = min(
                    cur_min_distance,  # current minManhattan distance from this cell, to any Thief
                    min_manh_distances[cell_row][cell_col] + 1  # distance from some thief we're traveling with BFS
                )
                que.append((new_row, new_col))
                visited.add((new_row, new_col))
    visited.clear()
    # Using Dijkstra's to get the safest path.
    # [(max ManhDistance of the path, row, col)]
    # Using maxHeap, because we need a maximum safeness from all the paths.
    # ! Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1). !
    heap: list[tuple[int, int, int]] = []
    heapq.heappush(heap, (min_manh_distances[0][0] * -1, 0, 0))
    visited.add((0, 0))
    end_row: int = len(grid) - 1
    end_col: int = len(grid[0]) - 1
    while heap:
        cur_safe_distance, cell_row, cell_col = heapq.heappop(heap)
        if cell_row == end_row and cell_col == end_col:
            return cur_safe_distance * -1
        for step_row, step_col in options:
            new_row = cell_row + step_row
            new_col = cell_col + step_col
            if (0 <= new_row < len(grid)
                    and 0 <= new_col < len(grid[0])
                    and (new_row, new_col) not in visited
                    and min_manh_distances[new_row][new_col]):
                # But in the meantime, we need a MINIMUM distance of the path.
                # ! The safeness factor of a path on the grid is defined
                #    as the minimum manhattan distance from any cell in the path to any thief in the grid. !
                new_safe_distance: int = min(cur_safe_distance * -1, min_manh_distances[new_row][new_col])
                heapq.heappush(heap, (new_safe_distance * -1, new_row, new_col))
                visited.add((new_row, new_col))
    return 0


# Time complexity: O(m * n * log(m * n)) <- m - number of rows in input `grid`, n - number of columns in input `grid`.
# First, we're traversing the whole input `grid` to get all positions of the thieves, but before it, we're recreating
#  the `grid` with placeholder values, but its creation depends on input, so => O(2 * m * n).
# Second, we're using BFS from every Thief position we found, to get distance from these Thieves to the empty cells
#  which is another => O(m * n).
# Finally, we're using BFS_Dijkstra to get the safest path.
# Dijkstra always uses every cell only once, but for every cell we're pushing and popping values.
# `heappush()` and `heappop()` is log(k) <- k - elements in a heap.
# O(m * n * log(m * n)) - in the worst case like [[0, 1], [0, 0]] we will have (m * n) - 1 elements in a heap.
# -------------------------------
# Auxiliary space: O(m * n)
# First, BFS.
# `que` can allocate space for every cell of the `grid`, `visited` will always hold all the cells of the `grid`
#  and we're always creating a copy of the `grid` in means of sizing `min_manh_distances` => O(3 * m * n).
# Second, BFS_Dijkstra.
# `heap` will allocate space for every cell of the `grid` and also `visited` can store all of them again => O(2 * m *n).


test: list[list[int]] = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
test_out: int = 0
assert test_out == maximum_safeness_factor(test)

test = [[0, 0, 1], [0, 0, 0], [0, 0, 0]]
test_out = 2
assert test_out == maximum_safeness_factor(test)

test = [[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]
test_out = 2
assert test_out == maximum_safeness_factor(test)

test = [[randint(0, 1) for _ in range(400)] for _ in range(400)]
print(test)
