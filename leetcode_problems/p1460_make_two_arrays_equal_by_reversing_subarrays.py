# You are given two integer arrays of equal length target and arr.
# In one step, you can select any non-empty subarray of arr and reverse it.
# You are allowed to make any number of steps.
# Return true if you can make arr equal to target or false otherwise.
# --------------------
# target.length == arr.length
# 1 <= target.length <= 1000
# 1 <= target[i] <= 1000
# 1 <= arr[i] <= 1000
from collections import Counter


def can_be_equal(target: list[int], arr: list[int]) -> bool:
    # working_sol (75.78%, 59.80%) -> (71ms, 16.71mb)  time: O(n + k) | space: O(n + k)
    # We don't care about anything, except value occurrences.
    # Because we can take any [val1, val2] pair and switch any char from place1 -> place2.
    # So, if value is present in `target` and `arr,` we can place it on the desired placement.
    target_vals: dict[int, int] = Counter(target)
    arr_vals: dict[int, int] = Counter(arr)
    for val, occurs in target_vals.items():
        if val in arr_vals and arr_vals[val] == occurs:
            continue
        return False
    return True


# Time complexity: O(n + k) <- n - length of the input array `target`, k - length of the input array `arr`.
# We're always traversing both input arrays to get values and their occurrences => O(n + k).
# In the worst case, every value is unique, extra traverse `n` keys to check existence in counterpart => O(2n + k).
# --------------------
# Auxiliary space: O(n + k).
# Every value is unique and stored in `target_vals` and `arr_vals` => O(n + k).


test: list[int] = [1, 2, 3, 4]
test_arr: list[int] = [2, 4, 1, 3]
test_out: bool = True
assert test_out == can_be_equal(test, test_arr)

test = [7]
test_arr = [7]
test_out = True
assert test_out == can_be_equal(test, test_arr)

test = [3, 7, 9]
test_arr = [3, 7, 11]
test_out = False
assert test_out == can_be_equal(test, test_arr)
