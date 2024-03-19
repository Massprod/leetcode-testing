# You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time,
#  n. Each cycle or interval allows the completion of one task.
# Tasks can be completed in any order, but there's a constraint:
#  identical tasks must be separated by at least n intervals due to cooling time.
# Return the minimum number of intervals required to complete all tasks.
# -----------------
# 1 <= tasks.length <= 10 ** 4
# tasks[i] is an uppercase English letter.
# 0 <= n <= 100
from random import choice
from collections import Counter
from string import ascii_uppercase


def least_interval(tasks: list[str], n: int) -> int:
    # working_sol (99.35%, 79.06%) -> (336ms, 17.10mb)  time: O(g) | space: O(g)
    all_seq: int = len(tasks)
    enc_tasks: dict[str, int] = Counter(tasks)
    max_enc: int = max(enc_tasks.values())
    max_tasks: int = 0
    for enc in enc_tasks.values():
        if enc == max_enc:
            max_tasks += 1
    better_seq: int = (max_enc - 1) * (n + 1) + max_tasks
    out: int = max(better_seq, all_seq)
    return out


# Time complexity: O(g) <- g - length of input array `tasks`.
# Single traverse of the whole array `tasks` to count all occurrences.
# In the worst case, only unique chars => another traverse of the same Number of elements in `enc_tasks`.
# Another traverse of them, to get # of tasks with such # of occurrences => O(3g).
# -----------------
# Auxiliary space: O(g)
# Dictionary `max_enc` will hold every unique char from `tasks` => O(g).
# We can even call it Constant, because there's only 26 unique Chars in ENG_dict. But w.e.
# -----------------
# (n + 1) <- maximum number of Tasks we can complete in the BEST sequence we could ever build.
# (max_enc - 1) <- minimum number of Sequences we need to do to complete all the Tasks.
# (max_tasks) <- extra Time we need to complete other Tasks which can be used to start a Sequence as well.
# Because, we should always start using MaxOccurrence tasks first.
# Then it's something like: MwwwwwwMwwwwww <- w - any other tasks, M - maximum occurrence task.
# The Distance between EVERY M is the Time we need to Idle before we could start another M task.
# So, we should either just WAIT this time OR in BEST option we need to fill it with other TASKS.
# This is why (n + 1) == DISTANCE between M and next M. +1 - for task itself, because every task == 1s.
# Because we need to complete every task, we can't skip any M's.
# In this case, our best option of all is to try and fill this Gap with other Tasks.
# Even if we can't fill it, we still will need to wait time == `n` to start another sequence.
# Like: Mww__Mww__ <- `_` - empty spot, and we can't start anything == idle.
# Essentially, we will need some (max_enc - 1) number of sequences starting with ANY of the MAX occurrences Tasks.
# Every such sequence will take (n + 1) Time to be completed: n - to start another, +1 for starting Task.
# And because we can have more than 1 starting Task with MAX occurrences,
#  we need to include their time as +1 for each.
# In case like: ["A", "B", "A", "B"], n = 1. We need to consider len(tasks).
# Because: `better_seq` = 0 * 1 + 2 == 2, and we need to have 4s to complete it.
# We can't combine them to any sequences, and every Task should be done OneByOne with 1s to complete.
# So, if we can't perfectly combine all Tasks to such sequences == len(tasks).


test: list[str] = ["A", "A", "A", "B", "B", "B"]
test_n: int = 2
test_out: int = 8
assert test_out == least_interval(test, test_n)

test = ["A", "C", "A", "B", "D", "B"]
test_n = 1
test_out = 6
assert test_out == least_interval(test, test_n)

test = ["A", "A", "A", "B", "B", "B"]
test_n = 3
test_out = 10
assert test_out == least_interval(test, test_n)

test = ["A", "B", "C"]
test_n = 100
test_out = 3
assert test_out == least_interval(test, test_n)

test = [choice(ascii_uppercase) for _ in range(10 ** 4)]
print(test)
