# You have n jobs and m workers.
# You are given three arrays: difficulty, profit, and worker where:
#  - difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
#  - worker[j] is the ability of jth worker
#    (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
# Every worker can be assigned at most one job, but one job can be completed multiple times.
#  - For example, if three workers attempt the same job that pays $1,
#    then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
# Return the maximum profit we can achieve after assigning the workers to the jobs.
# -----------------------------
# n == difficulty.length
# n == profit.length
# m == worker.length
# 1 <= n, m <= 10 ** 4
# 1 <= difficulty[i], profit[i], worker[i] <= 10 ** 5


def max_profit_assignment(difficulty: list[int], profit: list[int], worker: list[int]) -> int:
    # working_sol (10.85%, 74.98%) -> (436ms, 19.57mb)  time: O(n * log n + k * log n) | space: O(n)

    def bs(target: int, array: list[tuple[int, int]]) -> int:
        left_l: int = 0
        right_l: int = len(array) - 1
        max_profit: int = 0
        while left_l <= right_l:
            middle: int = (left_l + right_l) // 2
            if array[middle][0] <= target:
                max_profit = max(array[middle][1], max_profit)
                left_l = middle + 1
            else:
                right_l = middle - 1
        return max_profit

    dif_prof: list[tuple[int, int]] = [
        (difficulty[index], profit[index]) for index in range(len(difficulty))
    ]
    dif_prof.sort(key=lambda x: x[0])
    for index in range(1, len(dif_prof)):
        dif_prof[index] = (dif_prof[index][0], max(dif_prof[index][1], dif_prof[index - 1][1]))
    out: int = 0
    for possibility in worker:
        out += bs(possibility, dif_prof)
    return out


# Time complexity: O(n * log n + k * log n) <- n - length of the input array `difficulty` or `profit`,
#                                              k - length of the input array `worker`.
# Traversing `difficulty` to get a combined array with difficulty levels and profit we get => O(n).
# Sorting resulted array with a size of `n` => O(n * log n).
# Traversing resulted array `dif_prof` to sert maximum profit for every difficulty => O(n)
# Traversing `worker` array to find maximum difficulty for every worker and get maximized profit => O(k * log n).
# -----------------------------
# Auxiliary space: O(n)
# Standard `sort` takes `n`, and also we create an extra array `dif_prof` with the same size as `difficulty` => O(2n).


test_diff: list[int] = [2, 4, 6, 8, 10]
test_profit: list[int] = [10, 20, 30, 40, 50]
test_worker: list[int] = [4, 5, 6, 7]
test_out: int = 100
assert test_out == max_profit_assignment(test_diff, test_profit, test_worker)

test_diff = [85, 47, 57]
test_profit = [24, 66, 99]
test_worker = [40, 25, 25]
test_out = 0
assert test_out == max_profit_assignment(test_diff, test_profit, test_worker)

test_diff = [5, 50, 92, 21, 24, 70, 17, 63, 30, 53]
test_profit = [68, 100, 3, 99, 56, 43, 26, 93, 55, 25]
test_worker = [96, 3, 55, 30, 11, 58, 68, 36, 26, 1]
test_out = 765
assert test_out == max_profit_assignment(test_diff, test_profit, test_worker)
