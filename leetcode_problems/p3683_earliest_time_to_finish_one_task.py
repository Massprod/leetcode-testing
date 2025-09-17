# You are given a 2D integer array tasks where tasks[i] = [si, ti].
# Each [si, ti] in tasks represents a task with start time si that takes
#  ti units of time to finish.
# Return the earliest time at which at least one task is finished.
# --- --- --- ---
# 1 <= tasks.length <= 100
# tasks[i] = [si, ti]
# 1 <= si, ti <= 100
from random import randint
from pyperclip import copy


def earliest_time(tasks: list[list[int]]) -> int:
    # working_solution: (54.47%, 98.14%) -> (3ms, 17.68mb)  Time: O(n) Space: O(n)
    return min(
        [sum(task) for task in tasks]
    )


# Time complexity: O(n) <- n - length of the input array `tasks`.
# Always traversing the whole input array `tasks`, once => O(n).
# --- --- --- ---
# Space complexity: O(n)
# We're creating an extra array with the same size => O(n).


test: list[list[int]] = [[1, 6], [2, 3]]
test_out: int = 5
assert test_out == earliest_time(test)

test = [[100, 100], [100, 100], [100, 100]]
test_out = 200
assert test_out == earliest_time(test)

test = [[randint(1,45), randint(46, 100)] for _ in range(100)]
copy(test)  # type: ignore
