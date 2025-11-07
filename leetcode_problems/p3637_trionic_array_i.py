# You are given an integer array nums of length n.
# An array is trionic if there exist indices 0 < p < q < n − 1 such that:
#  - nums[0...p] is strictly increasing,
#  - nums[p...q] is strictly decreasing,
#  - nums[q...n − 1] is strictly increasing.
# Return true if nums is trionic, otherwise return false.
# --- --- --- ---
# 3 <= n <= 100
# -1000 <= nums[i] <= 1000


def is_trionic(nums: list[int]) -> bool:
    # working_solution: (100%, 74.62%) -> (0ms, 17.72mb)  Time: O(n) Space: O(1)
    if 3 >= len(nums):
        return False
    # Instantly decreasing => incorrect.
    if nums[0] > nums[1]:
        return False
    breaks: int = 1
    # True -> asc | False -> desc
    cur: bool = True
    for index in range(1, len(nums)):
        if nums[index] == nums[index - 1]:
            return False
        if 3 < breaks:
            return False
        if cur:
            if nums[index] < nums[index - 1]:
                cur = False
                breaks += 1
        else:
            if nums[index] > nums[index - 1]:
                cur = True
                breaks += 1
    
    return 3 == breaks


# Time complexity: O(n)
# n - length of the input array `nums`.
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [1, 3, 5, 4, 2, 6]
test_out: bool = True
assert test_out == is_trionic(test)

test = [2, 1, 3]
test_out = False
assert test_out == is_trionic(test)
