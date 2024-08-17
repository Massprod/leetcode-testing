# You are given two 2D integer arrays, items1 and items2,
#  representing two sets of items.
# Each array items has the following properties:
#  - items[i] = [valuei, weighti] where valuei represents the value
#    and weighti represents the weight of the ith item.
#  - The value of each item in items is unique.
# Return a 2D integer array ret where ret[i] = [valuei, weighti],
#  with weighti being the sum of weights of all items with value valuei.
# Note: ret should be returned in ascending order by value.
# --------------------------
# 1 <= items1.length, items2.length <= 1000
# items1[i].length == items2[i].length == 2
# 1 <= valuei, weighti <= 1000
# Each valuei in items1 is unique.
# Each valuei in items2 is unique.
from random import randint
from collections import defaultdict


def merge_similar_items(items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
    # working_sol (61.43%, 84.89%) -> (108ms, 17.27mb)  time: O((n + m) * log (n + m)) | space: O(n + m)
    # { value_of_items: weight_sum_of_items}
    items: dict[int, int] = defaultdict(int)
    for item, weight in items1:
        items[item] += weight
    for item, weight in items2:
        items[item] += weight
    out: list[[list[int]]] = sorted(
        [[value, weight] for value, weight in items.items()],
        key=lambda x: x[0]
    )
    return out


# Time complexity: O((n + m) * log (n + m)) <- n - length of the input array `items1`,
#                                              m - length of the input array `items2`.
# In the worst case, every `value` in both arrays is unique.
# We will traverse both arrays, and extra traverse all the values again => O(n + m + (n + m))
# Extra sorting it with default `sorted` => O(2 * (n + m) + (n + m) * log (n + m)).
# --------------------------
# Auxiliary space: O(n + m)
# `items` <- will allocate space for every unique `value` => O(n + m)
# `out` <- will allocate space for every unique `value` as well => O(2 * (n + m)).


test_1: list[list[int]] = [[1, 1], [4, 5], [3, 8]]
test_2: list[list[int]] = [[3, 1], [1, 5]]
test_out: list[list[int]] = [[1, 6], [3, 9], [4, 5]]
assert test_out == merge_similar_items(test_1, test_2)

test_1 = [[1, 1], [3, 2], [2, 3]]
test_2 = [[2, 1], [3, 2], [1, 3]]
test_out = [[1, 4], [2, 4], [3, 4]]
assert test_out == merge_similar_items(test_1, test_2)

test_1 = [[1, 3], [2, 2]]
test_2 = [[7, 1], [2, 2], [1, 4]]
test_out = [[1, 7], [2, 4], [7, 1]]
assert test_out == merge_similar_items(test_1, test_2)
