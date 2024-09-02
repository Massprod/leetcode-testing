# You are given a positive integer array nums.
#  - The element sum is the sum of all the elements in nums.
#  - The digit sum is the sum of all the digits
#    (not necessarily distinct) that appear in nums.
# Return the absolute difference between the element sum and digit sum of nums.
# Note that the absolute difference between two integers x and y is defined as |x - y|.
# ------------------------
# 1 <= nums.length <= 2000
# 1 <= nums[i] <= 2000


def difference_of_sum(nums: list[int]) -> int:
    # working_sol (92.73%, 54.03%) -> (99ms, 16.86mb)  time: O(n * k) | space: O(1)
    digits_sum: int = 0
    numbers_sum: int = sum(nums)
    for number in nums:
        while number:
            digits_sum += number % 10
            number //= 10
    return abs(digits_sum - numbers_sum)


# Time complexity: O(n * k) <- n - length of the input array `nums`, k - average number of digits in numbers of `nums`.
# Always traversing `nums`, twice.
# First, we get numbers sum => O(n).
# Second, we're using every digit of numbers in `nums` => O(n * k).
# ------------------------
# Auxiliary space: O(1)
# Only two constant INTs used, none of them depends on input => O(1).


test: list[int] = [1, 15, 6, 3]
test_out: int = 9
assert test_out == difference_of_sum(test)

test = [1, 2, 3, 4]
test_out = 0
assert test_out == difference_of_sum(test)
