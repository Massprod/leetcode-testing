# You want to schedule a list of jobs in d days.
# Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).
# You have to finish at least one task every day.
# The difficulty of a job schedule is the sum of difficulties of each day of the d days.
# The difficulty of a day is the maximum difficulty of a job done on that day.
# You are given an integer array jobDifficulty and an integer d.
# The difficulty of the ith job is jobDifficulty[i].
# Return the minimum difficulty of a job schedule.
# If you cannot find a schedule for the jobs return -1.
# ---------------------
# 1 <= jobDifficulty.length <= 300
# 0 <= jobDifficulty[i] <= 1000
# 1 <= d <= 10
from functools import cache
from random import randint


def min_difficulty(jobDifficulty: list[int], d: int) -> int:
    # working_sol (67.95%, 8.39%) -> (532ms, 18.68mb)  time: O(n * d * n) | space: O(n * d)
    if len(jobDifficulty) < d:
        return -1
    max_possible: int = 10 * 1000  # 10 days, all with maximum difficulty.

    @cache
    def check(index: int, days: int) -> int:
        if not days:
            return max(jobDifficulty[index:])
        out: int = max_possible
        # Maximum difficulty of current slice(day).
        max_diff: int = jobDifficulty[index]
        # We need at least 1 task per day.
        # So, we can't use more indexes in current day than:
        left_to_use: int = len(jobDifficulty) - index - days
        # We can't slice it, just use 1 task on this day.
        if left_to_use == 1:
            out = min(out, check(index + 1, days - 1) + max_diff)
        # Otherwise, trying to slice from (index -> last_index we can use +1), not inclusive.
        else:
            for slice_index in range(index + 1, index + left_to_use + 1):
                out = min(out, check(slice_index, days - 1) + max_diff)
                # After we check() path from current slice, we expand == include next index.
                # Better to maintain maximum value of the current slice than use max(slice).
                max_diff = max(max_diff, jobDifficulty[slice_index])
        return out

    return check(0, d - 1)


# Time complexity: O(n * d * n) <- n - length of input array `jobDifficulty`.
# We only calculate (n * d) states, and for each state we traverse some part of the array.
# And because it can be (n - 1), it's linear => O(n * d * n).
# Extra for base case (days == 0) we slice and check for max(), which in the worst case can be full array slice.
# ---------------------
# Auxiliary space: O(n * d).
# We memorize every state we calculate => O(n * d).
# Extra we can include base case slicing, in the worst case (index == 0, days == 0) => full array slice => O(n).
# Stack of recursion is it max will have height == (d - 1) => O(d - 1).
# As always ignoring stack + slicing: O(n * d), and it will dominate them anyway.


test: list[int] = [6, 5, 4, 3, 2, 1]
test_d: int = 2
test_out: int = 7
assert test_out == min_difficulty(test, test_d)

test = [9, 9, 9]
test_d = 4
test_out = -1
assert test_out == min_difficulty(test, test_d)

test = [1, 1, 1]
test_d = 3
test_out = 3
assert test_out == min_difficulty(test, test_d)

test = [416, 934, 64, 670, 697, 321, 534, 822, 13, 137]
test_d = 10
test_out = 4608
assert test_out == min_difficulty(test, test_d)

test = [786, 307, 394, 204, 845, 880, 133, 341, 343, 890, 302, 142, 653, 993, 823]
test_d = 10
test_out = 5014
assert test_out == min_difficulty(test, test_d)

test = [randint(0, 1000) for _ in range(300)]
print(test)
