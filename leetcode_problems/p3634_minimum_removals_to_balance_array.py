# You are given an integer array nums and an integer k.
# An array is considered balanced if the value of its maximum element
#  is at most k times the minimum element.
# You may remove any number of elements from nums​​​​​​​ without making it empty.
# Return the minimum number of elements to remove so that the remaining array is balanced.
# Note: An array of size 1 is considered balanced as its maximum and minimum are equal,
#  and the condition always holds true.
# --- --- --- ---
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 9
# 1 <= k <= 10 ** 5
from random import randint
from pyperclip import copy


def min_removal(nums: list[int], k: int) -> int:
    # working_solution: (25.89%, 30.14%) -> (171ms, 34.64mb)  Time: O(n + n * log n) Space: O(n)
    # Sort, so we could check everything: lower -> higher.
    # No way of linear, but at least we can skip some higher value iterations.
    sorted_nums: list[int] = sorted(nums)
    out: int = len(sorted_nums)
    left: int = 0
    right: int = 0
    while left < len(sorted_nums):
        while right < len(sorted_nums) and sorted_nums[right] <= (sorted_nums[left] * k):
            right += 1
        out = min(
            out,
            left + (len(sorted_nums) - right)  # 0 -> left + right -> end
        )
        left += 1
    
    return out


# Time complexity: O(n + n * log n)
# n - length of the input array `nums`
# Always sorting the initial array => O(n * logn)
# Extra traversing the array indexes, using them at mose 2 times each => O(2 * n).
# --- --- --- ---
# Space complexity: O(n)
# `sorted_nums` <- allocates space for each value from the `nums`.


test: list[int] = [2, 1, 5] 
test_k: int = 2
test_out: int = 1
assert test_out == min_removal(test, test_k)

test = [1, 6, 2, 9]
test_k = 3
test_out = 2
assert test_out == min_removal(test, test_k)

test = [4, 6]
test_k = 2
test_out = 0
assert test_out == min_removal(test, test_k)

test = [randint(1, 10 ** 9) for _ in range(10 ** 5)]
copy(test)  # type: ignore
