# Given an array nums of n integers where nums[i] is in the range [1, n],
#  return an array of all the integers in the range [1, n] that do not appear in nums.
# -----------------
# n == nums.length
# 1 <= n <= 10 ** 5
# 1 <= nums[i] <= n
# -----------------
# Follow up: Could you do it without extra space and in O(n) runtime?
#  You may assume the returned list does not count as extra space.


def find_disappeared_number(nums: list[int]) -> list[int]:
    # working_sol (53.23%, 98.63%) -> (283ms, 24.74mb)  time: O(n) | space: O(1)
    # !  n == nums.length , 1 <= nums[i] <= n !
    index: int = 0
    while index != len(nums):
        # Correct placement [1 -> n] inclusive, so every value is (index + 1).
        value: int = nums[index]
        correct_index: int = value - 1
        # We're always given array with same size as Correct one, but missed values are replaced with duplicates.
        # So, we can either place value in Correct placements or we will have duplicates.
        # And one of them will be placed on `correct_index` where it belongs,
        #  and another at [index] where we're leaving it == marking missed value.
        if nums[correct_index] != value:
            nums[correct_index], nums[index] = nums[index], nums[correct_index]
        else:
            index += 1
    out: list[int] = []
    for index, value in enumerate(nums):
        correct_value: int = index + 1
        if correct_value != value:
            out.append(correct_value)
    return out


# Time complexity: O(n) <- n - length of input array `nums`.
# We're not using every index once, but it's still Linear => O(n).
# Because we can use some indexes once, another 3-4 times w.e. Still Linear growth.
# And extra traverse of the whole array `nums` to get missing values => O(n).
# -----------------
# Auxiliary space: O(1).
# ! You may assume the returned list does not count as extra space. !
# With this rule, we're only using 3 INTs and none of them depends on input => O(1)


test: list[int] = [4, 3, 2, 7, 8, 2, 3, 1]
test_out: list[int] = [5, 6]
assert test_out == find_disappeared_number(test)

test = [1, 1]
test_out = [2]
assert test_out == find_disappeared_number(test)
