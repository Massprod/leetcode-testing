# You are given an integer array nums.
# An index i is balanced if the sum of elements strictly to the left of i 
#  equals the product of elements strictly to the right of i.
# If there are no elements to the left, the sum is considered as 0.
# Similarly, if there are no elements to the right, the product is considered as 1.
# Return an integer denoting the smallest balanced index.
# If no balanced index exists, return -1.
# --- --- --- ---
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 9
from random import randint
from pyperclip import copy


def smallest_balanced_index(nums: list[int]) -> int:
    # working_solution: (98.46%, 95.78%) -> (48ms, 31.14mb)  Time: O(n) Space: O(1)
    out: int = -1
    c_sum: int = sum(nums)
    c_prod: int = 1
    for index in range(len(nums) -1, -1, -1):
        c_sum -= nums[index]
        if c_sum == c_prod:
            out = index
        # product will only increase, no reasons to keep going
        if c_sum < c_prod:
            break
        c_prod *= nums[index]
    
    return out


# Time complexity: O(n)
# n - length of the input array `nums`
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [2, 1, 2]
test_out: int = 1
assert test_out == smallest_balanced_index(test)

test = [2, 8, 2, 2, 5]
test_out = 2
assert test_out == smallest_balanced_index(test)

test = [1]
test_out = -1
assert test_out == smallest_balanced_index(test)

test = [randint(1, 10 ** 9) for _ in range(10 ** 5)]
copy(test)  # type: ignore
