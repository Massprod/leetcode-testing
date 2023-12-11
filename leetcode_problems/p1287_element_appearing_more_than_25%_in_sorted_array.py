# Given an integer array sorted in non-decreasing order,
#  there is exactly one integer in the array that occurs more than 25% of the time, return that integer.
# --------------------
# 1 <= arr.length <= 10 ** 4
# 0 <= arr[i] <= 10 ** 5
from collections import Counter


def find_special_int(arr: list[int]) -> int:
    # working_sol (96.96%, 30.41%) -> (79ms, 17.97mb)  time: O(n) | space: O(log n)
    # {value: encounters}
    vals: dict[int, int] = Counter(arr)
    # [most_common so far, encounters]
    out: list[int] = [0, 0]
    for val in vals:
        if out[1] < vals[val]:
            out[0] = val
            out[1] = vals[val]
    return out[0]


# Time complexity: O(n) <- n - length of input array `arr`.
# Double traverse of original input array `arr` => O(2n).
# Auxiliary space: O(log n).
# We're forced to have duplicates, and we will store only part of the original array.


test: list[int] = [1, 2, 2, 6, 6, 6, 6, 7, 10]
test_out: int = 6
assert test_out == find_special_int(test)

test = [1, 1]
test_out = 1
assert test_out == find_special_int(test)
