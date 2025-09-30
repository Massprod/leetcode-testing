# There is an m x n rectangular island that borders both the Pacific Ocea
#  and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges,
#  and the Atlantic Ocean touches the island's right and bottom edges.
# The island is partitioned into a grid of square cells.
# You are given an m x n integer matrix heights where heights[r][c] represents
#  the height above sea level of the cell at coordinate (r, c).
# The island receives a lot of rain, and the rain water can flow
#  to neighboring cells directly north, south, east, and west if the neighboring cell's
#  height is less than or equal to the current cell's height.
# Water can flow from any cell adjacent to an ocean into the ocean.
# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes
#  that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
# --- --- --- ---
# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 10 ** 5


def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    # working_solution: (42.82%, 80.07%) -> (37ms, 19.26mb)  Time: O(m * n) Space: O(m * n)
    # (dy, dx) <- top, right, bot, left
    directions: list[tuple[int, int]] = [
        (-1, 0), (0, 1), (1, 0), (0, -1)
    ]
    # (pacific, atlantic) <- indicator of the ocean reaching this cell
    cells_map: list[list[tuple[bool, bool]]] = [[
        (False, False) for _ in range(len(heights[0]))
    ] for _ in range(len(heights))]


    def dfs(
        cell: tuple[int, int],
        original_cells: list[list[int]],
        map: list[list[tuple[bool, bool]]],
        ocean_side: bool,
    ) -> None:
        """
        cell <- (row, column)
        ocean_side <- True - pacific, False - atlantic
        """
        nonlocal directions
        
        row, column = cell
        cur_cell: tuple[bool, bool] = map[row][column]
        # Pacific and Pacific already was at this cell
        if ocean_side and cur_cell[0] is True:
            return
        # Atlantic and Atlantic already was at this cell
        if not ocean_side and cur_cell[1] is True:
            return
        # Both was there.
        if all(map[row][column]):
            return
        cur_value: int = original_cells[row][column]
        # Pacific
        if ocean_side:
            map[row][column] = (
                True, map[row][column][1]
            )
        # Atlantic
        if not ocean_side:
            map[row][column] = (
                map[row][column][0], True
            )
        for dy, dx in directions:
            new_row, new_column = row + dy, column + dx
            if (
                not (0 <= new_row < len(original_cells))
                or
                not (0 <= new_column < len(original_cells[0]))
            ):
                continue
            new_value: int = original_cells[new_row][new_column]
            # We go backwars, so we can't go on the lower heights.
            # We only care about elevating.
            if new_value < cur_value:
                continue
            dfs(
                (new_row, new_column),
                original_cells,
                map,
                ocean_side,
            )

    #region StartPoints
    # (row, column) == (y, x)
    pacific_start_points: set[tuple[int, int]] = {
        (0, column) for column in range(len(heights[0]))

    }
    pacific_start_points.update({
        (row, 0) for row in range(len(heights))
    })
    atlantic_start_points: set[tuple[int, int]] = {
        (len(heights) - 1, column) for column in range(len(heights[0]))
    }
    atlantic_start_points.update({
        (row, len(heights[0]) - 1) for row in range(len(heights))
    })
    #endregion
    for start_cell in pacific_start_points:
        dfs(start_cell, heights, cells_map, True)
    for start_cell in atlantic_start_points:
        dfs(start_cell, heights, cells_map, False)
    
    out: list[list[int]] = []
    for row in range(len(heights)):
        for column in range(len(heights[0])):
            if not all(cells_map[row][column]):
                continue
            out.append([row, column])
    
    return out


# Time complexity: O(m * n) <- m - length of the input matrix `heights`,
#                              n - height of the input matrix `heights`.
# Always visit every all of the input matrix cells, twice => O(2 * m * n).
# --- --- --- ---
# Space complexity: O(m * n)
# `cells_map` <- allocates space for each cell of the input matrix `heights` => O(m * n).
# `pacific_start_points` <- top_left borders == (m + n) - 1.
# `atlantic_start_points` <- bot_right borders == (m + n) - 1.


test: list[list[int]] = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
test_out: list[list[int]] = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
assert test_out == pacific_atlantic(test)

test = [[1]]
test_out = [[0, 0]]
assert test_out == pacific_atlantic(test)
