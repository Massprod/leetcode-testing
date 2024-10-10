# There is an n x n grid, with the top-left cell at (0, 0) and the bottom-right cell at (n - 1, n - 1).
# You are given the integer n and an integer array startPos where startPos = [startrow, startcol]
#  indicates that a robot is initially at cell (startrow, startcol).
# You are also given a 0-indexed string s of length m where s[i] is the ith instruction for the robot:
#  'L' (move left), 'R' (move right), 'U' (move up), and 'D' (move down).
# The robot can begin executing from any ith instruction in s.
# It executes the instructions one by one towards the end of s
#  but it stops if either of these conditions is met:
#  - The next instruction will move the robot off the grid.
#  - There are no more instructions left to execute.
# Return an array answer of length m where answer[i] is the number of instructions the robot
#  can execute if the robot begins executing from the ith instruction in s.
# -----------------------
# m == s.length
# 1 <= n, m <= 500
# startPos.length == 2
# 0 <= startrow, startcol < n
# s consists of 'L', 'R', 'U', and 'D'.


def execute_instructions(n: int, startPos: list[int], s: str) -> list[int]:
    # working_sol (13.81%, 8.21%) -> (1120ms, 16.98mb)  time: O(s ** 2) | space: O(s)
    # { direction: (dy, dx) }
    moves: dict[str, tuple[int, int]] = {
        'U': (-1, 0),
        'L': (0, -1),
        'D': (1, 0),
        'R': (0, 1),
    }
    out: list[int] = []

    def dfs(start_row: int, start_col: int, instr_index: int) -> int:
        dy: int
        dx: int
        if instr_index == len(s):
            return 0
        dy, dx = moves[s[instr_index]]
        next_row: int = dy + start_row
        next_col: int = dx + start_col
        next_instr: int = instr_index + 1
        if 0 <= next_row < n and 0 <= next_col < n and next_instr <= len(s):
            return 1 + dfs(next_row, next_col, next_instr)
        return 0

    for index in range(len(s)):
        out.append(
            dfs(startPos[0], startPos[1], index)
        )
    return out


# Time complexity: O(s ** 2)
# In the worst case, all `s` is going to give us the correct sequences.
# We will traverse all `s` for each index => O(s * s).
# -----------------------
# Auxiliary space: O(s)
# `out` <- allocates space for each index of `s` => O(s).
# Recursion stack can be at max of `s` size => O(2 * s).


test_n: int = 3
test_start: list[int] = [0, 1]
test_s: str = "RRDDLU"
test_out: list[int] = [1, 5, 4, 3, 1, 0]
assert test_out == execute_instructions(test_n, test_start, test_s)

test_n = 2
test_start = [1, 1]
test_s = "LURD"
test_out = [4, 1, 0, 0]
assert test_out == execute_instructions(test_n, test_start, test_s)

test_n = 1
test_start = [0, 0]
test_s = "LRUD"
test_out = [0, 0, 0, 0]
assert test_out == execute_instructions(test_n, test_start, test_s)
