# There is a robot starting at the position (0, 0), the origin, on a 2D plane.
# Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.
# You are given a string moves that represents the move sequence of the robot
#  where moves[i] represents its ith move.
# Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).
# Return true if the robot returns to the origin after it finishes all of its moves,
#  or false otherwise.
# Note: The way that the robot is "facing" is irrelevant.
# 'R' will always make the robot move to the right once,
#  'L' will always make it move left, etc.
# Also, assume that the magnitude of the robot's movement is the same for each move.
# -------------------------
# 1 <= moves.length <= 2 * 10 ** 4
# moves only contains the characters 'U', 'D', 'L' and 'R'.
from random import choice


def judge_circle(moves: str) -> bool:
    # working_sol (23.35%, 93.58%) -> (60ms, 16.45mb)  time: O(n) | space: O(1)
    # {move_type: (dy, dx)}
    move_changes: dict[str, tuple[int, int]] = {
        'U': (1, 0),
        'R': (0, 1),
        'L': (0, -1),
        'D': (-1, 0),
    }
    # (y, x)
    origin: tuple[int, int] = (0, 0)
    for move in moves:
        origin = origin[0] + move_changes[move][0], origin[1] + move_changes[move][1]
    return (0, 0) == origin


# Time complexity: O(n) <- n - length of the input string `moves`.
# Always traversing whole input string `moves`, once => O(n).
# -------------------------
# Auxiliary space: O(1)
# Everything is constant and doesn't depend on input => O(1).
# -------------------------
# We can also just count his move like: `U` == `D` AND `L` == `R`.
# Because if he moves in circle, he will need to have all of these as counterparts.


test: str = 'UD'
test_out: bool = True
assert test_out == judge_circle(test)

test = 'LL'
test_out = False
assert test_out == judge_circle(test)

test = ''.join([choice(['U', 'D', 'L', 'R']) for _ in range(2 * 10 ** 4)])
print(test)
