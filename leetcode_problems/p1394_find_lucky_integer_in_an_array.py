# Given an array of integers arr,
#  a lucky integer is an integer that has a frequency in the array equal to its value.
# Return the largest lucky integer in the array.
# If there is no lucky integer return -1.
# ------------------
# 1 <= arr.length <= 500
# 1 <= arr[i] <= 500
from collections import Counter


def find_lucky(arr: list[int]) -> int:
    # working_sol (70.29%, 71.71%) -> (55ms, 16.57mb)  time: O(n) | space: O(n)
    out: int = -1
    # {value: occurrences}
    frequencies: dict[int, int] = Counter(arr)
    for key, value in frequencies.items():
        if key == value:
            out = max(key, out)
    return out


# Time complexity: O(n) <- n - length of the input array `arr`.
# We're always traversing whole input array `arr` to get all occurrences => O(n).
# In the worst case - all the values are unique.
# And we extra traverse all of them again => O(2 * n).
# ------------------
# Auxiliary space: O(n)
# `frequencies` <- stores every unique value from `arr` => O(n).


test: list[int] = [2, 2, 3, 4]
test_out: int = 2
assert test_out == find_lucky(test)

test = [1, 2, 2, 3, 3, 3]
test_out = 3
assert test_out == find_lucky(test)

test = [2, 2, 2, 3, 3]
test_out = -1
assert test_out == find_lucky(test)
