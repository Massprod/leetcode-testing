# There are n employees in a company, numbered from 0 to n - 1.
# Each employee i has worked for hours[i] hours in the company.
# The company requires each employee to work for at least target hours.
# You are given a 0-indexed array of non-negative integers hours of length n and a non-negative integer target.
# Return the integer denoting the number of employees who worked at least target hours.
# --------------------------
# 1 <= n == hours.length <= 50
# 0 <= hours[i], target <= 10 ** 5


def number_of_employees(hours: list[int], target: int) -> int:
    # working_sol (71.13%, 93.41%) -> (42ms, 16.31mb)  time: O(n) | space: O(1)
    out: int = 0
    for val in hours:
        if val >= target:
            out += 1
    return out


# Time complexity: O(n) <- n - length of the input array `hours`.
# Always traversing whole `hours`, once => O(n).
# --------------------------
# Auxiliary space: O(1)
# Only one constant INT used, doesn't depend on input => O(1).


test: list[int] = [0, 1, 2, 3, 4]
test_target: int = 2
test_out: int = 3
assert test_out == number_of_employees(test, test_target)

test = [5, 1, 4, 2, 2]
test_target = 6
test_out = 0
assert test_out == number_of_employees(test, test_target)
