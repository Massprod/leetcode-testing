# Given an array of integers nums and an integer k,
#   return the number of contiguous subarrays where the product of all the elements
#   in the subarray is strictly less than k.
# ------------------------
# 1 <= nums.length <= 3 * 10 ** 4
# 1 <= nums[i] <= 1000
# 0 <= k <= 10 ** 6
from random import randint


def num_subproduct_less_than_k(nums: list[int], k: int) -> int:
    # working_sol (99.13%, 55.8%) -> (576ms, 19.6mb)  time: O(n) | space: O(1)
    # Constraints are 1 - 1000
    # We can't get product less than 1, cuz 1 * 1 is smallest == 1.
    if k <= 1:
        return 0
    subs: int = 0
    left_l: int = 0
    right_l: int = 0
    # We're starting from 1 index itself.
    cur_sub: int = nums[left_l]
    # So if it's correct we need it subarray included.
    if cur_sub < k:
        subs += 1
    for x in range(1, len(nums)):
        # Expend window by 1 index.
        right_l += 1
        # Current window product.
        cur_sub *= nums[right_l]
        # Shrink window if it's incorrect.
        while cur_sub >= k and left_l <= right_l:
            cur_sub /= nums[left_l]
            left_l += 1
        # Every value by itself == +1.
        # Extra to this we need subarrays from left_limit to right_limit.
        # Which is correct window.
        subs += right_l - left_l + 1
    return subs


# Time complexity: O(n) -> always traversing whole input_array, once => O(n) -> best case all array is used as
# n - len of input_array^^| one correct product, so we're not shrinking the window, in the worst case ->
#                           -> for every step, we're going to shrink the window by 1 index, so it's extra O(n) =>
#                           => O(2n) => O(n).
# Auxiliary space: O(1) -> only extra constants used, none of them depends on input and used always same way => O(1).
# ------------------------
# Ok. Working with 4 test_cases with maximum constraints, but there's might be some tricks.
# Worked fine, maybe later build DP solution.
# ------------------------
# First we can cull K <= 1, cuz we're given ! 1 <= nums[i] <= 1000 ! product can't be negative and min value is 1.
# Even if we 1 * 1 it's still 1, and 0 can't be present in the array.
# Hint again pointing to DP problem, but I see it as window problem ->
# -> like just take some window count every possible option by itself and summ of them ->
# -> [1, 2, 3] k == 4, window 1, 2, 3 every option by itself is correct and whole window as well.


test1 = [10, 5, 2, 6]
test1_k = 100
test1_out = 8
assert test1_out == num_subproduct_less_than_k(test1, test1_k)

test2 = [1, 2, 3]
test2_k = 0
test2_out = 0
assert test2_out == num_subproduct_less_than_k(test2, test2_k)

test: list[int] = []
for _ in range(3 * 10 ** 4):
    test.append(randint(1, 1000))
test_k: int = randint(0, 10 ** 6)
print(test)
print(test_k)
