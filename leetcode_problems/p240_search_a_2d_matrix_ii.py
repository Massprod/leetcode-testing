# Write an efficient algorithm that searches for a value target
#  in an m x n integer matrix matrix. This matrix has the following properties:
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# --- --- --- ---
# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -10 ** 9 <= matrix[i][j] <= 10 ** 9
# All the integers in each row are sorted in ascending order.
# All the integers in each column are sorted in ascending order.
# -10 ** 9 <= target <= 10 ** 9


def search_matrix(matrix: list[list[int]], target: int) -> bool:    
    # working_solution: (97.27%, 31.35%) -> (129ms, 25.66mb)  Time: O(log (n * m)) Space: O(1)
    y: int
    x: int
    # [ row, column ] = [ y, x ]
    start: list[int] = [0, len(matrix[0]) - 1]
    # We check in reverse.
    while (y := start[0]) < len(matrix) and (x := start[1]) >= 0:
        current: int = matrix[y][x]
        if target == current:
            return True
        # Everything on the bottom is higher than a current => shift column.
        if target < current:
            start[1] -= 1
        # Everything on the left is lower than a current => shift row.
        elif target > current:
            start[0] += 1
        
    return False


# Time complexity: O(log (n * m))
# n - length of the input matrix `matrix`.
# m - height of the input matrix `matrix`.
# --- --- --- ---
# Space complexity: O(1)


test: list[list[int]] = [
    [1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]
]
test_target: int = 5
test_out: bool = True
assert test_out == search_matrix(test, test_target)

test = [
    [1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]
]
test_target = 20
test_out = False
assert test_out == search_matrix(test, test_target)
