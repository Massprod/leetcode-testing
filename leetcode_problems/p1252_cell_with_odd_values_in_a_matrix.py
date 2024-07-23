# There is an m x n matrix that is initialized to all 0's.
# There is also a 2D array indices where each indices[i] = [ri, ci]
#  represents a 0-indexed location to perform some increment operations on the matrix.
# For each location indices[i], do both of the following:
#  1. Increment all the cells on row ri.
#  2. Increment all the cells on column ci.
# Given m, n, and indices, return the number of odd-valued cells
#  in the matrix after applying the increment to all locations in indices.
# ---------------------------
# 1 <= m, n <= 50
# 1 <= indices.length <= 100
# 0 <= ri < m
# 0 <= ci < n
# ---------------------------
# Follow up: Could you solve this in O(n + m + indices.length) time with only O(n + m) extra space?


def odd_cells(m: int, n: int, indices: list[list[int]]) -> int:
    # working_sol (99.48%, 30.31%) -> (32ms, 16.67mb)  time: O(n * m) | space: O(n + m)
    rows: list[int] = [0] * m
    cols: list[int] = [0] * n
    for row, col in indices:
        rows[row] += 1
        cols[col] += 1
    out: int = 0
    for col in range(len(cols)):
        for row in range(len(rows)):
            if (rows[row] + cols[col]) % 2:
                out += 1
    return out


# Time complexity: O(n * m) <- k - length of the input array `indices`.
# Always creating `rows` and `cols` with sizes `m` and `n` => O(n + m).
# Traversing all indexes of `indices` => O(n + m + k).
# Extra traversing every cell of the `m` * `n` matrix => O(n * m).
# ---------------------------
# Auxiliary space: O(n + m).
# `rows` <- always of size `m` => O(m).
# `cols` <- always of size `n` => O(n + m).


test_m: int = 2
test_n: int = 3
test_indices: list[list[int]] = [[0, 1], [1, 1]]
test_out: int = 6
assert test_out == odd_cells(test_m, test_n, test_indices)

test_m = 2
test_n = 2
test_indices = [[1, 1], [0, 0]]
test_out = 0
assert test_out == odd_cells(test_m, test_n, test_indices)
