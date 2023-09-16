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
from collections import deque
from random import randint


def minimum_effort_path(heights: list[list[int]]) -> int:
    # working_sol (26.48%, 6.80%) -> (1624ms, 24.2mb)  time: O(log k * (m * n)) | space: O(m * n)
    # {vertex: {vertex: edge_weight}}
    row: int = len(heights[0])
    col: int = len(heights)
    if row == 1 and col == 1:
        return 0
    graph: dict[tuple[int, int], dict[tuple[int, int], int]] = {}
    # min, max efforts we can meet between ALL the cells.
    min_effort: int = 10 ** 6
    max_effort: int = 0
    for y in range(col):
        for x in range(row):
            # {vertex: edge_weight}
            neighbours: dict[tuple[int, int], int] = {}
            if 0 <= y - 1 < col:  # Same style for easier read, we actually only need (<= 0)
                effort: int = abs(heights[y][x] - heights[y - 1][x])
                min_effort = min(min_effort, effort)
                max_effort = max(max_effort, effort)
                neighbours[(y - 1, x)] = effort
            if 0 <= y + 1 < col:
                effort = abs(heights[y][x] - heights[y + 1][x])
                min_effort = min(min_effort, effort)
                max_effort = max(max_effort, effort)
                neighbours[(y + 1, x)] = effort
            if 0 <= x - 1 < row:
                effort = abs(heights[y][x] - heights[y][x - 1])
                min_effort = min(min_effort, effort)
                max_effort = max(max_effort, effort)
                neighbours[(y, x - 1)] = effort
            if 0 <= x + 1 < row:
                effort = abs(heights[y][x] - heights[y][x + 1])
                min_effort = min(min_effort, effort)
                max_effort = max(max_effort, effort)
                neighbours[(y, x + 1)] = effort
            graph[(y, x)] = neighbours

    def bfs(check_effort: int, node: tuple[int, int] = (0, 0)) -> bool:
        # Standard BFS.
        if node == (col - 1, row - 1):
            return True
        que: deque[tuple[int, int]] = deque([node])
        visited: set[tuple[int, int]] = {node}
        while que:
            cur_vert: tuple[int, int] = que.popleft()
            for edge in graph[cur_vert]:
                if edge not in visited and graph[cur_vert][edge] <= check_effort:
                    # All we need is to reach last cell, we can return whenever it happens.
                    if edge == (col - 1, row - 1):
                        return True
                    que.append(edge)
                    visited.add(edge)
        # Didn't reach last cell.
        return False
    # Standard BS.
    while min_effort <= max_effort:
        middle: int = (min_effort + max_effort) // 2
        # Correct path, we can try lower value.
        if bfs(middle):
            max_effort = middle - 1
            continue
        # Incorrect, we need higher limit.
        min_effort = middle + 1
    return min_effort


# Time complexity: O(log k * (m * n)) -> creating graph by traversing whole input_matrix => O(m * n) ->
# k - max_effort - min_effort, between cells^^| -> binary search with found limits, and BFS for every check =>
# m - len of matrix row^^| => O(log k * (m * n)) <- worst case == BFS will lead to last cell for every check, but
# n - len of matrix col^^| with some path which includes every cell except 1 neighbour of the last_cell.
# Auxiliary space: O(m * n) -> dictionary with every cell as key, and dictionary as value which holds at max
#                           4 edges => O(4 * (m * n))? well they scale Linearly with input, but don't know how to calc
#                           this extra dictionaries with edges correctly. There will never be more than 4 keys inside.
#                           Extra set() with visited nodes inside of BFS which can in the worst case hold all nodes,
#                           except last one, cuz we're breaking on him => O(m * n).
#                           Should be correct to say, linear: O(m * n).
# -----------------------
# All correct, but this BS limits is still mystery for me.
# Random cases correct, some cases given as well, but others failing.
# And logic is correct, if we can make a path we're Lowering max_limit, and Increase min_limit when we can't.
# Always failing with, that. And always it's different limits for the tasks...
# Ok. Working with standard BS limits:
# (middle - 1) to lower
# (middle + 1) to increase
# and check until min <= max
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

test = [[7, 9], [3, 6], [6, 9], [3, 6]]
test_out = 3
assert test_out == minimum_effort_path(test)

test = [[randint(1, 10 ** 6) for _ in range(100)] for _ in range(100)]
print(test)
