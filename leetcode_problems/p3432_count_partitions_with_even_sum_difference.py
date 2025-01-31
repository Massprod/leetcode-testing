# You are given an integer array nums of length n.
# A partition is defined as an index i where 0 <= i < n - 1,
#  splitting the array into two non-empty subarrays such that:
#  - Left subarray contains indices [0, i].
#  - Right subarray contains indices [i + 1, n - 1].
# Return the number of partitions where the difference
#  between the sum of the left and right subarrays is even.
# --------------------
# 2 <= n == nums.length <= 100
# 1 <= nums[i] <= 100


def count_partitions(nums: list[int]) -> int:
    # working_sol (100.00%, 47.77%) -> (0ms, 17.82mb)  time: O(n) | space: O(1)
    # [0, i] <- inclusive
    prefix: int = nums[0]
    # [i + 1, n - 1] <- inclusive
    suffix: int = sum(nums) - nums[0]

    out: int = 0
    for index in range(1, len(nums)):
        if not ((suffix - prefix) % 2):
            out += 1
        suffix -= nums[index]
        prefix += nums[index]

    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole input array `nums`, once => O(n).
# --------------------
# Auxiliary space: O(1).
# Only 2 contant INTs used, none of them depends on input => O(1). 


test: list[int] = [10, 10, 3, 7, 6]
test_out: int = 4
assert test_out == count_partitions(test)

test = [1, 2, 2]
test_out = 0
assert test_out == count_partitions(test)

test = [2, 4, 6, 8]
test_out = 3
assert test_out == count_partitions(test)
