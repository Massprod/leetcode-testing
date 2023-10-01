# Given an array of integers nums and an integer target,
#  return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
#  and you may not use the same element twice.
# You can return the answer in any order.
# -----------------
# 2 <= nums.length <= 10 ** 4
# -10 ** 9 <= nums[i] <= 10 ** 9
# -10 ** 9 <= target <= 10 ** 9
# Only one valid answer exists.


def two_sum(nums: list[int], target: int) -> list[int]:
    # working_sol (92.18%, 11.91%) -> (57ms, 17.7mb)  time: O(n) | space: O(n)
    remainders: dict[int, int] = {}
    # ! You may assume that each input would have exactly one solution !
    # (num1 + num2) = num3 <- target
    # (num3 - num1|num2) = num2|num1
    for x in range(len(nums)):
        if nums[x] in remainders:
            return [remainders[nums[x]], x]
        remainders[target - nums[x]] = x


# Time complexity: O(n) -> worst case == first and last indexes -> traverse of whole input array => O(n).
# n - len of input array^^|
# Auxiliary space: O(n) -> worst case == every remainder is unique -> for every index(value) we will store unique
#                          remainder => O(n).


test: list[int] = [2, 7, 11, 15]
test_target: int = 9
test_out: list[int] = [0, 1]
assert test_out == two_sum(test, test_target)

test = [3, 2, 4]
test_target = 6
test_out = [1, 2]
assert test_out == two_sum(test, test_target)

test = [3, 3]
test_target = 6
test_out = [0, 1]
assert test_out == two_sum(test, test_target)
