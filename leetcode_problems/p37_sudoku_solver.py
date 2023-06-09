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
    # working_sol (55.46%, 58.35%)  time: O(9**(n*n)) | space: O(n*n)
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
    empty = {"coordinates": [],
             "path": [],
             "end": [],
             }
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
            if board[y][x] == ".":
                empty["coordinates"].append((y, x))
            if board[y][x] not in cubes[cube] and board[y][x] != ".":
                cubes[cube].append(board[y][x])
            if board[y][x] not in rows[y] and board[y][x] != ".":
                rows[y].append(board[y][x])
            if board[y][x] not in columns[x] and board[y][x] != ".":
                columns[x].append(board[y][x])

    def populate(k: int = 0):
        if k == len(empty["coordinates"]):
            # empty["end"] = empty["path"].copy()
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
                empty["path"].append(value)
                board[row][column] = value
                if populate(k + 1):
                    return True
                rows[row].pop()
                empty["path"].pop()
                columns[column].pop()
                cubes[cur_cube].pop()

    populate()
    # for z in range(len(empty["coordinates"])):
    #     empty_coor = empty["coordinates"][z]
    #     new_value = empty["end"][z]
    #     board[empty_coor[0]][empty_coor[1]] = new_value


# Time complexity: O(9**(n*n)) -> worst case calling populate() 9 times, with n*n times repeating populate() inside.
# Space complexity: O(n*n) -> 1d + 1d + 1d + 1d + 1l. Creating 4 new dictionaries and creating n size lists inside.

# Ok. I forgot about INPLACE change, we can't populate after loop :)
# All problem I had with that is breaking from a  loop without changing correct SUDOKU.
# Fixed just with returning True on every call if we reach correct path. Now it's INPLACE solution

# Mistakes: I made correct version almost at the start, but with a lack of recursion experience, was trying to get -
# correct matrix as output just from reaching k == len(empty["coordinates"])....
# For the future, when we're using recursion, we need to record our correct *path* or multiple *paths*.

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
assert test1 == test1_out
for _ in test1:
    print(_, end="\n")
