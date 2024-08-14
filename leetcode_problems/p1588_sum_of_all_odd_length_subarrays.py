# Given an array of positive integers arr,
#  return the sum of all possible odd-length subarrays of arr.
# A subarray is a contiguous subsequence of the array.
# -------------------
# 1 <= arr.length <= 100
# 1 <= arr[i] <= 1000
from random import randint


def sum_odd_length_subarrays(arr: list[int]) -> int:
    # working_sol (86.18%, 39.65%) -> (39ms, 16.52mb)  time: O(n * n) | space: O(1)
    def check_window(window_size: int) -> int:
        window_sum: int = sum(arr[0: window_size])
        check_out: int = window_sum
        left: int = 0
        right: int = window_size - 1
        while right < len(arr) - 1:
            right += 1
            window_sum += arr[right]
            window_sum -= arr[left]
            left += 1
            check_out += window_sum
        return check_out

    out: int = 0
    for size in range(1, len(arr) + 1, 2):
        out += check_window(size)
    return out


# Time complexity: O(n * n) <- n - length of the input array `arr`.
# Always traversing whole `arr` for every odd length window => O(n * n).
# -------------------
# Auxiliary space: O(1)
# Only constant INTs used, none of them depends on input => O(1).


test: list[int] = [1, 4, 2, 5, 3]
test_out: int = 58
assert test_out == sum_odd_length_subarrays(test)

test = [1, 2]
test_out = 3
assert test_out == sum_odd_length_subarrays(test)

test = [10, 11, 12]
test_out = 66
assert test_out == sum_odd_length_subarrays(test)

test = [randint(1, 1000) for _ in range(100)]
print(test)
