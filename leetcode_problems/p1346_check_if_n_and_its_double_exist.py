# Given an array arr of integers, check if there exist two indices i and j such that :
#  - i != j
#  - 0 <= i, j < arr.length
#  - arr[i] == 2 * arr[j]
# -----------------------
# 2 <= arr.length <= 500
# -10 ** 3 <= arr[i] <= 10 ** 3
from random import randint


def check_if_exist(arr: list[int]) -> bool:
    # working_sol (100.00%, 5.25%) -> (0ms, 17.32mb)  time: O(n) | space: O(n)
    uniques: set[int] = set()
    for val in arr:
        if val * 2 in uniques or val / 2 in uniques:
            return True
        uniques.add(val)
    return False


# Time complexity: O(n) <- n - length of the input array `arr`.
# Always traversing whole input array `arr`, once => O(n).
# Auxiliary space: O(n)
# In the worst case there are no doubles, and all values are unique, we will store all values from `arr` in uniques.
# uniques <- allocates space for each unique value from `arr` => O(n).


test: list[int] = [10, 2, 5, 3]
test_out: bool = True
assert test_out == check_if_exist(test)

test = [3, 1, 7, 11]
test_out = False
assert test_out == check_if_exist(test)

test = [randint(-10 ** 3, 10 ** 3) for _ in range(500)]
print(test)
