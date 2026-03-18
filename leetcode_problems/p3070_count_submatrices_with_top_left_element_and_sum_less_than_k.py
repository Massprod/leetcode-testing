# You are given a 0-indexed integer matrix grid and an integer k.
# Return the number of submatrices that contain the top-left element of the grid,
#  and have a sum less than or equal to k.
# --- --- --- ---
# m == grid.length 
# n == grid[i].length
# 1 <= n, m <= 1000 
# 0 <= grid[i][j] <= 1000
# 1 <= k <= 10 **9
from random import randint
from pyperclip import copy


def count_submatrices(grid: list[list[int]], k: int) -> int:
    # working_solution: (17.93%, 31.03%) -> (499ms, 67.22mb)  Time: O(n * m) Space: O(n * m)
    prefixes: list[list[int]] = [
        [0 for _ in range(len(grid[0]))] for _ in range(len(grid))
    ]
    # Horizontal prefixes
    for row in range(len(grid)):
        for col in range(1, len(grid[row])):
            prefixes[row][col] += grid[row][col - 1] + prefixes[row][col - 1]
    # Vertical prefixes (includes horizontal)
    for col in range(len(grid[0])):
        for row in range(1, len(grid)):
            prefixes[row][col] += grid[row - 1][col] + prefixes[row - 1][col]
    out: int = 0
    # Now we can just take the cell and prefixes to check.
    for row in range(len(prefixes)):
        for col in range(len(prefixes[0])):
            sub_sum: int = prefixes[row][col] + grid[row][col]
            if k < sub_sum:
                continue
            out += 1

    return out


# Time complexity: O(n * m)
# n - length of the input matrix `grid`,
# m - height of the input matrix `grid`.
# --- --- --- ---
# Space complexity: O(n * m)


test: list[list[int]] = [[7, 6, 3], [6, 6, 1]]
test_k: int = 18
test_out: int = 4
assert test_out == count_submatrices(test, test_k)

test = [[7, 2, 9], [1, 5, 0], [2, 6, 6]]
test_k = 20
test_out = 6
assert test_out == count_submatrices(test, test_k)

test = [[randint(0, 1_000) for _ in range(1_000)] for _ in range(1_000)]
copy(test)  # type: ignore
