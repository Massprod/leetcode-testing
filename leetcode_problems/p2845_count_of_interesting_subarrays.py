# You are given a 0-indexed integer array nums, an integer modulo, and an integer k.
# Your task is to find the count of subarrays that are interesting.
# A subarray nums[l..r] is interesting if the following condition holds:
#  - Let cnt be the number of indices i in the range [l, r]
#    such that nums[i] % modulo == k. Then, cnt % modulo == k.
# Return an integer denoting the count of interesting subarrays.
# Note: A subarray is a contiguous non-empty sequence of elements within an array.
# ------------------
# 1 <= nums.length <= 10 ** 5 
# 1 <= nums[i] <= 10 ** 9
# 1 <= modulo <= 10 ** 9
# 0 <= k < modulo


def count_interesting_subarrays(nums: list[int], modulo: int, k: int) -> int:
    # working_sol (69.54%, 78.74%) -> (140ms, 38.78mb)  time: O(n) | space: O(n)
    out: int = 0
    prefix: int = 0
    # Standard case (0 -> 1)
    occurs: dict[int, int] = {0: 1}
    for value in nums:
        if (value % modulo) == k:
            prefix += 1
        check: int = (prefix - k + modulo) % modulo
        out += occurs.get(check, 0)
        prev_prefixes: int = prefix % modulo
        if prev_prefixes in occurs:
            occurs[prev_prefixes] += 1
        else:
            occurs[prev_prefixes] = 1
    
    return out


# Time complexity: O(n) <- n - legnth of the input array `nums`.
# Always traversing whole input array `nums`, once => O(n).
# ------------------
# Auxiliary space: O(n)
# In the worst case every value will give us unique `prev_prefixes`.
# `occurs` <- allocates space for each of them => O(n).


test: list[int] = [3, 2, 4]
test_modulo: int = 2
test_k: int = 1
test_out: int = 3
assert test_out == count_interesting_subarrays(
    test, test_modulo, test_k
)

test = [3, 1, 9, 6]
test_modulo = 3
test_k = 0
test_out = 2
assert test_out == count_interesting_subarrays(
    test, test_modulo, test_k
)
