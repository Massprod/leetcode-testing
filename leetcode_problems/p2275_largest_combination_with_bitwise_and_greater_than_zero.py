# The bitwise AND of an array nums is the bitwise AND of all integers in nums.
#  - For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.
#  - Also, for nums = [7], the bitwise AND is 7.
# You are given an array of positive integers candidates.
# Evaluate the bitwise AND of every combination of numbers of candidates.
# Each number in candidates may only be used once in each combination.
# Return the size of the largest combination of candidates with a bitwise AND greater than 0.
# ----------------------------
# 1 <= candidates.length <= 10 ** 5
# 1 <= candidates[i] <= 10 ** 7
from random import randint


def largest_combination(candidates: list[int]) -> int:
    # working_sol (32.50%, 60.30%) -> (594ms, 26.87mb)  time: O(n) | space: O(1)
    # 10 ** 7 == max of 24 bits | still using 25 for no reason :)
    pos_count: list[int] = [0 for _ in range(25)]
    # All we actually care is that what BIT position is holding
    #  the most SET bits from all the numbers.
    # Because we don't care about anything, except the length of a sequence.
    for candidate in candidates:
        cur_bit: int = 0
        while candidate:
            pos_count[cur_bit] += 1 if candidate & 1 else 0
            candidate >>= 1
            cur_bit += 1
    return max(pos_count)


# Time complexity: O(n) <- n - length of the input array `candidates`.
# At max, there are 24 bits used, assuming this as a constant.
# Using every number from the input array `candidates` => O(n).
# ----------------------------
# Auxiliary space: O(1)
# `pos_count` <- always of the same size == 25 => O(1).


test: list[int] = [16, 17, 71, 62, 12, 24, 14]
test_out: int = 4
assert test_out == largest_combination(test)

test = [8, 8]
test_out = 2
assert test_out == largest_combination(test)

test = [randint(1, 10 ** 7) for _ in range(10 ** 5)]
print(test)
