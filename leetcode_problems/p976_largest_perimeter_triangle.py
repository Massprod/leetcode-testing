# Given an integer array nums, return the largest perimeter of a triangle
#  with a non-zero area, formed from three of these lengths.
# If it is impossible to form any triangle of a non-zero area, return 0.
# --- --- --- ---
# 3 <= nums.length <= 10 ** 4
# 1 <= nums[i] <= 10 ** 6


def largest_perimeter(nums: list[int]) -> int:
    # working_solution: (87.025%, 45.24%) -> (10ms, 18.72mb)  Time: O(n * log n) Space: O(n)
    out: int = 0
    # side1 + side2 > side3 == correct.
    # Take the highest sizes and check if they can be used.
    nums.sort()
    for index in range(len(nums) - 3, -1, -1):
        # side1 >= side2 >= side
        side1, side2, side3 = nums[index], nums[index + 1], nums[index + 2]
        if side1 + side2 > side3:
            out = side1 + side2 + side3
            return out
        
    return out


# Time complexity: O(n * log n) <- n - length of the input array `nums`.
# Sort original input array => O(n * log n).
# --- --- --- ---
# Space complexity: O(n)
# `sort` <- takes O(n).


test: list[int] = [2, 1, 2]
test_out: int = 5
assert test_out == largest_perimeter(test)

test = [1, 2, 1, 10]
test_out = 0
assert test_out == largest_perimeter(test)
