# You are given a 0-indexed array nums of n integers, and an integer k.
# The k-radius average for a subarray of nums centered at some index i with the radius k is the average
#   of all elements in nums between the indices i - k and i + k (inclusive).
# If there are less than k elements before or after the index i, then the k-radius average is -1.
# Build and return an array avgs of length n where avgs[i] is the k-radius average
#   for the subarray centered at index i.
# The average of x elements is the sum of the x elements divided by x,
#   using integer division. The integer division truncates toward zero, which means losing its fractional part.
# For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75,
#   which truncates to 2.
# -------------------------
# n == nums.length
# 1 <= n <= 10 ** 5  ,  0 <= nums[i], k <= 10 ** 5


def get_averages(nums: list[int], k: int) -> list[int]:
    # working_sol (
    length: int = len(nums)
    for x in range(1, length):
        nums[x] = nums[x] + nums[x - 1]
    averages: list[int] = [-1 for _ in range(length)]
    shift: int | None = None
    for y in range(k, length):
        if (y + k) < length:
            if shift is None:
                shift = 0
                averages[y] = int(nums[y + k] / (k + k + 1))
                continue
            averages[y] = int((nums[y + k] - nums[shift]) / (k + k + 1))
            shift += 1
    return averages


# Time complexity: O(n) -> traversing once to sum everything in input_list(nums) => O(n) ->
# n - len of input_list^^| -> creating extra list to store averages with same size as input_list => O(n) ->
#                          -> for indexes in range(k, len(nums)) calculating average sum of subarray => O(log n) ->
#                          -> O(n) + O(n) + O(log n) => O(n).
# Auxiliary space: O(n) -> creating extra list of size n to store every average sums of sub_arrays => O(n).
# -------------------------
# SumUp everything and take values from index == (k + k + 1) - 1 (for zero index)??
# How is it medium_task then?
# Don't see how it could not work, let's try.


test1 = [7, 4, 3, 9, 1, 8, 5, 2, 6]
test1_k = 3
test1_out = [-1, -1, -1, 5, 4, 4, -1, -1, -1]
assert test1_out == get_averages(test1, test1_k)

test2 = [100000]
test2_k = 0
test2_out = [100000]
assert test2_out == get_averages(test2, test2_k)

test3 = [8]
test3_k = 100000
test3_out = [-1]
assert test3_out == get_averages(test3, test3_k)
