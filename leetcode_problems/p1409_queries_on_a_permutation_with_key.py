# Given the array queries of positive integers between 1 and m,
#  you have to process all queries[i] (from i=0 to i=queries.length-1) according to the following rules:
# In the beginning, you have the permutation P=[1,2,3,...,m].
# For the current i, find the position of queries[i] in the permutation P (indexing from 0)
#  and then move this at the beginning of the permutation P.
# Notice that the position of queries[i] in P is the result for queries[i].
# Return an array containing the result for the given queries.
# ---------------------------
# 1 <= m <= 10 ** 3
# 1 <= queries.length <= m
# 1 <= queries[i] <= m
from random import randint


def process_queries(queries: list[int], m: int) -> list[int]:
    # working_sol (72.12%, 87.67%) -> (52ms, 16.66mb)  time: O(m * m) | space: O(n + m)
    out: list[int] = []
    targets_list: list[int] = [_ for _ in range(1, 1 + m)]
    for target in queries:
        target_ind: int = targets_list.index(target)
        out.append(target_ind)
        targets_list.remove(target)
        targets_list.insert(0, target)
    return out


# Time complexity: O(m * m)
# In the worst case `len(queries) == m`, and we will always query the last index.
# So, every query => get last index O(m) + remove this index => O(m) + insert new index and shift others => O(m).
# Repeats for each query => O(m * 3m)
# ---------------------------
# Auxiliary space: O(n + m) <- n - length of the input array `queries`.
# `out` <- allocates space for each query result => O(n).
# `target_list` <- allocates space for values in range `1 -> m` => O(n + m)


test: list[int] = [3, 1, 2, 1]
test_m: int = 5
test_out: list[int] = [2, 1, 2, 1]
assert test_out == process_queries(test, test_m)

test = [4, 1, 2, 2]
test_m = 4
test_out = [3, 1, 2, 0]
assert test_out == process_queries(test, test_m)

test = [7, 5, 5, 8, 3]
test_m = 8
test_out = [6, 5, 0, 7, 5]
assert test_out == process_queries(test, test_m)

test = [randint(1, 10 ** 3) for _ in range(10 ** 3)]
print(test)
