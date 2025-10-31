# You are given an m x n char matrix board representing the game board where:
#  - 'M' represents an unrevealed mine,
#  - 'E' represents an unrevealed empty square,
#  - 'B' represents a revealed blank square that has no adjacent mines
#    (i.e., above, below, left, right, and all 4 diagonals),
#  - digit ('1' to '8') represents how many mines are adjacent to this revealed square
#  - 'X' represents a revealed mine.
# You are also given an integer array click where click = [clickr, clickc] represents
#  the next click position among all the unrevealed squares ('M' or 'E').
# Return the board after revealing this position according to the following rules:
#  1. If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
#  2. If an empty square 'E' with no adjacent mines is revealed,
#   then change it to a revealed blank 'B' and all of its adjacent unrevealed squares
#   should be revealed recursively.
#  3. If an empty square 'E' with at least one adjacent mine is revealed,
#   then change it to a digit ('1' to '8') representing the number of adjacent mines.
#  4. Return the board when no more squares will be revealed.
# --- --- --- ---
# m == board.length
# n == board[i].length
# 1 <= m, n <= 50
# board[i][j] is either 'M', 'E', 'B', or a digit from '1' to '8'.
# click.length == 2
# 0 <= clickr < m
# 0 <= clickc < n
# board[clickr][clickc] is either 'M' or 'E'.
from collections import defaultdict


def update_board(
    board: list[list[str]],
    click: list[int],
) -> list[list[str]]:
    # working_solution: (5.02%, 9.04%) -> (43ms, 21.56mb)  Time: O(m * n) Space: O(m * n)
    U_MINE: str = 'M'
    R_MINE: str = 'X'

    # Check if it's game over.
    click_row, click_col = click
    if U_MINE == board[click_row][click_col]:
        board[click_row][click_col] = R_MINE
        return board
    U_EMPTY: str = 'E'
    R_EMPTY: str = 'B'

    # Otherwise we will need to reveal stuff.
    # Because, we guaranteed:
    # ! next click position among all the unrevealed squares ('M' or 'E') !
    # (dy, dx) -> [ top, topRight, right, botRight, bot, botLeft, left, topLeft]
    directions: list[tuple[int, int]] = [
        (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)
    ]

    # Instead of counting all the adjacent mines on the go.
    # It's better to just store the digits in the map to use.
    # We don't need all of the cells => dict.

    # { (row, col): count }
    adj_count: dict[tuple[int, int], int] = defaultdict(int)
    for row in range(len(board)):
        for col in range(len(board[0])):
            if U_MINE != board[row][col]:
                continue
            for dy, dx in directions:
                new_row, new_col = row + dy, col + dx
                if not (
                    0 <= new_row < len(board)
                    or
                    0 <= new_col < len(board[0])
                ):
                    continue
                adj_count[(new_row, new_col)] += 1
    # Now we can take these values in O(1), when we meet a bomb neighbour.
    visited: set[tuple[int, int]] = {(click_row, click_col)}

    def bfs(row: int, col: int) -> None:
        nonlocal visited, board, directions, adj_count

        mines_around: int = adj_count.get((row, col), 0)
        # Mark as a mine and stop.
        if 0 != mines_around:
            board[row][col] = str(mines_around)
            return
        # Otherwise continue revealing.
        board[row][col] = R_EMPTY
        for dy, dx in directions:
            new_row, new_col = row + dy, col + dx
            new_cell: tuple[int, int] = (new_row, new_col)
            if new_cell in visited:
                continue
            if not (
                0 <= new_row < len(board)
                and
                0 <= new_col < len(board[0])
            ):
                continue
            # We don't care about any cell, except Empty-Not-Revealed
            if U_EMPTY != board[new_row][new_col]:
                continue
            visited.add(new_cell)
            bfs(new_row, new_col)

    bfs(click_row, click_col)

    return board


# Time complexity: O(m * n) <- m - length of the input matrix `board`,
#                              n - height of the input matrix `board`.
# In the worst case, we have only `E` cells.
# First we traverse whole matrix to get `adj_count` => O(m * n).
# BFS will use every cell of the input matrix `board`, once => O(m * n).
# --- --- --- ---
# Space complexity: O(m * n)
# Same case.
# `visited` <- allocates space for 2 INT tuple for each cell => O(m * n).


test: list[list[str]] = [
    ["E", "E", "E", "E", "E"],
    ["E", "E", "M", "E", "E"],
    ["E", "E", "E", "E", "E"],
    ["E", "E", "E", "E", "E"]
]
test_click: list[int] = [3,0]
test_out: list[list[str]] = [
    ["B", "1", "E", "1", "B"],
    ["B", "1", "M", "1", "B"],
    ["B", "1", "1", "1", "B"],
    ["B", "B", "B", "B", "B"]
]
assert test_out == update_board(test, test_click)

test = [
    ["B", "1", "E", "1", "B"],
    ["B", "1", "M", "1", "B"],
    ["B", "1", "1", "1", "B"],
    ["B", "B", "B", "B", "B"]
]
test_click = [1,2]
test_out =[
    ["B", "1", "E", "1", "B"],
    ["B", "1", "X", "1", "B"],
    ["B", "1", "1", "1", "B"],
    ["B", "B", "B", "B", "B"]
]
assert test_out == update_board(test, test_click)
