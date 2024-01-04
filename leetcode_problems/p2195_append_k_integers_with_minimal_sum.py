# You are given an integer array nums and an integer k.
# Append k unique positive integers that do not appear in nums to nums such that the resulting total sum is minimum.
# Return the sum of the k integers appended to nums.
# ------------------------
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 9
# 1 <= k <= 10 ** 8


def minimal_k_sum(nums: list[int], k: int) -> int:
    # working_sol (98.95%, 46.07%) -> (507ms, 31.62mb)  time: O(n * log n) | space: O(n)
    # We can take sum 1 -> k, inclusive as base.
    # And if we meet something from 1 -> k in `nums`.
    # We can take it out from this sum, change current highest == k, to (k + 1).
    # And change sum accordingly: sum += (k - val).
    cur_sum: int = k * (k + 1) // 2
    prev: int = 0
    for val in sorted(nums):
        # Ignore duplicates.
        if prev < val:
            if val <= k:
                cur_sum -= val
                k += 1
                cur_sum += k
            else:
                break
            prev = val
    return cur_sum


# Time complexity: O(n * log n) <- n - length of input array `nums`.
# Single traverse of `nums`, but we sort() it before => O(n * log n).
# Auxiliary space: O(n).
# Standard builtin sort() takes O(n) space.
# Extra 2 constant INTs.


test: list[int] = [1, 4, 25, 10, 25]
test_k: int = 2
test_out: int = 5
assert test_out == minimal_k_sum(test, test_k)

test = [5, 6]
test_k = 6
test_out = 25
assert test_out == minimal_k_sum(test, test_k)

test = [1]
test_k = 10000000
test_out = 50000015000000
assert test_out == minimal_k_sum(test, test_k)
