# There are n students in a class numbered from 0 to n - 1.
# The teacher will give each student a problem starting with the student number 0,
#  then the student number 1, and so on until the teacher reaches the student number n - 1.
# After that, the teacher will restart the process, starting with the student number 0 again.
# You are given a 0-indexed integer array chalk and an integer k.
# There are initially k pieces of chalk.
# When the student number i is given a problem to solve,
#  they will use chalk[i] pieces of chalk to solve that problem.
# However, if the current number of chalk pieces is strictly less than chalk[i],
#  then the student number i will be asked to replace the chalk.
# Return the index of the student that will replace the chalk pieces.
# -----------------------------
# chalk.length == n
# 1 <= n <= 10 ** 5
# 1 <= chalk[i] <= 10 ** 5
# 1 <= k <= 10 ** 9
from random import randint


def chalk_replacer(chalk: list[int], k: int) -> int:
    # working_sol (89.97%, 90.90%) -> (562ms, 29.79mb)  time: O(n) | space: O(1)
    out: int = 0
    full_round: int = sum(chalk)
    # Take everything we can from `k` with full circles.
    left_over: int = k % full_round
    # Take what's left until we can.
    for student, takes in enumerate(chalk):
        left_over -= takes
        if left_over < 0:
            out = student
            break
    return out


# Time complexity: O(n) <- n - length of the input array `chalk`.
# Always traversing whole input array `chalk` to get `sum`, once => O(n).
# In the worst case, the last student is going to be replacer, extra traverse all indexes of `chalk` again => O(2 * n).
# -----------------------------
# Auxiliary space: O(1).
# Only two constant INTs used, none of them depends on input => O(1).


test: list[int] = [5, 1, 5]
test_k: int = 22
test_out: int = 0
assert test_out == chalk_replacer(test, test_k)

test = [3, 4, 1, 2]
test_k = 25
test_out = 1
assert test_out == chalk_replacer(test, test_k)

test = [randint(1, 10 ** 5) for _ in range(10 ** 5)]
print(test)
