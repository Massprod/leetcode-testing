# You are given an m x n 2D array grid of positive integers.
# Your task is to traverse grid in a zigzag pattern while skipping every alternate cell.
# Zigzag pattern traversal is defined as following the below actions:
#  - Start at the top-left cell (0, 0).
#  - Move right within a row until the end of the row is reached.
#  - Drop down to the next row, then traverse left until
#    the beginning of the row is reached.
#  - Continue alternating between right and left traversal until every row
#    has been traversed.
# Note that you must skip every alternate cell during the traversal.
# Return an array of integers result containing, in order,
#  the value of the cells visited during the zigzag traversal with skips.
# ----------------------
# 2 <= n == grid.length <= 50
# 2 <= m == grid[i].length <= 50
# 1 <= grid[i][j] <= 2500


def zigzag_traversal(grid: list[list[int]]) -> list[int]:
    # working_sol (100.00%, 35.52%) -> (0ms, 18.30mb)  time: O(n) | space: O(n)
    out: list[int] = []

    alternate: bool = False
    record: bool = True
    for row in range(len(grid)):
        if not alternate:
            for column in range(len(grid[0])):
                if not record:
                    record = not record
                    continue
                out.append(grid[row][column])
                record = not record
        else:
            for column in range(len(grid[0]) - 1, -1, -1):
                if not record:
                    record = not record
                    continue
                out.append(grid[row][column])
                record = not record
        alternate = not alternate

    return out


# Time complexity: O(n) <- n - length of the input array `grid`.
# Always traversing whole input array `grid`, once => O(n).
# ----------------------
# Auxiliary space: O(n)
# `out` <- allocates space for (n // 2) cells from `grid` => O(n)


test: list[list[int]] = [[1, 2], [3, 4]]
test_out: list[int] = [1, 4]
assert test_out == zigzag_traversal(test)

test = [[2,1],[2,1],[2,1]]
test_out = [2, 1, 2]
assert test_out == zigzag_traversal(test)

test = [[1,2,3],[4,5,6],[7,8,9]]
test_out = [1, 3, 5, 7, 9]
assert test_out == zigzag_traversal(test)
