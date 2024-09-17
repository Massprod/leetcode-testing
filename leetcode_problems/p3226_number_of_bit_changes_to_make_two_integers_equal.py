# You are given two positive integers n and k.
# You can choose any bit in the binary representation
#  of n that is equal to 1 and change it to 0.
# Return the number of changes needed to make n equal to k.
# If it is impossible, return -1.
# ---------------------------
# 1 <= n, k <= 10 ** 6


def min_changes(n: int, k: int) -> int:
    # working_sol (92.28%, 80.01%) -> (28ms, 16.50mb)  time: O(n) | space: O(1)
    out: int = 0
    while n:
        n_lsb: int = n & 1
        k_lsb: int = k & 1
        if 0 == n_lsb and 1 == k_lsb:
            return -1
        elif 1 == n_lsb and n_lsb != k_lsb:
            out += 1
        n >>= 1
        k >>= 1
    if n != k:
        return -1
    return out


# Time complexity: O(n) <- n - input value `n`.
# Always depleting `n` to 0 => O(n).
# ---------------------------
# Auxiliary space: O(1)
# Only three constant INTs used, none of them depends on input => O(1).


test_n: int = 13
test_k: int = 4
test_out: int = 2
assert test_out == min_changes(test_n, test_k)

test_n = 21
test_k = 21
test_out = 0
assert test_out == min_changes(test_n, test_k)

test_n = 14
test_k = 13
test_out = -1
assert test_out == min_changes(test_n, test_k)

test_n = 11
test_k = 56
test_out = -1
assert test_out == min_changes(test_n, test_k)
