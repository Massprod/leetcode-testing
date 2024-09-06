# You are given a 0-indexed integer array nums.
# The concatenation of two numbers is the number formed
#  by concatenating their numerals.
#  - For example, the concatenation of 15, 49 is 1549.
# The concatenation value of nums is initially equal to 0.
# Perform this operation until nums becomes empty:
#  - If there exists more than one number in nums, pick the first element and last element in nums
#    respectively and add the value of their concatenation to the concatenation value of nums,
#    then delete the first and last element from nums.
#  - If one element exists, add its value to the concatenation value of nums, then delete it.
# Return the concatenation value of the nums.
# -------------------------
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 10 ** 4


def find_the_array_conc_val(nums: list[int]) -> int:
    # working_sol (85.38%, 65.94%) -> (48ms, 16.65)  time: O(n) | space: O(1)
    out: int = 0
    left: int = 0
    right: int = len(nums) - 1
    while left < right:
        out += int(str(nums[left]) + str(nums[right]))
        left += 1
        right -= 1
    if left == right:
        out += nums[left]
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always using every index of `nums`, once => O(n).
# Auxiliary space: O(1).
# Only 3 constant INTs used, none of them depends on input => O(1).


test: list[int] = [7, 52, 2, 4]
test_out: int = 596
assert test_out == find_the_array_conc_val(test)

test = [5, 14, 13, 8, 12]
test_out = 673
assert test_out == find_the_array_conc_val(test)
