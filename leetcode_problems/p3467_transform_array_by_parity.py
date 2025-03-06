# You are given an integer array nums.
# Transform nums by performing the following operations in the exact order specified:
#  1) Replace each even number with 0.
#  2) Replace each odd numbers with 1.
#  3) Sort the modified array in non-decreasing order.
# Return the resulting array after performing these operations.
# -----------------------
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 1000


def transform_array(nums: list[int]) -> list[int]:
    # working_sol (100.00%, 86.33%) -> (0ms, 17.77mb)  time: O(n) | space: O(n)
    out: list[int] = [0 for _ in nums]
    odd_index: int = -1
    for num in nums:
        if num % 2:
            out[odd_index] = 1
            odd_index -= 1

    return out
    

# Time complexity: O(n) <- n - length of the input array `nums`
# Always traversing whole input array `nums`, twice => O(2 * n).
# -----------------------
# Auxiliary space: O(n)
# `out` <- allocates space for each value from `nums` => O(n).


test: list[int] = [4, 3, 2, 1]
test_out: list[int] = [0, 0, 1, 1]
assert test_out == transform_array(test)

test = [1, 5, 1, 4, 2]
test_out = [0, 0, 1, 1, 1]
assert test_out == transform_array(test)
