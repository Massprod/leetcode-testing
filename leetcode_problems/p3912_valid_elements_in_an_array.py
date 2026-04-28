# You are given an integer array nums.
# An element nums[i] is considered valid if it satisfies at least one of the following conditions:
#  - It is strictly greater than every element to its left.
#  - It is strictly greater than every element to its right.
# The first and last elements are always valid.
# Return an array of all valid elements in the same order as they appear in nums.
# --- --- --- ---
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


def find_valid_elements(nums: list[int]) -> list[int]:
    # working_solution: (100%, 97.78%) -> (0ms, 19.19mb)  Time: O(n) Space: O(n)
    if 2 >= len(nums):
        return nums
    cur_max: int = 0
    max_left: list[int] = [0 for _ in nums]
    for index in range(1, len(nums)):
        cur_max = max(cur_max, nums[index - 1])
        max_left[index] = cur_max
    cur_max = 0
    max_right: list[int] = [0 for _ in nums]
    for index in range(len(nums) - 2, 0, -1):
        cur_max = max(cur_max, nums[index + 1])
        max_right[index] = cur_max

    out: list[int] = [nums[0]]
    for index in range(1, len(nums) - 1):
        if not (
            max_left[index] < nums[index]
            or
            max_right[index] < nums[index]
        ):
            continue
        out.append(nums[index])
    out.append(nums[-1])

    return out


# Time complexity: O(n)
# n - length of the input array `nums`.
# --- --- --- ---
# Space complexity: O(n)


test: list[int] = [1, 2, 4, 2, 3, 2]
test_out: list[int] = [1, 2, 4, 3, 2]
assert test_out == find_valid_elements(test)

test = [5, 5, 5, 5]
test_out = [5, 5]
assert test_out == find_valid_elements(test)

test = [1]
test_out = [1]
assert test_out == find_valid_elements(test)
