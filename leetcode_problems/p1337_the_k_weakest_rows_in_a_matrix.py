# You are given an m x n binary matrix mat of 1's (representing soldiers)
#  and 0's (representing civilians).
# The soldiers are positioned in front of the civilians.
# That is, all the 1's will appear to the left of all the 0's in each row.
# A row i is weaker than a row j if one of the following is true:
# The number of soldiers in row i is less than the number of soldiers in row j.
# Both rows have the same number of soldiers and i < j.
# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.
# ----------------------
# m == mat.length
# n == mat[i].length
# 2 <= n, m <= 100
# 1 <= k <= m
# matrix[i][j] is either 0 or 1.
from random import randint


def k_weakest_rows(mat: list[list[int]], k: int) -> list[int]:
    # working_sol (97.49%, 99.87%) -> (94ms, 16.4mb)  time: O(m * n) | space: O(k)
    # Count every row.
    for row in range(len(mat)):
        sold_count: int = 0
        for col in range(len(mat[row])):
            if mat[row][col] == 1:
                sold_count += 1
                continue
            break
        mat[row] = [sold_count, row]
    # Sort by soldiers, ascending.
    mat.sort()
    # Can be changed to return mat[:k], with change of first k elements of mat for O(1).
    # But, then I need to change input|out annotations. So it's extra O(k) space for a new list.
    # Assume we're not allowed to do that.
    return [row[1] for row in mat[:k]]


# Time complexity: O(m * n) -> worst case == every cell is '1' => traverse to count soldiers => O(m * n) ->
# m - row length of input_matrix^^| -> we're using same list to store (row_soldiers, row) so it's always same
# n - col length of input_matrix^^| lists to sort, only thing changing is number of rows to sort => O(n * log n) ->
# k - input value^^|                -> extra traverse of sorted matrix for k elements => O(k).
# Auxiliary space: O(k) -> use of the same input matrix to store everything and sorting in place => O(1) ->
#                       -> but we're returning list with k elements, so it's still extra space for this lest => O(k).
#                       ! 2 <= n, m <= 100 ! <-  we're changing input_matrix to len(row_soldiers, row) == 2.
#                       So, it's always minimum size we can be given that's why we can say it's O(1).


test: list[list[int]] = [
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1],
]
test_k: int = 3
test_out: list[int] = [2, 0, 3]
assert test_out == k_weakest_rows(test, test_k)

test = [
    [1, 0, 0, 0],
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 0]
]
test_k = 2
test_out = [0, 2]
assert test_out == k_weakest_rows(test, test_k)

test = []
for _ in range(100):
    row_ones: int = randint(0, 100)
    row_zeroes: int = 100 - row_ones
    test_row: list[int] = [1 for _ in range(row_ones)] + [0 for _ in range(row_zeroes)]
    test.append(test_row)
print(test)
