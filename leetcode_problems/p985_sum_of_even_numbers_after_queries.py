# You are given an integer array nums and an array queries where
#  queries[i] = [vali, indexi].
# For each query i, first, apply nums[indexi] = nums[indexi] + vali,
#  then print the sum of the even values of nums.
# Return an integer array answer where answer[i] is the answer to the ith query.
# ----------------------
# 1 <= nums.length <= 10 ** 4
# -10 ** 4 <= nums[i] <= 10 ** 4
# 1 <= queries.length <= 10 ** 4
# -10 ** 4 <= vali <= 10 ** 4
# 0 <= indexi < nums.length


def sum_even_after_queries(nums: list[int], queries: list[list[int]]) -> list[int]:
    # working_sol (84.33%, 64.93%) -> (10ms, 23.35mb)  time: O(n + m) | space: O(m)
    out: list[int] = []
    even_sum: int = 0
    for num in nums:
        if num % 2:
            continue
        even_sum += num
    
    for value, index in queries:
        cur_val: int = nums[index]
        if not cur_val % 2:
            even_sum -= cur_val
        new_val: int = cur_val + value
        nums[index] = new_val
        if not new_val % 2:
            even_sum += new_val
        out.append(even_sum)
        
    return out


# Time complexity: O(n + m) <- n - length of the input array `nums`,
#                              m - length of the input array `queries`.
# Traversing whole input array `nums`, to get the `even` sum => O(n).
# Traversing `queries` to check every query => O(n + m).
# ----------------------
# Auxiliary space: O(m)
# `out` <- allocates space for each query of the `queries` => O(m).


test: list[int] = [1, 2, 3, 4]
test_queries: list[list[int]] = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
test_out: list[int] = [8, 6, 2, 4]
assert test_out == sum_even_after_queries(test, test_queries)

test = [1]
test_queries = [[4, 0]]
test_out = [0]
assert test_out == sum_even_after_queries(test, test_queries)
