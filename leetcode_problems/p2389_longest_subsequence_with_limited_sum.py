# You are given an integer array nums of length n,
#  and an integer array queries of length m.
# Return an array answer of length m where answer[i] is the maximum size of a subsequence
#  that you can take from nums such that the sum of its elements is less than or equal to queries[i]/
# A subsequence is an array that can be derived from another array by deleting some
#  or no elements without changing the order of the remaining elements.
# ---------------------------
# n == nums.length
# m == queries.length
# 1 <= n, m <= 1000
# 1 <= nums[i], queries[i] <= 10 ** 6
import pyperclip
from random import randint
from bisect import bisect_left


def answer_queries(nums: list[int], queries: list[int]) -> list[int]:
    # working_sol: (98.90%, 13.08%) -> (1ms, 18.08mb)  time: O(n * log n + k * log n) space: O(n + k)
    # !
    # subsequence is an array that can be derived from another array
    # by deleting some or no elemenths without changing the order
    # !
    # We're operating with a sum, so we don't care about order at all.
    # Only thing that matter is that can we use some elements to get correct
    #  summ or not.
    # And the most efficient way of searching correct subsequence.
    # It's to make smallest -> highest values.
    # Because, we need it to be a longest subsequence.
    nums.sort()
    # We either need to calc a running sum for every query.
    # Or we can just count prefixes of the sorted `nums` and reuse it.
    prefixes: list[int] = [nums[0]]
    for index in range(1, len(nums)):
        prefixes.append(
            prefixes[-1] + nums[index]
        )
    out: list[int] = []
    for query in queries:
        place_index: int = bisect_left(
            prefixes, query
        )
        # We can't use prefix we found == this element excluded.
        sub_length: int = place_index
        # We got prefix equal to query == this element included.
        if (place_index < len(prefixes)
              and prefixes[place_index] == query):
            sub_length += 1
        out.append(
            sub_length
        )
    
    return out


# Time complexity: O(n * log n + k * log n) <- n - length of the input array `nums`,
#                                              k - length of the input array `queries`.
# Always sorting `nums` to get correct order to count => O(n * log n).
# Counting running sum => O(n + n * log n).
# For every query in `queries` searching for it's placement in `prefixes` => O(k * log n)
# ---------------------------
# Auxiliary space: O(n + k)
# Sort takes O(n) => O(n).
# `prefixes` <- always of the same length as an input array `nums` => O(2 * n).
# `out` <- always of the same size as `queries` => O(2 * n + k).


test: list[int] = [4,5,2,1]
test_queries: list[int] = [3, 10, 21]
test_out: list[int] = [2, 3, 4]
assert test_out == answer_queries(test, test_queries)

test = [2,3,4,5]
test_queries = [1]
test_out = [0]
assert test_out == answer_queries(test, test_queries)

test = [randint(1, 10 ** 6) for _ in range(800)]
pyperclip.copy(test)
