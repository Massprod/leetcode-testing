# An attendance record for a student can be represented
#  as a string where each character signifies whether the student was absent, late, or present on that day.
# The record only contains the following three characters:
#  - 'A': Absent.
#  - 'L': Late.
#  - 'P': Present.
# Any student is eligible for an attendance award if they meet both of the following criteria:
#  - The student was absent ('A') for strictly fewer than 2 days total.
#  - The student was never late ('L') for 3 or more consecutive days.
# Given an integer n, return the number of possible attendance records of length n
#  that make a student eligible for an attendance award.
# The answer may be very large, so return it modulo 10 ** 9 + 7.
# -----------------------
# 1 <= n <= 10 ** 5


def check_record(n: int) -> int:
    # working_sol (12.33%, 22.75%) -> (6556ms, 79.45mb)  time: O(n) | space: O(n)
    cache: list[list[list[int]]] = [[[-1] * 3 for _ in range(2)] for _ in range(n + 1)]
    modul: int = 10 ** 9 + 7

    def check(index: int, num_late: int, num_abs: int) -> int:
        nonlocal modul
        if num_late > 2 or num_abs > 1:
            return 0
        if index == n:
            return 1
        if -1 != cache[index][num_abs][num_late]:
            return cache[index][num_abs][num_late]
        out: int = check(index + 1, 0, num_abs) % modul
        out += check(index + 1, 0, num_abs + 1) % modul
        out += check(index + 1, num_late + 1, num_abs) % modul
        cache[index][num_abs][num_late] = out
        return out

    return check(0, 0, 0) % modul


# Time complexity: O(n)
# There's (n * 2 * 3) unique combinations, and because we're using memorization, all of them used once => O(6n)
# -----------------------
# Auxiliary space: O(n)
# Our `cache` is always stores all of these unique combinations => O(6n).
# And every recursion at max has a stack with size `n` => O(7n)


test: int = 2
test_out: int = 8
assert test_out == check_record(test)

test = 1
test_out = 3
assert test_out == check_record(test)

test = 10101
test_out = 183236316
assert test_out == check_record(test)
