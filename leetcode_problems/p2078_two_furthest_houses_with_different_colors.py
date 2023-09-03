# There are n houses evenly lined up on the street, and each house is beautifully painted.
# You are given a 0-indexed integer array colors of length n,
#  where colors[i] represents the color of the ith house.
# Return the maximum distance between two houses with different colors.
# The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.
# -----------------
# n == colors.length
# 2 <= n <= 100
# 0 <= colors[i] <= 100
# Test data are generated such that at least two houses have different colors.


def max_distance(colors: list[int]) -> int:
    # working_sol (98.62%, 91.34%) -> (34ms, 16.12mb)  time: O(n) | space: O(1)
    max_dist: int = 0
    # Maximum distance possible is always from one of the sides.
    # So we can just check distances starting from each:
    for x in range(len(colors)):
        if colors[0] != colors[x]:
            # ! The distance between the ith and jth houses is abs(i - j) !
            max_dist = max(max_dist, abs(0 - x))
    for y in range(len(colors) - 2, -1, -1):
        if colors[-1] != colors[y]:
            # -1 for 0 indexing.
            max_dist = max(max_dist, abs(y - (len(colors) - 1)))
    return max_dist


# Time complexity: O(n) -> traversing whole input_array from 0 -> -1 and from -1 -> 0 => O(2n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> only One constant INT used, doesn't depend on input => O(1).


test: list[int] = [1, 1, 1, 6, 1, 1, 1]
test_out: int = 3
assert test_out == max_distance(test)

test = [1, 8, 3, 8, 3]
test_out = 4
assert test_out == max_distance(test)

test = [0, 1]
test_out = 1
assert test_out == max_distance(test)
