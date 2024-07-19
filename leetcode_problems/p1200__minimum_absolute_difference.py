# Given an array of distinct integers arr,
#  find all pairs of elements with the minimum absolute difference of any two elements.
# Return a list of pairs in ascending order(with respect to pairs),
#  each pair [a, b] follows:
#   - a, b are from arr
#   - a < b
#   - b - a equals to the minimum absolute difference of any two elements in arr
# ---------------------
# 2 <= arr.length <= 10 ** 5
# -10 ** 6 <= arr[i] <= 10 ** 6
from random import randint


def minimum_absolute_difference(arr: list[int]) -> list[list[int]]:
    # working_sol (80.89%, 70.53%) -> (250ms, 31.03mb)  time: O(n * log n) | space: O(n)
    arr.sort()
    out: list[list[int]] = [[arr[0], arr[1]]]
    min_diff: int = abs(arr[0] - arr[1])
    for index in range(2, len(arr)):
        cur_diff: int = abs(arr[index] - arr[index - 1])
        if cur_diff < min_diff:
            out = [[arr[index - 1], arr[index]]]
            min_diff = cur_diff
        elif min_diff == cur_diff:
            if arr[index - 1] > arr[index]:
                out.append([arr[index], arr[index - 1]])
            else:
                out.append([arr[index - 1], arr[index]])
    return out


# Time complexity: O(n * log n) <- n - length of the input array `arr`.
# Always sorting input array `arr`, once => O(n * log n).
# Extra traversing every index of the `arr` again to get all the correct pairs => O(n).
# ---------------------
# Auxiliary space: O(n).
# `sort` will allocate `n` space for itself => O(n).
# `out` can be at max with the size of `n` every value used  == `n` pairs => O(n).


test: list[int] = [4, 2, 1, 3]
test_out: list[list[int]] = [[1, 2], [2, 3], [3, 4]]
assert test_out == minimum_absolute_difference(test)

test = [1, 3, 6, 10, 15]
test_out = [[1, 3]]
assert test_out == minimum_absolute_difference(test)

test = [3, 8, -10, 23, 19, -4, -14, 27]
test_out = [[-14, -10], [19, 23], [23, 27]]
assert test_out == minimum_absolute_difference(test)

test_values: set[int] = set()
while len(test_values) < 10 ** 5:
    test_values.add(randint(-10 ** 6, 10 ** 6))
print(list(test_values))
