# You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.')
#  and walls (represented as '+').
# You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol]
#  denotes the row and column of the cell you are initially standing at.
# In one step, you can move one cell up, down, left, or right.
# You cannot step into a cell with a wall, and you cannot step outside the maze.
# Your goal is to find the nearest exit from the entrance.
# An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.
# Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.
# -------------------
# maze.length == m
# maze[i].length == n
# 1 <= m, n <= 100
# maze[i][j] is either '.' or '+'.
# entrance.length == 2
# 0 <= entrancerow < m
# 0 <= entrancecol < n
# entrance will always be an empty cell.
from collections import deque


def nearest_exit(maze: list[list[str]], entrance: list[int]) -> int:
    # working_sol (100%, 81.35%) -> (688ms, 16.9mb)  time: O(log(m * n) | space: O(log(m * n))
    found: bool = False
    row: int = len(maze[0])
    col: int = len(maze)
    # We don't care about entrance, so it's better to cull IF checks.
    maze[entrance[0]][entrance[1]] = '-'
    # Maybe rebuild this later, as extra function
    #  with switching x, y inputs. But I need working version first.
    # Check for correct exits:
    # First row.
    y_: int = 0
    for x_ in range(row):
        if maze[y_][x_] == '.':
            found = True
    # Last row.
    y_ = col - 1
    if not found:
        for x_ in range(row):
            if maze[y_][x_] == '.':
                found = True
    # First column.
    x_: int = 0
    if not found:
        for y_ in range(col):
            if maze[y_][x_] == '.':
                found = True
    # Last column.
    x_ = row - 1
    if not found:
        for y_ in range(col):
            if maze[y_][x_] == '.':
                found = True
    # If there's no empty cells on matrix border,
    #  then there's no existing Exits.
    if not found:
        return -1
    # Standard BFS with delimiter.
    steps_que: deque[tuple[int, int] | None] = deque()
    steps_que.append((entrance[0], entrance[1]))
    steps_que.appendleft(None)
    distance: int = 0
    while any(steps_que):
        cur_cell: tuple[int, int] = steps_que.pop()
        # Every new round, increment distance
        #  and mark end of this round.
        if cur_cell is None:
            distance += 1
            steps_que.appendleft(None)
            continue
        y: int = cur_cell[0]
        x: int = cur_cell[1]
        if [y, x] != entrance:
            # First or Last row, X doesn't matter.
            if y == 0 or y == col - 1:
                return distance
            # First or Last col, Y doesn't matter.
            if x == 0 or x == row - 1:
                return distance
        # Check every neighbour cell we can step into ->
        if col > y + 1:
            # -> if we can step in it, try to use it later.
            if maze[y + 1][x] == '.':
                steps_que.appendleft((y + 1, x))
                # '-' <- used cell.
                maze[y + 1][x] = '-'
        if 0 <= y - 1:
            if maze[y - 1][x] == '.':
                steps_que.appendleft((y - 1, x))
                maze[y - 1][x] = '-'
        if row > x + 1:
            if maze[y][x + 1] == '.':
                steps_que.appendleft((y, x + 1))
                maze[y][x + 1] = '-'
        if 0 <= x - 1:
            if maze[y][x - 1] == '.':
                steps_que.appendleft((y, x - 1))
                maze[y][x - 1] = '-'
    # Exit exist, but unreachable.
    return -1


# Time complexity: O(log(m * n)) -> traversing borders, worst case exit on last index of last column => O(2m + 2n) ->
# m - row of input_matrix^^| -> using every empty cell we can reach in BFS => O(log (m * n)) ->
# n - col of input_matrix^^| -> it's always some part of the matrix, even if we have all cells == empty,
#                            we still will leave some of them unchecked.
# Auxiliary space: O(log(m * n)) -> worst case everything empty, every index will be used but only part of them
#                                will be stored into a step_que at any given time => O(log(m * n).
#                                Even with 2 indexes, still only 1 will be added into a que and insta return.
# -------------------
# Marked as BFS problem, so we just need to check everything from the entrance in rounds|steps.
# And for every round change distance, so it's like RottenOranges but with search of any BorderCell.
# No way to test it locally, at least Fast. Cuz they don't allow single_quotes for a string on Leetcode...
# And I don't know how to change console out in pycharm to double_quotes, let's fail and see it's faster.
# Well, didn't failed :)


test: list[list[str]] = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
test_ent: list[int] = [1, 2]
test_out: int = 1
assert test_out == nearest_exit(test, test_ent)

test = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
test_ent = [1, 0]
test_out = 2
assert test_out == nearest_exit(test, test_ent)

test = [[".", "+"]]
test_ent = [0, 0]
test_out = -1
assert test_out == nearest_exit(test, test_ent)
