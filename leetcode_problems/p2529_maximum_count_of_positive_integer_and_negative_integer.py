# Given an array nums sorted in non-decreasing order,
#  return the maximum between the number of positive integers and the number of negative integers.
# In other words, if the number of positive integers in nums is pos and the number of negative integers is neg,
#  then return the maximum of pos and neg.
# Note that 0 is neither positive nor negative.
# -----------------------------
# 1 <= nums.length <= 2000
# -2000 <= nums[i] <= 2000
# nums is sorted in a non-decreasing order.
# -----------------------------
# Follow up: Can you solve the problem in O(log(n)) time complexity?
from random import randint


def maximum_count(nums: list[int]) -> int:
    # working_sol (96.49%, 59.97%) -> (95ms, 16.89mb)  time: O(log n) | space: O(1)
    if 0 == nums[0] and 0 == nums[-1]:
        return 0

    def bs(left: int, right: int, _positive: bool) -> int:
        while left < right:
            middle: int = ((left + right) // 2) + 1
            if _positive:
                if 0 >= nums[middle]:
                    left = middle
                else:
                    right = middle - 1
            else:
                if 0 <= nums[middle]:
                    right = middle - 1
                else:
                    left = middle
        return left

    last_negative: int = bs(0, len(nums) - 1, False)
    first_positive: int = bs(last_negative, len(nums) - 1, True)
    negatives: int = (last_negative + 1)
    if 0 >= nums[first_positive]:
        first_positive += 1
    positive: int = len(nums) - first_positive
    return max(negatives, positive)


# Time complexity: O(log n) <- n - length of the input array `nums`.
# Always using standard BS to get the last index of negative and (first index - 1) of positive values => O(2 * log n).
# -----------------------------
# Auxiliary space: O(1)
# Only 5 constant INTs used, none of them depends on input => O(1).


test: list[int] = [-2, -1, -1, 1, 2, 3]
test_out: int = 3
assert test_out == maximum_count(test)

test = [-3, -2, -1, 0, 0, 1, 2]
test_out = 3
assert test_out == maximum_count(test)

test = [5, 20, 66, 1314]
test_out = 4
assert test_out == maximum_count(test)

test = sorted([randint(-2000, 2000) for _ in range(2000)])
print(test)
