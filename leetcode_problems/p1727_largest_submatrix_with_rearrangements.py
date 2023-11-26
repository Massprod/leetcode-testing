# You are given a binary matrix matrix of size m x n,
#  and you are allowed to rearrange the columns of the matrix in any order.
# Return the area of the largest submatrix within matrix where every element of the submatrix
#  is 1 after reordering the columns optimally.
# ----------------------
# m == matrix.length
# n == matrix[i].length
# 1 <= m * n <= 10 ** 5
# matrix[i][j] is either 0 or 1.


def largest_submatrix(matrix: list[list[int]]) -> int:
    # working_sol (25.70%, 40.97%) -> (1129ms, 42.7mb)  time: O(n * m * log m) | space: O(m)
    out: int = 0
    sub_options: list[int] = sorted(matrix[0], reverse=True)
    for col in range(len(sub_options)):
        if sub_options[col]:
            out = max(out, col + 1)
        else:
            break
    for row in range(1, len(matrix)):
        # Find everything we have above every cell.
        for col in range(len(matrix[row])):
            # We have something above, and we can continue it with '1' cell.
            if matrix[row][col]:
                matrix[row][col] += matrix[row - 1][col]
        # Descending to get highest -> lowest, and we could use what we have above with current row '1's streak.
        sub_options = sorted(matrix[row], reverse=True)
        for col in range(len(sub_options)):
            if sub_options[col]:
                out = max(out, sub_options[col] * (col + 1))
            else:
                break
    return out


# Time complexity: O((n * m) + (n * m * log m)) -> traverse every row of 'matrix' + every column twice => O(n * 2m) ->
# n - height of input 'matrix'^^| -> after every row traver we sorting it in descending order => O(n * m * log m).
# m - length of input 'matrix'^^|
# Auxiliary space: O(m) -> always recreating sorted in descending order version of current row we're using => O(m).
# ----------------------
# Hints:
# ! For each column, find the number of consecutive ones ending at each position. !
# ! For each row, sort the cumulative ones in non-increasing order and "fit" the largest submatrix. !
# So, we need to know what we have ABOVE and what we have on CURRENT row and them just combine it to maximum?
# And because it's descending order we will always can multiply by CURRENT row streak of '1's.


test: list[list[int]] = [[0, 0, 1], [1, 1, 1], [1, 0, 1]]
test_out: int = 4
assert test_out == largest_submatrix(test)

test = [[1, 0, 1, 0, 1]]
test_out = 3
assert test_out == largest_submatrix(test)

test = [[1, 1, 0], [1, 0, 1]]
test_out = 2
assert test_out == largest_submatrix(test)
