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
    path: set = set()

    def search_around(y: int, x: int, index: int, reverse: bool) -> bool:
        if index == len(word) or index < (len(word) * -1):
            return True
        to_find: str = word[index]
        point: int = 1
        if reverse:
            index = len(word) + index
            point = -1
        step: tuple[int, int] = (y - 1, x)
        if y > 0 and board[step[0]][step[1]] == to_find and (step not in path):
            path.add(step)
            if search_around(step[0], step[1], index + point, reverse):
                return True
        step = (y + 1, x)
        if y < (len(board) - 1) and board[step[0]][step[1]] == to_find and (step not in path):
            path.add(step)
            if search_around(step[0], step[1], index + point, reverse):
                return True
        step = (y, x - 1)
        if x > 0 and board[step[0]][step[1]] == to_find and (step not in path):
            path.add(step)
            if search_around(step[0], step[1], index + point, reverse):
                return True
        step = (y, x + 1)
        if x < (len(board[0]) - 1) and board[step[0]][step[1]] == to_find and (step not in path):
            path.add(step)
            if search_around(step[0], step[1], index + point, reverse):
                return True

    for g in range(len(board)):
        for h in range(len(board[0])):
            if board[g][h] == word[0]:
                path.add((g, h))
                if search_around(g, h, 1, False):
                    return True
                path.clear()
            if board[g][h] == word[0] and board[g][h] == word[-1]:
                continue
            if board[g][h] == word[-1]:
                path.add((g, h))
                if search_around(g, h, -2, True):
                    return True
                path.clear()
    return False


# ------------------------
#  ! pruning to make your solution faster !
#  What we can prune? Cuz I want to create a solution which going to stop at 0 and -1 indexes and check
#  every symbol on 4 cells around and made a recursion of it, until we reach correct length and word.
#  We can't delete anything in this case, cuz we're obliged to check every start and end.
#  W.e let's make it work for a start.


test1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
test1_word = "ABCCED"
test1_out = True
print(exist(test1, test1_word))

test2 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
test2_word = "SEE"
test2_out = True
print(exist(test2, test2_word))

test3 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
test3_word = "ABCB"
test3_out = False
print(exist(test3, test3_word))

