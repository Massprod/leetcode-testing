# You are given positive integers n and m.
# Define two integers as follows:
#  - num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m.
#  - num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.
# Return the integer num1 - num2.
# ----------------------
# 1 <= n, m <= 1000


def difference_of_sums(n: int, m: int) -> int:
    # working_sol (68.15%, 51.89%) -> (37ms, 16.58mb)  time: O(n) | space: O(1)
    num1: int
    num2: int
    # We can't divide any value in `range(1, n + 1)`.
    # So, `num2` == 0, and we only need `num1`.
    if n < m:
        num1 = (n + 1) * n // 2
        return num1
    num1 = 0
    num2 = 0
    for val in range(1, n + 1):
        if val % m:
            num1 += val
        else:
            num2 += val
    return num1 - num2


# Time complexity: O(n)
# In the worst case n >= m traversing all values in `range(1, n + 1)` => O(n).
# ----------------------
# Auxiliary space: O(1)
# Only 2 constant INTs used, none of them depends on input => O(1).


test_n: int = 10
test_m: int = 3
test_out: int = 19
assert test_out == difference_of_sums(test_n, test_m)

test_n = 5
test_m = 6
test_out = 15
assert test_out == difference_of_sums(test_n, test_m)

test_n = 5
test_m = 1
test_out = -15
assert test_out == difference_of_sums(test_n, test_m)
