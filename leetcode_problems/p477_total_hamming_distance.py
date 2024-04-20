# The Hamming distance between two integers is the number of positions
#  at which the corresponding bits are different.
# Given an integer array nums, return the sum of Hamming distances between all
#  the pairs of the integers in nums.
# -------------------
# 1 <= nums.length <= 10 ** 4
# 0 <= nums[i] <= 10 ** 9
# The answer for the given input will fit in a 32-bit integer.


def total_hamming_distance(nums: list[int]) -> int:
    # working_sol (39.82%, 39.51%) -> (325ms, 18.12mb)  time: O(n) | space: O(1)
    # Essentially, all we care about is how many values in `nums`
    #  have 1's or 0's bits placed on some position.
    # So, just check every position and count how many values with 0's and 1's.
    out: int = 0
    for position in range(32):
        zeroes: int = 0
        ones: int = 0
        for num in nums:
            cur_bit: int = (num >> position) & 1
            if 1 == cur_bit:
                ones += 1
            else:
                zeroes += 1
        # And because we need pairs, we need all of their permutations.
        out += zeroes * ones
    return out


# Time complexity: O(n) <- n - length of input array `nums`.
# We check all 32 bits of every num in `nums` => O(32 * n).
# -------------------
# Auxiliary space: O(1)


test: list[int] = [4, 14, 2]
test_out: int = 6
assert test_out == total_hamming_distance(test)

test = [4, 14, 4]
test_out = 4
assert test_out == total_hamming_distance(test)
