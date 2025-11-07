# You are given an integer array nums.
# Return the smallest absent positive integer in nums such that it is strictly greater
#  than the average of all elements in nums.
# The average of an array is defined as the sum of all its elements divided
#  by the number of elements.
# --- --- --- ---
# 1 <= nums.length <= 100
# -100 <= nums[i] <= 100​​​​​​​


def smallest_absent(nums: list[int]) -> int:
    # working_solution: (88.87%, 67.40%) -> (1ms, 17.87mb)  Time: O(n) Space: O(n)
    avg: int = sum(nums) // len(nums)
    fast_nums: set[int] = set(nums)
    # ! smallest absent positive integer !
    out: int = max(1, avg + 1)
    # We can use BS. But, constraints are too small to bother.
    while out in fast_nums:
        out += 1

    return out


# Time complexity: O(n)
# n - length of the input array `nums`.
# --- --- --- ---
# Space complexity: O(n)
# `fast_nums` <- allocates space for each value from `nums` => O(n)


test: list[int] = [3, 5]
test_out: int = 6
assert test_out == smallest_absent(test)

test = [-1, 1, 2]
test_out = 3
assert test_out == smallest_absent(test)

test = [4, -1]
test_out = 2
assert test_out == smallest_absent(test)
