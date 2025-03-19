# You have a certain number of processors, each having 4 cores.
# The number of tasks to be executed is four times the number of processors.
# Each task must be assigned to a unique core, and each core can only be used once.
# You are given an array processorTime representing the time each processor
#  becomes available and an array tasks representing how long each task takes to complete.
# Return the minimum time needed to complete all tasks.
# ---------------------------
# 1 <= n == processorTime.length <= 25000
# 1 <= tasks.length <= 10 ** 5
# 0 <= processorTime[i] <= 10 ** 9
# 1 <= tasks[i] <= 10 ** 9
# tasks.length == 4 * n


def min_processing_time(processorTime: list[int], tasks: list[int]) -> int:
    # working_sol (38.02%, 93.58%) -> (92ms, 32.79mb)  time: O(n * log n) | space: O(n)
    # Assign earliest time processor with longest tasks => profit?
    # Don't see any extra there, even indexing is intact ! tasks.length == 4 * n !
    # We're not notified, that processor are in order => extra sorting.
    processorTime.sort()
    tasks.sort(reverse=True)
    out: int = 0
    tasks_index: int = 0
    for start in processorTime:
        for time in tasks[tasks_index: tasks_index + 4]:
            out = max(out, start + time)
        tasks_index += 4

    return out


# Time complexity: O(n * log n) <- n - length of the input array `processorTime`.
# Sorting both input arrays.
# We know that ! tasks.length == 4 * n ! => we can just count it as constant:
# O(n * log n + 4 * n * log (4 * n)) => O(n * log n).
# Extra traversing both input arrays after sorting => O(n + 4 * n).
# ---------------------------
# Auxiliary space: O(n)
# `sort` takes O(n) by default, O(n + 4 * n).


test: list[int] = [8, 10]
test_tasks: list[int] = [2, 2, 3, 1, 8, 7, 4, 5]
test_out: int = 16
assert test_out == min_processing_time(test, test_tasks)

test = [10, 20]
test_tasks = [2, 3, 1, 2, 5, 8, 4, 3]
test_out = 23
assert test_out == min_processing_time(test, test_tasks)
