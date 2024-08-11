# You are given an array of integers nums.
# You are also given an integer original which is the first number that needs
#  to be searched for in nums.
# You then do the following steps:
#  1. If original is found in nums, multiply it by two (i.e., set original = 2 * original).
#  2. Otherwise, stop the process.
#  3. Repeat this process with the new number as long as you keep finding the number.
# Return the final value of original.
# -----------------------
# 1 <= nums.length <= 1000
# 1 <= nums[i], original <= 1000
from collections import Counter


def find_final_value(nums: list[int], original: int) -> int:
    # working_sol (59.57%, 23.54%) -> (59ms, 16.89mb)  time: O(n) | space: O(n)
    all_vals: dict[int, int] = Counter(nums)
    target: int = original
    while target in all_vals:
        target *= 2
    return target


# Time complexity: O(n) <- n - length of the input array `nums`.
# In the worst case, we're going to have every value after multiplying in `nums`.
# Traversing `nums`, once to get all the unique values => O(n).
# Traversing it again, because every value we multiply is going to be present => O(n + n - 1).
# -----------------------
# Auxiliary space: O(n)
# In the worst case, every value is unique.
# `all_vals` <- allocates space for every unique value from `nums` => O(n).


test: list[int] = [5, 3, 6, 1, 12]
test_original: int = 3
test_out: int = 24
assert test_out == find_final_value(test, test_original)

test = [2, 7, 9]
test_original = 4
test_out = 4
assert test_out == find_final_value(test, test_original)
