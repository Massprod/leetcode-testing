# There is a hidden integer array arr that consists of n non-negative integers.
# It was encoded into another integer array encoded of length n - 1,
#  such that encoded[i] = arr[i] XOR arr[i + 1].
# For example, if arr = [1,0,2,1], then encoded = [1,2,3].
# You are given the encoded array.
# You are also given an integer first, that is the first element of arr, i.e. arr[0].
# Return the original array arr. It can be proved that the answer exists and is unique.
# -------------------------
# 2 <= n <= 10 ** 4
# encoded.length == n - 1
# 0 <= encoded[i] <= 10 ** 5
# 0 <= first <= 10 ** 5


def decode(encoded: list[int], first: int) -> list[int]:
    # working_sol (52.00%, 94.91%) -> (164ms, 18.40mb)  time: O(n) | space: O(n)
    out: list[int] = [first]
    for val in encoded:
        first = first ^ val
        out.append(first)
    return out


# Time complexity: O(n) <- n - length of the input array `encoded`.
# Always using `XOR` on every value from `encoded` => O(n).
# -------------------------
# Auxiliary space: O(n)
# `out` <- always of the size `n + 1` => O(n + 1).


test: list[int] = [1, 2, 3]
test_first: int = 1
test_out: list[int] = [1, 0, 2, 1]
assert test_out == decode(test, test_first)

test = [6, 2, 7, 3]
test_first = 4
test_out = [4, 2, 0, 7, 4]
assert test_out == decode(test, test_first)
