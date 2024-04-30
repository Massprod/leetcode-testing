# You are given a 0-indexed integer array nums and a positive integer k.
# You can apply the following operation on the array any number of times:
#  - Choose any element of the array and flip a bit in its binary representation.
#    Flipping a bit means changing a 0 to 1 or vice versa.
# Return the minimum number of operations required to make the bitwise XOR of all elements
#  of the final array equal to k.
# Note that you can flip leading zero bits in the binary representation of elements.
# For example, for the number (101)2 you can flip the fourth bit and obtain (1101)2.
# -----------------
# 1 <= nums.length <= 10 ** 5
# 0 <= nums[i] <= 10 ** 6
# 0 <= k <= 10 ** 6
from random import randint


def min_operations(nums: list[int], k: int) -> int:
    # working_sol (32.48%, 94.90%) -> (595ms, 30.86mb)  time: O(n + k) | space: O(1)
    # We only care about WHOLE array XOR.
    # So, we need to know what we get in the end.
    base: int = nums[0]
    for index in range(1, len(nums)):
        base ^= nums[index]
    out: int = 0
    # And because we need to make them equal to `k`.
    # We can just switch what's left incorrect.
    # Because it's equal to XOR everything except some single value in `nums`,
    #  and change it beats to satisfy `k`.
    while base or k:
        base_lsb: int = 1 if base & 1 else 0
        k_lsb: int = 1 if k & 1 else 0
        base >>= 1
        k >>= 1
        if base_lsb != k_lsb:
            out += 1
    return out


# Time complexity: O(n + k) <- n - length of the input array `nums`.
# Always traversing whole input array `nums` to get full array XOR => O(n).
# Extra using all bits of `k` or full array XOR, suppose in the worst case `k` is holding more bits => O(n + k).
# -----------------
# Auxiliary space: O(1)
# Only 4 constant INTs used.


test: list[int] = [2, 1, 3, 4]
test_k: int = 1
test_out: int = 2
assert test_out == min_operations(test, test_k)

test = [2, 0, 2, 0]
test_k = 0
test_out = 0
assert test_out == min_operations(test, test_k)

test = [9, 7, 9, 14, 8, 6]
test_k = 12
test_out = 3
assert test_out == min_operations(test, test_k)

test = [randint(0, 10 ** 6) for _ in range(10 ** 5)]
test_k = randint(0, 10 ** 6)
print(test)
print(test_k)
