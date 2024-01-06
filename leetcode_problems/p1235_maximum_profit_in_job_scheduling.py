# We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i],
#  obtaining a profit of profit[i].
# You're given the startTime, endTime and profit arrays,
#  return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.
# If you choose a job that ends at time X you will be able to start another job that starts at time X.
# -------------------
# 1 <= startTime.length == endTime.length == profit.length <= 5 * 10 ** 4
# 1 <= startTime[i] < endTime[i] <= 10 ** 9
# 1 <= profit[i] <= 10 ** 4
from functools import cache
from random import randint


def job_scheduling(startTime: list[int], endTime: list[int], profit: list[int]) -> int:
    # working_sol (36.55%, 11.17%) -> (759ms, 114.6mb)  time: O(n * log n) | space: O(n)
    @cache
    def bs(target: int) -> int:
        """
        Binary search to get leftmost index with value == target.
        Or where it can be placed without disrupting sorted order in `all_data`.
        bisect.bisect_left () <- similar.
        :param target: value for placement search
        :return: index with correct insert() position
        """
        # Because, we allowed to have duplicates, like: starts [2, 2, 2] ends [3, 3, 3]
        # We can cache `target` to skip this BS.
        left: int = 0
        right: int = len(startTime) - 1
        while left <= right:
            middle: int = (right + left) // 2
            if all_data[middle][0] < target:
                left = middle + 1
            else:
                right = middle - 1
        return left

    # (start, end, profit)
    all_data: list[tuple[int, int, int]] = [(startTime[x], endTime[x], profit[x]) for x in range(len(startTime))]
    all_data.sort(key=lambda x: x[0])

    @cache
    def check(index: int) -> int:
        # We can't start more jobs.
        if index == len(all_data):
            return 0
        max_profit: int = max(
            check(index + 1),  # skip job, and start from next.
            check(bs(all_data[index][1])) + all_data[index][2]  # complete this job + continue.
        )
        return max_profit

    return check(0)


# Time complexity: O(n * log n) <- n - length of input arrays `startTime`, `endTime`, `profit`, all equal.
# Creating `all_data` with zipping all data from 3 input arrays => O(n).
# Sorting `all_data` with standard sort() => O(n * log n).
# With memorization(cache) we only check() all indexes once, and for each we find correct `startTime` with BS.
# And because we're doing BS on same size array as `n` => O(n * log n).
# -------------------
# Auxiliary space: O(n).
# First we're zipping all 3 input array in 1 with styling (start, end, profit) => O(3n).
# Extra recursion stack will be of size `n`, because we can have streak from (0 -> last_ind) jobs in it => O(n).
# Extra sort() takes O(n).


test: list[int] = [1, 2, 3, 3]
test_ends: list[int] = [3, 4, 5, 6]
test_profit: list[int] = [50, 10, 40, 70]
test_out: int = 120
assert test_out == job_scheduling(test, test_ends, test_profit)

test = [1, 2, 3, 4, 6]
test_ends = [3, 5, 10, 6, 9]
test_profit = [20, 20, 100, 70, 60]
test_out = 150
assert test_out == job_scheduling(test, test_ends, test_profit)

test = [1, 1, 1]
test_ends = [2, 3, 4]
test_profit = [5, 6, 4]
test_out = 6
assert test_out == job_scheduling(test, test_ends, test_profit)

test = [randint(1, 10 ** 5) for _ in range(5 * 10 ** 4)]
test_ends = [start + randint(1, 10 ** 3) for start in test]
test_profit = [randint(1, 10 ** 4) for _ in test]
print(f'{test}\n\n\n!!!!===\n\n\n{test_ends}\n\n\n!!!!===\n\n\n{test_profit}')
