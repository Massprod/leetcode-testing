# You are given a 0-indexed integer array arr, and an m x n integer matrix mat.
#  arr and mat both contain all the integers in the range [1, m * n].
# Go through each index i in arr starting from index 0
#  and paint the cell in mat containing the integer arr[i].
# Return the smallest index i at which either a row
#  or a column will be completely painted in mat.
# -----------------------
# m == mat.length
# n = mat[i].length
# arr.length == m * n
# 1 <= m, n <= 10 ** 5
# 1 <= m * n <= 10 ** 5
# 1 <= arr[i], mat[r][c] <= m * n
# All the integers of arr are unique.
# All the integers of mat are unique.


def first_complete_index(arr: list[int], mat: list[list[int]]) -> int:
    # working_sol (33.75%, 8.20%) -> (145ms, 55.51mb)  time: O(m * n) | space: O(m * n)
    # { row : used_cells }
    rows: dict[int, int] = {
        row: 0 for row in range(len(mat))
    }
    # { columns: used_cell }
    columns: dict[int, int] = {
        col: 0 for col in range(len(mat[0]))
    }
    cells: dict[int, tuple[int, int]] = {}
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            cell_value: int = mat[row][col]
            cells[cell_value] = (row, col)

    target_row: int = len(mat[0])
    target_col: int = len(mat)
    for index, cell_value in enumerate(arr):
        cell_row, cell_col = cells[cell_value]
        rows[cell_row] += 1
        columns[cell_col] += 1
        if ((rows[cell_row] == target_row)
             or columns[cell_col] == target_col):
            return index
    return -1


# Time complexity: O(m * n) <- m - length of the input array `mat`,
#                              n - height of the input array `mat`.
# Always traversing rows and cols to build dicts => O(m + n).
# Traversing all cell from `arr` which has equal length to `mat` => O(m + n + m * n).
# In the worst case, there' only 1 row and we will just go left -> right on it.
# Extra traversing all the cells again => O(m + n + 2 * m * n).
# -----------------------
# Auxiliary space: O(m * n)
# `rows` <- allocates space for each row from `mat` => O(m).
# `cols` <- allocates space for each column from `mat` => O(m + n).
# `cells` <- allocates space for each cell from `mat` => O(m * n + m + n).


test: list[int] = [1, 3, 4, 2]
test_mat: list[list[int]] = [[1, 4], [2, 3]]
test_out: int = 2
assert test_out == first_complete_index(test, test_mat)

test = [2,8,7,4,1,3,5,6,9]
test_mat = [[3, 2, 5], [1, 4, 6], [8, 7, 9]]
test_out = 3
assert test_out == first_complete_index(test, test_mat)
