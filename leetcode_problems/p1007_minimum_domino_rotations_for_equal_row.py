# In a row of dominoes, tops[i] and bottoms[i] represent the top
#  and bottom halves of the ith domino.
# (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
# We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.
# Return the minimum number of rotations so that all the values in tops are the same,
#  or all the values in bottoms are the same.
# If it cannot be done, return -1.
# -------------------------
# 2 <= tops.length <= 2 * 10 ** 4
# bottoms.length == tops.length
# 1 <= tops[i], bottoms[i] <= 6


def min_domino_rotations(tops: list[int], bottoms: list[int]) -> int:
    # working_sol (76.58%, 66.24%) -> (31ms, 18.49mb)  time: O(n) | space: O(1)

    # If we need to make one of the rows equal.
    # We need to make EVERY value the same.
    # So, the First value of each row should be used.
    # But, in two ways, either top row values are equal to top[0] or bot[0].
    # Same logic for the bottom row.
    # Which means, all we have to do, is to check if we can get top row.
    # With values == top[0] or bot[0] and if we can't extra check bottom.
    # Easy, peasy.

    def check(main: list[int], diff: list[int], target: int) -> int:
        main_val: int
        diff_val: int
        switches: int = 0
        for index in range(len(main)):
            main_val, diff_val = main[index], diff[index]
            if main_val == target:
                continue
            elif diff_val == target:
                switches += 1
            else:
                return -1
            
        return switches

    limit: int = len(tops) + 3
    out: int = limit
    # Top with tops[0] values:
    check_switch: int = check(tops, bottoms, tops[0])
    out = min(out, check_switch) if check_switch != -1 else out
    # We can't have less than 0 switches => no reasons to continue.
    if 0 == out:
        return out
    # Top with bottoms[0] values:
    check_switch = check(tops, bottoms, bottoms[0])
    out = min(out, check_switch) if check_switch != -1 else out
    if 0 == out:
        return out
    # Bot with tops[0] values:
    check_switch = check(bottoms, tops, tops[0])
    out = min(out, check_switch) if check_switch != -1 else out
    if 0 == out:
        return out
    # Bot with bottoms[0] values:
    check_switch = check(bottoms, tops, bottoms[0])
    out = min(out, check_switch) if check_switch != -1 else out

    return out if out != limit else -1


# Time complexity: O(n) <- n - legth of the input arrays `tops` || `bottoms`.
# In the worst case we're going to check all 4 options.
# And for each option, we traverse all indexes, onces => O(4 * n).
# -------------------------
# Auxiliary space: O(1).
# Only constant values used, none of them depends on input => O(1).


test_top: list[int] = [2, 1, 2, 4, 2, 2]
test_bot: list[int] = [5, 2, 6, 2, 3, 2]
test_out: int = 2
assert test_out == min_domino_rotations(test_top, test_bot)

test_top = [3, 5, 1, 2, 3]
test_bot = [3, 6, 3, 3, 4]
test_out = -1
assert test_out == min_domino_rotations(test_top, test_bot)
