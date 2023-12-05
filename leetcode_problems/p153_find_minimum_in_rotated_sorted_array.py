# Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
# For example, the array nums = [0,1,2,4,5,6,7] might become:
#   - [4,5,6,7,0,1,2] if it was rotated 4 times.
#   - [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]]
#  1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.
# --------------------
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.
from random import randint


def find_min(nums: list[int]) -> int:
    # working_sol (97.56%, 87.84%) -> (36ms, 16.4mb)  time: O(log n) | space: O(1)
    # ! All the integers of nums are unique. ! <- we don't care about duplicates.
    # Array not rotated.
    if nums[0] < nums[-1]:
        return nums[0]
    # If array rotated, lowest value will always be in rotated part.
    left: int = 0
    right: int = len(nums) - 1
    while left < right:
        middle: int = (left + right) // 2
        # If 'middle' inside rotated part.
        # We already in rotated part, and lowest is always somewhere on the left.
        if nums[middle] < nums[right]:
            right = middle
        # If 'middle' not inside rotated part.
        # We only care about getting into rotated part, because lowest is here.
        # And we know that all values in rotated part is lower than nums[left].
        elif nums[middle] >= nums[left]:
            left = middle + 1
    return nums[left]


# Time complexity: O(log n) <- n - length of input array 'nums'.
# Standard BinarySearch.
# Auxiliary space: O(1).


test: list[int] = [3, 4, 5, 1, 2]
test_out: int = 1
assert test_out == find_min(test)

test = [4, 5, 6, 7, 0, 1, 2]
test_out = 0
assert test_out == find_min(test)

test = [11, 13, 15, 17]
test_out = 11
assert test_out == find_min(test)

test = [2, 1]
test_out = 1
assert test_out == find_min(test)

test = [3, 1, 2]
test_out = 1
assert test_out == find_min(test)

test = sorted(set([randint(-5000, 5000) for _ in range(5000)]))
pivot_point: int = randint(0, len(test) - 1)
test = test[pivot_point:] + test[:pivot_point]
test_out = min(test)
assert test_out == find_min(test)
print(test)
