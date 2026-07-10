# You are given an integer array nums of odd length n.
# Return true if the middle element of nums appears exactly once in the array.
# Otherwise return false.
# --- --- --- ---
# 1 <= n == nums.length <= 100
# n is odd.
# 1 <= nums[i] <= 100
from collections import Counter


def is_middle_element_unique(nums: list[int]) -> bool:
    # working_solution: (32.38%, 19.08%) -> (2ms, 19.36mb)  Time: O(n) Space: O(n)
    if 1 == len(nums):
        return True
    middle: int = len(nums) // 2
    count = Counter(nums)
    
    return 1 == count[nums[middle]]


# Time complexity: O(n)
# n - length of the input array `nums`
# --- --- --- ---
# Space complexity: O(n)


test: list[int] = [1, 2, 3]
test_out: bool = True
assert test_out == is_middle_element_unique(test)

test = [1, 2, 2]
test_out = False
assert test_out == is_middle_element_unique(test)
