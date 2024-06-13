# There are n seats and n students in a room.
# You are given an array seats of length n, where seats[i] is the position of the ith seat.
# You are also given the array students of length n, where students[j] is the position of the jth student.
# You may perform the following move any number of times:
#  - Increase or decrease the position of the ith student by 1
#    (i.e., moving the ith student from position x to x + 1 or x - 1)
# Return the minimum number of moves required to move each student to a seat
#  such that no two students are in the same seat.
# Note that there may be multiple seats or students in the same position at the beginning.
# -----------------------------
# n == seats.length == students.length
# 1 <= n <= 100
# 1 <= seats[i], students[j] <= 100
from random import randint


def min_moves_to_seat(seats: list[int], students: list[int]) -> int:
    # working_sol (94.05%, 96.88%) -> (51ms, 16.39mb)  time: O((n * log n) + n) | space: O(n)
    seats.sort()
    students.sort()
    # It's obvious we can sort both and set smallest to smallest.
    # But, what about case like: seat = 4, stud1 = 1, stud2= 5.
    # Then a higher student will need fewer moves.
    # ! n == seats.length == students.length ! <- this.
    # In this case, we can guarantee that we're going to have another seat with a higher index.
    # So, we will do 3 steps with stud1, but later we're guaranteed to have some seat >= 4
    # And stud2 will make fewer steps to this seat, which is going to cover the difference.
    # Because if we let stud2 take a first seat == 4, and let stud1 take next higher,
    #  he is going to do some `k` extra steps and mitigate the difference with stud2.
    out: int = 0
    for index, stud_place in enumerate(students):
        out += abs(seats[index] - stud_place)
    return out


# Time complexity: O((n * log n) + n) <- n - length of the input arrays `seats` or `students`.
# Always sorting both array and single traversing `students` => O(2 * (n * log n) + n)
# -----------------------------
# Auxiliary space: O(n)
# Both `sort`'s taking `n` => O(2n)


test: list[int] = [3, 1, 5]
test_students: list[int] = [2, 7, 4]
test_out: int = 4
assert test_out == min_moves_to_seat(test, test_students)

test = [4, 1, 5, 9]
test_students = [1, 3, 2, 6]
test_out = 7
assert test_out == min_moves_to_seat(test, test_students)

test = [2, 2, 6, 6]
test_students = [1, 3, 2, 6]
test_out = 4
assert test_out == min_moves_to_seat(test, test_students)

test = [randint(1, 100) for _ in range(100)]
print(test)
test_students = [randint(1, 100) for _ in range(100)]
print(test_students)
