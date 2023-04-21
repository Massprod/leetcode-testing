# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.
# It is guaranteed that the input board has only one solution.


def solve_sudoku(board: list[list[str]]) -> None:
    rows = {}
    for _ in range(9):
        rows[_] = []
    columns = {}
    for _ in range(9):
        columns[_] = []
    cubes = {}
    for _ in range(9):
        cubes[_] = []
    cube = 0
    for y in range(len(board)):
        if 0 <= y < 3:
            cube = 0
        if 3 <= y < 6:
            cube = 3
        if 6 <= y < 9:
            cube = 6
        for x in range(len(board)):
            if x % 3 == 0 and x != 0:
                cube += 1
            if board[y][x] not in cubes[cube] or board[y][x] == ".":
                cubes[cube].append(board[y][x])
            if board[y][x] not in rows[y] or board[y][x] == ".":
                rows[y].append(board[y][x])
            if board[y][x] not in columns[x] or board[y][x] == ".":
                columns[x].append(board[y][x])
    for key, value in rows.items():
        print(value, end="\n")
    print("------------------")
    for key, value in columns.items():
        print(value, end="\n")
    print("------------------")
    for key, value in cubes.items():
        print(value, end="\n")
    return True


test1 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
test1_out = [
    ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
    ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
    ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
    ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
    ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
    ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
    ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
    ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
    ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
]

print(solve_sudoku(test1))
