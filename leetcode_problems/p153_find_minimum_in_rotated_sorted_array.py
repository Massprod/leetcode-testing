# Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
# For example, the array nums = [0,1,2,4,5,6,7] might become:
#       [4,5,6,7,0,1,2] if it was rotated 4 times.
#       [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]]
#   1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.
# --------------------
# n == nums.length  ,  1 <= n <= 5000  ,  -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.
from math import ceil


def find_min(nums: list[int]) -> int:

    def slice_search(sliced: list[int]) -> int:
        if len(sliced) == 1:
            return sliced[0]
        if len(sliced) == 2:
            return min(sliced)
        if sliced[0] < sliced[-1]:
            return sliced[0]
        middle: int = ceil((len(sliced) - 1) / 2)
        if sliced[middle] > sliced[-1]:
            return slice_search(sliced[middle + 1:])
        if sliced[middle] < sliced[-1]:
            return slice_search(sliced[: middle + 1])
    return slice_search(nums)


# Ok. In the end come up with some rebuild of merge sorting, instead of just looping to find values,
# but I need more test_cases to see where it can fail. Time to fail to get these cases.
# Unique case with len == 2, should have seen it before failing, because we can't take middle of 2...
#
# --------------------
# Ok. Sorted in ascending -> first we can get minimum instantly if it's not rotated ->
# -> it's always can be checked by nums[0] < nums[-1], return nums[0], w.e index of rotation is, should be correct.
# For O(n) it's just walk from left to right, for O(log n) we at least should eliminate half ->
# -> which is easy, because we always know where's descending halve.
# But what about these halves, where to start in them?
# Extra check middle or just start by checking middle? W.e point we start there's always [x - 1] < [x + 1] or >
# check to get where's ascending path.


test1 = [3, 4, 5, 1, 2]
test1_out = 1
print(find_min(test1))

test2 = [4, 5, 6, 7, 0, 1, 2]
test2_out = 0
print(find_min(test2))

test3 = [11, 13, 15, 17]
test3_out = 11
print(find_min(test3))

# test4 - failed -> Yeah. We can't take a middle of 2, and I missed this part, actually
#                   maybe it's better to just find min for cases with len < 4? At least for 2 is better.
test4 = [2, 1]
print(find_min(test4))

test5 = [3, 1, 2]
print(find_min(test5))

