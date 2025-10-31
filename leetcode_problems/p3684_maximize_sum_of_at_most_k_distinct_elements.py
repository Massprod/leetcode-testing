# You are given a positive integer array nums and an integer k.
# Choose at most k elements from nums so that their sum is maximized.
# However, the chosen numbers must be distinct.
# Return an array containing the chosen numbers in strictly descending order.
# --- --- --- ---
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 10 ** 9
# 1 <= k <= nums.length


def max_k_distinct(nums: list[int], k: int) -> list[int]:
    # working_solution: (100%, 96.42%) -> (0ms, 17.70mb)  Time: O(n * log n) Space: O(n)
    return sorted(set(nums), reverse=True)[:k]


# Time complexity: O(n * log n) <- n - length of the input array `nums`.
# First, we remove all duplicates => O(n).
# ! In the worst case, there's no duplicates.
# Second, sorting to get the correct order => O(n + n * log n).
# Third, we slice `k` elements => O(n + n * log n + k).
# --- --- --- ---
# Space complexity: O(n)
# `set` <- allocates space for the `n` elements => O(n).
# `sorted` <- allocates space for the `n` elements array => O(2 * n).
# In the worst case `k` == len(nums).
# So, we allocate extra space for the input array copy => O(3 * n).


test: list[int] = [84, 93, 100, 77, 90]
test_k: int = 3
test_out: list[int] = [100, 93, 90]
assert test_out == max_k_distinct(test, test_k)

test = [84, 93, 100, 77, 93]
test_k = 3
test_out = [100, 93, 84]
assert test_out == max_k_distinct(test, test_k)

test = [1, 1, 1, 2, 2, 2]
test_k = 6
test_out = [2, 1]
assert test_out == max_k_distinct(test, test_k)
