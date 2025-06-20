# You are given a string s consisting of the characters 'N', 'S', 'E', and 'W',
#  where s[i] indicates movements in an infinite grid:
#  - 'N' : Move north by 1 unit.
#  - 'S' : Move south by 1 unit.
#  - 'E' : Move east by 1 unit.
#  - 'W' : Move west by 1 unit.
# Initially, you are at the origin (0, 0).
# You can change at most k characters to any of the four directions.
# Find the maximum Manhattan distance from the origin that can be achieved
#  at any time while performing the movements in order.
# The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.
# ---------------------------
# 1 <= s.length <= 10 ** 5
# 0 <= k <= s.length
# s consists of only 'N', 'S', 'E', and 'W'.
from random import choice

from pyperclip import copy


def max_distance(s: str, k: int) -> int:
    # working_sol (85.16%, 37.50%) -> (2317ms, 18.12mb)  time: O(n) | space: O(1)
    # |sumN - sumS| + |sumE - sumW| <- Manhattan distance at any moment.
    # If we want to add shifts => we can use (`shifts` * 2) as an extra value.
    # `shifts` <- changes we can make to any of the direction.
    # We need these as `*2` because the best option is to increase one by `shifts`
    #  and decrease by `shifts` => (`shifts` * 2)
    # (|sumN - sumS| + shifts * 2) + (|sumE - sumW| + shifts * 2)
    out: int = 0
    # [north, south, west, east]
    directions: list[int] = [0, 0, 0, 0]
    dir_maps: dict[str, int] = {
        'N': 0,
        'S': 1,
        'E': 2,
        'W': 3
    }
    for step in s:
        directions[dir_maps[step]] += 1
        # We can make at most `k` shifts to any of the direction.
        # (`shifts` * 2) < (2 * `k`) <-- should stand
        ns_shifts: int = min(
            directions[0], directions[1], k
        )
        # We already shift `ns` => we can use what's left `k - ns_shifts`.
        ew_shifts: int = min(
            directions[2], directions[3], k - ns_shifts
        )
        ns_steps: int = abs(directions[0] - directions[1]) + ns_shifts * 2
        ew_steps: int = abs(directions[2] - directions[3]) + ew_shifts * 2
        # (ns_steps + ew_steps) == Manhattan distance
        out = max(out, ns_steps + ew_steps)
    
    return out


# Time complexity: O(n)
# Always traversing whole input string `s`, once => O(n).
# ---------------------------
# Auxiliary space: O(1)
# Nothing extra is used, everything is contant => O(1).


test: str = "NWSE"
test_k: int = 1
test_out: int = 3
assert test_out == max_distance(test, test_k)

test = "NSWWEW"
test_k = 3
test_out = 6
assert test_out == max_distance(test, test_k)

test = ''.join([choice('NSWE') for _ in range(10 ** 5)])
copy(test)
