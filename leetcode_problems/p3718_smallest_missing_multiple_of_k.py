# Given an integer array nums and an integer k,
#  return the smallest positive multiple of k that is missing from nums.
# A multiple of k is any positive integer divisible by k.
# --- --- --- ---
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
# 1 <= k <= 100


def missing_multiple(nums: list[int], k: int) -> int:
    # working_solution: (100%, 53.35%) -> (0ms, 19.22mb)  Time: O(n) Space: O(n)
    out: int = k
    fast_nums: set[int] = set(nums)
    while out in fast_nums:
        out += k

    return out


# Time complexity: O(n)
# n - length of the input array `nums`
# --- --- --- ---
# Space complexity: O(n)


test: list[int] = [8, 2, 3, 4, 6]
test_k: int = 2
test_out: int = 10
assert test_out == missing_multiple(test, test_k)

test = [1, 4, 7, 10, 15]
test_k = 5
test_out = 5
assert test_out == missing_multiple(test, test_k)
