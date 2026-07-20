# You are given two integer arrays start and target, where each array is of the form [x, y]
#  representing a cell on a standard 8 x 8 chessboard.
# Return true if a knight can move from start to target in an even number of moves.
# Otherwise, return false.
# Note: A valid knight move consists of moving two squares in one direction
#  and one square perpendicular to it.
# The figure below illustrates all eight possible moves from a cell.
# --- --- --- ---
# start.length == target.length == 2
# 0 <= start[i], target[i] <= 7


def can_reach(start: list[int], target: list[int]) -> bool:
    # working_solution: (100%, 50%) -> (0ms, 19.27mb)  Time: O(1) Space: O(1)
    # 1. Knight able to reach any cell of the board. Otherwise you can't win.
    # 2. Every knight move is switch of the colour.
    # 3. (x + y) - even -> black | odd -> white
    # No matter the colour we start, but we can only land on the same colour.
    # If we make odd steps. So, start from one -> land on the same == even.
    # 0 - black | 1 - white
    colour_1: int = sum(start) % 2
    colour_2: int = sum(target) % 2
    return colour_1 == colour_2


# Time complexity: O(1)
# --- --- --- ---
# Space complexity: O(1)


test_start: list[int] = [1, 1]
test_target: list[int] = [2, 2]
test_out: bool = True
assert test_out == can_reach(test_start, test_target)

test_start = [4, 5]
test_target = [6, 6]
test_out = False
assert test_out == can_reach(test_start, test_target)
