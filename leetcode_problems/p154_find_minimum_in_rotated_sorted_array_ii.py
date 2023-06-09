# Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
# For example, the array nums = [0,1,4,4,5,6,7] might become:
#       [4,5,6,7,0,1,4] if it was rotated 4 times.
#       [0,1,4,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]]
#   1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.
# You must decrease the overall operation steps as much as possible.
# ----------------------
# n == nums.length  ,  1 <= n <= 5000  ,  -5000 <= nums[i] <= 5000
# nums is sorted and rotated between 1 and n times.
# ----------------------
# Follow up: This problem is similar to Find Minimum in Rotated Sorted Array, but nums may contain duplicates.
# Would this affect the runtime complexity? How and why?
from math import ceil
from random import randint


def find_min(nums: list[int]) -> int:

    def slice_search(sliced: list[int], duplicate: bool = False) -> int:
        if len(sliced) == 1:
            return sliced[0]
        if len(sliced) == 2:
            return min(sliced)
        if sliced[0] < sliced[-1]:
            return sliced[0]
        middle: int = ceil((len(sliced) - 1) / 2)
        if sliced[middle] == sliced[-1]:
            correct: int = slice_search(sliced[middle + 1:], True)
            if duplicate:
                return correct
            if correct < sliced[middle]:
                return correct
            if not duplicate:
                check_correct: int = slice_search(sliced[1: middle + 1])
                if check_correct:
                    return min(correct, check_correct)
        if sliced[middle] > sliced[-1]:
            return slice_search(sliced[middle + 1:])
        if sliced[middle] < sliced[-1]:
            return slice_search(sliced[: middle + 1])
    return slice_search(nums)


# Ok. Solved this case, but now we're checking both sides, and I need more cases to see mistakes.
# Tested with some random cases for constraints sizes, it's working, time to check commit.
# ----------------------
# Obviously it's just extra values to check for simple scroll O(n) and it's extra check in half for my solution,
# because middle can be equal to [-1] in this case, we need to check path of the half to decide.
# Either it's ascending half or not, and in the worst case like [2, 2, 1, 2, 2, 2, 2] -> we're going to check whole.
# So it's insta O(n) in this case.
# Can we take half anyway? Like remember this duplicate and if we checked whole and found this as minimum,
# returning false and checking another half? Can we ignore half with all duplicates? No we don't know about insides.
# Yeah, I don't see how to make this faster than O(n) in this case, we can't see is it ascending or not,
# we can't decide which half of side to start from, only way is to check all values.
# Even if I try to decide on half to check by changing [-1] to [-2] until hit something smaller,
# still same indexes will be checked.
# W.e let's try to solve this [2, 2, 1, 2, 2, 2, 2] case and if I can make it work, then commit and test time_limit.


test1 = [1, 3, 5]
test1_out = 1

test2 = [2, 2, 2, 0, 1]
test2_out = 0

test3 = [2, 2, 1, 2, 2, 2, 2]
test3_out = 1
print(find_min(test3))

test4 = [2500, 2500, -2500, -2500]
print(find_min(test4))

test_case: list[int] = [randint(-2500, 2500) for num in range(5000)]
test_case = test_case + test_case.copy()
print(len(test_case))
test_case.sort()
test_case = test_case[-3453:] + test_case[:-3453]
print(min(test_case))
print(find_min(test_case))
