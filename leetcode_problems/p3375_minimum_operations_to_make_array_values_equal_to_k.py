# You are given an integer array nums and an integer k.
# An integer h is called valid if all values in the array that are strictly greater than h are identical.
# For example, if nums = [10, 8, 10, 8], a valid integer is h = 9 because all nums[i] > 9 are equal to 10,
#  but 5 is not a valid integer.
# You are allowed to perform the following operation on nums:
#  - Select an integer h that is valid for the current values in nums.
#  - For each index i where nums[i] > h, set nums[i] to h.
# Return the minimum number of operations required to make every element in nums equal to k.
# If it is impossible to make all elements equal to k, return -1.
# -----------------------------
# 1 <= nums.length <= 100 
# 1 <= nums[i] <= 100
# 1 <= k <= 100


def min_operations(nums: list[int], k: int) -> int:
    # working_sol: (95.78%, 90.13%) -> (55ms, 17.16mb)  time: O(n) | space: O(n)
    uniques: set[int] = set()
    for val in nums:
        if val < k:
            return -1
        elif k == val:
            continue
        uniques.add(val)
    return len(uniques)


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always travervsing whole input array `nums` to get unique elements => O(n).
# -----------------------------
# Auxiliary space: O(n)
# In the worst case, there's only unique values and all of them higher than `k`.
# `nums` <- allocates space for each value from `nums` => O(n).


test: list[int] = [5, 2, 5, 4, 5]
test_k: int = 2
test_out: int = 2
assert test_out == min_operations(test, test_k)

test = [2, 1, 2]
test_k = 2
test_out = -1
assert test_out == min_operations(test, test_k)

test = [9, 7, 5, 3]
test_k = 1
test_out = 4
assert test_out == min_operations(test, test_k)
