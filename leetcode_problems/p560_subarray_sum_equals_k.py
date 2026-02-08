# Given an array of integers nums and an integer k,
#  return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.
# --- --- --- ---
# 1 <= nums.length <= 2 * 10 ** 4
# -1000 <= nums[i] <= 1000
# -10 ** 7 <= k <= 10 ** 7
from  collections import defaultdict


def subarray_sum(nums: list[int], k: int) -> int:
    # working_solution: (49.32%, 24.28%) -> (35ms, 22.08mb)  Time: O(n) Space: O(n)
    # nums[:right] - nums[:left] = k
    # nums[:left] = nums[:right] - k
    # So, we can basically store what we already traversed and if we get any index
    #  with nums[left], we increase the count and we can build from this index.
    # { nums[:left]: count }
    prefix_sums: dict[int, int] = defaultdict(int)
    out: int = 0
    run_sum: int = 0
    prefix_sums[run_sum] += 1
    for num in nums:
        run_sum += num
        nums_left: int = run_sum - k
        out += prefix_sums.get(nums_left, 0)
        prefix_sums[run_sum] += 1
    
    return out


# Time complexity: O(n)
# n - length of the input array `nums`.
# ---
# Always traversing the whole input array `nums`, once => O(n).
# --- --- --- ---
# Space complexity: O(n)
# `prefix_sums` <- allocates space for each unique sum


test: list[int] = [1, 1, 1]
test_k: int = 2
test_out: int = 2
assert test_out == subarray_sum(test, test_k)

test = [1, 2, 3]
test_k = 3
test_out = 2
assert test_out == subarray_sum(test, test_k)
