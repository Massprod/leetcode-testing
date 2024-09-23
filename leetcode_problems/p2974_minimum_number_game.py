# You are given a 0-indexed integer array nums of even length and there is also an empty array arr.
# Alice and Bob decided to play a game where in every round Alice and Bob will do one move.
# The rules of the game are as follows:
#  - Every round, first Alice will remove the minimum element from nums, and then Bob does the same.
#  - Now, first Bob will append the removed element in the array arr, and then Alice does the same.
#  - The game continues until nums becomes empty.
# Return the resulting array arr.
# ------------------------
# 2 <= nums.length <= 100
# 1 <= nums[i] <= 100
# nums.length % 2 == 0
from random import randint


def number_game(nums: list[int]) -> list[int]:
    # working_sol (80.52%, 34.06%) -> (48ms, 16.64mb)  time: O(n * log n) | space: O(n)
    alice: int
    bob: int
    nums.sort()
    out: list[int] = []
    for index in range(1, len(nums), 2):
        alice = nums[index - 1]
        bob = nums[index]
        out += [bob] + [alice]
    return out


# Time complexity: O(n * log n) <- n - length of the input array `nums`.
# Always sorting `nums` to get correct order => O(n * log n).
# Extra traversing every index of `nums`, once => O((n * log n) + n).
# ------------------------
# Auxiliary space: O(n)
# `sort` <- takes O(n) by itself => O(n).
# `out` <- always of the same size as `nums` => O(2 * n).


test: list[int] = [5, 4, 2, 3]
test_out: list[int] = [3, 2, 5, 4]
assert test_out == number_game(test)

test = [2, 5]
test_out = [5, 2]
assert test_out == number_game(test)

test = [randint(1, 100) for _ in range(100)]
print(test)
