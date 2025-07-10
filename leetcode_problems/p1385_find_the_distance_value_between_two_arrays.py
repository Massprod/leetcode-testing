# Given two integer arrays arr1 and arr2, and the integer d,
#  return the distance value between the two arrays.
# The distance value is defined as the number of elements arr1[i]
#  such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.
# ----------------------------
# 1 <= arr1.length, arr2.length <= 500
# -1000 <= arr1[i], arr2[j] <= 1000
# 0 <= d <= 100
from bisect import bisect_left


def find_the_distance_value(arr1: list[int], arr2: list[int], d: int) -> int:
    # working_sol (98.33%, 65.28%) -> (1ms, 17.88mb)  time: O(n * log n + m * log n) | space: O(n)
    arr2.sort()
    out: int = 0
    for value in arr1:
        min_index: int = bisect_left(arr2, value)
        if min_index < len(arr2) and arr2[min_index] - value <= d:
            continue
        if min_index > 0 and value - arr2[min_index - 1] <= d:
            continue
        out += 1
    
    return out


# Time complexity: O(n * log n + m * log n) <- m - length of the input array `arr1`,
#                                              n - length of the input array `arr2`.
# Always sorting the input array `arr2`, once => O(n * log n).
# Extra traversing every value of the `arr1` and BS on each step => O(n * log n + m * log n).
# ----------------------------
# Auxiliary space: O(n)
# `sort` <- takes O(n).


test_1: list[int] = [4, 5, 8]
test_2: list[int] = [10, 9, 1, 8]
test_d: int = 2
test_out: int = 2
assert test_out == find_the_distance_value(test_1, test_2, test_d)

test_1 = [1, 4, 2, 3]
test_2 = [-4, -3, 6, 10, 20, 30]
test_d = 3
test_out = 2
assert test_out == find_the_distance_value(test_1, test_2, test_d)

test_1 = [2, 1, 100, 3]
test_2 = [-5, -2, 10, -3, 7]
test_d = 6
test_out = 1
assert test_out == find_the_distance_value(test_1, test_2, test_d)
