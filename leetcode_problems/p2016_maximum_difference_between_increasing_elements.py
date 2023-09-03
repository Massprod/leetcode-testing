# Given a 0-indexed integer array nums of size n,
#  find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]),
#  such that 0 <= i < j < n and nums[i] < nums[j].
# Return the maximum difference. If no such i and j exists, return -1.
# ------------------
# n == nums.length
# 2 <= n <= 1000
# 1 <= nums[i] <= 10 ** 9
from random import randint


def maximum_difference(nums: list[int]) -> int:
    # working_sol (84.99%, 55.84%) -> (48ms, 16.5mb)  time: O(n) | space: O(1)
    max_dif: int = -1
    # Highest constraint instead of float('inf').
    min_num: int = 10 ** 9
    for num in nums:
        # We only care about value being lowest and placed on left.
        # So we can just maintain the lowest on the left side.
        if min_num > num:
            min_num = num
            continue
        # ! such that 0 <= i < j < n and nums[i] < nums[j] !
        # Traversing: left -> right, only thing we care is right > min.
        if num > min_num:
            # ! i.e., nums[j] - nums[i]) !
            max_dif = max(max_dif, num - min_num)
    return max_dif


# Time complexity: O(n) -> traversing whole input_array, once => O(n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> only 2 extra constant INTs used, none of them depends on input => O(1).


test: list[int] = [7, 1, 5, 4]
test_out: int = 4
assert test_out == maximum_difference(test)

test = [9, 4, 3, 2]
test_out = -1
assert test_out == maximum_difference(test)

test = [1, 5, 2, 10]
test_out = 9
assert test_out == maximum_difference(test)

test = [randint(1, 10 ** 9) for _ in range(1000)]
print(test)
