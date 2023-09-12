# You are given an array nums consisting of positive integers.
# You have to take each integer in the array, reverse its digits,
#  and add it to the end of the array. You should apply this operation to the original integers in nums.
# Return the number of distinct integers in the final array.
# ------------------
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 6
from random import randint


def count_distinct_integers(nums: list[int]) -> int:
    # working_sol (62.40%, 95.55%) -> (597ms, 41.1mb)  time: O(n * k) | space: O(n)
    used: set[int] = set()
    length: int = len(nums)
    for x in range(length):
        # Reverse original values.
        reverse: int = int(str(nums[x])[::-1])
        # Store unique values in set.
        used.add(nums[x])
        used.add(reverse)
    return len(used)


# Time complexity: O(n * k) -> for every value in nums, converting it to string and reversing => O(n * k).
# k - len of number_string^^|
# n - len of input_array^^|
# Auxiliary space: O(n) -> worst case == every value is unique and their reversed versions as well ->
#                       -> we will store every value, and it's reversed version as well => O(2n).


test: list[int] = [1, 13, 10, 12, 31]
test_out: int = 6
assert test_out == count_distinct_integers(test)

test = [2, 2, 2]
test_out = 1
assert test_out == count_distinct_integers(test)

test = [randint(1, 10 ** 6) for _ in range(10 ** 3)]
print(test)
