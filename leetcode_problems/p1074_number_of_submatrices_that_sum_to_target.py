# Given a matrix and a target, return the number of non-empty submatrices that sum to target.
# A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2
#  and y1 <= y <= y2.
# Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different
#  if they have some coordinate that is different: for example, if x1 != x1'.
# --------------------
# 1 <= matrix.length <= 100
# 1 <= matrix[0].length <= 100
# -1000 <= matrix[i] <= 1000
# -10 ** 8 <= target <= 10 ** 8
from random import randint
from collections import defaultdict


def num_submatrix_sum_target(matrix: list[list[int]], target: int) -> int:
    # working_sol (68.98%, 57.55%) -> (544ms, 17.72mb)  time: O(n ** 2 * m) | space: O(n)
    # Replace original matrix values with [prefix + value].
    for row in range(len(matrix)):
        for col in range(1, len(matrix[row])):
            matrix[row][col] += matrix[row][col - 1]
    out: int = 0
    # Sliding window.
    # We can't skip rows and columns, so we can use sliding window.
    # From top_row -> bot_row with all sizes.
    for start in range(len(matrix[0])):
        for end in range(start, len(matrix[0])):
            # {submatrix sum: # of submatrices with such sum}
            visited: dict[int, int] = defaultdict(int)
            # Sum of current top -> down, submatrix we build with start -> end window size.
            submatrix_sum: int = 0
            for row in range(len(matrix)):
                left: int = 0
                if start:
                    left = matrix[row][start - 1]  # we need to include start value.
                right: int = matrix[row][end]
                submatrix_sum += right - left
                to_find: int = submatrix_sum - target
                # Row by itself, creates One row matrix with sum == target.
                if 0 == to_find:
                    out += 1
                # If we already visited submatrix with sum == (sum + target = submatrix_sum)
                # Then we can exclude these submatrices and for each get submatrix with (sum == target),
                #  by (submatrix_sum - sum = target).
                if to_find in visited:
                    out += visited[to_find]
                visited[submatrix_sum] += 1
    return out


# Time complexity: O(n ** 2 * m) <- n - number of rows in input `matrix`, m - number of columns in input `matrix`.
# We calculate all prefixes + values => O(m * n).
# Then we try to create contiguous submatrices from 1 -> len(matrix) - 1 size and for each size
#  we check every row sum => O(n * m * n) => O(n ** 2 * m)
# Auxiliary space: O(n).
# Worst case: every row will change `submatrix_sum`, so for every row `n` we get unique sum.
# And all these sums are stored in `visited` => O(n).
# Every window size change, we're clearing(recreate) `visited`.


test: list[list[int]] = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
test_target: int = 0
test_out: int = 4
assert test_out == num_submatrix_sum_target(test, test_target)

test = [[1, -1], [-1, 1]]
test_target = 0
test_out = 5
assert test_out == num_submatrix_sum_target(test, test_target)

test = [[904]]
test_target = 0
test_out = 0
assert test_out == num_submatrix_sum_target(test, test_target)

test = [[randint(-1000, 1000) for _ in range(100)] for _ in range(100)]
print(test)
