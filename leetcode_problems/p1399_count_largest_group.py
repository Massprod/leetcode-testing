# You are given an integer n.
# Each number from 1 to n is grouped according to the sum of its digits.
# Return the number of groups that have the largest size.
# -----------------
# 1 <= n <= 10 ** 4
from collections import defaultdict


def count_largest_group(n: int) -> int:
    # working_sol (96.52%, 69.57%) -> (50ms, 16.44mb)  time: O(n) | space: O(n)
    # {digits_sum: number of values}
    groups: dict[int, int] = defaultdict(int)

    def count_digits_sum(num: int) -> int:
        digits_sum: int = 0
        while num:
            digits_sum += num % 10
            num //= 10
        return digits_sum

    while n:
        groups[count_digits_sum(n)] += 1
        n -= 1
    out: int = 0
    max_group_size: int = 0
    for group_sum, group_size in groups.items():
        if max_group_size == group_size:
            out += 1
        elif max_group_size < group_size:
            out = 1
            max_group_size = group_size
    return out


# Time complexity: O(n)
# Always depleting `n` to 0 => O(n)
# Even if we're going to have all groups unique from `n` we're still going to have `n` groups => O(2 * n).
# -----------------
# Auxiliary space: O(n)
# `groups` <- stores every unique group => O(n).


test: int = 13
test_out: int = 4
assert test_out == count_largest_group(test)

test = 2
test_out = 2
assert test_out == count_largest_group(test)
