# Given an m x n matrix board containing 'X' and 'O', capture all regions
#   that are 4-directionally surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
# m == board.length  ,  n == board[i].length
# 1 <= m, n <= 200  ,  board[i][j] is 'X' or 'O'.


def solve(board: list[list[str]]) -> None:
    already_flipped: set[tuple[int, int]] = set()
    path: set[tuple[int, int]] = set()
    max_x: int = len(board[0]) - 1
    max_y: int = len(board) - 1

    def is_surrounded(start: tuple[int, int]) -> bool:
        y: int = start[0]
        x: int = start[1]
        if y == 0 or x == 0 or y == max_y or x == max_x:
            return False
        path.add((y, x))
        blocked: list[tuple[int, int]] = []
        free: list[tuple[int, int]] = []
        if board[y + 1][x] == "X":
            blocked.append((y + 1, x))
        else:
            if (y + 1, x) not in path:
                free.append((y + 1, x))
        if board[y - 1][x] == "X":
            blocked.append((y - 1, x))
        else:
            if (y - 1, x) not in path:
                free.append((y - 1, x))
        if board[y][x - 1] == "X":
            blocked.append((y, x - 1))
        else:
            if (y, x - 1) not in path:
                free.append((y, x - 1))
        if board[y][x + 1] == "X":
            blocked.append((y, x + 1))
        else:
            if (y, x + 1) not in path:
                free.append((y, x + 1))
        if len(blocked) == 4:
            board[y][x] = "X"
            already_flipped.add(start)
            return True
        for point in free:
            if is_surrounded(point):
                path.add(point)
                return True
            return False
        if len(blocked) == 3:
            return True

    for y_ in range(max_y + 1):
        for x_ in range(max_x + 1):
            if ((y_, x_) in already_flipped) or board[y_][x_] == "X":
                continue
            if is_surrounded((y_, x_)):
                for val in path:
                    board[val[0]][val[1]] = "X"
                    already_flipped.add((val[0], val[1]))
                path.clear()


# Ok. P79 but simpler on the first look, because there's no check for correct matrix, and we can insta add
# flipped "O" indexes and ignore them after.
# There's no limit to what use, so I will stick to recursion, because iterations is way harder for this case.


test1 = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
test1_out = [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]
solve(test1)
print(test1)

test2 = [["X"]]
test2_out = [["X"]]
solve(test2)
print(test2)

test3 = [["O"]]
test3_out = [["O"]]
solve(test3)
print(test3)
