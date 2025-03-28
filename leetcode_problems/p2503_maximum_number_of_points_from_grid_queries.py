# You are given an m x n integer matrix grid and an array queries of size k.
# Find an array answer of size k such that for each integer queries[i]
#  you start in the top left cell of the matrix and repeat the following process:
#  - If queries[i] is strictly greater than the value of the current cell
#  that you are in, then you get one point if it is your first time visiting this cell,
#  and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
#  - Otherwise, you do not get any points, and you end this process.
# After the process, answer[i] is the maximum number of points you can get.
# Note that for each query you are allowed to visit the same cell multiple times.
# Return the resulting array answer.
# ------------------------------
# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 1000
# 4 <= m * n <= 10 ** 5
# k == queries.length
# 1 <= k <= 10 ** 4
# 1 <= grid[i][j], queries[i] <= 10 ** 6
import heapq


def max_points(grid: list[list[int]], queries: list[int]) -> list[int]:
    # working_sol (69.93%, 18.30%) -> (571ms, 42.81mb) 
    #                                 time: O(n * log n + (g * k) * log(g * k))
    #                                 space: O(g * k + n)
    out: list[int] = [0 for _ in queries]
    # [ top, right, bot, left ] (dy, dx)
    options: list[tuple[int, int]] = [
        (-1, 0), (0, 1), (1, 0), (0, -1)
    ]
    # [ (cell_value, row, col) ]
    min_heap_que: list[tuple[int, int, int]] = [ (grid[0][0], 0, 0) ]
    heapq.heapify(min_heap_que)
    visited: set[tuple[int, int]] = { (0, 0) }
    cur_points: int = 0
    # We want to make it in one go => use lowest first.
    # [ (value, index) sorted in ascending ]
    sorted_queries: list[tuple[int, int]] = sorted([
        (value, index) for index, value in enumerate(queries)
    ], key=lambda x: x[0])
    for value, index in sorted_queries:
        # Standard BFS while:
        #  - there's still cells to traverse
        #  - ! If queries[i] is strictly greater than the value of the current cell !
        while (min_heap_que
                and min_heap_que[0][0] < value):
            cell_value, row, col = heapq.heappop(min_heap_que)
            cur_points += 1
            for dy, dx in options:
                new_row: int = row + dy
                new_col: int = col + dx
                new_coords: tuple[int, int] = (new_row, new_col)
                if (0 <= new_row < len(grid)
                    and 0 <= new_col < len(grid[0])
                    and new_coords not in visited):
                    new_value: int = grid[new_row][new_col]
                    heapq.heappush(min_heap_que, (new_value, new_row, new_col))
                    visited.add(new_coords)
        out[index] = cur_points
    
    return out


# Time complexity: O(n * log n + (g * k) * log(g * k)) <-
#                       n - length of the input array `queries`,
#                       g - length of the input matrix `grid`,
#                       k - height of the input matrix `grid`.
# Sorting all queries => O(n * log n).
# Traversing whole matrix `grid`, once.
# Every cell we visit we push and pop into heap => O(g * k * log(g * k) * 2).
# ------------------------------
# Auxiliary space: O(g * k + n)
# `min_heap_que` <- allocates space for every cell of the `grid` => O(g * k).
# `sorted_queries` <- allocates space for each query of the `queries` => O(n).
# `visited` <- allocates space for each cell we visit => O(g * k).


test: list[list[int]] = [[1, 2, 3], [2, 5, 7], [3, 5, 1]]
test_queries: list[int] = [5, 6, 2]
test_out: list[int] = [5, 8, 1]
assert test_out == max_points(test, test_queries)

test = [[5, 2, 1], [1, 1, 2]]
test_queries = [3]
test_out = [0]
assert test_out == max_points(test, test_queries)
