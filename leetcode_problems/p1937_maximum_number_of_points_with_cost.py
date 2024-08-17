# You are given an m x n integer matrix points (0-indexed).
# Starting with 0 points, you want to maximize the number of points you can get from the matrix.
# To gain points, you must pick one cell in each row.
# Picking the cell at coordinates (r, c) will add points[r][c] to your score.
# However, you will lose points if you pick a cell too far from the cell that you picked
#  in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1),
#  picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.
# Return the maximum number of points you can achieve.
# abs(x) is defined as:
#  - x for x >= 0.
#  - -x for x < 0.
# ------------------------
# m == points.length
# n == points[r].length
# 1 <= m, n <= 10 ** 5
# 1 <= m * n <= 10 ** 5
# 0 <= points[r][c] <= 10 ** 5


def max_points(points: list[list[int]]) -> int:
    # working_sol (45.85, 34.63%) -> (1565ms, 50.96mb)  time: O(n * m + k) | space: O(k)
    prev_row: list[int] = points[0]
    for row in range(1, len(points)):
        left_max: list[int] = [0 for _ in range(len(points[0]))]
        right_max: list[int] = left_max.copy()
        cur_row: list[int] = left_max.copy()
        left_max[0] = prev_row[0]
        for col in range(1, len(points[0])):
            left_max[col] = max(
                left_max[col - 1] - 1, prev_row[col]
            )
        right_max[-1] = prev_row[-1]
        for col in range(len(points[0]) - 2, -1, -1):
            right_max[col] = max(
                right_max[col + 1] - 1, prev_row[col]
            )
        for col in range(len(points[0])):
            cur_row[col] = points[row][col] + max(left_max[col], right_max[col])
        prev_row = cur_row
    return max(prev_row)


# Time complexity: O(n * m + k) <- n - height of the input matrix `points`, m - length of the input matrix `points`.
# Always traversing whole input array `points`, once => O(n * m).
# Extra traverse of the `prev_row` with size `k` => O(n * m + k).
# ------------------------
# Auxiliary space: O(k)
# We're using 4 arrays of the size `k` => O(4 * k).


test: list[list[int]] = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]
test_out: int = 9
assert test_out == max_points(test)

test = [[1, 5], [2, 3], [4, 2]]
test_out = 11
assert test_out == max_points(test)
