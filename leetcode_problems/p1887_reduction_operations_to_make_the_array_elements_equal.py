# Given an integer array nums, your goal is to make all elements in nums equal.
# To complete one operation, follow these steps:
#  - Find the largest value in nums. Let its index be i (0-indexed) and its value be largest.
#    If there are multiple elements with the largest value, pick the smallest i.
#  - Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.
#  - Reduce nums[i] to nextLargest.
# Return the number of operations to make all elements in nums equal.
# --------------------
# 1 <= nums.length <= 5 * 10 ** 4
# 1 <= nums[i] <= 5 * 10 ** 4
from random import randint


def reduction_operations(nums: list[int]) -> int:
    # working_sol (45.88%, 82.47%) -> (849ms, 23.8mb)  time: O(n * log n) | space: O(n)
    nums.sort()
    # Index of the first smaller value we found.
    index: int = len(nums) - 1
    # ! Find the largest value in nums. !
    largest: int = nums[index]
    ops: int = 0
    while index >= 0:
        # ! Find the next largest value in nums strictly smaller than largest. !
        if nums[index] == largest:
            index -= 1
        # ! Reduce nums[i] to nextLargest !
        else:
            # 1-operation == 1 value reduced.
            # All values visited before smaller should be reduced.
            #                -1 for 0-indexing.
            ops += len(nums) - 1 - index
            largest = nums[index]
    return ops


# Time complexity: O(n * log n) -> sorting with built_in => O(n * log n) -> extra traversing whole array, once => O(n).
# n - len of input array 'nums'^^|
# Auxiliary space: O(n) -> built_in sort takes O(n) + 3 constant INTs none of which depends on input => O(n).


test: list[int] = [5, 1, 3]
test_out: int = 3
assert test_out == reduction_operations(test)

test = [1, 1, 1]
test_out = 0
assert test_out == reduction_operations(test)

test = [1, 1, 2, 2, 3]
test_out = 4
assert test_out == reduction_operations(test)

test = [randint(1, 5 * 10 ** 4) for _ in range(10 ** 4)]
print(test)
