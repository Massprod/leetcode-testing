# Given an array of integers arr.
# We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).
# Let's define a and b as follows:
#  - a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
#  - b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
# Note that ^ denotes the bitwise-xor operation.
# Return the number of triplets (i, j and k) Where a == b.
# -----------------------
# 1 <= arr.length <= 300
# 1 <= arr[i] <= 10 ** 8
from random import randint


def count_triplets(arr: list[int]) -> int:
    # working_sol (82.76%, 99.43%) -> (42ms, 16.40mb)  time: O(n ** 2) | O(1)
    # Two sub-arrays will be equal after XOR everything.
    # Only if sub1 ^ sub2 == 0 <- sub1 ^ 0 == sub2, cuz ^ 0 does nothing.
    # So, we just need one subarray with all values giving XOR == 0.
    # And we can reshuffle them in w.e manner, so it's (n - 1) combinations for sub-array with n-length
    out: int = 0
    for start in range(len(arr)):
        cur_sub: int = arr[start]
        for end in range(start + 1, len(arr)):
            cur_sub ^= arr[end]
            if 0 == cur_sub:
                out += end - start
    return out


# Time complexity: O(n ** 2) <- n - length of the input array `arr`.
# We're always check every possible subarray => O(n ** 2).
# -----------------------
# Auxiliary space: O(1)
# Only 2 constant INT's used, none of them depends on input => O(1)


test: list[int] = [2, 3, 1, 6, 7]
test_out: int = 4
assert test_out == count_triplets(test)

test = [1, 1, 1, 1, 1]
test_out = 10
assert test_out == count_triplets(test)

test = [randint(1, 10 ** 8) for _ in range(300)]
print(test)
