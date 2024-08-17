# You are given a 0-indexed string num of length n consisting of digits.
# Return true if for every index i in the range 0 <= i < n,
#  the digit i occurs num[i] times in num, otherwise return false.
# --------------------------
# n == num.length
# 1 <= n <= 10
# num consists of digits.
from string import digits
from random import choice
from collections import defaultdict


def digit_count(num: str) -> bool:
    # working_sol (61.62%, 73.41%) -> (35ms, 16.50mb)  time: O(n) | space: O(n)
    # { digit: occurrences }
    occurs: dict[str, int] = defaultdict(int)
    for digit in num:
        occurs[digit] += 1
    for index in range(len(num)):
        if occurs[str(index)] != int(num[index]):
            return False
    return True


# Time complexity: O(n) <- n - length of the input string `num`.
# In the worst case, there's all unique digits in `num`.
# We will traverse all the digits, twice => O(2 * n).
# --------------------------
# Auxiliary space: O(n)
# `occurs` <- allocates space for every digit string in `num` => O(n).


test: str = "1210"
test_out: bool = True
assert test_out == digit_count(test)

test = "030"
test_out = False
assert test_out == digit_count(test)

test = ''.join([choice(digits) for _ in range(10)])
print(test)
