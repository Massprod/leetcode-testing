# Given an m x n matrix, return all elements of the matrix in spiral order.
# Clockwise.

def spiral_read(matrix: list[list[int]]) -> list[int]:
    x = 0
    dx = 1
    y = 0
    dy = 0
    all_steps = len(matrix[0]) * len(matrix)
    steps = 1
    turn = 0
    max_x = len(matrix[0]) - 1
    if max_x == 0:
        spiral = []
        for _ in matrix:
            spiral.append(_[0])
        return spiral
    min_x = 0
    max_y = len(matrix) - 1
    if max_y == 0:
        spiral = []
        for _ in matrix[0]:
            spiral.append(_)
        return spiral
    min_y = 0
    spiral = [matrix[y][x]]
    while steps < all_steps:
        if turn % 3 == 0 and turn >= 3:
            min_y += 1
            max_y -= 1
        if turn % 4 == 0 and turn >= 4:
            min_x += 1
            max_x -= 1
            turn = 0
        x += dx
        y += dy
        spiral.append(matrix[y][x])
        if x == max_x and dy == 0 and dx == 1:
            turn += 1
            dy = 1
            dx = 0
        elif y == max_y and dx == 0 and dy == 1:
            turn += 1
            dy = 0
            dx = -1
        elif x == min_x and dy == 0 and dx == -1:
            turn += 1
            dy = -1
            dx = 0
        elif y == min_y and dx == 0 and dy == -1:
            turn += 1
            dy = 0
            dx = 1
        steps += 1
    return spiral


# Failed with single column and won't be failed with single row, but its unique cases.
# Better to just return whole single column or row without even coming to a while loop.
# -------------------------------
# Already been solving this with clockwise and counter_clockwise, but I was changing input matrix.
# In this one I might fail, but I will try to save initial matrix state and only read indexes.
# Main problems here, is where to TURN, cuz with changing indexes it's just simple turn on left_right side
# when we encounter some changed symbol -> (-) -> but without changing input matrix, I will try to count turns.


test1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test1_out = [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert spiral_read(test1) == test1_out
print(spiral_read(test1))

test2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
test2_out = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
assert spiral_read(test2) == test2_out
print(spiral_read(test2))

test3 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
test3_out = [1, 2, 3, 4, 5, 10, 15, 14, 13, 12, 11, 6, 7, 8, 9]
assert spiral_read(test3) == test3_out
print(spiral_read(test3))

# test4 - failed -> never ever thought about ONE column matrix
test4 = [[3], [2]]
test4_out = [3, 2]
assert spiral_read(test4) == test4_out
print(spiral_read(test4))

test5 = [[1, 2, 3, 4, 5]]
test5_out = [1, 2, 3, 4, 5]
assert spiral_read(test5) == test5_out
print(spiral_read(test5))

test6 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test6_out = [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert spiral_read(test6) == test6_out
print(spiral_read(test6))
