# An array is considered special if every pair of its adjacent elements contains two numbers with different parity.
# You are given an array of integer nums and a 2D integer matrix queries, where for queries[i] = [fromi, toi]
#   your task is to check that subarray nums[fromi..toi] is special or not.
# Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.
# -------------------------------
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 5
# 1 <= queries.length <= 10 ** 5
# queries[i].length == 2
# 0 <= queries[i][0] <= queries[i][1] <= nums.length - 1
from random import randint


def is_array_special(nums: list[int], queries: list[list[int]]) -> list[bool]:
    # working_sol: (98.68%, 55.04%) -> (24ms, 46.57mb)  time: O(n + m) | space: O(n + m)
    start: int
    end: int
    # First value is always correct array.
    prefix: int = 0
    prefixes: list[int] = [prefix]
    # All we essentially care is breakPoints.
    # Indexes on which we're getting the same parity.
    # These indexes, breaks special array and we're building a new one.
    # But if there's no breakpoint == correct.
    for index in range(1, len(nums)):
        parity_1: int = nums[index] % 2
        parity_2: int = nums[index - 1] % 2
        if parity_1 == parity_2:
            prefix += 1
        prefixes.append(prefix)
    
    out: list[bool] = []
    # Same # of breakpoints == we didn't get a new breakpoint in between == correct.
    for start, end in queries:
        out.append(
            prefixes[start] == prefixes[end]
        )
    return out


# Time complexity: O(n + m) <- n - length of the input array `nums`, m - length of the input array `queries`.
# Always traversing whole input array `nums`, to get all the prefixes => O(n).
# Extra travresing whole input array `queries`, to check all the pairs => O(n + m).
# -------------------------------
# Auxiliary space: O(n + m)
# `prefixes` <- allocates space for each value in `nums` => O(n).
# `out` <- allocates space for each query in `queries` => O(n + m).


test: list[int] = [3,4,1,2,6]
test_queries: list[list[int]] = [[0, 4]]
test_out: list[bool] = [False]
assert test_out == is_array_special(test, test_queries)

test = [4, 3, 1, 6]
test_queries = [[0, 2], [2, 3]]
test_out = [False, True]
assert test_out == is_array_special(test, test_queries)
