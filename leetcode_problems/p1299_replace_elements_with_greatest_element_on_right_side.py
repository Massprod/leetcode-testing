# Given an array arr, replace every element in that array with the greatest element among
#  the elements to its right, and replace the last element with -1.
# After doing so, return the array.
# --------------------
# 1 <= arr.length <= 10 ** 4
# 1 <= arr[i] <= 10 ** 5
from random import randint


def replace_elements(arr: list[int]) -> list[int]:
    # working_sol (98.07%, 64.51%) -> (571ms, 17.82mb)  time: O(n) | space: O(1)
    highest: int = arr[-1]
    # Last doesn't have right_side => always -1.
    arr[-1] = -1
    # Everything else is always Highest we can meet on the right_side.
    for x in range(len(arr) - 2, -1, -1):
        # Maintain Highest on the right_side.
        if arr[x] > highest:
            highest, arr[x] = arr[x], highest
            continue
        arr[x] = highest
    return arr


# Time complexity: O(n) -> traversing whole input_array, once => O(n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> changing input_array in place and using only One extra const INT => O(1).


test: list[int] = [17, 18, 5, 4, 6, 1]
test_out: list[int] = [18, 6, 6, 6, 1, -1]
assert test_out == replace_elements(test)

test = [400]
test_out = [-1]
assert test_out == replace_elements(test)

test = [randint(1, 10 ** 5) for _ in range(10 ** 4)]
print(test)
