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
    # working_sol (80.82%, 8.37%) -> (2712ms, 16.9mb)  time: O( ) | space: O( )
    path: list[tuple[int, int]] = []
    used_starts: dict = {}
    correct_matrix: dict = {}
    for n in range(len(board)):
        for m in range(len(board[0])):
            used_starts[(n, m)] = False
            correct_matrix[board[n][m]] = True

    for _ in word:
        if _ not in correct_matrix:
            return False

    def search_around(y: int, x: int, index: int, reverse: bool, inside_path: list[tuple[int, int]]) -> bool:
        if index == len(word) or index < (len(word) * -1):
            return True
        to_find: str = word[index]
        point: int = 1
        if reverse:
            point = -1
        step: tuple[int, int] = (y - 1, x)
        if y > 0 and board[step[0]][step[1]] == to_find and (step not in inside_path):
            if board[step[0]][step[1]] == word[0] and not used_starts[(step[0], step[1])]:
                used_starts[(step[0], step[1])] = True
                if search_around(step[0], step[1], 1, False, [(step[0], step[1])]):
                    return True
            if board[step[0]][step[1]] == word[-1] and not used_starts[(step[0], step[1])]:
                used_starts[(step[0], step[1])] = True
                if search_around(step[0], step[1], -2, True, [(step[0], step[1])]):
                    return True
            inside_path.append(step)
            if search_around(step[0], step[1], index + point, reverse, inside_path):
                return True
            inside_path.pop()
        step = (y + 1, x)
        if y < (len(board) - 1) and board[step[0]][step[1]] == to_find and (step not in inside_path):
            if board[step[0]][step[1]] == word[0] and not used_starts[(step[0], step[1])]:
                used_starts[(step[0], step[1])] = True
                if search_around(step[0], step[1], 1, False, [(step[0], step[1])]):
                    return True
            if board[step[0]][step[1]] == word[-1] and not used_starts[(step[0], step[1])]:
                used_starts[(step[0], step[1])] = True
                if search_around(step[0], step[1], -2, True, [(step[0], step[1])]):
                    return True
            inside_path.append(step)
            if search_around(step[0], step[1], index + point, reverse, inside_path):
                return True
            inside_path.pop()
        step = (y, x - 1)
        if x > 0 and board[step[0]][step[1]] == to_find and (step not in inside_path):
            if board[step[0]][step[1]] == word[0] and not used_starts[(step[0], step[1])]:
                used_starts[(step[0], step[1])] = True
                if search_around(step[0], step[1], 1, False, [(step[0], step[1])]):
                    return True
            if board[step[0]][step[1]] == word[-1] and not used_starts[(step[0], step[1])]:
                used_starts[(step[0], step[1])] = True
                if search_around(step[0], step[1], -2, True, [(step[0], step[1])]):
                    return True
            inside_path.append(step)
            if search_around(step[0], step[1], index + point, reverse, inside_path):
                return True
            inside_path.pop()
        step = (y, x + 1)
        if x < (len(board[0]) - 1) and board[step[0]][step[1]] == to_find and (step not in inside_path):
            if board[step[0]][step[1]] == word[0] and not used_starts[(step[0], step[1])]:
                used_starts[(step[0], step[1])] = True
                if search_around(step[0], step[1], 1, False, [(step[0], step[1])]):
                    return True
            if board[step[0]][step[1]] == word[-1] and not used_starts[(step[0], step[1])]:
                used_starts[(step[0], step[1])] = True
                if search_around(step[0], step[1], -2, True, [(step[0], step[1])]):
                    return True
            inside_path.append(step)
            if search_around(step[0], step[1], index + point, reverse, inside_path):
                return True
            inside_path.pop()

    for g in range(len(board)):
        for h in range(len(board[0])):
            if board[g][h] == word[0] and not used_starts[(g, h)]:
                path.append((g, h))
                if search_around(g, h, 1, False, path):
                    return True
                path.pop()
            if board[g][h] == word[0] and board[g][h] == word[-1] and not used_starts[(g, h)]:
                continue
            if board[g][h] == word[-1] and not used_starts[(g, h)]:
                path.append((g, h))
                if search_around(g, h, -2, True, path):
                    return True
                path.pop()
            used_starts[(g, h)] = True
    return False




# Totally need to be polished, really hard to read_solution. Maybe I will revisit and rebuild later.
# ------------------------
# Yep. Totally not my fault with failing time_limit, I even make it better, and now we're checking
# every starting and ending symbols in word along the standard search, maybe it's actually slower with these checks.
# But it's still not passable without checking correct matrix. I will leave it with extra checks, just why not.
# With checking correct matrix both hits time_limit. 2712ms with checks -> 2127 without.
# But it's good to have extra experience and actually made it work, might be useful in a future.
# ------------------------
# Bruh. Literally took a complete solution with this trick and deleted trick_part.
# And it 5161ms, when mine is 4000...
# Guess it's just a test_case to check my understanding of input. If input isn't correct from the start,
# and we can save time without running algorithm for incorrect inputs.
# ------------------------
# Wtf with this time_limit, even after googling and checking ready_solution, there's *correct* solutions with 2500ms.
# My 4000 not so bad in compare. I even made check of starting positions along the way.
# Obviously I could make a trick to just skip test_cases, if count of symbols from word isn't presented in matrix.
# But it's stupid to make time_limit based on this.
# ------------------------
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
assert test6_out == exist(test6, test6_word)
