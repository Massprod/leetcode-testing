# You are given two non-negative integers num1 and num2.
# In one operation, if num1 >= num2, you must subtract num2 from num1,
#  otherwise subtract num1 from num2.
# For example, if num1 = 5 and num2 = 4, subtract num2 from num1,
#  thus obtaining num1 = 1 and num2 = 4. However, if num1 = 4 and num2 = 5,
#  after one operation, num1 = 4 and num2 = 1.
# Return the number of operations required to make either num1 = 0 or num2 = 0.
# ----------------------
# 0 <= num1, num2 <= 10 ** 5
from random import randint


def count_operations(num1: int, num2: int) -> int:
    # working_sol (5.29%, 13.09%) -> (123ms, 16.63mb)  time: O(max(num1, num2)) | space: O(1)
    diff: int
    parts: int
    out: int = 0
    while num1 and num2:
        # num1 - num2
        if num1 == num2:
            out += 1
            num1 -= num2
        elif num1 > num2:
            # Difference we can try to take.
            diff = num1 % num2
            # Number of time we can take `num2` from `num1`
            parts = diff // num2
            # If they're not equal we can at least take 1 time.
            out += parts + 1
            num1 -= num2 + (num2 * parts)
        # num2 - num1
        elif num1 < num2:
            diff = num2 % num1
            parts = diff // num1
            out += parts + 1
            num2 -= num1 + (num1 * parts)
    return out


# Time complexity: O(max(num1, num2))
# We always taking down one of the values to 0 => O(max(num1, num2)).
# ----------------------
# Auxiliary space: O(1).


test_1: int = 2
test_2: int = 3
test_out: int = 3
assert test_out == count_operations(test_1, test_2)

test_1 = 10
test_2 = 10
test_out = 1
assert test_out == count_operations(test_1, test_2)

test_1 = randint(0, 10 ** 5)
test_2 = randint(0, 10 ** 5)
print(test_1)
print(test_2)
