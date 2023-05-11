# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
# 1 <= n <= 20

def generate_matrix(n: int) -> list[list[int]]:
    # working_sol (14.40%, 17.46%) -> (46ms, 16.3mb)  time: O( ) | space: O( )
    matrix: list[list[int]] = [[-1 for _ in range(n)] for _ in range(n)]
    all_steps: int = n * n
    max_y = max_x = len(matrix[0]) - 1  # always square matrix n * n
    min_y = min_x = 0
    steps: int = 1
    x: int = 0
    dx: int = 1
    y: int = 0
    dy: int = 0
    matrix[y][x] = steps
    steps += 1
    turn: int = 0
    while steps <= all_steps:
        if turn % 3 == 0 and turn == 3:
            min_y += 1
            max_y -= 1
            turn += 1
        if turn % 5 == 0 and turn == 5:
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

# Time complexity: O(n) -> there's only 2 loops, first to create matrix of n * n size.
#                          Second going through whole created matrix and populating it with values from 1 to n ** 2.
#                          O(n + n) -> O(2n) -> O(n)
# Space complexity: O(n * n) -> constants and one list with lists inside -> O(consts + (n * n))
#                              ! cringe calculations, cuz there's, formulas for it, but I still didn't learn them.
#                                Basic idea should be correct !
# --------------------------
# Solution with populating and creating in the same time is a lot harder, and I don't have time for this now.
# Actually there's going to be more matrix's stuff, and maybe I will encounter something familiar, for now it's enough.
# --------------------------
# There's basic 2 ways I see here, populate from empty list, and made (n * n) matrix and populate it with placeholder,
#   and replace placeholder with given values.
# Placeholder is simpler, but slower. Creating and after looping, not just creating and populating together.
# Try placeholder first.


test1 = 3
test1_out = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
test = generate_matrix(test1)
assert test == test1_out
for _ in test:
    print(_)

test2 = 1
test2_out = [[1]]
test = generate_matrix(test2)
assert test == test2_out
for _ in test:
    print(_)

test3 = 6
test3_out = [
    [1, 2, 3, 4, 5, 6],
    [20, 21, 22, 23, 24, 7],
    [19, 32, 33, 34, 25, 8],
    [18, 31, 36, 35, 26, 9],
    [17, 30, 29, 28, 27, 10],
    [16, 15, 14, 13, 12, 11],
]
test = generate_matrix(test3)
assert test == test3_out
for _ in test:
    print(_)
