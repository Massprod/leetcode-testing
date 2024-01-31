# You are given a 0-indexed m x n binary matrix matrix and an integer numSelect,
#  which denotes the number of distinct columns you must select from matrix.
# Let us consider s = {c1, c2, ...., cnumSelect} as the set of columns selected by you.
#  A row row is covered by s if:
#   - For each cell matrix[row][col] (0 <= col <= n - 1) where matrix[row][col] == 1,
#      col is present in s or,
#   - No cell in row has a value of 1.
# You need to choose numSelect columns such that the number of rows that are covered is maximized.
# Return the maximum number of rows that can be covered by a set of numSelect columns.
# -----------------------
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 12
# matrix[i][j] is either 0 or 1.
# 1 <= numSelect <= n
from random import randint


def maximum_rows(matrix: list[list[int]], numSelect: int) -> int:
    # working_sol (42.28%, 59.35%) -> (58ms, 17.28mb)  time: O(mCk * k * (n * m)) | space: O(mCk * k)
    # If we can choose all columns, then we can cover all rows.
    if numSelect == len(matrix[0]):
        return len(matrix)
    # Brute Force with checking all combinations.
    combs: set[tuple] = set()
    cur_comb: list[int] = []

    def all_combs(start: int, end: int, size: int) -> None:
        if 0 == size:
            combs.add(tuple(cur_comb))
            return
        for new_start in range(start, end + 1):
            cur_comb.append(new_start)
            all_combs(new_start + 1, end, size - 1)
            cur_comb.pop()

    # Creates all combinations of range 0 -> len(matrix[0]), with size == numSelect.
    all_combs(0, len(matrix[0]), numSelect)

    out: int = 0
    for comb in combs:
        covered: int = 0
        for row in matrix:
            covered += 1
            for col, value in enumerate(row):
                if 1 == value and not (col in comb):
                    covered -= 1
                    break
        out = max(out, covered)
    return out


# Time complexity: O(mCk * k * (n * m)) <- n - rows of input matrix `matrix`, m - columns of input matrix `matrix`.
# First creating all combinations with size == k => O(mCk * k).
# mCk == all possible subsets to create, k == creation of tuple(cur_comb).
# Second trying to use every combination to cover rows, traversing whole matrix => O(mCk * k * (n * m)).
# -----------------------
# Auxiliary space: O(mCk * k).
# Every combination we create, we store in set `combs` => O(mCk * k).
# mCk - combinations with size == k.


test: list[list[int]] = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 0, 1]]
test_select: int = 2
test_out: int = 3
assert test_out == maximum_rows(test, test_select)

test = [[1], [0]]
test_select = 1
test_out = 2
assert test_out == maximum_rows(test, test_select)

test = [[randint(0, 1) for _ in range(12)] for _ in range(12)]
print(test)
