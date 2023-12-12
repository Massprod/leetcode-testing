# Given the array of integers nums, you will choose two different indices i and j of that array.
# Return the maximum value of (nums[i]-1)*(nums[j]-1).
# --------------------
# 2 <= nums.length <= 500
# 1 <= nums[i] <= 10 ** 3
from random import randint


def max_product(nums: list[int]) -> int:
    # working_sol (81.72%, 41.49%) -> (52ms, 16.4mb)  time: O(n) | space: O(1)
    # Essentially all we care about is maximum product we can get.
    # And we can get maximum product if we take 2 highest values.
    pre_max: int = -1
    max_val: int = -1
    for val in nums:
        if val > max_val:
            pre_max = max_val
            max_val = val
        elif val > pre_max:
            pre_max = val
    return (pre_max - 1) * (max_val - 1)


# Time complexity: O(n) <- n - length of input array `nums`.
# Single traverse of whole input array.
# Auxiliary space: O(1).


test: list[int] = [3, 4, 5, 2]
test_out: int = 12
assert test_out == max_product(test)

test = [1, 5, 4, 5]
test_out = 16
assert test_out == max_product(test)

test = [3, 7]
test_out = 12
assert test_out == max_product(test)

test = [randint(1, 10 ** 3) for _ in range(500)]
print(test)
