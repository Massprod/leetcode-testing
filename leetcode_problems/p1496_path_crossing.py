# Given a string path, where path[i] = 'N', 'S', 'E' or 'W',
#  each representing moving one unit north, south, east, or west, respectively.
# You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
# Return true if the path crosses itself at any point, that is,
#  if at any time you are on a location you have previously visited.
# Return false otherwise.
# -------------------
# 1 <= path.length <= 10 ** 4
# path[i] is either 'N', 'S', 'E', or 'W'.
from random import choice


def is_path_crossing(path: str) -> bool:
    # working_sol (96.02%, 5.49%) -> (30ms, 17.53mb)  time: O(n) | space: O(n)
    dy: int
    dx: int
    # (y, x) coordinates
    visited: set[tuple[int, int]] = {(0, 0)}
    step_options: dict[str, tuple[int, int]] = {
        'N': (-1, 0),
        'E': (0, 1),
        'S': (1, 0),
        'W': (0, -1),
    }
    point: tuple[int, int] = (0, 0)
    for step in path:
        dy, dx = step_options[step]
        point = (point[0] + dy, point[1] + dx)
        if point in visited:
            return True
        visited.add(point)
    return False


# Time complexity: O(n) <- n - length of input string `path`.
# Single traverse of every index of `path` => O(n).
# Auxiliary space: O(n).
# Worst case: we don't have crossing, so we will add every step we make in `visited` => O(n).


test: str = "NES"
test_out: bool = False
assert test_out is is_path_crossing(test)

test = "NESWW"
test_out = True
assert test_out is is_path_crossing(test)

test = ''.join([choice(['N', 'E', 'S', 'W']) for _ in range(10 ** 4)])
print(test)
