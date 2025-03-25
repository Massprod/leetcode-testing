# Given a m x n matrix mat and an integer k,
#  return a matrix answer where each answer[i][j]
#  is the sum of all elements mat[r][c] for:
#  - i - k <= r <= i + k,
#  - j - k <= c <= j + k, and
#  - (r, c) is a valid position in the matrix.
# -----------------------------
# m == mat.length
# n == mat[i].length
# 1 <= m, n, k <= 100
# 1 <= mat[i][j] <= 100


def matrix_block_sum(mat: list[list[int]], k: int) -> list[list[int]]:
    # working_sol (86.02%, 72.47%) -> (12ms, 19.08mb)  time: O(m * n) | space: O(m * n)
    # Prefixes + cumulative for all rectangles
    # [
    #   [ sum of the rectangles of the row]
    #   sum of the rectangles on the row + all of the prev_rows
    # ]
    prefixes: list[list[int]] = [[0] for _ in mat]
    for row in range(len(mat)):
        prev_row: int = row - 1
        for column in range(len(mat[row])):
            prev_rect: int = 0
            # We already included prev row for the [-1].
            # So, we need to exclude this rectangle values
            #  and include the new rectangle values.
            if 0 <= prev_row:
                prev_rect = prefixes[prev_row][column + 1] - prefixes[prev_row][column]
            prefixes[row].append(
                prefixes[row][-1] + mat[row][column] + prev_rect
            )
    # region MainIdea
    # We're always calculatin rectangles.
    # And now we can just use cumulative sum to get them in O(1).
    # Because we don't care about saving original array,
    #  let's reuse it => save some space :)
    # Main idea:
    # [1, 1, 1]
    # [1, 1, 1]
    # [1, 1, 1]
    # To get botRight corner we need have sum of the rect (0, 0) -> (2, 2)
    # And we need to remove topSide + leftSide rectangles:
    # [r, r, r] 
    # [r, 1, 1]
    # [r, 1, 1]
    # And because we already acumulative sum, we can remove them with:
    #  1rect: (0, 1) -> (0, 2)
    #  2rect: (0, 0) -> (2, 0)
    # 1rect is only removed when we're calculatin rows >= 0.
    # 2rect is always used
    # endregion MainIdea
    start_row: int
    end_row: int
    start_col: int
    end_col: int
    row_limit: int = len(mat) - 1
    for row in range(len(mat)):
        for column in range(len(mat[row])):
            col_limit: int = len(mat[row]) - 1
            start_row, end_row = max(0, row - k), min(row + k, row_limit)
            start_col, end_col = max(0, column - k), min(column + k, col_limit)
            exclude_prev_rect: int = 0
            if 0 < start_row:
                shift_row: int = start_row - 1
                exclude_prev_rect = (
                    prefixes[shift_row][end_col + 1] - prefixes[shift_row][start_col]
                )
            cur_rect: int = prefixes[end_row][end_col + 1] - prefixes[end_row][start_col]
            mat[row][column] = cur_rect - exclude_prev_rect

    return mat


# Time complexity: O(m * n) <- m - length of the input array `mat`,
#                              n - height of the input array `mat`.
# Always traversing whole input array `mat`, twice => O(2 * m * n).
# -----------------------------
# Auxiliary space: O(m * n)
# `prefixes` <- allocates space for each index from `mat`,
#  and extra +1 index for the [0] prefix of the each row => O(m * n + n).


test: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test_k: int = 1
test_out: list[list[int]] = [[12, 21, 16], [27, 45, 33], [24, 39, 28]]
assert test_out == matrix_block_sum(test,test_k)

test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test_k = 2
test_out = [[45, 45, 45], [45, 45, 45], [45, 45, 45]]
assert test_out == matrix_block_sum(test,test_k)
