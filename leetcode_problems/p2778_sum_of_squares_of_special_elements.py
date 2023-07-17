# You are given a 1-indexed integer array nums of length n.
# An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.
# Return the sum of the squares of all special elements of nums.
# -----------------
# 1 <= nums.length == n <= 50
# 1 <= nums[i] <= 50
from random import randint


def sum_of_squares(nums: list[int]) -> int:
    # working_sol (72.73%, 100%) -> (74ms, 16mb)  time: O(n) | space: O(1)
    summ: int = 0
    length: int = len(nums)
    for x in range(length):
        if length % (x + 1) == 0:
            summ += nums[x] ** 2
    return summ


# Time complexity: O(n) -> traversing whole input_array, once => O(n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> only 2 constant INTs, both doesn't depend on input => O(1).


test1 = [1, 2, 3, 4]
test1_out = 21
assert test1_out == sum_of_squares(test1)

test2 = [2, 7, 1, 19, 18, 3]
test2_out = 63
assert test2_out == sum_of_squares(test2)

test: list[int] = []
for _ in range(50):
    test.append(randint(1, 50))
print(test)
print(sum_of_squares(test))
