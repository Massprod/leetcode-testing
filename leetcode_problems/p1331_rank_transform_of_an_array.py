# Given an array of integers arr, replace each element with its rank.
# The rank represents how large the element is. The rank has the following rules:
#  - Rank is an integer starting from 1.
#  - The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
#  - Rank should be as small as possible.
# ---------------------
# 0 <= arr.length <= 10 ** 5
# -10 ** 9 <= arr[i] <= 10 ** 9
from random import randint


def array_rank_transform(arr: list[int]) -> list[int]:
    # working_sol (29.75%, 65.57%) -> (257ms, 34.41mb)  time: O(n * log n) | space: O(n)
    if not arr:
        return arr
    indexed: list[tuple[int, int]] = [(index, arr[index]) for index in range(len(arr))]
    indexed.sort(key=lambda x: x[1])
    rank: int = 1
    prev_val: int = indexed[0][1]
    for orig_index, value in indexed:
        if prev_val != value:
            prev_val = value
            rank += 1
        arr[orig_index] = rank
    return arr


# Time complexity: O(n * log n) <- n - length of the input array `arr`.
# Always building `indexed` from original `arr` => O(n).
# Sorting it with standard `sort` => O(n + n * log n).
# Extra traversing every index after sorting => O(2 * n + n * log n).
# ---------------------
# Auxiliary space: O(n)
# `indexed` <- always of the same size as `arr` => O(n).
# `sort` <- extra takes O(n) while sorting => O(2 * n).


test: list[int] = [40, 10, 20, 30]
test_out: list[int] = [4, 1, 2, 3]
assert test_out == array_rank_transform(test)

test = [100, 100, 100]
test_out = [1, 1, 1]
assert test_out == array_rank_transform(test)

test = [37, 12, 28, 9, 100, 56, 80, 5, 12]
test_out = [5, 3, 4, 2, 8, 6, 7, 1, 3]
assert test_out == array_rank_transform(test)

test = [randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 3)]
print(test)
