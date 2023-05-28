# Given a non-empty array of integers nums, every element appears twice except for one.
# Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# --------------------------
# 1 <= nums.length <= 3 * 104  ,  -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.


def single_number(nums: list[int]) -> int:
    # working_sol (78.33%, 33.84%) -> (134ms, 18.9mb)  time: O(n) | space: O(1)
    if len(nums) == 1:
        return nums[0]
    mask: int = 0
    for _ in nums:
        mask = mask ^ _
    return mask


# Time complexity: O(n) -> calling (mask ^ _) on every index => O(n)
# Space complexity: O(1) -> only 1 constant used, doesn't depend on input => O(1)
# --------------------------
# Basic idea with sum was somewhat correct, but I didn't know how to extract numbers from it correctly.
# After some experience with bit_tasks, it's not going to be a problem.
# --------------------------
# Well, I learned about bit shifts and basic manipulations. But having almost no experience with tasks on it.
# So I failed to see that we can just rebuild any INT from any other INT by switching bits:
# Flow:
#   taking mask as 0 -> calling XOR(excl_or) for every value in nums ->
#   0 ^ 2 == 2, 2 ^ 2 == 0, 0 ^ 1 == 1 -> like in test1
#   0b0 ^ 0b10 -> 0b10 , 0b10 ^ 0b10 -> 0b00 , 0b00 ^ 0b01 -> 0b01
#   !
#   mask is taking every True(1) inside on open spaces(0), and deletes every occupied(1)!
#   most important to remember this^^, because (_ ^ mask) will give us same values,
#                                      cuz mask doesn't have anything to compare/switch.
# --------------------------
# O(1) - space, O(n) - time, huh.
# So we can't rebuild or sort, only some constants.
# Sum? Like, left_right loop with summarizing everything and extracting after we encounter double?
# Nah, we would need extra space to store used values, and if only 1 value remembered we will lose values.


test1 = [2, 2, 1]
test1_out = 1
print(single_number(test1))

test2 = [4, 1, 2, 1, 2]
test2_out = 4
print(single_number(test2))

test3 = [1]
test3_out = 1
print(single_number(test3))

test4 = [1, 2, 3, 4, 5, 6, 7, 10, 9, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(single_number(test4))

test5 = [1, 2, 3, 4, 2, 1, 3]
print(single_number(test5))
