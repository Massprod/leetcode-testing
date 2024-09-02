# You are given a 1-indexed array of distinct integers nums of length n.
# You need to distribute all the elements of nums between two arrays arr1 and arr2 using n operations.
# In the first operation, append nums[1] to arr1.
# In the second operation, append nums[2] to arr2.
# Afterwards, in the ith operation:
#  - If the last element of arr1 is greater than the last element of arr2, append nums[i] to arr1.
#    Otherwise, append nums[i] to arr2.
# The array result is formed by concatenating the arrays arr1 and arr2.
# For example, if arr1 == [1,2,3] and arr2 == [4,5,6], then result = [1,2,3,4,5,6].
# Return the array result.
# --------------------------
# 3 <= n <= 50
# 1 <= nums[i] <= 100
# All elements in nums are distinct.
from random import randint


def result_array(nums: list[int]) -> list[int]:
    # working_sol (40.05%, 65.94%) -> (52ms, 16.42mb)  time: O(n) | space: O(n)
    arr1: list[int] = [nums[0]]
    if 1 == len(nums):
        return arr1
    arr2: list[int] = [nums[1]]
    for index in range(2, len(nums)):
        if arr1[-1] > arr2[-1]:
            arr1.append(nums[index])
        else:
            arr2.append(nums[index])
    return arr1 + arr2


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always using every value from `nums`, once => O(n).
# --------------------------
# Auxiliary space: O(n)
# Essentially `arr1` and `arr2` will always contain all elements from `nums`.
# But they're always spread between them => O(n).


test: list[int] = [2, 1, 3]
test_out: list[int] = [2, 3, 1]
assert test_out == result_array(test)

test = [5, 4, 3, 8]
test_out = [5, 3, 4, 8]
assert test_out == result_array(test)

test = list(set([randint(1, 100) for _ in range(50)]))
print(test)
