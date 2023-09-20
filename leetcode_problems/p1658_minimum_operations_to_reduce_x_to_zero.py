# You are given an integer array nums and an integer x.
# In one operation, you can either remove the leftmost or the rightmost element from the array nums
#   and subtract its value from x. Note that this modifies the array for future operations.
# Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.
# ---------------------------------
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 4
# 1 <= x <= 10 ** 9


def min_operations(nums: list[int], x: int) -> int:
    # working_sol (94.36%, 98.66%) -> (922ms, 30.16mb)  time: O(n) | space: O(1)
    # We can't delete side elements at all.
    if nums[0] > x and nums[-1] > x:
        return -1
    # We can delete just one == shortest.
    if nums[0] == x or nums[-1] == x:
        return 1
    max_sub_target: int = sum(nums) - x
    # Whole array gives sum of x.
    # So we need to delete everything.
    if max_sub_target == 0:
        return len(nums)
    # Whole array gives less than x.
    # So we can't reduce it to 0 at all.
    elif max_sub_target < 0:
        return -1
    # Placeholder value.
    minimum_operations: int = len(nums)
    sub_sum: int = 0
    start_index: int = 0
    # Standard sliding window.
    for y in range(len(nums)):
        sub_sum += nums[y]
        if sub_sum > max_sub_target:
            # Shrink window, and try to find correct subarray.
            while sub_sum > max_sub_target:
                sub_sum -= nums[start_index]
                start_index += 1
        # Subarray we need.
        if sub_sum == max_sub_target:
            operations: int = len(nums) - (y + 1 - start_index)
            # There's multiple, we need to find longest.
            # Longer subarray => lower operations to get it.
            minimum_operations = min(operations, minimum_operations)
    return minimum_operations


# Time complexity: O(n) -> worst case == [1,1,1,1,1,1 .. 1] and x == 1 ->  we will create window of size 1,
# n - len of input_list^^|  and shrink it for every index step -> so every index used at most twice => O(2n).
# Auxiliary space: O(1) -> only 4 extra constant INTs used, none of them depends on input => O(1).
# ---------------------------------
# W.e we delete from both sides, we will always stay with subarray of some kind.
# And we need to minimize delete operations, so it's BIGGER subarray == SMALLER operations number.
# Just check every subarray with sliding window, and find longest.


test: list[int] = [1, 1, 4, 2, 3]
test_x: int = 5
test_out: int = 2
assert test_out == min_operations(test, test_x)

test = [5, 6, 7, 8, 9]
test_x = 4
test_out = -1
assert test_out == min_operations(test, test_x)

test = [3, 2, 20, 1, 1, 3]
test_x = 10
test_out = 5
assert test_out == min_operations(test, test_x)

test = [3, 2, 10, 10, 10, 10, 1, 1, 3]
test_x = 20
test_out = 6
assert test_out == min_operations(test, test_x)

test = [5, 4, 3, 3, 3]
test_x = 9
test_out = 2
assert test_out == min_operations(test, test_x)

test = [1, 1]
test_x = 3
test_out = -1
assert test_out == min_operations(test, test_x)

test = [2, 3, 1, 1, 1]
test_x = 5
test_out = 2
assert test_out == min_operations(test, test_x)
