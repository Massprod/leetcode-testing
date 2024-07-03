# You are given an integer array nums.
# In one move, you can choose one element of nums and change it to any value.
# Return the minimum difference between the largest
#  and smallest value of nums after performing at most three moves.
# -----------------------------
# 1 <= nums.length <= 10 ** 5
# -10 ** 9 <= nums[i] <= 10 ** 9
from random import randint


def min_difference(nums: list[int]) -> int:
    # working_sol (71.93%, 98.59%) -> (274ms, 27.16mb)  time: O(n * log n) | space: O(n)
    # W.e we can always make 3/4 elements equal to element 4.
    if 4 >= len(nums):
        return 0
    nums.sort()
    out: int | float = float('inf')
    # We can only change 3 elements, on both sides.
    # Deletions:
    # 0_left == 3_right
    # 1_left == 2_right
    # 2_left == 1_right
    # 3_left == 0_right.
    # Even if they have the same values, we still need to change w.e was before them.
    # So, it's only valid options to do them like this.
    for left_l in range(4):
        right_l: int = len(nums) - 4 + left_l
        out = min(out, nums[right_l] - nums[left_l])
    return out


# Time complexity: O(n * log n) <- n - length of the input array `nums`.
# Always sorting the input array with built_in `sort` => O(n * log n)
# -----------------------------
# Auxiliary space: O(n)
# `sort` takes O(n).


test: list[int] = [5, 3, 2, 4]
test_out: int = 0
assert test_out == min_difference(test)

test = [1, 5, 0, 10, 14]
test_out = 1
assert test_out == min_difference(test)

test = [3, 100, 20]
test_out = 0
assert test_out == min_difference(test)

test = [1, 5, 6, 14, 15]
test_out = 1
assert test_out == min_difference(test)

test = [randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 3)]
print(test)
