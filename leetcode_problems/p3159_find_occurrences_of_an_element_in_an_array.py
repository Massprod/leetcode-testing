# You are given an integer array nums, an integer array queries, and an integer x.
# For each queries[i], you need to find the index of the queries[i]th occurrence of x in the nums array.
# If there are fewer than queries[i] occurrences of x, the answer should be -1 for that query.
# Return an integer array answer containing the answers to all queries.
# -----------------------
# 1 <= nums.length, queries.length <= 10 ** 5
# 1 <= queries[i] <= 10 ** 5
# 1 <= nums[i], x <= 10 ** 4


def occurrences_of_element(nums: list[int], queries: list[int], x: int) -> list[int]:
    # working_sol (67.78%, 67.17%) -> (1222ms, 34.73mb)  time: O(n + k) | space: O(n + k)
    occurrences: dict[int, int] = {}
    occurs: int = 0
    for index, num in enumerate(nums):
        if num == x:
            occurs += 1
            occurrences[occurs] = index
    out: list[int] = []
    for query in queries:
        if query in occurrences:
            out.append(occurrences[query])
        else:
            out.append(-1)
    return out


# Time complexity: O(n + k) <- n - length of the input array `nums`, k - length of the input array `queries`.
# Always traversing whole input array `nums` to get all occurrences, once => O(n).
# Traversing every query from `queries`, once => O(k).
# -----------------------
# Auxiliary space: O(n + k)
# `occurrences` <- allocates space for every `index` from `nums` => O(n).
# `out` <- allocates space for result of each `query` => O(n + k).


test: list[int] = [1, 3, 1, 7]
test_queries: list[int] = [1, 3, 2, 4]
test_x: int = 1
test_out: list[int] = [0, -1, 2, -1]
assert test_out == occurrences_of_element(test, test_queries, test_x)

test = [1, 2, 3]
test_queries = [10]
test_x = 5
test_out = [-1]
assert test_out == occurrences_of_element(test, test_queries, test_x)
