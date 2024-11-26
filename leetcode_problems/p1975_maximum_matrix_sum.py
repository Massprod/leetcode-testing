# You are given an n x n integer matrix. You can do the following operation any number of times:
#  - Choose any two adjacent elements of matrix and multiply each of them by -1.
# Two elements are considered adjacent if and only if they share a border.
# Your goal is to maximize the summation of the matrix's elements.
# Return the maximum sum of the matrix's elements using the operation mentioned above.
# --------------------------
# n == matrix.length == matrix[i].length
# 2 <= n <= 250
# -10 ** 5 <= matrix[i][j] <= 10 ** 5


def max_matrix_sum(matrix: list[list[int]]) -> int:
    # working_sol (69.82%, 41.30%) -> (83ms, 25.00mb)  time: O(m * n) | space: O(1)
    # If there's EVEN negatives == we can transform all of them without care.
    # If there's ODD negatives == we can transform all of them, except one.
    # But we can transform any other smaller value to be negative instead.
    # So, all we need is to find the smallest value for ODD negatives
    #  and reverse it to negative, or leave the current highest negative.
    out: int = 0
    min_val: int = 10 ** 5
    negatives: int = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            value: int = abs(matrix[row][col])
            out += value
            min_val = min(min_val, value)
            negatives += 1 if matrix[row][col] < 0 else 0
    if negatives % 2:
        # x2 <- because we already counted it as positive
        # So, we need to take it from sum and extra take this value converted to negative.
        out -= min_val * 2
    return out


# Time complexity: O(m * n) <- m - height of the input `matrix`, n - length of the input `matrix`.
# Always traversing whole input `matrix`, once => O(m * n).
# --------------------------
# Auxiliary space: O(1)
# Only 4 constant INTs used, none of them depends on input => O(1).


test: list[list[int]] = [[1, -1], [-1, 1]]
test_out: int = 4
assert test_out == max_matrix_sum(test)

test = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]
test_out = 16
assert test_out == max_matrix_sum(test)
