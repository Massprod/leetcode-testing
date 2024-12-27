# You are given an integer array values where values[i] represents
#  the value of the ith sightseeing spot.
# Two sightseeing spots i and j have a distance j - i between them.
# The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j:
#  the sum of the values of the sightseeing spots, minus the distance between them.
# Return the maximum score of a pair of sightseeing spots.
# ------------------------
# 2 <= values.length <= 5 * 10 ** 4
# 1 <= values[i] <= 1000
import pyperclip
from random import randint


def max_score_sightseeing_pair(values: list[int]) -> int:
    # working_sol (90.98%, 10.49%) -> (53ms, 23.36mb)  time: O(n) | space: O(1)
    # values[i] + values[j] + i - j <- we need this maximised
    # values[j] - j <- new value on each step.
    # values[i] + i <- essentially we want this to be maximised,
    #                  before we're doing the step.
    # So, we can maintain max(prev_max, values[i] + i)
    # And calc expression for each new index `j` we visit.
    # ---
    # (value[i], i, value[i] + i)
    out: int = 0
    cur_max: tuple[int, int, int] = (0, 0, 0)
    for index, value in enumerate(values):
        check: int = index + value
        out = max(out, cur_max[0] + value + cur_max[1] - index)
        if check > cur_max[2]:
            cur_max = (value, index, check)
    return out


# Time complexity: O(n) <- n - length of the input array `values`.
# Always traversing whole input array `values`, once => O(n).
# ------------------------
# Auxiliary space: O(1)
# Nothing depends on input => O(1).


test: list[int] = [8, 1, 5, 2, 6]
test_out: int = 11
assert test_out == max_score_sightseeing_pair(test)

test = [1, 2]
test_out = 2
assert test_out == max_score_sightseeing_pair(test)

test = [randint(1, 1000) for _ in range(10 ** 4)]
pyperclip.copy(test)
