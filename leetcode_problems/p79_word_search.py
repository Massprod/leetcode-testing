# Given an m x n grid of characters board and a string word,
#  return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells,
#  where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once.
# -----------------------
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
# -----------------------
# Follow up: Could you use search pruning to make your solution faster with a larger board?


def exist(board: list[list[str]], word: str) -> bool:
    # working_sol (90.65%, 78.87%) -> (1381ms, 16.2mb)  time: O(n * m + (m * n - 3) * 3 ** k)
    #                                                   space: O(m * n + (k - 1))
    max_x: int = len(board[0])
    max_y: int = len(board)
    # {symbol: # of occurrences}
    all_symbols: dict[str, int] = {}
    for row_ in range(max_y):
        for col_ in range(max_x):
            if board[row_][col_] in all_symbols:
                all_symbols[board[row_][col_]] += 1
            else:
                all_symbols[board[row_][col_]] = 1
    for symbol in word:
        # Symbol doesn't exist in matrix, we can't build 'word'.
        if symbol not in all_symbols:
            return False
        # Symbol is present, but there's not enough occurrences of him to build 'word'.
        if not all_symbols[symbol]:
            return False
        all_symbols[symbol] -= 1
    # Last index of reverse option.
    neg_limit: int = -len(word) - 1
    # (dy, dx) step options: top, right, bot, left.
    options: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def dfs(cell: tuple[int, int], index: int) -> bool:
        # We start DFS from both options: start -> end | end -> start.
        if index == len(word) or index == neg_limit:
            return True
        # Standard DFS
        row: int = cell[0]
        col: int = cell[1]
        # Mark as visited.
        restore: str = board[row][col]
        board[row][col] = ''
        for dy, dx in options:
            new_row: int = row + dy
            new_col: int = col + dx
            if 0 <= new_row < max_y and 0 <= new_col < max_x and board[new_row][new_col] == word[index]:
                if dfs((new_row, new_col), index + 1 if index >= 0 else index - 1):
                    return True
        board[row][col] = restore
        return False

    for row_ in range(max_y):
        for col_ in range(max_x):
            # If we can start from [0] symbol and reach end, then we can start from [-1] symbol
            #  and still get correct sequence of 'word'. So, we should start from either of them, but not both.
            if board[row_][col_] == word[0]:
                if dfs((row_, col_), 1):
                    return True
            elif board[row_][col_] == word[-1]:
                if dfs((row_, col_), -2):
                    return True
    return False


# Time complexity: O(n * m + (m * n - 3) * 3 ** k) <- n - height of input matrix 'board',
#                                                     m - length of input matrix 'board',
#                                                     k - length of input string 'word'.
# Worst case == we have all symbols present in matrix, but we can't build whole word last symbol is unreachable,
#  and we have first symbol on (m * n - 3 ) matrix cells, last symbol is w.e we can't reach it.
# ['A', 'E', 'A', 'A' ... 'A']  word = 'AAAA...AA' <- with len(word) == (m * n - 2).
# ['E', 'A', 'A', 'A' ... 'A']  So, we have all correct symbols, and will start DFS. But will never reach 'word'.
# ['A', 'A', 'A', 'A' ... 'A']
# [...]
# We will traverse full matrix => O(n * m).
# And start DFS on (m * n - 3) cells, and every DFS is going to be recursion with 3 options to turn and length of
#  recursion tree == k.
# O(n * m + (m * n - 3) * 3 ** k).
# -----------------------
# Auxiliary space: O(m * n + (k - 1))
# Dictionary with all symbols from 'board'. Worst case every symbol is unique => O(m * n).
# Marking visited cells without extra space, and recursion stack is at max == (k - 1).
# Because we're always starting DFS from second symbol or pre_last symbol.
# O(m * n + (k - 1)).


test: list[list[str]] = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
test_word: str = "ABCCED"
test_out: bool = True
assert test_out == exist(test, test_word)

test = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
test_word = "SEE"
test_out = True
assert test_out == exist(test, test_word)

test = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
test_word = "ABCB"
test_out = False
assert test_out == exist(test, test_word)

test = [["A", "B", "C", "D"], ["E", "F", "G", "H"], ["c", "c", "b", "a"]]
test_word = "ccbaHDCGFBAE"
test_out = True
assert test_out == exist(test, test_word)

test = [["A", "A", "a", "a", "A", "a"], ["a", "a", "a", "A", "A", "a"], ["A", "a", "A", "a", "a", "A"]]
test_word = "AAaaAAaAaaAaAaA"
test_out = True
assert test_out == exist(test, test_word)

test = [
    ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"],
]
test_word = "AAAAAAAAAAAAAAa"
test_out = False
assert test_out == exist(test, test_word)
