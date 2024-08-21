# Given an array of positive integers nums,
#  return the maximum possible sum of an ascending subarray in nums.
# A subarray is defined as a contiguous sequence of numbers in an array.
# A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i
#  where l <= i < r, numsi  < numsi+1.
# Note that a subarray of size 1 is ascending.
# -------------------------
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


def max_ascending_sum(nums: list[int]) -> int:
    # working_sol (95.31%, 66.56%) -> (29ms, 16.50mb)  time: O(n) | space: O(1)
    out: int = 0
    cur_sub: int = nums[0]
    for index in range(1, len(nums)):
        if nums[index - 1] < nums[index]:
            cur_sub += nums[index]
        else:
            out = max(out, cur_sub)
            cur_sub = nums[index]
    return max(out, cur_sub)


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing `nums`, once => O(n).
# -------------------------
# Auxiliary space: O(1).


test: list[int] = [10, 20, 30, 5, 10, 50]
test_out: int = 65
assert test_out == max_ascending_sum(test)

test = [10, 20, 30, 40, 50]
test_out = 150
assert test_out == max_ascending_sum(test)

test = [12, 17, 15, 13, 10, 11, 12]
test_out = 33
assert test_out == max_ascending_sum(test)
