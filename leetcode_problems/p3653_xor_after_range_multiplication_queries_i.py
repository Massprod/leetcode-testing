# You are given an integer array nums of length n and a 2D integer array
#  queries of size q, where queries[i] = [li, ri, ki, vi].
# For each query, you must apply the following operations in order:
#  - Set idx = li.
#  - While idx <= ri:
#   - Update: nums[idx] = (nums[idx] * vi) % (109 + 7)
#   - Set idx += ki.
# Return the bitwise XOR of all elements in nums after processing all queries.
# --- --- --- ---
# 1 <= n == nums.length <= 10 ** 3
# 1 <= nums[i] <= 10 ** 9
# 1 <= q == queries.length <= 10 ** 3
# queries[i] = [li, ri, ki, vi]
# 0 <= li <= ri < n
# 1 <= ki <= n
# 1 <= vi <= 10 ** 5


def xor_after_queries(nums: list[int], queries: list[list[int]]) -> int:
    # working_solution: (18.45%, 96.34%) -> (1703ms, 19.99mb)  Time: O(n * n) Space: O(1)
    for l, r, k, v in queries:
        idx: int = l
        while idx <= r:
            nums[idx] = (nums[idx] * v) % (10 ** 9 + 7)
            idx += k
    out: int = 0
    for num in nums:
        out ^= num
    
    return out


# Time complexity: O(n * n)
# n - length of the input array `queries`.
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [1, 1, 1]
test_queries: list[list[int]] = [[0, 2, 1, 4]]
test_out: int = 4
assert test_out == xor_after_queries(test, test_queries)

test = [2, 3, 1, 5, 4]
test_queries = [[1, 4, 2, 3], [0, 2, 1, 2]]
test_out = 31
assert test_out == xor_after_queries(test, test_queries)
