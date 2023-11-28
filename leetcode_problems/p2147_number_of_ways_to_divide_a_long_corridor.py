# Along a long library corridor, there is a line of seats and decorative plants.
# You are given a 0-indexed string corridor of length n consisting of letters 'S' and 'P'
#  where each 'S' represents a seat and each 'P' represents a plant.
# One room divider has already been installed to the left of index 0,
#  and another to the right of index n - 1.
# Additional room dividers can be installed.
# For each position between indices i - 1 and i (1 <= i <= n - 1), at most one divider can be installed.
# Divide the corridor into non-overlapping sections,
#  where each section has exactly two seats with any number of plants.
# There may be multiple ways to perform the division.
# Two ways are different if there is a position with a room divider installed
#  in the first way but not in the second way.
# Return the number of ways to divide the corridor.
# Since the answer may be very large, return it modulo 10 ** 9 + 7.
# If there is no way, return 0.
# --------------------
# n == corridor.length
# 1 <= n <= 10 ** 5
# corridor[i] is either 'S' or 'P'.
from random import choice


def number_of_ways(corridor: str) -> int:
    # working_sol (77.14%, 31.43%) -> (375ms, 21.2mb)  time: O(n) | space: O(n)
    seats: list[int] = [x for x in range(len(corridor)) if corridor[x] == 'S']
    out: int = 1
    # No seats at all.
    if not seats:
        return 0
    # There's ODD seats, we can't have correct slices.
    if len(seats) % 2:
        return 0
    # We only care about 2 seat slices.
    # So, we can just make double steps and get distance between them == plants between.
    # And we need to start from 2nd seat and end on pre-last seat.
    for x in range(1, len(seats) - 1, 2):
        # S S P P S => seats[0, 1, 4], we need part between slices.
        #    | | |  Last seat of 1st slice -> First seat of 2nd slice.
        out *= seats[x + 1] - seats[x]
    return out % (10 ** 9 + 7)


# Time complexity: O(n) -> traversing original string 'corridor' once to get all seats => O(n) ->
# n - len of input string 'corridor'^^| -> extra traverse with double step, using only half of indexes => O(n + n//2).
# Auxiliary space: O(n) -> worst case == there's only 'S' in 'corridor' -> we will recreate original string
#                          as array with INT for every symbol => O(n).
# --------------------
# 100% we can insta return with odd 'seats'. <-! each section has exactly two seats !
# But if I don't use Counter() it's better to just traverse and count plants on the way.
# Actually no, it's still using of every index to count, so it's irrelevant but Counter() is always faster.
# Tags: Math, DynamicProgramming.
# Do we need a recursion? Like all, we care is how many combinations of placements we have.
# We can only place divider after last seat of 2 seats in a row + after every plant between such 2 seats combos.
# Can we just calculate all combinations? 2 seats in a row + all plants before next combo == all_placements.
# And we can combine them with every other sequence of plants and correct 2 seats.
# Like: S S P S S P P S S P P
#          | |   | | |
# 1st ->   |     |
#          |       |
#          |         |
# 2nd ->     |   |
#            |     |
#            |       |
# 3 combinations == 1 * 3
# 2nd ->     | start from 2nd divider and repeat everything
# 3 combinations == 1 * 3
# So, we can just use 'all' divider placements we have and multiply them.
# 6 combinations in total == 2 * 3 == 6
# Should be correct.
# --------------------
# Ok. What we essentially doing?
# First -> we need to know if we have EVEN seats or not.
# Second -> we're trying to find how many plants we have between every double SEAT slices.
# Can we just find every SEAT position and then just take distance between them as # of PLANTS?
# Let's try.


test: str = "SSPPSPS"
test_out: int = 3
assert test_out == number_of_ways(test)

test = "PPSPSP"
test_out = 1
assert test_out == number_of_ways(test)

test = "s"
test_out = 0
assert test_out == number_of_ways(test)

test = "PPPPPPSSPPSPSPPPPPPPPPP"
test_out = 3
assert test_out == number_of_ways(test)

test = "SSSSSSSSSSSSSSSSPP"
test_out = 1
assert test_out == number_of_ways(test)

test = ''
for _ in range(10 ** 5):
    test += choice(['S', 'P'])
print(test)
