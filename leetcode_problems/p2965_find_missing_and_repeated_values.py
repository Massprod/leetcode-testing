# You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2].
# Each integer appears exactly once except a which appears twice and b which is missing.
# The task is to find the repeating and missing numbers a and b.
# Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.
# -------------------------
# 2 <= n == grid.length == grid[i].length <= 50
# 1 <= grid[i][j] <= n * n
# For all x that 1 <= x <= n * n there is exactly one
#  x that is not equal to any of the grid members.
# For all x that 1 <= x <= n * n there is exactly one
#  x that is equal to exactly two of the grid members.
# For all x that 1 <= x <= n * n except two of them there is exactly
#  one pair of i, j that 0 <= i, j <= n - 1 and grid[i][j] == x.


def find_missing_repeated_values(grid: list[list[int]]) -> list[int]:
    # working_sol (88.13%, 96.23%) -> (110ms, 16.77mb)  time: O(n * n) | space: O(n * n)
    all_val: set[int] = {val for val in range(1, len(grid) ** 2 + 1)}
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            cur_val: int = grid[row][col]
            if cur_val not in all_val:
                all_val.add(cur_val * -1)
            else:
                all_val.remove(cur_val)
    out: list[int] = sorted(all_val)
    out[0] *= -1
    return out


# Time complexity: O(n * n) <- n - length | height of the input matrix `grid`.
# Always creating `all_val` with the same # of values as `grid` size => O(n * n).
# Always traversing `grid`, once => O(n * n * 2).
# `out` always of the same size `2` and we're sorting it because we reversed repeated value.
# So, we can count it as constant, because we're guaranteed to have an answer => O(n * n).
# -------------------------
# Auxiliary space: O(n * n)
# `all_val` <- always of the `grid` size == `n * n` => O(n * n).


test: list[list[int]] = [[1, 3], [2, 2]]
test_out: list[int] = [2, 4]
assert test_out == find_missing_repeated_values(test)

test = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
test_out = [9, 5]
assert test_out == find_missing_repeated_values(test)
