# You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
# That is, each element of nums is covered by exactly one of the ranges,
#   and there is no integer x such that x is in one of the ranges but not in nums.
# Each range [a,b] in the list should be output as:
#   "a->b" if a != b
#   "a" if a == b
# -------------------
# 0 <= nums.length <= 20
# -2 ** 31 <= nums[i] <= 2 ** 31 - 1
# All the values of nums are unique.
# nums is sorted in ascending order.


def summary_ranges(nums: list[int]) -> list[str] | list[int]:
    # working_sol (97.74%, 81.48%) -> (27ms, 16.2mb)  time: O(n) | space: O(n)
    if len(nums) == 0:
        return nums
    if len(nums) == 1:
        return [str(nums[0])]
    ranges: list[str] = []
    # Start or range by itself == nums[0].
    cur_range: str = str(nums[0])
    is_range: bool = False
    for x in range(1, len(nums)):
        if nums[x] - nums[x-1] == 1:
            is_range = True
            if x == len(nums) - 1:
                cur_range += f"->{nums[x]}"
                ranges.append(cur_range)
        else:
            if is_range:
                cur_range += f"->{nums[x - 1]}"
                is_range = False
            ranges.append(cur_range)
            cur_range = str(nums[x])
            if x == len(nums) - 1:
                ranges.append(cur_range)
    return ranges


# Time complexity: O(n) -> traversing input_list only once in any case => O(n).
# n - len of input array^^|
# Auxiliary space: O(n) -> in the worst case we're having input without ranges, and creating duplicated list with
#                          the same values as original list but changed into a strings => O(n).
# -------------------
# All should be incremented by 1 to be correct range().


test: list[int] = [0, 1, 2, 4, 5, 7]
test_out: list[str] = ["0->2", "4->5", "7"]
assert test_out == summary_ranges(test)

test = [0, 2, 3, 4, 6, 8, 9]
test_out = ["0", "2->4", "6", "8->9"]
assert test_out == summary_ranges(test)
