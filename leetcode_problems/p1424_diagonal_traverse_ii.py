# Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.
# Diagonal reading from bot_left -> top_right for every row.
# -----------------------
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i].length <= 10 ** 5
# 1 <= sum(nums[i].length) <= 10 ** 5
# 1 <= nums[i][j] <= 10 ** 5
from collections import defaultdict


def find_diagonal_order(nums: list[list[int]]) -> list[int]:
    # working_sol (94.91%, 55.53%) -> (758ms, 41.1mb)  time: O(n * m) | space: O(n * m)
    # {row + col: [diagonal values]}
    diags: dict[int, list[int]] = defaultdict(list)
    # If we go from top -> bottom, we will get values of ascending diagonal in reverse.
    # So, we can just go bottom -> top for correct order.
    for row in range(len(nums) - 1, -1, -1):
        for col in range(len(nums[row])):
            # All values on the same diagonal have equal sum of indexes == (row + col).
            diags[row + col].append(nums[row][col])
    out: list[int] = []
    for row in range(max(diags) + 1):
        out += diags[row]
    return out


# Time complexity: O(n * m + (n + (k - (n + len(nums[-1]) - 1))) <- 'n' - height of the input matrix 'nums',
#                                                                   'm' - average length of rows in the matrix 'nums',
#                                                                   'k' - max length of row in the 'nums'.
# Every row is always start of the diagonal, and we can't have empty row by constraints.
# They can be of a different size, but they will always have a starting value.
# So, every row is diagonal and extra to this diagonal we can have:
# [1, 2, 3]
# [1]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2]
# 4 basic diagonals for every row + 1 diagonal for last row extra values + 7 diagonals in the third row:
#   n + k - (n + len(nums[-1]) - 1) <- -1 for the first diagonal which included in 'n'.
# It will be dominated by traverse of the whole matrix, but it's still a search for max(diags).
# In every sum(diagonal) we store every value on this diagonal, so in the end we will always reuse same
# (n * m) values to add them into 'out'.
# So, something like: O(2 * (n * m) + (n + (k - (n + len(nums[-1]) - 1))).
# Worst case == we will have first column with length == 10 ** 3
# and every row except last one will have only One value, but last row will have length == 10 ** 2
# We will close constraints ! 1 <= sum(nums[i].length) <= 10 ** 5 ! and in this case we will have number of
# diagonals equal to number of values, so it's going to be: O(3 * (n * m)).
# So, I guess it's correct to just stick to O(n * m).
# -----------------------
# Auxiliary space: O(n * m + (n + (k - (n + len(nums[-1]) - 1))).
# For every diagonal we will have INT + all values of the diagonal in the list.
# Extra to this, 'out' will be an actual copy of all values of the input matrix 'nums':
#   O(2 * (n * m) + (n + (k - (n + len(nums[-1]) - 1))).


test: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test_out: list[int] = [1, 4, 2, 7, 5, 3, 8, 6, 9]
assert test_out == find_diagonal_order(test)

test = [[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]
test_out = [1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16]
assert test_out == find_diagonal_order(test)
