# Given an array of integers arr, return true if and only if it is a valid mountain array.
# Recall that arr is a mountain array if and only if:
#  - arr.length >= 3
#  - There exists some i with 0 < i < arr.length - 1 such that:
#    - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#    - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# ------------------------
# 1 <= arr.length <= 10 ** 4
# 0 <= arr[i] <= 10 ** 4


def valid_mountain_array(arr: list[int]) -> bool:
    # working_sol (92.21%, 99.34%) -> (149ms, 17.66mb)  time: O(n) | space: O(1)
    if len(arr) < 3:
        return False
    # We don't care about one way slide.
    if arr[0] >= arr[1] or arr[-1] >= arr[-2]:
        return False
    ascending: bool = True
    for index in range(1, len(arr)):
        if arr[index] == arr[index - 1]:
            return False
        elif ascending and arr[index] < arr[index - 1]:
            ascending = not ascending
        elif not ascending and arr[index] > arr[index - 1]:
            return False
    return True


# Time complexity: O(n) <- n - length of the input array `arr`.
# Always traversing `arr`, once => O(n).
# ------------------------
# Auxiliary space: O(1)
# Only 1 constant `boolean` used => O(1).


test: list[int] = [2, 1]
test_out: bool = False
assert test_out == valid_mountain_array(test)

test = [3, 5, 5]
test_out = False
assert test_out == valid_mountain_array(test)

test = [0, 3, 2, 1]
test_out = True
assert test_out == valid_mountain_array(test)
