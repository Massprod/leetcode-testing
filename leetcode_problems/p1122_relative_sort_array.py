# Given two arrays arr1 and arr2, the elements of arr2 are distinct,
#  and all elements in arr2 are also in arr1.
# Sort the elements of arr1 such that the relative ordering of items in arr1
#  are the same as in arr2.
# Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.
# --------------------
# 1 <= arr1.length, arr2.length <= 1000
# 0 <= arr1[i], arr2[i] <= 1000
# All the elements of arr2 are distinct.
# Each arr2[i] is in arr1.


def relative_sort_array(arr1: list[int], arr2: list[int]) -> list[int]:
    # working_sol (85.24%, 93.48%) -> (35ms, 16.56mb)  time: O(n * log n + k) | space: O(k + n)
    values_cost: dict[int, int] = {
        value: index for index, value in enumerate(arr2)
    }
    first_part: list[int] = []
    second_part: list[int] = []
    for val in arr1:
        if val in values_cost:
            first_part.append(val)
        else:
            second_part.append(val)
    first_part.sort(key=lambda x: values_cost[x])
    second_part.sort()
    return first_part + second_part


# Time complexity: O(n * log n + k) <- n - length of the input array `arr1`, k - length of the input array `arr2`.
# Worst case: every value from `arr1` is present in `arr2`.
# We will traverse `arr2` to get all the costs to use => O(k).
# `first_part` size == `arr1` size => O(n * log n).
# Even if we're going to have `second_part` it's overall same actions.
# --------------------
# Auxiliary space: O(k + n)
# `values_cost` is always of size `arr2` => O(k)
# Sort will take basic `n` and extra `n` for the new `out` array => O(2n).


test_1: list[int] = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
test_2: list[int] = [2, 1, 4, 3, 9, 6]
test_out: list[int] = [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
assert test_out == relative_sort_array(test_1, test_2)

test_1 = [28, 6, 22, 8, 44, 17]
test_2 = [22, 28, 8, 6]
test_out = [22, 28, 8, 6, 17, 44]
assert test_out == relative_sort_array(test_1, test_2)
