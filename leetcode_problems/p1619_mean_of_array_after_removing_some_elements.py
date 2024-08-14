# Given an integer array arr, return the mean of the remaining integers
#  after removing the smallest 5% and the largest 5% of the elements.
# Answers within 10-5 of the actual answer will be considered accepted.
# -------------------
# 20 <= arr.length <= 1000
# arr.length is a multiple of 20.
# 0 <= arr[i] <= 10 ** 5
from random import randint


def trim_mean(arr: list[int]) -> float:
    # working_sol (43.59%, 81.20%) -> (59ms, 16.64mb)  time: O(n * log n) | space: O(n)
    # ! arr.length is a multiple of 20. ! <- we can just take it every time.
    arr.sort()
    delete_elements: int = int(len(arr) / 100 * 5)
    out: list[int] = arr[delete_elements: len(arr) - delete_elements]
    return sum(out) / len(out)


# Time complexity: O(n * log n) <- n - length of the input array `arr`.
# Always sorting `arr` => O(n * log n).
# Extra deleting elements, in the worst case there's only 1 element to delete => O(n * log n + n).
# Extra traversing it to get `sum` => O(n * log n + n + n).
# -------------------
# Auxiliary space: O(n)
# `sort` <- takes O(n) by itself => O(n).
# `out` <- can be of size `n - 2` => O(n + n - 2).


test: list[int] = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]
test_out: float = 2.000
assert test_out == trim_mean(test)

test = [6, 2, 7, 5, 1, 2, 0, 3, 10, 2, 5, 0, 5, 5, 0, 8, 7, 6, 8, 0]
test_out = 4.000
assert test_out == trim_mean(test)

test = [6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 0, 7, 8, 1, 6, 8, 1, 1, 2, 4, 8, 1, 9, 5, 4, 3, 8, 5, 10, 8, 6, 6, 1, 0, 6, 10, 8,
        2, 3, 4]
test_out = 4.777777777777778
assert test_out == trim_mean(test)

test = [randint(0, 10 ** 5) for _ in range(1000)]
print(test)
