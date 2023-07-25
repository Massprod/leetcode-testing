# An array arr a mountain if the following properties hold:
#   arr.length >= 3
#   There exists some i with 0 < i < arr.length - 1 such that:
#       arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#       arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array arr, return the index i such that:
#   arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
# You must solve it in O(log(arr.length)) time complexity.
# -------------------
# 3 <= arr.length <= 10 ** 5
# 0 <= arr[i] <= 10 ** 6
# arr is guaranteed to be a mountain array.


def peak_index_of_mountain(arr: list[int]) -> int:
    # working_sol (95.89%, 55.46%) -> (574ms, 30.1mb)  time: O(log n) | space: O(1)
    left: int = 0
    right: int = len(arr) - 1
    while left < right:
        middle: int = (left + right) // 2
        # Peak itself.
        if arr[middle - 1] < arr[middle] > arr[middle + 1]:
            return middle
        # Descending slope, we can cull it ->
        # -> everything after middle is lower.
        elif arr[middle - 1] > arr[middle]:
            right = middle
        # Ascending slope, we can cull left part of it ->
        # -> cuz everything after middle is higher or middle == peak.
        elif arr[middle - 1] < arr[middle]:
            left = middle


# Time complexity: O(log n) -> standard binary search approach for the array => O(log n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> only 3 extra constant INTs used, none of them depends on input => O(1).
# -------------------
# Ok. Was trying to test my case with [1,2,3,4] and it was failing because we need to take middle +- 1 for
# switch if we're having EDGE peaks. But in this task we're given only this arrays:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# So PEAK is never going to be on EDGE, and we can just leave it as switch to the middle.
# -------------------
# Obviously the easiest way is to just find break_point where x - 1 < x > x + 1 or just last index.
# But it's a linear way and we need logarithmic.
# Basic improve from linear search to logarithmic is binary_search, so let's try this one first.
# So we need point where [x - 1] < x > [x + 1]. We can't use left or right pointers for this, cuz
# first it's going to be first/last indexes and after that it just some middle we already checked.
# So we need to check middle for that and switch left/right pointers to the middle.


test1 = [0, 1, 0]
test1_out = 1
assert test1_out == peak_index_of_mountain(test1)

test2 = [0, 2, 1, 0]
test2_out = 1
assert test2_out == peak_index_of_mountain(test2)

test3 = [0, 10, 5, 2]
test3_out = 1
assert test3_out == peak_index_of_mountain(test3)

test4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10]
test4_out = 14
assert test4_out == peak_index_of_mountain(test4)
