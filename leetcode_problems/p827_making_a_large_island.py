# You are given an n x n binary matrix grid.
# You are allowed to change at most one 0 to be 1.
# Return the size of the largest island in grid after applying this operation.
# An island is a 4-directionally connected group of 1s.
# --------------------
# n == grid.length
# n == grid[i].length
# 1 <= n <= 500
# grid[i][j] is either 0 or 1.
from collections import deque


def largest_island(grid: list[list[int]]) -> int:
    # working_sol (62.54%, 90.95%) -> (947ms, 27.26mb)  time: O(m * n) | space: O(m * n)

    # [ top, right, bot, left ]
    directions: list[tuple[int, int]] = [
        (1, 0), (0, 1), (-1, 0), (0, -1)
    ]

    def bfs_count(
        start: tuple[int, int],
        grid: list[list[int]],
        island_id: int,
    ) -> int:
        """
        start[0] == row
        start[1] == column
        """
        nonlocal directions
        row: int
        column: int

        # Standard BFS with marked visited cells with id's of the islands.
        bfs_out: int = 1
        que: deque[tuple[int, int]] = deque([start])
        while que:
            row, column = que.popleft()
            for dy, dx in directions:
                new_row: int = row + dy
                new_column: int = column + dx
                if (0 <= new_row < len(grid) and 0 <= new_column < len(grid[0])
                    and 1 == grid[new_row][new_column]):
                    que.append(
                        (new_row, new_column)
                    )
                    grid[new_row][new_column] = island_id
                    bfs_out += 1
    
        return bfs_out
    
    out: int = 0
    # { island_id: island_size }
    islands: dict[int, int] = {}
    id: int = -1
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if 1 != grid[row][column]:
                continue
            # Mark initial cell.
            grid[row][column] = id
            island_size: int = bfs_count(
                (row, column), grid, id
            )
            islands[id] = island_size
            id -= 1
            # We can have no `0` cells in `grid`.
            # So, we need to check islands by themselves.
            out = max(out, island_size)

    # Every island is marked with `island_id` == just check them.
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if 0 != grid[row][column]:
                continue
            # 0 -> 1 => size of size 1.
            island_size: int = 1
            # We can have `0` cell surrounded by 1 island in 4 directions.
            # We should count this only once.
            checked_islands: set[int] = set()
            for dy, dx in directions:
                new_row: int = row + dy
                new_column: int = column + dx
                if not (0 <= new_row < len(grid)
                    and 0 <= new_column < len(grid[0])):
                    continue
                id = grid[new_row][new_column]
                if 0 == id or id in checked_islands:
                    continue
                island_size += islands[id]
                checked_islands.add(id)
            out = max(out, island_size)
    
    return out


# Time complexity: O(m * n) <- m - length of the input matrix `grid`,
#                              n - height of the input matrix `grid`.
# Always traversing whole input matrix `grid` once with BFS to count all the island
#  sizes => O(m * n).
# Extra traversing `grid` again to find the biggest island we can build => O(2 * m * n).
# --------------------
# Auxiliary space: O(m * n)
# In the worst case `grid` will have all cells as `1`.
# `que` <- in BFS will allocate space for each cell => O(m * n).


test: list[list[int]] = [[1, 0], [0, 1]]
test_out: int = 3
assert test_out == largest_island(test)

test = [[1, 1], [1, 0]]
test_out = 4
assert test_out == largest_island(test)

test = [[1, 1], [1, 1]]
test_out = 4
assert test_out == largest_island(test)
