# There is a school that has classes of students and each class will be having a final exam.
# You are given a 2D integer array classes, where classes[i] = [passi, totali].
# You know beforehand that in the ith class, there are totali total students,
#  but only passi number of students will pass the exam.
# You are also given an integer extraStudents.
# There are another extraStudents brilliant students that are guaranteed to pass the exam
#   of any class they are assigned to.
# You want to assign each of the extraStudents students to a class in a way that maximizes
#  the average pass ratio across all the classes.
# The pass ratio of a class is equal to the number of students of the class
#  that will pass the exam divided by the total number of students of the class.
# The average pass ratio is the sum of pass ratios of all the classes
#  divided by the number of the classes.
# Return the maximum possible average pass ratio after assigning the extraStudents students.
# Answers within 10 ** -5 of the actual answer will be accepted.
# ----------------------------
# 1 <= classes.length <= 10 ** 5
# classes[i].length == 2
# 1 <= passi <= totali <= 10 ** 5
# 1 <= extraStudents <= 10 ** 5
import heapq


def max_average_ratio(classes: list[list[int]], extraStudents: int) -> float:
    # working_sol: (19.75%, 18.45%) -> (1330ms, 54.62mb)  time: O(n log n + k * log n) | space: O(n)

    def potential_gain(will_pass: int, total_students: int) -> float:
        out: int = (will_pass + 1) / (total_students + 1) - will_pass / total_students
        return out
    
    # [potential_gain, will_pass, students] <- MaxHeap
    pass_ratios: list[tuple[int, int, int]] = []
    heapq.heapify(pass_ratios)
    for passes, total in classes:
        # We only care about potential profit of adding a 100% pass student.
        heapq.heappush(
            pass_ratios, (potential_gain(passes, total) * -1, passes, total)
        )
    # Now we can just take a maximum potential profit and make it real.
    while extraStudents:
        extraStudents -= 1
        pot_gain, passes, total = heapq.heappop(pass_ratios)
        # And if we can make it even more profitable, we should try to add another one.
        heapq.heappush(
            pass_ratios, (potential_gain(passes + 1, total + 1) * -1, passes + 1, total + 1)
        )
    out: int = 0
    while pass_ratios:
        gain, passes, total = heapq.heappop(pass_ratios)
        out += passes / total
    # ! return the maximum possible average pass ratio !
    # Average between all of the `classes`
    return out / len(classes)


# Time complexity: O(n * log n + k * log n) <- n - length of the input array `classes`, k - input value `extraStudents`.
# We create a maxHeap with all potential gains for every class in `classes` => O(n * log n).
# We use all best options to increase gains for every `extraStudents` => O(n * log n + k * log n).
# And finally we use every class gain => O(n * log n + k * log n + n * log n).
# Every push(), pop() is `log m` <- m - current length of the heap.
# ----------------------------
# Auxiliary space: O(n)
# `pass_ratios` <- allocates space for each class from `classes` => O(n).


test: list[list[int]] = [[1, 2], [3, 5], [2, 2]]
test_extra: int = 2
test_out: float = 0.78333
av_range: int = 10 ** -5
assert (test_out - av_range) <= max_average_ratio(test, test_extra) <= (test_out + av_range)

test = [[2, 4], [3, 9], [4, 5], [2, 10]]
test_extra = 4
test_out = 0.53485
assert (test_out - av_range) <= max_average_ratio(test, test_extra) <= (test_out + av_range)
