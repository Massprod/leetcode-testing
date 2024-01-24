# Given an integer array nums, return the third distinct maximum number in this array.
# If the third maximum does not exist, return the maximum number.
# -------------------
# 1 <= nums.length <= 10 ** 4
# -2 ** 31 <= nums[i] <= 2 ** 31 - 1
from random import randint


def third_max(nums: list[int]) -> int:
    # working_sol (85.06%, 85.57%) -> (49ms, 17.46mb)  time: O(n) | space: O(1)
    if len(nums) < 3:
        return max(nums)
    # We can have case with Third highest == (-2 ** 31), so we need lower to check if Third exist.
    # Or float('-inf'), but don't want to change annots.
    limit: int = -2 ** 31 - 1
    # [highest, second to highest, third to highest]
    out: list[int] = [limit] * 3
    for num in nums:
        # Found new highest -> change previous highest to second highest, and second to third.
        if out[0] < num:
            out[0], out[1], out[2] = num, out[0], out[1]
        # Found new second highest -> change previous second highest to third highest.
        elif out[1] < num < out[0]:
            out[1], out[2] = num, out[1]
        # Found new third highest -> just update it.
        elif out[2] < num < out[1]:
            out[2] = num
    # We can have all duplicates, then we only have Highest.
    # Or we can have Highest and Second to Highest, and no Third Highest.
    # So, we need to extra check if Third Highest exist, not equal to `limit` or w.e placeholder.
    return out[-1] if out[-1] != limit else out[0]


# Time complexity: O(n) <- n - length of input array `nums`.
# Single traverse of the whole input array `nums` => O(n).
# -------------------
# Auxiliary space: O(1).
# No matter the input size, we're always creating list `out` with 3 INTs inside => O(1).


test: list[int] = [3, 2, 1]
test_out: int = 1
assert test_out == third_max(test)

test = [1, 2]
test_out = 2
assert test_out == third_max(test)

test = [2, 2, 3, 1]
test_out = 1
assert test_out == third_max(test)

for _ in range(100):
    test = [randint(-2 ** 31, 2 ** 31 - 1) for _ in range(10 ** 4)]
    assert sorted(test)[-3] == third_max(test)
# print(test)
