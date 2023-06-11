# A peak element is an element that is strictly greater than its neighbors.
#   Given a 0-indexed integer array nums, find a peak element, and return its index.
#   If the array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞.
# In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
#
# You must write an algorithm that runs in O(log n) time.
# ----------------------
# 1 <= nums.length <= 1000  ,  -2 ** 31 <= nums[i] <= 2 ** 31 - 1
# nums[i] != nums[i + 1] for all valid i.
from random import randint


def find_peak_element(nums: list[int]) -> int:
    # working_sol (58.60%, 51.61%) -> (58ms, 16.4mb)  time: O(log n) | space: O(1)
    if len(nums) == 1:
        return 0
    # eliminate 2 unique cases
    if nums[0] > nums[1]:
        return 0
    if nums[-1] > nums[-2]:
        return len(nums) - 1
    left: int = 1
    right: int = len(nums) - 2
    while left < right:
        # extra checks to reduce calls in some cases
        if nums[left - 1] < nums[left] > nums[left + 1]:
            return left
        if nums[right - 1] < nums[right] > nums[right + 1]:
            return right
        middle: int = int((right + left) / 2)
        # peak check
        if nums[middle - 1] < nums[middle] > nums[middle + 1]:
            return middle
        # ascending half check
        elif nums[middle - 1] < nums[middle] < nums[middle + 1]:
            left = middle + 1
        # descending half check
        elif nums[middle + 1] < nums[middle] < nums[middle - 1]:
            right = middle - 1
        # duplicates or lowest, can be (right = middle - 1)
        elif nums[middle - 1] >= nums[middle] <= nums[middle + 1]:
            left = middle + 1
    # in the end right == left, so we can return either
    return left


# Time complexity: O(log n) -> default, binary search, but for breaking points not some number => O(log n)
# n - len of input_list^^|
# Space complexity: O(1) -> 3 extra constant INTs, doesn't depends on input => O(1)
# ----------------------
# Well in the end, did the same solution as I did in p154 but instead of recursion now it's iterative.
# Actually if I ever revisit 153 I can rebuild it to be constant_space.
# Because instead of slicing and searching in slice, we can just operate with indexes in original list like here.
# ----------------------
# Only way I know with searching in O(log n) is binary_search. How can we implement this?
# Break points?
# !
# an element is always considered to be strictly greater than a neighbor that is outside the array. !
# ^^Check first, last values to eliminate unique cases, because we cant check +1 -1 indexes for them.
# Search for a break_points instead of a some number, like in basic search.
# If something is getting bigger on the next index than it's always will break at some point into descending ->
# -> except unique case, with ascending to last_index, which we already checked.
# Same goes for descending, either unique case with everything descending into [0] index, or it breaks on the way.
# This break_points is always change from ascending to descending which is a PEAK, or
# from descending into ascending and if unique case is failed than there's 100% some other break point on the way,
# which will give us another PEAK. Should work.


test1 = [1, 2, 3, 1]
test1_out = 2
print(find_peak_element(test1))
assert test1_out == find_peak_element(test1)

test2 = [1, 2, 1, 3, 5, 6, 4]
test2_out = 1
print(find_peak_element(test2))
assert test2_out == find_peak_element(test2)

for _ in range(100):
    test_case: list[int] = [-2600] + [randint(-2500, 2500) for num in range(1000)]
    test_case = test_case + test_case.copy() + [-2600]  # eliminating unique cases
    test_out: set[int] = set()
    for x in range(1, (len(test_case) - 1)):
        if test_case[x - 1] < test_case[x] > test_case[x + 1]:
            test_out.add(x)
    test = find_peak_element(test_case)
    assert test in test_out
    test_out.clear()
