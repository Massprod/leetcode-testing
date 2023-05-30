# Given an m x n matrix board containing 'X' and 'O', capture all regions
#   that are 4-directionally surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
# ------------------
# m == board.length  ,  n == board[i].length
# 1 <= m, n <= 200  ,  board[i][j] is 'X' or 'O'.


def solve(board: list[list[str]]) -> None:
    # working_sol (6.20%, 11.34%) -> (290ms, 47.1mb)  time: O(2 * (m - 2) * (n - 2)) | O(m * n)
    #                                                 space: O(2 * ((m - 2) * (n - 2)) + (g * 4)) | O(m * n + g)
    already_flipped: set[tuple[int, int]] = set()
    path: dict[tuple[int, int]] = {}
    max_x: int = len(board[0]) - 1
    max_y: int = len(board) - 1

    def is_surrounded(start: tuple[int, int]) -> bool | None:
        y: int = start[0]
        x: int = start[1]
        if y == 0 or x == 0 or y == max_y or x == max_x:
            return False
        path[start] = True
        blocked: set[tuple[int, int]] = set()
        free: set[tuple[int, int]] = set()
        if board[y + 1][x] == "X":
            blocked.add((y + 1, x))
        else:
            if (y + 1, x) not in path:
                free.add((y + 1, x))
        if board[y - 1][x] == "X":
            blocked.add((y - 1, x))
        else:
            if (y - 1, x) not in path:
                free.add((y - 1, x))
        if board[y][x - 1] == "X":
            blocked.add((y, x - 1))
        else:
            if (y, x - 1) not in path:
                free.add((y, x - 1))
        if board[y][x + 1] == "X":
            blocked.add((y, x + 1))
        else:
            if (y, x + 1) not in path:
                free.add((y, x + 1))
        if len(blocked) == 4:
            board[y][x] = "X"
            already_flipped.add(start)
            return True
        for point in free:
            if point[0] == 0 or point[0] == max_y or point[1] == 0 or point[1] == max_x:
                path[point] = False
            if is_surrounded(point):
                path[point] = True
        if len(blocked) == 3:
            return True

    for y_ in range(1, max_y):
        for x_ in range(1, max_x):
            if ((y_, x_) in already_flipped) or board[y_][x_] == "X":
                continue
            is_surrounded((y_, x_))
            broke: bool = False
            for _ in path.keys():
                if path[_] is False:
                    for coor in path.keys():
                        already_flipped.add(coor)
                    broke = True
                    path = {}
                    break
            if not broke:
                for val in path.keys():
                    board[val[0]][val[1]] = "X"
                    already_flipped.add((val[0], val[1]))
                path = {}
                continue
            for _ in path.keys():
                already_flipped.add(_)
            path = {}


# Time complexity: O(2 * (m - 2) * (n - 2)) -> traversing once through whole matrix and ignoring indexes
# n - len of matrix rows^^ | we have already met in the recursion, ignoring borders as well => O((m - 2) * (n - 2)) ->
# m - num of matrix col's^^| -> changing indexes on the path into "X", worst case: borders is "X" and insides only "O"
#                            same path as in recursion, but with changing values on coor => O((m - 2) * (n - 2)) ->
#                            -> assuming that HASH operations is O(1) like in p128, than reading, clearing path(dict())
#                            adding elements in already_flipped(set()) and path itself => O(1) -> -> leading us to =>
#                            => O((m - 2)  * (n - 2)) + O((m -2) * (n -2)) => O(2 * (m - 2) * (n - 2)).
# Space complexity: O(2 * ((m - 2) * (n - 2)) + (g * 4)) -> worst case == every border index is "X" insides "O" ->
# g - num of unique paths^^| -> extra dict() to store path, which in the worst case can be size of (m - 2) * (n - 2) ->
#                            -> same goes to the already_flipped(set()), values on the  path we walk added into it =>
#                            => O(2 * ((m - 2) * (n - 2))) -> every recursion creates two extra sets to store
#                            all values around coordinate it called(start), both of them store only 4 values
#                            distributed between them => O(g * 4), recursion called only once for every unique path.
# ------------------
# Solution is a mess and not so good on performance but working.
# Can be changed to remove recursion and check less extra pointers, but maybe later.
# There's too much to do to stop for this.
# ------------------
# Actually all I needed to check if any "O" connected to a borders, otherwise any path can be changed to "X",
# because there's only "X" and "O", so if there's no border connection means it's blocked for sure.
# But how to stop check? Because right now im checking every point on a path without breaking when we get to border.
# How to correctly break recursion in this case?
# Assuming that we have O(1) speed to check dictionary like in p128, then I could check dict(),
# before starting any recursion and insta break from it? Hmm. But that's what im already doing, because
# right now we're checking WHOLE path and after coming out from recursion flipping all path, or
# adding it into already_flipped and ignore next_time we meet this coordinate.
# It's changing nothing. W.e google or revisit, after I get more experience and maybe change it.
# ------------------
# Seems working, but I don't want to create nore test cases, so let's fail.
# ------------------
# Ok. P79 but simpler on the first look, because there's no check for correct matrix, and we can insta add
# flipped "O" indexes and ignore them after.
# There's no limit to what use, so I will stick to recursion, because iterations is way harder for this case.


test1 = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
test1_out = [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]
solve(test1)
assert test1_out == test1

test2 = [["X"]]
test2_out = [["X"]]
solve(test2)
assert test2_out == test2

test3 = [["O"]]
test3_out = [["O"]]
solve(test3)
assert test3_out == test3

test4 = [
    ["O", "O", "X", "O", "O", "O"],
    ["X", "O", "O", "O", "O", "X"],
    ["X", "X", "X", "X", "X", "X"],
    ["X", "O", "O", "O", "X", "X"],
    ["X", "X", "X", "O", "O", "X"],
    ["X", "O", "O", "O", "X", "O"],
    ["O", "X", "X", "X", "O", "O"],
]
test4_out = [
    ['O', 'O', 'X', 'O', 'O', 'O'],
    ['X', 'O', 'O', 'O', 'O', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'O'],
    ['O', 'X', 'X', 'X', 'O', 'O'],
]
solve(test4)
assert test4_out == test4

# test5 - failed -> I was using set(), just to store values along the path and didn't consider the case.
#                   If we have only 1 value which returns True it still will be added on a path,
#                   and if it's value was a last one to check path will have this value in the end.
#                   When he should because path should be cleared if at least one value is not correct.
#                   Either I should change it into a dict() and check if all keys added have same value,
#                   or I can break recursion and clear path after we met boarder points. How?
test5 = [
    ["O", "X", "X", "O", "X"],
    ["X", "O", "O", "X", "O"],
    ["X", "O", "X", "O", "X"],
    ["O", "X", "O", "O", "O"],
    ["X", "X", "O", "X", "O"],
]
test5_out = [
    ['O', 'X', 'X', 'O', 'X'],
    ['X', 'X', 'X', 'X', 'O'],
    ['X', 'X', 'X', 'O', 'X'],
    ['O', 'X', 'O', 'O', 'O'],
    ['X', 'X', 'O', 'X', 'O'],
]
solve(test5)
assert test5_out == test5
