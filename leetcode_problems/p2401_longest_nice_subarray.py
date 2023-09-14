# You are given an array nums consisting of positive integers.
# We call a subarray of nums nice if the bitwise AND of every pair of elements
#  that are in different positions in the subarray is equal to 0.
# Return the length of the longest nice subarray.
# A subarray is a contiguous part of an array.
# Note that subarrays of length 1 are always considered nice.
# ------------------------
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 9
from random import randint


def longest_nice_sub(nums: list[int]) -> int:
    # working_sol (85.25%, 98.77%) -> (561ms, 30.8mb)  time: O(n) | space: O(1)
    # Standard sliding window.
    l_limit: int = 0
    r_limit: int = 0
    bit_mask: int = 0
    max_len: int = 0
    # Essentially we shouldn't have any pair with same position of '1' bit.
    # We can just store all '1' placements in a bit_mask, and check on it.
    while r_limit != len(nums):
        while (nums[r_limit] & bit_mask) != 0:
            # 1-1 == 0, and remove it with XOR.
            bit_mask ^= nums[l_limit]
            l_limit += 1
        # 1-0, 0-1 == 1, place every '1' with OR.
        bit_mask |= nums[r_limit]
        # 0-indexed, +1 for correct length.
        max_len = max(max_len, (r_limit - l_limit) + 1)
        # ! 1 <= nums[i] <= 10 ** 9 ! <- constraint.
        # If all 1 placed, we will never have option with 0.
        # So it's always fail after 30.
        if max_len == 30:
            return max_len
        r_limit += 1
    return max_len


# Time complexity: O(n) -> worst case ==  only 1 correct num in nums, and no pairs ->
# n - len of input_array^^| -> we will traverse every index, and delete every previously checked index once => O(2n).
# Auxiliary space: O(1) -> only 4 extra constant INTs used, none of them depends on input => O(1).
# ------------------------
# Hint:
# ! The length of the longest nice subarray cannot exceed 30. Why is that? !
# Break when already 30? All 1 bit placed, and we can't have nums[i] == 0 <- ! 1 <= nums[i] <= 10 ** 9 !
# So it's at least 1 bit placed for any num we will check, and it will fail after 30 taken.
# ------------------------
# !
# bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.
# !
# Bitmask with all 1 placed from every num in window?
# Only way # & # will be 0 is if (1-0) or (0-1) bit pairs. So we need to annul everything.
# Start with mask 0 and place all 1 from every num in cur_window.
# Cuz we need to get 0 from EVERY pair, and if at least 1 bit is left != 0.
# Essentially we shouldn't have any 1 bit placed on the same place for every number in subarray.
# And simply remove placed bits after we start shrinking window with XOR.
# Should be correct.


test: list[int] = [1, 3, 8, 48, 10]
test_out: int = 3
assert test_out == longest_nice_sub(test)

test = [3, 1, 5, 11, 13]
test_out = 1
assert test_out == longest_nice_sub(test)

test = [randint(1, 10 ** 9) for _ in range(10 ** 3)]
print(test)
