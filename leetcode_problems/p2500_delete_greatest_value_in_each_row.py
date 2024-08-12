# You are given an m x n matrix grid consisting of positive integers.
# Perform the following operation until grid becomes empty:
#  - Delete the element with the greatest value from each row.
#    If multiple such elements exist, delete any of them.
#  - Add the maximum of deleted elements to the answer.
# Note that the number of columns decreases by one after each operation.
# Return the answer after performing the operations described above.
# ----------------------
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 1 <= grid[i][j] <= 100
from random import randint


def delete_greatest_value(grid: list[list[int]]) -> int:
    # working_sol (81.76%, 74.38%) -> (84ms, 16.51mb)  time: O(n * (k * log k)) | space: O(n * k)
    rows: list[list[int]] = []
    for row in range(len(grid)):
        rows.append(sorted(grid[row]))
    out: int = 0
    while rows[0]:
        cur_max: int = 0
        for row in rows:
            cur_max = max(cur_max, row.pop())
        out += cur_max
    return out


# Time complexity: O(n * (k * log k)) <- n - height of the input matrix `grid`, k - length of the input matrix `grid`.
# Always sorting every row of the `grid` => O(n * (k * log k)).
# Extra traversing every element in rows, again => O(n * (k * log k) + n * k).
# ----------------------
# Auxiliary space: O(n * k)
# Creating a copy of the original `grid` but sorted => O(n * k).


test: list[list[int]] = [[1, 2, 4], [3, 3, 1]]
test_out: int = 8
assert test_out == delete_greatest_value(test)

test = [[10]]
test_out = 10
assert test_out == delete_greatest_value(test)

test = [[randint(1, 100) for _ in range(50)] for _ in range(50)]
print(test)
