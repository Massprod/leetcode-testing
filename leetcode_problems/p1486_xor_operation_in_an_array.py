# You are given an integer n and an integer start.
# Define an array nums where nums[i] = start + 2 * i (0-indexed)
#  and n == nums.length.
# Return the bitwise XOR of all elements of nums.
# ----------------------
# 1 <= n <= 1000
# 0 <= start <= 1000
# n == nums.length


def xor_operation(n: int, start: int) -> int:
    # working_sol (71.04%, 59.02%) -> (33ms, 16.49mb)  time: O(n) | space: O(1)
    xor_: int = 0
    index: int = 0
    while index != n:
        xor_ ^= start + 2 * index
        index += 1
    return xor_


# Time complexity: O(n)
# Always incrementing `index` until we reach `n` => O(n).
# ----------------------
# Auxiliary space: O(1)
# Only 2 constant INTs used, none of them depends on input => O(1).


test_n: int = 5
test_start: int = 0
test_out: int = 8
assert test_out == xor_operation(test_n, test_start)

test_n = 4
test_start = 3
test_out = 8
assert test_out == xor_operation(test_n, test_start)
