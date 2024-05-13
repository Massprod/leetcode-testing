# You are given an m x n binary matrix grid.
# A move consists of choosing any row or column and toggling each value in that row or column
#  (i.e., changing all 0's to 1's, and all 1's to 0's).
# Every row of the matrix is interpreted as a binary number,
#  and the score of the matrix is the sum of these numbers.
# Return the highest possible score after making any number of moves (including zero moves).
# --------------------
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 20
# grid[i][j] is either 0 or 1.
from random import randint


def matrix_score(grid: list[list[int]]) -> int:
    # working_sol (87.93%, 59.05%) -> (36ms, 16.57mb)  time: O(n * m) | space: O(n)
    out: int = 0
    flip: bool = False
    # We're given `rows` as binary representation of numbers.
    # The best way to make them into the biggest number is to flip MSB(MostSignificantBit).
    # So, if we find an empty bit place before MSB, we need to flip this row.
    for row in range(len(grid)):
        for val in grid[row]:
            if 0 == val:
                flip = True
                break
            elif 1 == val:
                break
        if flip:
            for index in range(len(grid[row])):
                if grid[row][index]:
                    grid[row][index] = 0
                else:
                    grid[row][index] = 1
            flip = False
    # We need to maximize summ of the all rows == numbers (each row == number).
    # We can see these rows just as some number of (2 ** column).
    # So, the best way to maximize columns is to make as much (2 ** column) as possible.
    # Check every value in a column, and if we can flip and get more of them, then we need to flip it.
    for col in range(len(grid[0])):
        col_zeroes: int = 0
        col_ones: int = 0
        for row in range(len(grid)):
            if grid[row][col]:
                col_ones += 1
            else:
                col_zeroes += 1
        if col_ones < col_zeroes:
            flip = True
        if flip:
            for row_ind in range(len(grid)):
                if grid[row_ind][col]:
                    grid[row_ind][col] = 0
                else:
                    grid[row_ind][col] = 1
            flip = False
    for row in range(len(grid)):
        num: str = ''
        for col in range(len(grid[row])):
            num += str(grid[row][col])
        out += int(num, 2)
    return out


# Time complexity: O(m * n) <- m - number of rows in input matrix `grid`, n - number of columns in input matrix `grid`.
# Always traversing every row of the matrix, to get the rows we need to flip => O(n).
# Extra traversing all the columns, to get the columns we need to flip => O(n).
# And extra traversing all the values again, to get rows == binary representations into a numbers => O(n).
# --------------------
# Auxiliary space: O(n)
# We're using `num` for temporary store all single row values in it => O(n).
# Everything else is constant INTs, which doesn't depend on input => O(1).


test: list[list[int]] = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
test_out: int = 39
assert test_out == matrix_score(test)

test = [[0]]
test_out = 1
assert test_out == matrix_score(test)

test = [[randint(0, 1) for _ in range(20)] for _ in range(20)]
print(test)
