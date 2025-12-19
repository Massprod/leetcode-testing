# You are given an integer array nums and an integer k.
# Find the absolute difference between:
#  - the sum of the k largest elements in the array; and
#  - the sum of the k smallest elements in the array.
# Return an integer denoting this difference.
# --- --- --- ---
# 1 <= n == nums.length <= 100
# 1 <= nums[i] <= 100
# 1 <= k <= n


def abs_difference(nums: list[int], k: int) -> int:
    # working_solution: (100%, 100%) -> (0ms, 17.04mb)  Time: O(n * log n + k) Space: O(1)
    nums.sort()
    return abs(sum(nums[-k:]) - sum(nums[:k]))


# Time complexity: O(n * log n + k)
# n - length of the input array `nums`.
# Always sorting `nums` to get the correct order => O(n * log n).
# Extra slicing `k` slices, twice => O(n * log n + 2 * k).
# And summing these slices => O(n * log n + 4 * k).
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [5, 2, 2, 4]
test_k: int = 2
test_out: int = 5
assert test_out == abs_difference(test, test_k)

test = [100]
test_k = 1
test_out = 0
assert test_out == abs_difference(test, test_k)
