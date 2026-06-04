# You are given an integer n.
# The score of n is defined as the sum of d * freq(d) over all distinct digits d,
#  where freq(d) denotes the number of times the digit d appears in n.
# Return an integer denoting the score of n.
# --- --- --- ---
# 1 <= n <= 10 ** 9
from collections import Counter


def digit_frequency_score(n: int) -> int:
    # working_solution: (100%, 92.61%) -> (0ms, 19.18mb)  Time: O(n) Space: O(n)
    count: dict[str, int] = Counter(str(n))
    out: int = 0
    for digit, occurence in count.items():
        out += int(digit) * occurence

    return out


# Time complexity: O(n)
# --- --- --- ---
# Space complexity: O(n)


test: int = 122
test_out: int = 5
assert test_out == digit_frequency_score(test)

test = 101
test_out = 2
assert test_out == digit_frequency_score(test)
