# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
# ----------------
# 1 <= n <= 20


def generate_matrix(n: int) -> list[list[int]]:
    # working_sol (91.26%, 96.50%) -> (33ms, 16.2mb)  time: O(n * n) | space: O(n * n)
    # always square matrix n * n
    matrix: list[list[int]] = [[-1 for _ in range(n)] for _ in range(n)]
    all_steps: int = n * n
    max_y: int = n - 1
    max_x: int = n - 1
    min_y: int = 0
    min_x: int = 0
    steps: int = 1
    x: int = 0
    dx: int = 1
    y: int = 0
    dy: int = 0
    matrix[y][x] = steps
    steps += 1
    turn: int = 0
    while steps <= all_steps:
        if turn == 3:
            min_y += 1
            max_y -= 1
            turn += 1
        if turn == 5:
            min_x += 1
            max_x -= 1
            turn = 0
        x += dx
        y += dy
        matrix[y][x] = steps
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
    return matrix


# Time complexity: O(n * n) -> creating matrix of (n * n) size => O(n * n) -> populating it by using every index, once.
# n - input value^^|
# Space complexity: O(n * n) -> always creating square matrix of length == n => O(n * n)


test: int = 3
test_out: list[list[int]] = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
assert test_out == generate_matrix(test)

test = 1
test_out = [[1]]
assert test_out == generate_matrix(test)

test = 6
test_out = [
    [1, 2, 3, 4, 5, 6],
    [20, 21, 22, 23, 24, 7],
    [19, 32, 33, 34, 25, 8],
    [18, 31, 36, 35, 26, 9],
    [17, 30, 29, 28, 27, 10],
    [16, 15, 14, 13, 12, 11],
]
assert test_out == generate_matrix(test)
