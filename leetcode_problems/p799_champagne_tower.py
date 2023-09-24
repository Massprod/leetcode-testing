# We stack glasses in a pyramid, where the first row has 1 glass,
#  the second row has 2 glasses, and so on until the 100th row.
# Each glass holds one cup of champagne.
# Then, some champagne is poured into the first glass at the top.
# When the topmost glass is full, any excess liquid poured will fall equally
#  to the glass immediately to the left and right of it.
# When those glasses become full, any excess champagne will fall equally to the left and right of those glasses,
#  and so on.
# (A glass at the bottom row has its excess champagne fall on the floor.)
# For example, after one cup of champagne is poured, the top most glass is full.
# After two cups of champagne are poured, the two glasses on the second row are half full.
# After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.
# After four cups of champagne are poured, the third row has the middle glass half full,
#  and the two outside glasses are a quarter full.
# Now after pouring some non-negative integer cups of champagne,
#  return how full the jth glass in the ith row is (both i and j are 0-indexed.)
# ---------------------
# 0 <= poured <= 10 ** 9
# 0 <= query_glass <= query_row < 100


def champagne_tower(poured: int, query_row: int, query_glass: int) -> float:
    # working_sol (86.89%, 90.79%) -> (78ms, 16.24mb)  time: O(n * n) | space: O(n * n)
    # row_number == cups on this row.
    tower: list[list[int]] = [[0 for _ in range(row)] for row in range(1, query_row + 2)]
    # Fill the first cup.
    tower[0][0] = poured
    for row in range(query_row):
        for cup in range(len(tower[row])):
            if tower[row][cup] > 1:
                # Fill the cup and equally split excess on both sides.
                excess: float = (tower[row][cup] - 1) / 2
                tower[row + 1][cup] += excess
                tower[row + 1][cup + 1] += excess
    # ! 0 <= poured <= 10 ** 9 ! <- constraints.
    # We're saving excess in a cup to use later, and its can be more than 1.
    # But cup itself only can fill a 1. So it's either 1 or lower to return.
    return min(1, tower[query_row][query_glass])


# Time complexity: O(n * n) -> creating tower with rows and cups == query_row * query_row, row_number == cups on row ->
# k - input value == query_glass^^| -> O(n * n) -> worst case: n = 99, k = 99 and 10 ** 9 poured =>
# n - input value == query_row^^| => traverse of (n * n) indexes to get this cup value => O(n * n).
# Auxiliary space: O(n * n) -> tower with n rows and n cups (row_number == cups on this row) => O(n * n).
# ---------------------
# What we care about? What's left after filling the cup, and where to place it.
# We fill the cup, and over limits will be split equally for right_left sides.
# Every cup == 1. over_limit == ((poured - 1) / 2)?
# But it's only for the first cup, what about others? Store in other cups?
# List with all cups and store what's left in them. Ok. How to place them?
# Every row == # of cups on this row.
# But we can't just place 100 cups on every row and use 50 index for first cup and -1 + 1 for right, left.
# Cuz then we need to use 200+ for last row.
# Place them on top of each other?
# Like:
# cup
# cup, cup
# cup, cup, cup
# [0][0] -> [1][0] <- left side.
# [0][0] -> [1][1] <- right side.
# [1][0] -> [2][0] + [2][1]
# [1][1] -> [2][1] + [2][2].
# Seems correct. Let's try.


test: int = 1
test_row: int = 1
test_glass: int = 1
test_out: float = 0.0
assert test_out == champagne_tower(test, test_row, test_glass)

test = 2
test_row = 1
test_glass = 1
test_out = 0.5
assert test_out == champagne_tower(test, test_row, test_glass)

test = 100000009
test_row = 33
test_glass = 17
test_out = 1.0
assert test_out == champagne_tower(test, test_row, test_glass)
