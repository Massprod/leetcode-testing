# You have an array arr of length n where arr[i] = (2 * i) + 1
#  for all valid values of i (i.e., 0 <= i < n).
# In one operation, you can select two indices x and y where 0 <= x, y < n
#  and subtract 1 from arr[x] and add 1 to arr[y] (i.e., perform arr[x] -=1 and arr[y] += 1).
# The goal is to make all the elements of the array equal.
# It is guaranteed that all the elements of the array can be made equal using some operations.
# Given an integer n, the length of the array, return the minimum number of operations needed
#  to make all the elements of arr equal.
# --------------------------
# 1 <= n <= 10 ** 4


def min_operations(n: int) -> int:
    # working_sol (18.07%, 13.76%) -> (99ms, 16.83mb)  time: O(n) | space: O(n)
    arr: list[int] = []
    for index in range(n):
        arr.append(
            index * 2 + 1
        )
    average = sum(arr) // n
    out: int = 0
    for index in range(len(arr) // 2):
        out += abs(average - arr[index])
    return out


# Time complexity: O(n).
# Building `arr` of size `n` => O(n).
# Always traversing half of this array => O(n + n // 2).
# --------------------------
# Auxiliary space: O(n)
# `arr` <- allocates space for `n` values => O(n).


test: int = 3
test_out: int = 2
assert test_out == min_operations(test)

test  = 6
test_out = 9
assert test_out == min_operations(test)
