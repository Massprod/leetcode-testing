# You are given two arrays with positive integers arr1 and arr2.
# A prefix of a positive integer is an integer formed by one or more of its digits,
#  starting from its leftmost digit.
# For example, 123 is a prefix of the integer 12345, while 234 is not.
# A common prefix of two integers a and b is an integer c, such that c is a prefix of both a and b.
# For example, 5655359 and 56554 have a common prefix 565 while 1223 and 43456 do not have a common prefix.
# You need to find the length of the longest common prefix between all pairs of integers (x, y)
#  such that x belongs to arr1 and y belongs to arr2.
# Return the length of the longest common prefix among all pairs.
# If no common prefix exists among them, return 0.
# -------------------------
# 1 <= arr1.length, arr2.length <= 5 * 10 ** 4
# 1 <= arr1[i], arr2[i] <= 10 ** 8
from random import randint
from collections import deque


def longest_common_prefix(arr1: list[int], arr2: list[int]) -> int:
    # working_sol (10.88%, 98.08%) -> (1174ms, 27.62mb)  time: O(n * log_10_k + m * log_10_g)
    #                                                    space: O(n * log_10_k + log_10_max(max(n), max(m))
    value_prefixes: deque[int]
    cur_prefix: int
    digit: int
    out: int = 0
    arr1_prefixes: set[int] = set()
    for value in arr1:
        value_prefixes = deque([])
        while value:
            digit = value % 10
            value_prefixes.appendleft(digit)
            value //= 10
        cur_prefix = 0
        for prefix in value_prefixes:
            cur_prefix += prefix
            arr1_prefixes.add(cur_prefix)
            cur_prefix *= 10
    for value in arr2:
        value_prefixes = deque([])
        while value:
            digit = value % 10
            value_prefixes.appendleft(digit)
            value //= 10
        cur_prefix = 0
        for index in range(len(value_prefixes)):
            cur_prefix += value_prefixes[index]
            if cur_prefix in arr1_prefixes:
                out = max(out, index + 1)
            cur_prefix *= 10
    return out


# Time complexity: O(n * log_10_k + m * log_10_g) <- n - length of the input array `arr1`,
#                                                    k - average length of the values inside `arr1` (digits),
#                                                    m - length of the input array `arr2`,
#                                                    g - average length of the values inside `arr2` (digits).
# Always traversing both input arrays, once.
# And for each value, we deplete it to get all the digits == log_10_value.
# Extra using every digit we got to check prefixes => O(n * log_10_k * 2 + m * log_10_g * 2).
# -------------------------
# Auxiliary space: O(n * log_10_k + log_10_max(max(n), max(m)).
# `value_prefixes` <- always contains maximum value digits => O(log_10_max(max(n), max(m)).
# `arr1_prefixes` <- in the worst case, every value in `arr1` is going to have unique prefixes.
# So, we will have every value with unique prefixes == to their length => O(n * log_10_k + log_10_max(max(n), max(m)).


test_1: list[int] = [1, 10, 100]
test_2: list[int] = [1000]
test_out: int = 3
assert test_out == longest_common_prefix(test_1, test_2)

test_1 = [1, 2, 3]
test_2 = [4, 4, 4]
test_out = 0
assert test_out == longest_common_prefix(test_1, test_2)

test_1 = [randint(1, 10 ** 8) for _ in range(10 ** 4)]
print(test_1)
