# You are given an n x n integer matrix grid where each value grid[i][j]
#  represents the elevation at that point (i, j).
# It starts raining, and water gradually rises over time.
# At time t, the water level is t, meaning any cell with elevation less
#  than equal to t is submerged or reachable.
# You can swim from a square to another 4-directionally adjacent square
#  if and only if the elevation of both squares individually are at most t.
# You can swim infinite distances in zero time.
# Of course, you must stay within the boundaries of the grid during your swim.
# Return the minimum time until you can reach the bottom right square (n - 1, n - 1)
#  if you start at the top left square (0, 0).
# --- --- --- ---
# n == grid.length
# n == grid[i].length
# 1 <= n <= 50
# 0 <= grid[i][j] < n2
# Each value grid[i][j] is unique.
import heapq


def swim_in_water(grid: list[list[int]]) -> int:
    # working_solution: (99.09%, 96.69%) -> (15ms, 18.04mb)  Time: O(n * m * log n) Space: O(n * m)
    # Dijkstra to get the minimum cost option on every turn?
    # ---
    # We need to visit both of these cells.
    # We start at [0][0] and we can only visit cells with lower cost,
    #  than our currently maximum visited option.
    out: int = max(grid[0][0], grid[-1][-1])
    # [ (cost, row, column) ]
    min_heap: list[tuple[int, int, int]] = [(out, 0, 0)]
    heapq.heapify(min_heap)
    # [ (dy, dx) ] <- top, right, bot, left
    directions: list[tuple[int, int]] = [
        (-1, 0), (0, 1), (1, 0), (0, -1)
    ]
    end_row: int = len(grid) - 1
    end_col: int = len(grid[0]) - 1

    while min_heap:
        cost, row, column = heapq.heappop(min_heap)
        out = max(out, cost)
        if end_row == row  and end_col == column:
            break
        for dy, dx in directions:
            new_row, new_col = row + dy, column + dx
            # Out of bounds.
            if not (
                0 <= new_row <= end_row
                and
                0 <= new_col <= end_col
            ):
                continue
            # Visited.
            if -1 == grid[new_row][new_col]:
                continue
            heapq.heappush(
                min_heap,
                (grid[new_row][new_col], new_row, new_col)
            )
            # Mark cell as visited.
            grid[new_row][new_col] = -1

    return out


# Time complexity: O(n * m * log n ) <- n - length of the input matrix `grid`,
#                                       m - height of the input matrix `grid`.
# In the worst case, we will have all cells of the matrix stored in the `min_heap`.
# And every turn we're going to get/add options in it => O(n * m * log n).
# --- --- --- ---
# Space complexity: O(n * m)
## `min_heap` <- allocates space for each cell of the input matrix `grid`.


test: list[list[int]] = [[0, 2], [1, 3]]
test_out: int = 3
assert test_out == swim_in_water(test)

test = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
test_out = 16
assert test_out == swim_in_water(test)
