# You are given an integer array nums of length n and a 2D
#  array queries where queries[i] = [li, ri, vali].
# Each queries[i] represents the following action on nums:
#  - Decrement the value at each index in the range [li, ri] in nums by at most vali.
#  - The amount by which each value is decremented can be chosen independently
#    for each index.
# A Zero Array is an array with all its elements equal to 0.
# Return the minimum possible non-negative value of k,
#  such that after processing the first k queries in sequence,
#  nums becomes a Zero Array.
# If no such k exists, return -1.
# ----------------------------
# 1 <= nums.length <= 10 ** 5
# 0 <= nums[i] <= 5 * 10 ** 5
# 1 <= queries.length <= 10 ** 5
# queries[i].length == 3
# 0 <= li <= ri < nums.length
# 1 <= vali <= 5


def min_zero_array(nums: list[int], queries: list[list[int]]) -> int:
    # working_sol (81.80%, 18.43%) -> (159ms, 64.35mb)  time: O(n + k) | space: O(n)
    start: int
    end: int
    value: int
    out: int = 0
    run_sum: int = 0
    difference_array = [0 for _ in range(len(nums) + 1)]
    for index in range(len(nums)):
        # We can't cover value with current running sum.
        # So, we need to use an extra query.
        while run_sum + difference_array[index] < nums[index]:
            out += 1
            # We already used every query.
            # But we need more => can't be done.
            if out > len(queries):
                return -1
            
            start, end, value = queries[out - 1]
            # Add value at the start of the range.
            # Add negative at the end.
            # We check if we can cover the value on `nums[index]`
            #  with running sum which increases by the value we take out
            #  in the start of the range and decreases by the (end + 1)
            #  => start of the next range.
            if index <= end:
                difference_array[max(start, index)] += value
                difference_array[end + 1] -= value
        run_sum += difference_array[index]
    
    return out


# Time complexity: O(n + k) <- n - length of the input array `nums`,
#                              k - length of the input array `queries`.
# Always using every index of the both input arrays, once => O(n + k).
# ----------------------------
# Auxiliary space: O(n)
# `difference_array` <- allocates space for `n + 1` values => O(n + 1).


test: list[int] = [2, 0, 2]
test_queries: list[list[int]] = [[0, 2, 1], [0, 2, 1], [1, 1, 3]]
test_out: int = 2
assert test_out == min_zero_array(test, test_queries)

test = [4, 3, 2, 1]
test_queries = [[1, 3, 2], [0, 2, 1]]
test_out = -1
assert test_out == min_zero_array(test, test_queries)
