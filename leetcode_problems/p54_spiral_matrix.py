# Given an m x n matrix, return all elements of the matrix in spiral order.
# Clockwise.
# --------------------
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100


def spiral_read(matrix: list[list[int]]) -> list[int]:
    # working_sol (50%, 70.44%) -> (39ms, 16.27mb)  time: O(n * m) | space: O(n * m)
    # Empty matrix.
    if len(matrix) == 0:
        return []
    x: int = 0
    dx: int = 1
    y: int = 0
    dy: int = 0
    all_steps: int = len(matrix[0]) * len(matrix)
    steps: int = 1
    turn: int = 0
    max_x: int = len(matrix[0]) - 1
    spiral: list[int] = []
    # Only one column.
    if max_x == 0:
        for _ in matrix:
            spiral.append(_[0])
        return spiral
    min_x: int = 0
    max_y: int = len(matrix) - 1
    # Only one row.
    if max_y == 0:
        for _ in matrix[0]:
            spiral.append(_)
        return spiral
    min_y: int = 0
    spiral.append(matrix[y][x])
    # Visit all cells.
    while steps < all_steps:
        # Making turn on every corner cell.
        if turn == 3:
            min_y += 1
            max_y -= 1
            # Placeholder to skip this check later.
            # Because we will make 1+ steps before turn will become >3.
            # And every step will trigger (turn == 3).
            turn += 1
        elif turn == 5:
            min_x += 1
            max_x -= 1
            turn = 0
        x += dx
        y += dy
        spiral.append(matrix[y][x])
        # Down.
        if x == max_x and dy == 0 and dx == 1:
            turn += 1
            dy = 1
            dx = 0
        # Left.
        elif y == max_y and dx == 0 and dy == 1:
            turn += 1
            dy = 0
            dx = -1
        # Up.
        elif x == min_x and dy == 0 and dx == -1:
            turn += 1
            dy = -1
            dx = 0
        # Right
        elif y == min_y and dx == 0 and dy == -1:
            turn += 1
            dy = 0
            dx = 1
        steps += 1
    return spiral


# Time complexity: O(n * m) -> looping through whole input matrix, once => O(n * m).
# n - length of input matrix^^|
# m - height of input matrix^^|
# Space complexity: O(n * m) -> new array with size of all values from input matrix => O(n * m)
# -------------------------------
# 1 <= m, n <= 10  <-- 100% no empty list's as matrix, so I will ignore that input.
#                       or it's better to set empty return?
# -------------------------------
# Failed with single column and won't fail with single row, but its unique cases.
# Better to just return whole single column or row without even coming to a while loop.
# -------------------------------
# Already been solving this with clockwise and counter_clockwise, but I was changing input matrix.
# In this one I might fail, but I will try to save initial matrix state and only read indexes.
# Main problems here, is where to TURN, cuz with changing indexes it's just simple turn on left_right side
# when we encounter some changed symbol -> (-) -> but without changing input matrix, I will try to count turns.


test: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test_out: list[int] = [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert spiral_read(test) == test_out

test = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
test_out = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
assert spiral_read(test) == test_out

test = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
test_out = [1, 2, 3, 4, 5, 10, 15, 14, 13, 12, 11, 6, 7, 8, 9]
assert spiral_read(test) == test_out

test = [[3], [2]]
test_out = [3, 2]
assert spiral_read(test) == test_out

test = [[1, 2, 3, 4, 5]]
test_out = [1, 2, 3, 4, 5]
assert spiral_read(test) == test_out

test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test_out = [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert spiral_read(test) == test_out

test = [[1]]
test_out = [1]
assert spiral_read(test) == test_out

test = []
test_out = []
assert spiral_read(test) == test_out

test = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
test_out = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
assert spiral_read(test) == test_out
