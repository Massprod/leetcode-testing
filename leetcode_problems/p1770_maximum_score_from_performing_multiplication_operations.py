# You are given two 0-indexed integer arrays nums and multipliers of size n and m respectively,
#  where n >= m.
# You begin with a score of 0. You want to perform exactly m operations.
# On the ith operation (0-indexed) you will:
#   - Choose one integer x from either the start or the end of the array nums.
#   - Add multipliers[i] * x to your score.
#     - Note that multipliers[0] corresponds to the first operation, multipliers[1] to
#       the second operation, and so on.
#   - Remove x from nums.
# Return the maximum score after performing m operations.
# --------------------------------
# n == nums.length
# m == multipliers.length
# 1 <= m <= 300
# m <= n <= 10 ** 5
# -1000 <= nums[i], multipliers[i] <= 1000
from random import randint
from functools import cache


def maximum_score(nums: list[int], multipliers: list[int]) -> int:
    # working_sol (58.85%, 29.47%) -> (1031ms, 152.2mb)  time: O(m ** 2) | space: O(m ** 2)

    @cache
    def check(left: int, operation: int) -> int:
        # ! You want to perform exactly m operations !
        if operation == len(multipliers):
            return 0
        out: int = 0
        # Choose left side.
        left_side: int = nums[left] * multipliers[operation] + check(left + 1, operation + 1)
        # We know index of value we're taking from left side == `left`.
        # And we know number of operations we made so far == `operation`.
        # We can get index of right side value:
        #   (all ops made - ops we made on left side + 1) * -1, +1 to make 1-indexed in reverse negative.
        # OR len(nums) - 1 - (operation - left), if we don't use negative index (-1 to make 0-indexed).
        right: int = (operation - left + 1) * -1
        # Choose right side.
        right_side: int = nums[right] * multipliers[operation] + check(left, operation + 1)
        out += max(left_side, right_side)
        return out

    return check(0, 0)


# Time complexity: O(m ** 2) <- m - length of input array `multipliers`.
# We are caching every call and there's (left * available operations) states.
# And `available operations` == len(multipliers) - 1.
# Because ! 1 <= m <= 300 , m <= n <= 10 ** 5 !, left is bounded to m == 300 => O(m * m).
# --------------------------------
# Auxiliary space: O(m ** 2).
# We're caching every state, and there's (m * m) states => O(m * m).


test: list[int] = [1, 2, 3]
test_multipliers: list[int] = [3, 2, 1]
test_out: int = 14
assert test_out == maximum_score(test, test_multipliers)

test = [-5, -3, -3, -2, 7, 1]
test_multipliers = [-10, -5, 3, 4, 6]
test_out = 102
assert test_out == maximum_score(test, test_multipliers)

test = [randint(-1000, 1000) for _ in range(10 ** 4)]
test_multipliers = [randint(-1000, 1000) for _ in range(300)]
print(test, '\n\n', test_multipliers)
