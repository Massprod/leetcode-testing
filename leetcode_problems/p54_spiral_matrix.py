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
    min_x = 0
    max_y = len(matrix) - 1
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


test1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test1_out = [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert spiral_read(test1) == test1_out
print(spiral_read(test1))

test2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
test2_out = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
assert spiral_read(test2) == test2_out
print(spiral_read(test2))

test3 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
for _ in test3:
    print(_)
print(spiral_read(test3))

