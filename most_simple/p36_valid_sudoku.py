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
    rows = {}
    for _ in range(9):
        rows[_] = []
    columns = {}
    for _ in range(9):
        columns[_] = []
    for y in range(len(board)):
        for x in range(len(board)):
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
test1_out = True
print(valid_sudoku(test1))


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

