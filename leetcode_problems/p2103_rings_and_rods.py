# There are n rings and each ring is either red, green, or blue.
# The rings are distributed across ten rods labeled from 0 to 9.
# You are given a string rings of length 2n that describes the n rings that are placed onto the rods.
# Every two characters in rings forms a color-position pair that is used to describe each ring where:
#  - The first character of the ith pair denotes the ith ring's color ('R', 'G', 'B').
#  - The second character of the ith pair denotes the rod that the ith ring is placed on ('0' to '9').
# For example, "R3G2B1" describes n == 3 rings: a red ring placed onto the rod labeled 3,
#  a green ring placed onto the rod labeled 2, and a blue ring placed onto the rod labeled 1.
# Return the number of rods that have all three colors of rings on them.
# --------------------------
# rings.length == 2 * n
# 1 <= n <= 100
# rings[i] where i is even is either 'R', 'G', or 'B' (0-indexed).
# rings[i] where i is odd is a digit from '0' to '9' (0-indexed).
from collections import defaultdict


def count_points(rings: str) -> int:
    # working_sol (91.97%, 60.15%) -> (28ms, 16.46mb)  time: O(n) | space: O(n)
    # { rod: { unique_colors } }
    rods: dict[str, set[str]] = defaultdict(set)
    for index in range(1, len(rings), 2):
        rods[rings[index]].add(rings[index - 1])
    out: int = 0
    for rod, colors in rods.items():
        if 3 <= len(colors):
            out += 1
    return out




test: str = "B0B6G0R6R0R6G9"
test_out: int = 1
assert test_out == count_points(test)

test = "B0R0G0R9R0B0G0"
test_out = 1
assert test_out == count_points(test)

test = "G4"
test_out = 0
assert test_out == count_points(test)
