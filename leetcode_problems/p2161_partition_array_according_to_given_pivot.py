# You are given a 0-indexed integer array nums and an integer pivot.
# Rearrange nums such that the following conditions are satisfied:
#  - Every element less than pivot appears before every element greater than pivot.
#  - Every element equal to pivot appears in between the elements less than and greater than pivot.
#  - The relative order of the elements less than pivot and the elements greater than pivot is maintained.
#   - More formally, consider every pi, pj where pi is the new position of the ith element and pj
#     is the new position of the jth element.
#     For elements less than pivot, if i < j and nums[i] < pivot and nums[j] < pivot, then pi < pj.
#     Similarly for elements greater than pivot, if i < j and nums[i] > pivot and nums[j] > pivot, then pi < pj.
# Return nums after the rearrangement.
# --------------------------
# 1 <= nums.length <= 10 ** 5
# -10 ** 6 <= nums[i] <= 10 ** 6
# pivot equals to an element of nums.
from random import randint


def pivot_array(nums: list[int], pivot: int) -> list[int]:
    # working_sol (98.84%, 31.10%) -> (901ms, 34.13mb)  time: O(n) | space: O(n)
    lesser: list[int] = []
    equal: list[int] = []
    higher: list[int] = []
    for num in nums:
        if num < pivot:
            lesser.append(num)
        elif num > pivot:
            higher.append(num)
        else:
            equal.append(num)
    return lesser + equal + higher


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing `nums` to get all the values in order, once => O(n).
# Extra traversing it to combine all the values in correct order => O(2 * n).
# --------------------------
# Auxiliary space: O(n)
# All of the 3 extra arrays always contains the same `n` elements => O(n)


test: list[int] = [9, 12, 5, 10, 14, 3, 10]
test_pivot: int = 10
test_out: list[int] = [9, 5, 3, 10, 10, 12, 14]
assert test_out == pivot_array(test, test_pivot)

test = [-3, 4, 3, 2]
test_pivot = 2
test_out = [-3, 2, 4, 3]
assert test_out == pivot_array(test, test_pivot)

test = [randint(-10 ** 6, 10 ** 6) for _ in range(10 ** 5)]
print(test)
