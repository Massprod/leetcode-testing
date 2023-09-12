# You are given four integers row, cols, rCenter, and cCenter.
# There is a rows x cols matrix, and you are on the cell with the coordinates (rCenter, cCenter).
# Return the coordinates of all cells in the matrix,
#  sorted by their distance from (rCenter, cCenter) from the smallest distance to the largest distance.
# You may return the answer in any order that satisfies this condition.
# The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|.
# --------------------------
# 1 <= rows, cols <= 100
# 0 <= rCenter < rows
# 0 <= cCenter < cols
from collections import deque


def all_cells_dist_order(rows: int, cols: int, rCenter: int, cCenter: int) -> list[list[int]]:
    # working_sol (28.67%, 12.12%) -> (159ms, 19.4mb)  time: O(m * n) | space: O(m * n)
    # We always have same distance for the closest cells.
    # So it can be done with BFS. And we don't care about ordering for the same distance.
    # Standard BFS approach.
    que: deque[list[int, int]] = deque()
    que.append([rCenter, cCenter])
    ordered: list[list[int]] = [[rCenter, cCenter]]
    visited: set[tuple[int, int]] = {(rCenter, cCenter)}
    # Check every possible cell of the matrix.
    while que:
        cur_cell: list[int, int] = que.popleft()
        row: int = cur_cell[0]
        col: int = cur_cell[1]
        # If not visited => check it.
        if 0 <= row - 1 < rows and (row - 1, col) not in visited:
            que.append([row - 1, col])
            ordered.append([row - 1, col])
            # Store visited.
            visited.add((row - 1, col))
        if 0 <= row + 1 < rows and (row + 1, col) not in visited:
            que.append([row + 1, col])
            ordered.append([row + 1, col])
            visited.add((row + 1, col))
        if 0 <= col - 1 < cols and (row, col - 1) not in visited:
            que.append([row, col - 1])
            ordered.append([row, col - 1])
            visited.add((row, col - 1))
        if 0 <= col + 1 < cols and (row, col + 1) not in visited:
            que.append([row, col + 1])
            ordered.append([row, col + 1])
            visited.add((row, col + 1))
    return ordered


# Time complexity: O(m * n) -> every cell of the matrix will be visited once => O(m * n).
# m - input rows, height of matrix^^|
# n - input cols, length of matrix^^|
# Auxiliary space: O(m * n) -> set will all cells stored as visited, and extra list with same size => O(2 * (m * n)).
# --------------------------
# Isn't it BFS? We will always take closest cells first to process, and they're on the same distance.
# Let's try. Yep working, they're testing with w.e ordering for same distances.


test_rows: int = 1
test_cols: int = 2
test_rcenter: int = 0
test_ccenter: int = 0
test_out: list[list[int]] = [[0, 0], [0, 1]]
assert test_out == all_cells_dist_order(test_rows, test_cols, test_rcenter, test_ccenter)

test_rows = 2
test_cols = 2
test_rcenter = 0
test_ccenter = 1
test_out = [[0, 1], [1, 1], [0, 0], [1, 0]]
assert test_out == all_cells_dist_order(test_rows, test_cols, test_rcenter, test_ccenter)

test_rows = 2
test_cols = 3
test_rcenter = 1
test_ccenter = 2
test_out = [[1, 2], [0, 2], [1, 1], [0, 1], [1, 0], [0, 0]]
assert test_out == all_cells_dist_order(test_rows, test_cols, test_rcenter, test_ccenter)
