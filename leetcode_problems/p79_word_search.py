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
    path: list[tuple[int, int]] = []
    used_starts: dict = {}
    for n in range(len(board)):
        for m in range(len(board[0])):
            used_starts[(n, m)] = False

    def search_around(y: int, x: int, index: int, reverse: bool) -> bool:
        if index == len(word) or index < (len(word) * -1):
            return True
        to_find: str = word[index]
        point: int = 1
        if reverse:
            point = -1
        step: tuple[int, int] = (y - 1, x)
        if y > 0 and board[step[0]][step[1]] == to_find and (step not in path):
            if board[step[0]][step[1]] == word[0] and not used_starts[(step[0], step[1])]:
                used_starts[(step[0], step[1])] = True
                if search_around(step[0], step[1], 1, False):
                    return True
            if board[step[0]][step[1]] == word[-1] and not used_starts[(step[0], step[1])]:
                used_starts[(step[0], step[1])] = True
                if search_around(step[0], step[1], -2, True):
                    return True
            path.append(step)
            if search_around(step[0], step[1], index + point, reverse):
                return True
            path.pop()
        step = (y + 1, x)
        if y < (len(board) - 1) and board[step[0]][step[1]] == to_find and (step not in path):
            path.append(step)
            if search_around(step[0], step[1], index + point, reverse):
                return True
            path.pop()
        step = (y, x - 1)
        if x > 0 and board[step[0]][step[1]] == to_find and (step not in path):
            path.append(step)
            if search_around(step[0], step[1], index + point, reverse):
                return True
            path.pop()
        step = (y, x + 1)
        if x < (len(board[0]) - 1) and board[step[0]][step[1]] == to_find and (step not in path):
            path.append(step)
            if search_around(step[0], step[1], index + point, reverse):
                return True
            path.pop()

    for g in range(len(board)):
        for h in range(len(board[0])):
            if board[g][h] == word[0] and not used_starts[(g, h)]:
                path.append((g, h))
                if search_around(g, h, 1, False):
                    return True
                path.pop()
            if board[g][h] == word[0] and board[g][h] == word[-1] and not used_starts[(g, h)]:
                continue
            if board[g][h] == word[-1] and not used_starts[(g, h)]:
                path.append((g, h))
                if search_around(g, h, -2, True):
                    return True
                path.pop()
            used_starts[(g, h)] = True
    return False


# Can we count as adjacent cells most right to most left? like in test1 -> ES from 1 row and 2 row?
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
assert test1_out == exist(test1, test1_word)

test2 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
test2_word = "SEE"
test2_out = True
print(exist(test2, test2_word))
assert test2_out == exist(test2, test2_word)

test3 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
test3_word = "ABCB"
test3_out = False
print(exist(test3, test3_word))
assert test3_out == exist(test3, test3_word)

test4 = [["A", "B", "C", "D"], ["E", "F", "G", "H"], ["c", "c", "b", "a"]]
test4_word = "ccbaHDCGFBAE"
test4_out = True
print(exist(test4, test4_word))
assert test4_out == exist(test4, test4_word)

# test5 - failed -> I was using set to store used coordinates to exclude duplicate walks,
#                   and clearing after fully made 1 walk. But it overlapped with 4 ways walk, and some ways was just
#                   ignored, so we need to store it in ordered way and always delete step after failing this step.
test5 = [["A", "A", "a", "a", "A", "a"], ["a", "a", "a", "A", "A", "a"], ["A", "a", "A", "a", "a", "A"]]
test5_word = "AAaaAAaAaaAaAaA"
test5_out = True
print(exist(test5, test5_word))
assert test5_out == exist(test5, test5_word)

# test6 - failed -> time_limit fail not algorithm. How we can speed_this_up? 3979ms :)
test6 = [["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"],
         ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"]]
test6_word = "AAAAAAAAAAAAAAa"
test6_out = False
print(exist(test6, test6_word))
