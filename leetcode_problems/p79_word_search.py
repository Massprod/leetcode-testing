# Given an m x n grid of characters board and a string word,
# return true if word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once.
# -----------------------
# m == board.length  ,  n = board[i].length
# 1 <= m, n <= 6  ,  1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
# -----------------------
# Follow up: Could you use search pruning to make your solution faster with a larger board?


def exist(board: list[list[str]], word: str) -> bool:
    pass


test1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
test1_word = "ABCCED"
test1_out = True

test2 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
test2_word = "SEE"
test2_out = True

test3 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
test3_word = "ABCB"
test3_out = False
