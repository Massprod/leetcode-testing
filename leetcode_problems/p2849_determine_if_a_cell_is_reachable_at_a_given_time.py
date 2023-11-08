# You are given four integers sx, sy, fx, fy, and a non-negative integer t.
# In an infinite 2D grid, you start at the cell (sx, sy).
# Each second, you must move to any of its adjacent cells.
# Return true if you can reach cell (fx, fy) after exactly t seconds, or false otherwise.
# A cell's adjacent cells are the 8 cells around it that share at least one corner with it.
# You can visit the same cell several times.
# ----------------------
# 1 <= sx, sy, fx, fy <= 10 **9
# 0 <= t <= 10 ** 9


def is_reachable(sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
    # working_sol (96.05%, 99.28%) -> (31ms, 16.06mb)  time: O(1) | space: O(1)
    # 2D board|grid and distance between cells with 8 directions to move.
    # Almost always Chebyshev distance => max(abs(sx - fx), abs(sy - fy)).
    # And because we're moving 1 cell per second: distance == time.
    distance: int = max(abs(sx - fx), abs(sy - fy))
    # Unique case: we can't return to the original cell with only 1 move.
    # And we're forced to move -> ! you must move to any of its adjacent cells !.
    if t == 1 and distance == 0:
        return False
    return distance <= t


# Time complexity: O(1) -> always the same calculations for correct input, doesn't depend on it => O(1).
# Auxiliary space: O(1) -> nothing depends on input, only 1 constant INT => O(1).


test_sx: int = 2
test_sy: int = 4
test_fx: int = 7
test_fy: int = 7
test_time: int = 6
test_out: bool = True
assert test_out is is_reachable(test_sx, test_sy, test_fx, test_fy, test_time)

test_sx = 3
test_sy = 1
test_fx = 7
test_fy = 3
test_time = 3
test_out = False
assert test_out is is_reachable(test_sx, test_sy, test_fx, test_fy, test_time)
