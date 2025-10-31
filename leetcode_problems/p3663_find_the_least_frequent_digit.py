# Given an integer n, find the digit that occurs least frequently
#  in its decimal representation.
# If multiple digits have the same frequency, choose the smallest digit.
# Return the chosen digit as an integer.
# The frequency of a digit x is the number of times it appears
#  in the decimal representation of n.
# --- --- --- ---
# 1 <= n <= 2 ** 31​ - 1
from collections import defaultdict


def get_least_frequent_digit(n: int) -> int:
    # working_solution: (43.88%, 65.16%) -> (2ms, 17.70mb)  Time: O(n) Space: O(n)
    # { value: occurs }
    occurrences: dict[int, int] = defaultdict(int)
    while n:
        digit: int = n % 10
        occurrences[digit] += 1
        n //= 10
    
    # [value, occurs]
    out: list[int] = [10, 1_000]
    for value, occurs in occurrences.items():
        if out[1] > occurs:
            out[0], out[1] = value, occurs
        elif out[1] == occurs:
            out[0] = min(value, out[0])
    
    return out[0]


# Time complexity: O(n)
# In the worst case, all of the `n` digits are unique.
# Always using every digit, twice => O(2 * n).
# --- --- --- ---
# Space complexity: O(n)
# `occurrences` <- allocates space for each digit of `n`.


test: int = 1_553_322
test_out: int = 1
assert test_out == get_least_frequent_digit(test)

test = 723_344_511
test_out = 2
assert test_out == get_least_frequent_digit(test)

test = 115
test_out = 5
assert test_out == get_least_frequent_digit(test)
