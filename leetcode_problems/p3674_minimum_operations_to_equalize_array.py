# You are given an integer array nums of length n.
# In one operation, choose any subarray nums[l...r] (0 <= l <= r < n)
#  and replace each element in that subarray with the bitwise AND of all elements.
# Return the minimum number of operations required to make all elements of nums equal.
# A subarray is a contiguous non-empty sequence of elements within an array.
# --- --- --- ---
# 1 <= n == nums.length <= 100
# 1 <= nums[i] <= 10 ** 5


def min_operations(nums: list[int]) -> int:
    # working_solution: (20.43%, 67.15%) -> (3ms, 17.72mb)  Time: O(n) Space: O(n)
    # We can replace `any` subarray with `AND` of it's values.
    # Which is essentially making them equal in `one` move.
    # So, we either need to use this conversion and it's 1 move.
    # Or we don't need to use it and it's 0 moves.
    return 0 if 1 == len(set(nums)) else 1


# Time complexity: O(n) <- n - length of the input array `nums`.
# Converting the original input array into the `set` => O(n).
# --- --- --- ---
# Space complexity: O(n)


test: list[int] = [1, 2]
test_out: int = 1
assert test_out == min_operations(test)

test = [5, 5, 5]
test_out = 0
assert test_out == min_operations(test)
