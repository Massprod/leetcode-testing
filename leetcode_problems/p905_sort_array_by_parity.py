# Given an integer array nums, move all the even integers
#  at the beginning of the array followed by all the odd integers.
# Return any array that satisfies this condition.
# -------------------
# 1 <= nums.length <= 5000
# 0 <= nums[i] <= 5000
from random import randint


def sort_array_parity(nums: list[int]) -> list[int]:
    # working_sol (88.10%, 96.40%) -> (70ms, 17mb)  time: O(n) | space: O(n)
    # Rebuild full array, with 2 pointers on odd and even places.
    parity: list[int] = [0 for _ in nums]
    left_l: int = 0
    right_l: int = -1
    for num in nums:
        if num % 2 == 0:
            parity[left_l] = num
            left_l += 1
        else:
            parity[right_l] = num
            right_l -= 1
    return parity


# Time complexity: O(n) -> traversing whole input array to rebuild array with odd and even placed => O(n).
# n - len of input array^^|
# Auxiliary space: O(n) -> copy of the original array, but with different placement => O(n).


test: list[int] = [3, 1, 2, 4]
test_out: list[int] = [2, 4, 1, 3]
assert test_out == sort_array_parity(test)

test = [0]
test_out = [0]
assert test_out == sort_array_parity(test)

test = [randint(0, 5000) for _ in range(5000)]
print(test)
