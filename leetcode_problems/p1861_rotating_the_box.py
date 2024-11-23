# You are given an m x n matrix of characters box representing a side-view of a box.
# Each cell of the box is one of the following:
#  - A stone '#'
#  - A stationary obstacle '*'
#  - Empty '.'
# The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity.
# Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box.
# Gravity does not affect the obstacles' positions, and the inertia from the box's rotation
#  does not affect the stones' horizontal positions.
# It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.
# Return an n x m matrix representing the box after the rotation described above.
# -------------------------
# m == box.length
# n == box[i].length
# 1 <= m, n <= 500
# box[i][j] is either '#', '*', or '.'.
from random import choice


def rotate_the_box(box: list[list[str]]) -> list[list[str]]:
    # working_sol (54.11%, 94.14%) -> (1905ms, 28.4mb)  time: O(m * n) | space: O(m * n)
    out: list[list[str]] = [
        ['.' for _ in range(len(box))] for _ in range(len(box[0]))
    ]
    reversed_row: int = 0
    # We can place any stone on `empty` spot if there's no `obstacle` after it.
    for cur_row in range(len(box) - 1, -1, -1):
        cur_stack: list[str] = []
        # Get all obstacles and stones.
        for column in range(len(box[0])):
            if '.' != box[cur_row][column]:
                cur_stack.append(box[cur_row][column])
        # Place stones on empty spots if we no obstacle blocks them from falling.
        for column in range(len(box[0]) - 1, -1, -1):
            if not cur_stack:
                break
            if '*' != cur_stack[-1]:
                out[column][reversed_row] = cur_stack.pop()
            elif '*' == cur_stack[-1] and '*' == box[cur_row][column]:
                out[column][reversed_row] = cur_stack.pop()
        reversed_row += 1
    return out


# Time complexity: O(m * n) <- m - height of the input matrix `box`, n - length of the input matrix `box`.
# Always creating a copy `box` with the same number of cells => O(m * n).
# In the worst case, there's only stones or obstacles in cells.
# We will use every cell of the matrix, once to count it into the stack
#  and second time to place them in `out` => O(3 * m * n).
# -------------------------
# Auxiliary space: O(m * n)
# `out` <- allocates space for each cell from original `box` => O(m * n).


test: list[list[str]] = [
    ["#", ".", "#"]
]
test_out: list[list[str]] = [
    ["."],
    ["#"],
    ["#"]
]
assert test_out == rotate_the_box(test)

test = [
    ["#", ".", "*", "."],
    ["#", "#", "*", "."]
]
test_out = [
    ["#", "."],
    ["#", "#"],
    ["*", "*"],
    [".", "."]
]
assert test_out == rotate_the_box(test)

test = [
    ["#", "#", "*", ".", "*", "."],
    ["#", "#", "#", "*", ".", "."],
    ["#", "#", "#", ".", "#", "."]
]
test_out = [
    [".", "#", "#"],
    [".", "#", "#"],
    ["#", "#", "*"],
    ["#", "*", "."],
    ["#", ".", "*"],
    ["#", ".", "."]
]
assert test_out == rotate_the_box(test)

test = [[choice(['.', '#', '*']) for _ in range(300)] for _ in range(300)]
print(test)
