# You are given an n x n integer matrix board where the cells are labeled from 1 to n ** 2
#  in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0])
#  and alternating direction each row.
# You start on square 1 of the board.
# In each move, starting from square curr, do the following:
#  - Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n ** 2)].
#    This choice simulates the result of a standard 6-sided die roll: i.e.,
#     there are always at most 6 destinations, regardless of the size of the board.
#  - If next has a snake or ladder, you must move to the destination of that snake or ladder.
#    Otherwise, you move to next.
#  - The game ends when you reach the square n ** 2.
# A board square on row r and column c has a snake or ladder if board[r][c] != -1.
# The destination of that snake or ladder is board[r][c].
# Squares 1 and n ** 2 do not have a snake or ladder.
# Note that you only take a snake or ladder at most once per move.
# If the destination to a snake or ladder is the start of another snake or ladder,
#  you do not follow the subsequent snake or ladder.
# For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2.
# You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
# Return the least number of moves required to reach the square n ** 2.
# If it is not possible to reach the square, return -1.
# --------------------
# n == board.length == board[i].length
# 2 <= n <= 20
# board[i][j] is either -1 or in the range [1, n ** 2].
# The squares labeled 1 and n2 do not have any ladders or snakes.
from collections import deque


def snakes_and_ladders(board: list[list[int]]) -> int:
    # working_sol (94.51%, 87.62%) -> (97ms, 16.27mb)  time: O(m * n) | space: O(m * n)
    # There's only 2 options, either snake|ladder we MUST travel,
    #  or [cell + 1, min(cell + 6, len(board) ** 2)] options.
    # So, it's simple directed Nodes from 1 -> len(board) ** 2.
    graph: dict[int, int] = {}
    cell: int = 1
    row_reverse: bool = False
    for y in range(len(board) - 1, -1, -1):
        # ! alternating direction each row ! <- starts with: left -> right.
        if row_reverse:
            for x in range(len(board[0]) - 1, -1, -1):
                graph[cell] = board[y][x]
                cell += 1
        else:
            for x in range(len(board[0])):
                graph[cell] = board[y][x]
                cell += 1
        row_reverse = not row_reverse
    # Most important part:
    # ! If 'next' has a snake or ladder, you must move to the destination of that snake or ladder !
    # But, if we're already standing on snake|ladder after previous snake|ladder, we can ignore it.
    # And choose standard 6-step options.
    # Standard BFS with delimiter.
    que: deque[int | None] = deque([1, None])
    moves: int = 0
    visited: set[int] = set()
    max_cell: int = len(board) ** 2
    while que:
        cell = que.popleft()
        if not cell:
            if que:
                que.append(None)
            moves += 1
            continue
        if cell in visited:
            continue
        visited.add(cell)
        # ! [curr + 1, min(curr + 6, n ** 2)] !
        for new_cell in range(cell + 1, cell + 7):
            if new_cell > max_cell:
                break
            # We can make step from this cell in the next round and get to the end.
            elif new_cell == max_cell or graph[new_cell] == max_cell:
                moves += 1
                return moves
            # Simple cell without ladder|snake.
            elif graph[new_cell] < 0:
                que.append(new_cell)
            # Ladder|snake => we forced to move into cell it points.
            else:
                que.append(graph[new_cell])
    return -1


# Time complexity: O(m * n) -> traversing whole matrix to get Nodes and their directions => O(m * n) ->
# m - length of input matrix 'board'^^| -> BFS from bot_left_corner and in the worst case == everything is '-1' ->
# n - height of input matrix 'board'^^| -> we will add every Node(cell) into a que and check it, except last 5 Nodes ->
#                                       -> because we're always check if we can reach end from step options =>
#                                       => O((m * n) - 5), but we don't care about constants => O(m * n).
# --------------------
# Auxiliary space: O(m * n) -> always creating dictionary with size of (m * n), key == int, value == int => O(m * n) ->
#                           -> extra que with all Nodes allocated => O(2 * (m * n)) ->
#                           -> worst case == n ** 2 Node is unreachable -> visited will hold (m * n) - 1 Nodes =>
#                           => O(3 * (m * n)).
#                           Otherwise, we will ignore last Nodes in a que and return with (moves + 1) => O(log(m * n)).
# --------------------
# Build directed graph with all cells from 1 -> n ** 2 and BFS from 1 cell?
# Should be correct.
# Not really a graph, but separated Nodes.
# Failed a lot of commits, because I was thinking that we cannot skip snakes and ladders.
# So, when we forced to move from One snake to another we should take but count as 2 steps.
# In reality, we should just ignore second snake and just take any of 6 options from it.
# ! If 'next' has a snake or ladder, you must move to the destination of that snake or ladder !
#        ^^This is the most important part of description, and I missed it.
#          Because after we move 'next' is NOT this cell, but ! [cell + 1, min(cell + 6, n ** 2)] !


test: list[list[int]] = [
    [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1],
    [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1],
]
test_out: int = 4
assert test_out == snakes_and_ladders(test)

test = [[-1, -1], [-1, 3]]
test_out = 1
assert test_out == snakes_and_ladders(test)

test = [
    [-1, 10, 10, 10, 10, 10], [10, 10, 10, 10, -1, 10], [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1],
]
test_out = -1
assert test_out == snakes_and_ladders(test)

test = [[-1, -1, -1], [-1, 9, 8], [-1, 8, 9]]
test_out = 1
assert test_out == snakes_and_ladders(test)

test = [
    [-1, -1, -1, 46, 47, -1, -1, -1], [51, -1, -1, 63, -1, 31, 21, -1], [-1, -1, 26, -1, -1, 38, -1, -1],
    [-1, -1, 11, -1, 14, 23, 56, 57], [11, -1, -1, -1, 49, 36, -1, 48], [-1, -1, -1, 33, 56, -1, 57, 21],
    [-1, -1, -1, -1, -1, -1, 2, -1], [-1, -1, -1, 8, 3, -1, 6, 56],
]
test_out = 4
assert test_out == snakes_and_ladders(test)

test = [[-1, 1, 1, 1], [-1, 7, 1, 1], [16, 1, 1, 1], [-1, 1, 9, 1]]
test_out = 3
assert test_out == snakes_and_ladders(test)
