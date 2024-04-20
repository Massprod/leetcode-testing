# You are given a 2D integer grid of size m x n and an integer x.
# In one operation, you can add x to or subtract x from any element in the grid.
# A uni-value grid is a grid where all the elements of it are equal.
# Return the minimum number of operations to make the grid uni-value.
# If it is not possible, return -1.
# ------------------
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10 ** 5
# 1 <= m * n <= 10 ** 5
# 1 <= x, grid[i][j] <= 10 ** 4
from random import randint


def min_operations(grid: list[list[int]], x: int) -> int:
    # working_sol (88.51%, 80.46%) -> (1150ms, 50.63mb)  time: O((n * m) * log(m * n)) | space: O(n * m)
    out: int = 0
    all_values: list[int] = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            all_values.append(grid[row][col])
    all_values.sort()
    median: int = all_values[len(all_values) // 2]
    for val in all_values:
        diff: int = abs(median - val)
        if diff % x:
            return -1
        out += diff // x
    return out


# Time complexity: O((n * m) * log(m * n)) <- n - rows of input matrix `grid`, m - columns of input matrix `grid`.
# Traversing whole input matrix `grid` once to get all the values from it => O(m * n).
# Sorting all the values => O((n * m) * log(m * n)).
# Extra traversing all these values to get our steps `out` => O(m * n).
# ------------------
# Auxiliary space: O(n * m)
# `all_values` will allocate space for every value from the `grid` => O(m * n).
# ------------------
# We will always use some value from the initial `grid`.
# Because we need to INCREASE or DECREASE some values.
# And w.e steps we make they all will collide at some point.
# Suppose we want to get all values to something BIGGER than everything else:
#  1, 2, 3, 4, 11-> 14 , x = 1
# step by step increase will lead us to the same number 14, and EVERY value will be here.
# But there's never a reason to make them something BIGGER than currently HIGHEST value in `grid`.
# Because if we need EVERYTHING to become this HIGHEST value, then our currently HIGHEST will need
#  to make these # of steps, and it's EQUAL of making BIGGER number into currently HIGHEST.
# 11 -> 14 = 3
# 14 -> 11 = 3
# So, if we can reach this BIGGER number from currently HIGHEST, then we should be able to reach
# currently HIGHEST from anything lower, because they will need to cover the same STEPS.
# If they can't, then our currently HIGHEST can't reach BIGGER as well.
# Knowing this, we can be sure about using some value from the `grid`.
# And in our case == min_steps, the best way is to use MEDIAN.
# Because we will get the Minimum number of steps to reach this value from LOWEST and HIGHEST.
# The Only question is how we deal with EVEN length.
# Do we even care? Like if we use the RIGHT value of median for even == `all_values(len()// 2)`,
#  then we still need to make 1 extra step to cover from the LEFT value == `all_values(len() // 2 - 1)`.
# And for ODD it's always one value == ``all_values(len() // 2)`.
# So, it's universal for both cases, because we will count this extra step(-s) between LEFT and RIGHT.


test: list[list[int]] = [[1, 5], [2, 3]]
test_x: int = 1
test_out: int = 5
assert test_out == min_operations(test, test_x)

test = [[1, 2], [3, 4]]
test_x = 2
test_out = -1
assert test_out == min_operations(test, test_x)

test = [[2, 4], [6, 8]]
test_x = 2
test_out = 4
assert test_out == min_operations(test, test_x)

test = [[randint(1, 10 ** 4) for _ in range(10 ** 2)] for _ in range(10 ** 2)]
print(test)
