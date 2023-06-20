# You are given a 0-indexed array of distinct integers nums.
# There is an element in nums that has the lowest value and an element that has the highest value.
# We call them the minimum and maximum respectively. Your goal is to remove both these elements from the array.
# A deletion is defined as either removing an element from the front of the array or
#   removing an element from the back of the array.
# Return the minimum number of deletions it would take to remove both the minimum and maximum element from the array.
# ---------------------------
# 1 <= nums.length <= 10 ** 5
# -10 ** 5 <= nums[i] <= 10 ** 5
# The integers in nums are distinct.


def minimum_deletions(nums: list[int]) -> int:
    # working_sol (86.91%, 18.32%) -> (878ms, 31.5mb)  time: O(n) | space: O(1)
    if len(nums) == 1:
        return 1
    # finding min_max values and their indexes
    min_val: tuple[int, int] = (nums[0], 0)
    max_val: tuple[int, int] = (nums[0], 0)
    for x in range(1, len(nums)):
        if nums[x] < min_val[0]:
            min_val = (nums[x], x)
        elif nums[x] > max_val[0]:
            max_val = (nums[x], x)
    # finding what most left, right elements
    if min_val[1] < max_val[1]:
        left_index: int = min_val[1]
        right_index: int = max_val[1]
    else:
        left_index: int = max_val[1]
        right_index: int = min_val[1]
    # 3 unique options to delete: from left, from right, from both sides.
    del_left_option: int = right_index + 1  # zero indexed by default
    del_right_option: int = len(nums) - left_index  # len(nums) is already + 1 to ignore zero indexes
    del_both_option: int = (left_index + 1) + (len(nums) - right_index)
    return min(del_left_option, del_both_option, del_right_option)


# Time complexity: O(n) -> traversing whole input_list to find min, max values and their indexes => O(n) ->
# n - len of input_list^^| -> finding most left and right elements and calculating options => O(1) -> O(n).
# Auxiliary space: O(1) -> only constants used, all of them doesn't depend on input => O(1).
#                          ^^Actually tuples depends on input, but we're given constraint, so we're always
#                            going to have at least 1 element, and tuples will be set as default(nums[0], 0).
# ---------------------------
# There's no duplicates ! The integers in nums are distinct. !, and I don't see any other tricky parts, let's fail.
# ---------------------------
# I guess there's 3 options to consider for deletion:
#   1 -> we're counting all steps from left to max, min
#   2 -> we're counting all steps from right to max, min
#   3 -> we're counting all steps from left to most left, and from right to most right
#   min(1, 2, 3) => should be best option. Let's try.


test1 = [2, 10, 7, 5, 4, 1, 8, 6]
test1_out = 5
print(minimum_deletions(test1))
assert test1_out == minimum_deletions(test1)

test2 = [0, -4, 19, 1, 8, -2, -3, 5]
test2_out = 3
print(minimum_deletions(test2))
assert test2_out == minimum_deletions(test2)

test3 = [101]
test3_out = 1
print(minimum_deletions(test3))
assert test3_out == minimum_deletions(test3)

test4 = [10, 11, 12, 13, 14, 1, 18, 5, 6, 4, 3, 2, 9]
test4_out = 7
print(minimum_deletions(test4))
assert test4_out == minimum_deletions(test4)
