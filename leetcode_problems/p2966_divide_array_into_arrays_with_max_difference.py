# You are given an integer array nums of size n and a positive integer k.
# Divide the array into one or more arrays of size 3 satisfying the following conditions:
#   - Each element of nums should be in exactly one array.
#   - The difference between any two elements in one array is less than or equal to k.
# Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions,
#  return an empty array.
# And if there are multiple answers, return any of them.
# ----------------------------
# n == nums.length
# 1 <= n <= 10 ** 5
# n is a multiple of 3.
# 1 <= nums[i] <= 10 ** 5
# 1 <= k <= 10 ** 5
from random import randint


def divide_array(nums: list[int], k: int) -> list[list[int]]:
    # working_sol (98.46%, 96.29%) -> (689ms, 30.79mb)  time: O(n * log n) | space: O(n)
    # If we sort values, we can be sure that values with MINIMISED differences,
    #  are neighbours. Then we can use greedy approach to use every pair of 3.
    nums.sort()
    out: list[list[int]] = []
    for x in range(2, len(nums), 3):
        # `nums` already sorted, so we don't care about middle element.
        # Because it's higher than nums[x - 2] and lower than nums[x],
        #  so it's always going to have lower difference than: nums[x] - nums[x - 2].
        # Or it's equal to one of them and diff is the same.
        if nums[x] - nums[x - 2] <= k:
            out.append(nums[x - 2:x + 1])
        # We need to use ALL, otherwise it's incorrect.
        else:
            return []
    return out


# Time complexity: O(n * log n) <- n - length of input array `nums`.
# Sorting with builtin sort() => O(n * log n).
# Extra traversing only 1/3 of input array indexes, and for each constant operation of slicing 3 elements => O(n).
# ----------------------------
# Auxiliary space: O(n).
# If we can divide correctly, then we will get all values from `nums` in `out`.
# But inside lists of size 3 => O(n).


test: list[int] = [1, 3, 4, 8, 7, 9, 3, 5, 1]
test_k: int = 2
test_out: list[list[int]] = [[1, 1, 3], [3, 4, 5], [7, 8, 9]]
assert test_out == divide_array(test, test_k)

test = [1, 3, 3, 2, 7, 3]
test_k = 3
test_out = []
assert test_out == divide_array(test, test_k)

test = [randint(1, 10 ** 5) for _ in range(10 ** 3 * 3)]
print(test)
