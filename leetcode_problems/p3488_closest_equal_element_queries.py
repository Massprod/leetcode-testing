# You are given a circular array nums and an array queries.
# For each query i, you have to find the following:
#  - The minimum distance between the element at index queries[i]
#    and any other index j in the circular array, where nums[j] == nums[queries[i]].
#    If no such index exists, the answer for that query should be -1.
#  - Return an array answer of the same size as queries, where answer[i]
#    represents the result for query i.
# --- --- --- ---
# 1 <= queries.length <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 6
# 0 <= queries[i] < nums.length
from random import randint
from pyperclip import copy


def solve_queries(nums: list[int], queries: list[int]) -> list[int]:
    # working_solution: (5.47%, 5.47%) -> (729ms, 94.29mb)  Time: O(n + m) Space: O(n)
    t_limit: int = 10 ** 6
    # { value: [indexes where's present] | {internal map} }
    values: dict[int, dict] = {}
    for index, value in enumerate(nums):
        if value not in values:
            values[value] = {
                'indexes': [],
                'map': {}
            }
        value_indexes: list[int] = values[value]['indexes']
        value_int_map: dict[int, int] = values[value]['map']
        value_indexes.append(index)
        value_int_map[index] = len(value_indexes) - 1

    out: list[int] = []
    for query in queries:
        t_value: int = nums[query]
        t_indexes: list[int] = values[t_value]['indexes']
        t_map: dict[int, int] = values[t_value]['map']
        if 1 == len(t_indexes):
            out.append(-1)
            continue
        d_index: int = t_map[query]
        left_index: int = (d_index - 1)
        if 0 > left_index:
            left_index = len(t_indexes) - 1
            d_left: int = (len(nums) - t_indexes[left_index]) + t_indexes[d_index]
        else:
            d_left: int = abs(t_indexes[d_index] - t_indexes[left_index])
        if 0 == d_left:
            d_left = t_limit
        right_index: int = (d_index + 1)
        if len(t_indexes) <= right_index:
            right_index = 0
            d_right: int = abs(len(nums) - t_indexes[d_index] + t_indexes[right_index])
        else:
            d_right: int = abs(t_indexes[right_index] - t_indexes[d_index])
        if 0 == d_right:
            d_right = t_limit
        out.append(min(d_left, d_right))
    
    return out


# Time complexity: O(n + m)
# n - length of the input array `nums`
# m - length of the input array `queries`
# --- --- --- ---
# Space complexity: O(n)


test: list[int] = [1, 3, 1, 4, 1, 3, 2]
test_queries: list[int] = [0, 3, 5]
test_out: list[int] = [2, -1, 3]
assert test_out == solve_queries(test, test_queries)

test = [1, 2, 3, 4]
test_queries = [0, 1, 2, 3]
test_out = [-1, -1, -1, -1]
assert test_out == solve_queries(test, test_queries)

test = [randint(1, 10 ** 5) - 1 for _ in range(10 ** 5)]
copy(test)  # type: ignore
