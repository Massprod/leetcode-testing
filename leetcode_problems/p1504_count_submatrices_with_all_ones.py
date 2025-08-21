# Given an m x n binary matrix mat,
#  return the number of submatrices that have all ones.
# --- --- --- ---
# 1 <= m, n <= 150
# mat[i][j] is either 0 or 1.


def num_submat(mat: list[list[int]]) -> int:
    # working_solution: (97.51%, 28.97%) -> (31ms, 18.88mb)  Time: O(m * n) Space: O(m)
    # We're using columns for the histogram building.
    # [ current column height ]
    hist_heights: list[int] = [0 for _ in mat[0]]
    out: int = 0
    for row in mat:
        # Check every column if it still present == 1.
        # Otherwise, reset the column height.
        for index, value in enumerate(row):
            hist_heights[index] = 0 if 0 == value else hist_heights[index] + 1
        # [ index, number of submatrices, previous height ]
        # index - last index we used to build submatrices
        # height == -1 by default, because it will give us at least 1 `submatrix`
        # index == -1 by default, because it will give us `left_index` + 1 == 1 =>
        #  => submatrix with set height
        stack: list[tuple[int, int, int]] = [(-1, 0, -1)]
        for index, height in enumerate(hist_heights):
            # If the current height we have on index is higher|equal
            #  than the last we used on the left side.
            # Then we can't build from it, and we need to find something lower.
            # ! We need `submatrices` == rectangles.
            while stack[-1][2] >= height:
                stack.pop()
            left_index, prev_subs, _ = stack[-1]
            # (index - left_index) == length of the `submatrices` we can use.
            cur_subs: int = prev_subs + (index - left_index) * height
            stack.append(
                (index, cur_subs, height)
            )
            out += cur_subs
    
    return out


# Time complexity: O(m * n) <- m - length of the input matrix `mat`,
#                              n - height of the input matrix `mat`.
# Traversing each row of the input matrix to update columns heights => O(m * n).
# For each row we check, we extra traversing every column height
#  to get the submatrices => O(m * (n + n)).
# --- --- --- ---
# Space complexity: O(m)
# `hist_heights` <- allocates space for each column of the input matrix `mat` => O(m).
# `stack` <- allocates space for each column of the matrix aswell => O(m + m)


test: list[list[int]] = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]
test_out: int = 13
assert test_out == num_submat(test)

test = [[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]]
test_out: int = 24
assert test_out == num_submat(test)
