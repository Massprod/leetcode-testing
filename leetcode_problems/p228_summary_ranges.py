# You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
# That is, each element of nums is covered by exactly one of the ranges,
#   and there is no integer x such that x is in one of the ranges but not in nums.
# Each range [a,b] in the list should be output as:
#   "a->b" if a != b
#   "a" if a == b
# -------------------
# 0 <= nums.length <= 20  ,  -2 ** 31 <= nums[i] <= 2 ** 31 - 1
# All the values of nums are unique.
# nums is sorted in ascending order.


def summary_ranges(nums: list[int]) -> list[str] | list[int]:
    # working_sol (47.11%, 81.48%) -> (46ms, 16.2mb)  time: O(n) | space: O(n)
    if len(nums) == 0:
        return nums
    if len(nums) == 1:
        return [str(nums[0])]
    prev: int = nums[0]
    ranges: list[str] = []
    cur_range: str = str(prev)
    is_range: bool = False
    for x in range(1, len(nums)):
        current: int = nums[x]
        if current - prev == 1:
            prev = current
            is_range = True
            if x == len(nums) - 1:
                cur_range += f"->{prev}"
                ranges.append(cur_range)
        elif current - prev > 1:
            if is_range:
                cur_range += f"->{prev}"
                is_range = False
            ranges.append(cur_range)
            prev = current
            cur_range = str(current)
            if x == len(nums) - 1:
                ranges.append(cur_range)
    return ranges


# Time complexity: O(n) -> traversing input_list only once in any case=> O(n)
# n - len of input_list^^|
# Auxiliary space: O(n) -> in the worst case we're having input without ranges, and creating duplicated list with
#                          the same values as original list but changed into a strings => O(n)
# -------------------
# All should be incremented by 1 to be correct range().


test1 = [0, 1, 2, 4, 5, 7]
test1_out = ["0->2", "4->5", "7"]
print(summary_ranges(test1))
assert test1_out == summary_ranges(test1)

test2 = [0, 2, 3, 4, 6, 8, 9]
test2_out = ["0", "2->4", "6", "8->9"]
print(summary_ranges(test2))
assert test2_out == summary_ranges(test2)
