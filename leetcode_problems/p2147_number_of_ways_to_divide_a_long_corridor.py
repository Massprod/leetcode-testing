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
from collections import Counter
from random import choice


def number_of_ways(corridor: str) -> int:
    # working_sol (14.28%, 71.43%) -> (643ms, 17.4mb)  time: O(n) | space: O(1)
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
    present: Counter[str, int] = Counter(corridor)
    # No seats at all.
    if 'S' not in present:
        return 0
    # No plants present, so we can only divide them by 2 seats with 1 option.
    if 'P' not in present or present['S'] == 2:
        return 1
    # ! each section has exactly two seats ! == always even number of 'seats'
    # Otherwise, we can't have correct slices.
    if present['S'] % 2:
        return 0
    # Everything below works, only if we already know that we have EVEN # of seats.
    out: int = 1
    index: int = 0
    limit: int = len(corridor) - 1
    seats: int = 0
    # If seats slice ends not on last index, we can place 1 divider and +1 divider for every plant.
    while index < limit:
        while index < limit:
            if corridor[index] == 'S':
                seats += 1
                if seats == 2:
                    break
            index += 1
        # We can only place divider after the two 'seats' slice.
        dividers: int = 1
        while index < limit:
            index += 1
            if corridor[index] == 'S':
                seats = 0
                out *= dividers
                break
            # And +1 for every plant between previous and next slices.
            dividers += 1
    return out % (10 ** 9 + 7)


# Time complexity: O(n) -> double traverse of original input string 'corridor' => O(2n).
# Auxiliary space: O(1) -> because we only have 2 symbol options, we're always allocating 2 symbols in Counter()
#                          and 1 INT for each of them, everything else is constant => O(1)
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
