# You are given a 0-indexed m x n integer matrix grid.
# The width of a column is the maximum length of its integers.
# For example, if grid = [[-10], [3], [12]],
#  the width of the only column is 3 since -10 is of length 3.
# Return an integer array ans of size n where ans[i] is the width of the ith column.
# The length of an integer x with len digits is equal to len if x is non-negative,
#  and len + 1 otherwise.
# --------------------------
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100 
# -10 ** 9 <= grid[r][c] <= 10 ** 9


def find_column_width(grid: list[list[int]]) -> list[int]:
    # working_sol (11.05%, 46.29%) -> (23ms, 19.04mb)  time: O(m * n) | space: O(n)

    def count_digits(number: int) -> int:
        digits: int = 0
        while number:
            number //= 10
            digits += 1
        
        return digits
    
    out: list[int] = [1 for _ in range(len(grid[0]))]
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            value: int = grid[row][column]
            value_digits: int = count_digits(abs(value))
            out[column] = max(
                value_digits + 1 if value < 0 else value_digits,
                out[column]
            )

    return out


# Time complexity: O(m * n) <- m - height of the input matrix `grid`,
#                              n - length of the input matrix `grid`.
# --------------------------
# Auxiliary space: O(n)
# `out` <- allocates space for each column in `grid` => O(n).


test: list[list[int]] = [[1], [22], [333]] 
test_out: list[int] = [3]
assert test_out == find_column_width(test)

test = [[-15, 1, 3], [15, 7, 12], [5, 6, -2]]
test_out = [3, 1, 2]
assert test_out == find_column_width(test)
