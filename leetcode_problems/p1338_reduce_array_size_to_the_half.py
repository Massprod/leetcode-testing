# You are given an integer array arr.
# You can choose a set of integers
#  and remove all the occurrences of these integers in the array.
# Return the minimum size of the set so that at least half of the integers
#  of the array are removed.
# -----------------------
# 2 <= arr.length <= 10 ** 5
# arr.length is even.
# 1 <= arr[i] <= 10 ** 5
from collections import Counter

from random import randint

from pyperclip import copy


def min_set_size(arr: list[int]) -> int:
    # working_sol (55.11%, 28.78%) -> (56ms, 41.28mb)  time: O(n * log n) | space: O(n)
    value: int
    occurs: int
    # { value: occurrences }
    values: dict[int, int] = Counter(arr)
    # Greedy => use maximum occurrences and check length after it.
    leftovers: int = len(arr)
    half: int = leftovers // 2 + 1 if len(arr) % 2 else leftovers // 2
    sorted_values: list[tuple[int, int]] = (
        sorted(values.items(), key=lambda x: x[1], reverse=True)
    )
    out: int = 0
    for option in sorted_values:
        value, occurs = option
        leftovers -= occurs
        out += 1
        if leftovers <= half:
            break

    return out


# Time complexity: O(n * log n) <- n - length of the input array `arr`.
# We're always sorting input array `arr` => O(n * log n).
# And extra traversing sorted values, once => O((n * log n) + n).
# -----------------------
# Auxiliary space: O(n)
# `sort` => O(n).
# In the worst case, there's only unique value in `arr`.
# `values` <- allocates space for each unique value from `arr` => O(n).


test: list[int] = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
test_out: int = 2
assert test_out == min_set_size(test)

test = [7, 7, 7, 7, 7, 7]
test_out = 1
assert test_out == min_set_size(test)

test = [1, 9]
test_out =1
assert test_out == min_set_size(test)

test = [randint(1, 10 ** 5) for _ in range(10 ** 5)]
copy(test)
