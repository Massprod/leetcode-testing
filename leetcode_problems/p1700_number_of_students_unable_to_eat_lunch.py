# The school cafeteria offers circular and square sandwiches at lunch break,
#  referred to by numbers 0 and 1 respectively.
# All students stand in a queue. Each student either prefers square or circular sandwiches.
# The number of sandwiches in the cafeteria is equal to the number of students.
# The sandwiches are placed in a stack. At each step:
#   - If the student at the front of the queue prefers the sandwich on the top of the stack,
#      they will take it and leave the queue.
#   - Otherwise, they will leave it and go to the queue's end.
# This continues until none of the queue students want to take the top sandwich
#  and are thus unable to eat.
# You are given two integer arrays students and sandwiches where sandwiches[i]
#  is the type of the i_th sandwich in the stack (i = 0 is the top of the stack)
#  and students[j] is the preference of the i_th student in the initial queue
#  (j = 0 is the front of the queue).
# Return the number of students that are unable to eat.
# -----------------------
# 1 <= students.length, sandwiches.length <= 100
# students.length == sandwiches.length
# sandwiches[i] is 0 or 1.
# students[i] is 0 or 1.
from random import randint
from collections import Counter


def count_students(students: list[int], sandwiches: list[int]) -> int:
    # working_sol (96.97%, 15.70%) -> (34ms, 17.34mb)  time: O(n) | space: O(1)
    # We can switch students on Top for w.e times.
    # So, actually only thing we care is that:
    #  can we feed Any student in a que with our current top sandwich `sandwiches[0]`.
    # And we can't switch sandwiches, we only allowed to take Top-one.
    # {sandwich type: how many students will take it}
    all_students: dict[int, int] = Counter(students)
    for sandwich in sandwiches:
        if sandwich in all_students and all_students[sandwich]:
            all_students[sandwich] -= 1
        else:
            break
    return sum(all_students.values())


# Time complexity: O(n) <- n - length of input array `students` or `sandwiches`, equal sized.
# Traversing `students` to get all student preferences => O(n).
# Traversing `sandwiches` to distribute them, worst case: traverse whole => O(n).
# -----------------------
# Auxiliary space: O(1)
# We only have 2 types of sandwiches, so `all_students` is always size of 2 and value are constant INTs.
# Actually if we don't have 1 of the sandwiches type in `students`, then it's  size of 1.
# But it's w.e. Because we can't decide this on input size.


test: list[int] = [1, 1, 0, 0]
test_sandwiches: list[int] = [0, 1, 0, 1]
test_out: int = 0
assert test_out == count_students(test, test_sandwiches)

test = [1, 1, 1, 0, 0, 1]
test_sandwiches = [1, 0, 0, 0, 1, 1]
test_out = 3
assert test_out == count_students(test, test_sandwiches)

test = [randint(0, 1) for _ in range(100)]
test_sandwiches = [randint(0, 1) for _ in range(100)]
print(f'{test}\n\n{test_sandwiches}')
