# You are given a bitonic array nums of length n.
# Split the array into two parts:
#  - Ascending part: from index 0 to the peak element (inclusive).
#  - Descending part: from the peak element to index n - 1 (inclusive).
# The peak element belongs to both parts.
# Return:
#  - 0 if the sum of the ascending part is greater.
#  - 1 if the sum of the descending part is greater.
#  - -1 if both sums are equal.
# Notes:
#  - A bitonic array is an array that is strictly increasing up to a single peak element
#    and then strictly decreasing.
#  - An array is said to be strictly increasing if each element is strictly greater than
#    its previous one (if exists).
#  - An array is said to be strictly decreasing if each element is strictly smaller than
#    its previous one (if exists).
# --- --- --- ---
# 3 <= n == nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 9
# nums is a bitonic array.


def compare_bitonic_sums(nums: list[int]) -> int:
    # working_solution: (84.72%, 68.15%) -> (17ms, 35.04mb)  Time: O(n) Space: O(1)
    sum_asc: int = 0
    sum_desc: int = 0
    peak: int = 0
    for index in range(len(nums) - 1):
        if nums[index] > nums[index + 1]:
            peak = index
            break
    sum_asc = sum(nums[:peak + 1])
    sum_desc = sum(nums[peak:])
    if sum_asc > sum_desc:
        return 0
    elif sum_asc < sum_desc:
        return 1
    return -1


# Time complexity: O(n)
# n - legnth of the input array `nums`
# --- --- --- ---
# Space complexity: O(n)


test: list[int] = [1, 3, 2, 1]
test_out: int = 1
assert test_out == compare_bitonic_sums(test)

test = [2, 4, 5, 2]
test_out = 0
assert test_out == compare_bitonic_sums(test)

test = [1, 2, 4, 3]
test_out = -1
assert test_out == compare_bitonic_sums(test)
