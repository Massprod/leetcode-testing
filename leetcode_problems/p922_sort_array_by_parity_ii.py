# Given an array of integers nums, half of the integers in nums are odd,
#  and the other half are even.
# Sort the array so that whenever nums[i] is odd, i is odd,
#  and whenever nums[i] is even, i is even.
# Return any answer array that satisfies this condition.
# --------------------
# 2 <= nums.length <= 2 * 10 ** 4
# nums.length is even.
# Half of the integers in nums are even.
# 0 <= nums[i] <= 1000
# --------------------
# Follow Up: Could you solve it in-place?


def sort_array_by_parity_ii(nums: list[int]) -> list[int]:
    # working_sol (64.43%, 25.07%) -> (149ms, 19.11mb)  time: O(n) | space: O(1)
    even_index: int = 0
    odd_index: int = 1
    while even_index < len(nums) and odd_index < len(nums):
        # We search for the first `even_index` which is not setup already.
        while even_index < len(nums) and not nums[even_index] % 2:
            even_index += 2
        # We search for the first `odd_index` which is not setup already.
        while odd_index < len(nums) and nums[odd_index] % 2:
            odd_index += 2
        # After we find incorrect index setup, we can just switch them.
        if even_index < len(nums) and odd_index < len(nums):
            nums[even_index], nums[odd_index] = nums[odd_index], nums[even_index]
            even_index += 2
            odd_index += 2
    return nums


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always using every index of the input array `nums`, once => O(n).
# --------------------
# Auxiliary space: O(1)
# Only 2 constant INT's used, none of them depends on input => O(1).


test: list[int] = [4, 2, 5, 7]
test_out: list[int] = [4, 5, 2, 7]
assert test_out == sort_array_by_parity_ii(test)

test = [2, 3]
test_out = [2, 3]
assert test_out == sort_array_by_parity_ii(test)
