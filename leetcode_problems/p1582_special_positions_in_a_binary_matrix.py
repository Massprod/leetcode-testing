# Given an m x n binary matrix mat, return the number of special positions in mat.
# A position (i, j) is called special if mat[i][j] == 1
#  and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
# --------------------------
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# mat[i][j] is either 0 or 1.
from random import randint


def num_special(mat: list[list[int]]) -> int:
    # working_sol (84.40%, 64.83%) -> (148ms, 16.62mb)  time: O(m * n) | space: O(m + n)
    # Adding every row and col as keys, for easier checks.
    # {row: all '1' on this row}
    rows: dict[int, int] = {row: 0 for row in range(len(mat))}
    # {col: all '1' on this col}
    cols: dict[int, int] = {col: 0 for col in range(len(mat[0]))}
    # Count every '1' placed on each row and col.
    for row in range(len(mat)):
        for col in range(len(mat[row])):
            if mat[row][col]:
                rows[row] += 1
                cols[col] += 1
    out: int = 0
    for row in range(len(mat)):
        # Empty row, or more than one '1' on it => incorrect row.
        if rows[row] != 1:
            continue
        for col in range(len(mat[row])):
            # We need to find position of '1' == col and have only one '1' on this column.
            if mat[row][col] and cols[col] == 1:
                out += 1
                # Insta break, because only one '1' on row allowed.
                break
    return out


# Time complexity: O(m * n) <- m - length of input matrix `mat`, n - height of input matrix `mat`.
# Creating `rows` and `cols` to store all data, pre-populating them with all row and col indexes => O(m + n).
# Full traverse of matrix to get all # of placed bits on theirs rows and cols => O(m * n).
# Worst case == [[0, 0 ... 0, 1][0, 0 ..., 0 1] ... [0, 0 ... 0, 1]].
# So, we will start traverse of every row, because all of them have only one '1' placed.
# And we will check all indexes of rows until we hit '1' which isn't correct => O(m * n).
# O(2 * (m * n) + (m + n)) => O(m * n).
# Auxiliary space: O(m + n).
# We only store all indexes of rows and columns, and INT for each of the indexes => O(m + n).


test: list[list[int]] = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
test_out: int = 1
assert test_out == num_special(test)

test = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
test_out = 3
assert test_out == num_special(test)

test = [[randint(0, 1) for _ in range(100)] for _ in range(100)]
print(test)
