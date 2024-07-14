# Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.
# In one shift operation:
#   - Element at grid[i][j] moves to grid[i][j + 1].
#   - Element at grid[i][n - 1] moves to grid[i + 1][0].
#   - Element at grid[m - 1][n - 1] moves to grid[0][0].
# Return the 2D grid after applying shift operation k times.
# -----------------------
# m == grid.length
# n == grid[i].length
# 1 <= m <= 50
# 1 <= n <= 50
# -1000 <= grid[i][j] <= 1000
# 0 <= k <= 100
from random import randint


def shift_grid(grid: list[list], k: int) -> list[list[int]]:
    # working_sol (99.45%, 15.78%) -> (107ms, 17.06mb)  time: O(n * m) | space: O(n * m)
    # Essentially, we're just switching everything by 1 step.
    # So, we can just build a circular array from the `grid`.
    # And switch everything by `k` steps.
    # If we're going to make full circles, we can ignore them with `%`.
    circle: list[int] = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            circle.append(grid[row][col])
    shift: int = k % len(circle)
    # Shift `shift` values from end to the start of the array.
    circle = circle[len(circle) - shift:] + circle[:len(circle) - shift]
    out: list[list[int]] = []
    # Rebuild with the same number of rows and size.
    row_length: int = len(grid[0])
    row_start: int = 0
    row_end: int = row_length
    while row_start < len(circle):
        out.append(circle[row_start: row_end])
        row_start += row_length
        row_end += row_length
    return out


# Time complexity: O(n * m) <- n - height of the input matrix `grid`, m - length of the input matrix `grid`.
# Always traversing whole input matrix `grid`, once => O(n * m).
# Extra traversing all the values from `grid` again with slicing => O(2 * (n * m)).
# Rebuilding `out` to the same `grid` sizes, but with a new values order => O(3 * (n * m))
# -----------------------
# Auxiliary space: O(n * m)
# `circle` is always stores every value from `grid` => O(n * m).
# `out` is actual copy of the `grid`, but with a different order => O(2 * (n * m)).
# Slices for `circle` is going to take space for every value from `circle` => O(3 * (n * m)).
# Extra we will allocate space for `out` slices, `n` - slices with `m` sizes => O(4 * (n * m)).


test: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test_k: int = 1
test_out: list[list[int]] = [[9, 1, 2], [3, 4, 5], [6, 7, 8]]
assert test_out == shift_grid(test, test_k)

test = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
test_k = 4
test_out = [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]]
assert test_out == shift_grid(test, test_k)

test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test_k = 9
test_out = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
assert test_out == shift_grid(test, test_k)

test = [[randint(-1000, 1000) for _ in range(50)] for _ in range(50)]
print(test)
