# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need
# to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
#
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.


def valid_sudoku(board: list[list[str]]) -> bool:
    # working_sol (9.16%, 69.14%)  time: O(n**2) | space: O(n)
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
            else:
                return False
            if board[y][x] not in rows[y] or board[y][x] == ".":
                rows[y].append(board[y][x])
            else:
                return False
            if board[y][x] not in columns[x] or board[y][x] == ".":
                columns[x].append(board[y][x])
            else:
                return False
    # for key, value in rows.items():
    #     print(value, end="\n")
    # print("------------------")
    # for key, value in columns.items():
    #     print(value, end="\n")
    # print("------------------")
    # for key, value in cubes.items():
    #     print(value, end="\n")
    return True

# Time complexity: O(n**2) -> simple case of double for_loop with iteration through every index
# Space complexity : O(n) -> 1+1+1 dictionaries of n size.

# Really slow solution and I think we can use fewer dictionaries to store sudoku.
# But I have already seen p 37 and there's going to be filling of correct number into circles and row.
# I was solving according to this. Now with all rows, columns and cubes data
# we can populate them without duplicates (hope so).
# Once again cringe fail but at least at this day I was worn out.


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
test1_out = True
print(valid_sudoku(test1))
assert test1_out == valid_sudoku(test1)

test2 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
test2_out = False
print(valid_sudoku(test2))
assert test2_out == valid_sudoku(test2)

test3 = [
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."]
]
test3_out = False
# test3 - fail - cuz I rushed and forgot about 3x3 cubes.....most important part :)
# Tired today so w.e
print(valid_sudoku(test3))
assert test3_out == valid_sudoku(test3)

