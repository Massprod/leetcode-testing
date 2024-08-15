# Given two integers num1 and num2, return the sum of the two integers.
# -------------------
# -100 <= num1, num2 <= 100


def _sum(num1: int, num2: int) -> int:
    # working_sol (85.46%, 89.12%) -> (30ms, 16.35mb)  time: O(1) | space: O(1)
    return num1 + num2


# Time complexity: O(1)
# -------------------
# Auxiliary space: O(1)


test_1: int = 12
test_2: int = 5
test_out: int = 17
assert test_out == _sum(test_1, test_2)

test_1 = -10
test_2 = 4
test_out = -6
assert test_out == _sum(test_1, test_2)
