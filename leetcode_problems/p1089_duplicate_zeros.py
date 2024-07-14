# Given a fixed-length integer array arr,
#  duplicate each occurrence of zero, shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written.
# Do the above modifications to the input array in place and do not return anything.
# ------------------------------
# 1 <= arr.length <= 10 ** 4
# 0 <= arr[i] <= 9
from random import randint


def duplicate_zeros(arr: list[int]) -> None:
    # working_sol (96.07%, 19.71%) -> (56ms, 17.44mb)  time: O(n) | space: O(n)
    stack: list[int] = []
    for val in arr:
        if not val:
            stack.append(0)
            stack.append(0)
        else:
            stack.append(val)
    arr[:] = stack[:len(arr)]


# Time complexity: O(n) <- n - length of the input array `arr`.
# Always traversing whole input array `arr`, twice => O(2n).
# First, to get all the values in a stack.
# Second to slice values we need.
# ------------------------------
# Auxiliary space: O(n)
# In the worst case, every value is `0`, so we will store `n * 2` values in `stack` => O(n)


test: list[int] = [1, 0, 2, 3, 0, 4, 5, 0]
test_out: list[int] = [1, 0, 0, 2, 3, 0, 0, 4]
duplicate_zeros(test)
assert test_out == test_out

test = [1, 2, 3]
test_out = [1, 2, 3]
duplicate_zeros(test)
assert test_out == test_out

test = [randint(0, 9) for _ in range(10 ** 4)]
print(test)
