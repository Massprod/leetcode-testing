# There exists an infinitely large two-dimensional grid of uncolored unit cells.
# You are given a positive integer n,
#  indicating that you must do the following routine for n minutes:
#  - At the first minute, color any arbitrary unit cell blue.
#  - Every minute thereafter, color blue every uncolored cell that touches a blue cell.
# Below is a pictorial representation of the state of the grid after minutes 1, 2, and 3.
# -----------------------
# 1 <= n <= 10 ** 5


def colored_cells(n: int) -> int:
    # working_sol (22.18%, 75.19%) -> (154ms, 17.68mb)  time: O(n) | space: O(1)
    # At least for the first 4 levels, we're always appending 4 colored cells.
    # Should be correct rule for every level...
    out: int = 1
    minute_append: int = 4
    while 1 != n:
        out += minute_append
        minute_append += 4
        n -= 1

    return out


# Time complexity: O(n)
# Always depleting `n` to zero => O(n).
# -----------------------
# Auxiliary space: O(1)


test: int = 1
test_out: int = 1
assert test_out == colored_cells(test)

test = 2
test_out = 5
assert test_out == colored_cells(test)
