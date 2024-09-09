# Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:
#  - answer.length == nums.length.
#  - answer[i] = |leftSum[i] - rightSum[i]|.
# Where:
#  - leftSum[i] is the sum of elements to the left of the index i in the array nums.
#    If there is no such element, leftSum[i] = 0.
#  - rightSum[i] is the sum of elements to the right of the index i in the array nums.
#    If there is no such element, rightSum[i] = 0.
# Return the array answer.
# --------------------------
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 10 ** 5


def left_right_differences(nums: list[int]) -> list[int]:
    # working_sol (87.03%, 80.31%) -> (58ms, 16.75mb)  time: O(n) | space: O(n)
    out: list[int] = []
    prefix: int = 0
    suffix: int = sum(nums[1:])
    for index in range(len(nums) - 1):
        out.append(
            abs(prefix - suffix)
        )
        prefix += nums[index]
        suffix -= nums[index + 1]
    out.append(prefix)
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole input array `nums`, twice => O(2 * n).
# --------------------------
# Auxiliary space: O(n)
# `out` <- always allocates space for each value in `nums` => O(n).


test: list[int] = [10, 4, 8, 3]
test_out: list[int] = [15, 1, 11, 22]
assert test_out == left_right_differences(test)

test = [1]
test_out = [0]
assert test_out == left_right_differences(test)
