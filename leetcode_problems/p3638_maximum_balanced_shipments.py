# You are given an integer array weight of length n,
#  representing the weights of n parcels arranged in a straight line.
# A shipment is defined as a contiguous subarray of parcels.
# A shipment is considered balanced if the weight of the last parcel is strictly
#  less than the maximum weight among all parcels in that shipment.
# Select a set of non-overlapping, contiguous, balanced shipments
#  such that each parcel appears in at most one shipment (parcels may remain unshipped).
# Return the maximum possible number of balanced shipments that can be formed.
# --- --- --- ---
# 2 <= n <= 10 ** 5
# 1 <= weight[i] <= 10 ** 9
from random import randint
from pyperclip import copy


def max_balanced_shipments(weight: list[int]) -> int:
    # working_solution: (73.69%, 84.16%) -> (95ms, 32.82mb)  Time: O(n) Space: O(1)
    # The best way to get the maximum possible number of balanced shipments.
    # Is to create shipment `asap`, so every time we can build it => build it.
    max_weight: int = -1
    out: int = 0

    for parcel in weight:
        if -1 != max_weight and max_weight > parcel:
            out += 1
            max_weight = -1
            continue
        max_weight = max(max_weight, parcel)

    return out


# Time complexity: O(n)
# n - length of the input array `weight`
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [2, 5, 1, 4, 3]
test_out: int = 2
assert test_out == max_balanced_shipments(test)

test = [4, 4]
test_out = 0
assert test_out == max_balanced_shipments(test)

test = [randint(1, 10 ** 9) for _ in range(10 ** 5)]
copy(test)  # type: ignore
