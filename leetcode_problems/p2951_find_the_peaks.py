# You are given a 0-indexed array mountain.
# Your task is to find all the peaks in the mountain array.
# Return an array that consists of indices of peaks in the given array in any order.
# Notes:
#  - A peak is defined as an element that is strictly greater than its neighboring elements.
#  - The first and last elements of the array are not a peak.
# ------------------
# 3 <= mountain.length <= 100
# 1 <= mountain[i] <= 100


def find_peaks(mountain: list[int]) -> list[int]:
    # working_sol (89.58%, 63.03%) -> (42ms, 16.40mb)  time: O(n) | space: O(n)
    out: list[int] = []
    for index in range(1, len(mountain) - 1):
        if mountain[index - 1] < mountain[index] > mountain[index + 1]:
            out.append(index)
    return out


# Time complexity: O(n) <- n - length of the input array `mountain`.
# Always traversing `n - 2` indexes of the input array => O(n - 2).
# ------------------
# Auxiliary space: O(n)
# In the worst case there's `n // 2` peaks => O(n).


test: list[int] = [2, 4, 4]
test_out: list[int] = []
assert test_out == find_peaks(test)

test = [1, 4, 3, 8, 5]
test_out = [1, 3]
assert test_out == find_peaks(test)
