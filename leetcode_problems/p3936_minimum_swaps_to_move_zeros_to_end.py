# You are given an integer array nums.
# In one operation, you can choose any two distinct indices i and j
#  and swap nums[i] and nums[j].
# Return an integer denoting the minimum number of operations required
#  to move all 0s to the end of the array.
# --- --- --- ---
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
from random import randint
from pyperclip import copy


def minimum_swaps(nums: list[int]) -> int:
    # working_solution: (100%, 23.88%) -> (0ms, 19.36mb)  Time: O(n) Space: O(1)
    out: int = 0
    left: int = 0
    right: int = len(nums) - 1
    while left < right:
        while 0 != nums[left] and left < right:
            left += 1
        while 0 == nums[right] and left < right:
            right -= 1
        if left < right and 0 == nums[left] and 0 != nums[right]:
            out +=1
            left += 1
            right -= 1
    
    return out


# Time complexity: O(n)
# n - length of the input array `nums`.
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [0, 1, 0, 3, 12]
test_out: int = 2
assert test_out == minimum_swaps(test)

test = [0, 1, 0, 2]
test_out = 1
assert test_out == minimum_swaps(test)

test = [1, 2, 0]
test_out = 0
assert test_out == minimum_swaps(test)

test = [randint(0, 100) for _ in range(100)]
copy(test)  # type: ignore
