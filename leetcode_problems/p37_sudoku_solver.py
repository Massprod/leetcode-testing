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
    empty = {"coordinates": []}
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
            if board[y][x] not in cubes[cube]:
                cubes[cube].append(board[y][x])
            if board[y][x] not in rows[y]:
                rows[y].append(board[y][x])
            if board[y][x] not in columns[x]:
                columns[x].append(board[y][x])
            if board[y][x] == ".":
                empty["coordinates"].append((y, x))

    def populate(k: int = 0):
        if k == len(empty["coordinates"]):
            return True
        for value in range(1, 10):
            value = str(value)
            coor = empty["coordinates"][k]
            row = coor[0]
            column = coor[1]
            cur_cube = 0
            if 0 <= row < 3:
                cur_cube = 0
                if 3 <= column < 6:
                    cur_cube = 1
                if 6 <= column < 9:
                    cur_cube = 2
            if 3 <= row < 6:
                cur_cube = 3
                if 3 <= column < 6:
                    cur_cube = 4
                if 6 <= column < 9:
                    cur_cube = 5
            if 6 <= row < 9:
                cur_cube = 6
                if 3 <= column < 6:
                    cur_cube = 7
                if 6 <= column < 9:
                    cur_cube = 8
            if value not in rows[row] and value not in columns[column] and value not in cubes[cur_cube]:
                rows[row].append(value)
                columns[column].append(value)
                cubes[cur_cube].append(value)
                board[row][column] = value
                populate(k + 1)
                rows[row].pop()
                columns[column].pop()
                cubes[cur_cube].pop()
    populate()
    for _ in board:
        print(_, end="\n")


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
solve_sudoku(test1)
