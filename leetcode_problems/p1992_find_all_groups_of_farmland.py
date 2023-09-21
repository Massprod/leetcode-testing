# You are given a 0-indexed m x n binary matrix land where a 0 represents
#  a hectare of forested land and a 1 represents a hectare of farmland.
# To keep the land organized, there are designated rectangular areas of hectares
#  that consist entirely of farmland.
# These rectangular areas are called groups.
# No two groups are adjacent, meaning farmland in one group
#  is not four-directionally adjacent to another farmland in a different group.
# land can be represented by a coordinate system where the top left corner of land is (0, 0)
#  and the bottom right corner of land is (m-1, n-1).
# Find the coordinates of the top left and bottom right corner of each group of farmland.
# A group of farmland with a top left corner at (r1, c1) and a bottom right corner at (r2, c2)
#  is represented by the 4-length array [r1, c1, r2, c2].
# Return a 2D array containing the 4-length arrays described above for each group of farmland in land.
# If there are no groups of farmland, return an empty array. You may return the answer in any order.
# ------------------
# m == land.length
# n == land[i].length
# 1 <= m, n <= 300
# land consists of only 0's and 1's.
# Groups of farmland are rectangular in shape.
from collections import deque


def find_farmland(land: list[list[int]]) -> list[list[int]]:
    # working_sol (83.56%, 100%) -> (945ms, 29mb)  time: O(m * n) | space: O(m * n)
    farm_groups: list[list[int]] = []
    que: deque[tuple[int, int]] = deque()
    col_len: int = len(land)
    row_len: int = len(land[0])
    # Mark for visited, anything except 0 or 1.
    mark: int = 3
    # Always start from (0, 0).
    # Means we will always step into TOP_LEFT corner of any land first.
    for y in range(col_len):
        for x in range(row_len):
            if land[y][x] == 1:
                # Standard BFS from this corner.
                farm_groups.append([y, x])
                que.append((y, x))
                right_corner: tuple[int, int] = (y, x)
                while que:
                    cur_cell: tuple[int, int] = que.popleft()
                    col: int = cur_cell[0]
                    row: int = cur_cell[1]
                    # We're always traversing rectangles.
                    # We can just check BOT and RIGHT directions.
                    if 0 <= col + 1 < col_len and land[col + 1][row] == 1:
                        land[col + 1][row] = mark
                        que.append((col + 1, row))
                        right_corner = max(right_corner, (col + 1, row))
                    if 0 <= row + 1 < row_len and land[col][row + 1] == 1:
                        land[col][row + 1] = mark
                        que.append((col, row + 1))
                        right_corner = max(right_corner, (col, row + 1))
                farm_groups[-1] = farm_groups[-1] + [right_corner[0], right_corner[1]]
    return farm_groups


# Time complexity: O(m * n) -> worst case == all cells are '1', so we will traverse full matrix once => O(m * n).
# m - col_len of input matrix.
# n - row_len of input matrix.
# Auxiliary space: O(m * n) -> que with all these cells stored => O(m * n).
# ------------------
# Every land is distinct == surrounded by 0. So just traverse whole matrix until '1' is hit.
# BFS from this '1' to get mark this land and find left_top and bot_right corners.
# Only problem is how to cull max() check. Cuz it's easy to find maximum y, x for bot_right corner.
# But BFS should lead to it anyway. How we can check if it's last cell?
# W.e lets build working version with max(y, x) check, first.


test: list[list[int]] = [[1, 0, 0], [0, 1, 1], [0, 1, 1]]
test_out: list[list[int]] = [[0, 0, 0, 0], [1, 1, 2, 2]]
assert test_out == find_farmland(test)

test = [[1, 1], [1, 1]]
test_out = [[0, 0, 1, 1]]
assert test_out == find_farmland(test)

test = [[0]]
test_out = []
assert test_out == find_farmland(test)
