# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
# --------------------
# 0 <= num <= 2 ** 31 - 1
# --------------------
# Follow up: Could you do it without any loop/recursion in O(1) runtime?


def add_digits(num: int) -> int:
    # working_sol (41.15%, 50.58%) -> (45ms, 16.2mb)  time: O(1) | space: O(1)
    if num == 0:
        return 0
    return 1 + (num - 1) % 9


# Time complexity: O(1) -> nothing depends on input => O(1).
# Auxiliary space: O(1) -> no extra space => O(1).
# --------------------
# For doing this as a loop is simple -> taking num % 10 until we hit something lower than 10 -> summarize everything ->
# repeat -> until num < 10 and if num == 10, num % 10 will be 0 and return 1 in this case (1 + 0).
# For a O(1) no idea, so I'm taking a Hint, and it's extra_math. ! https://en.wikipedia.org/wiki/Digital_root !
# DRb(n) = 1 + ((num - 1) % (base - 1)), if n != 0
# DRb(n) = 0, if n == 0
# In our case base == 10, so DR10(num) = 1 + ((num - 1) % 9) for n > 0


test1 = 38
test1_out = 2
print(add_digits(test1))
assert test1_out == add_digits(test1)

test2 = 0
test2_out = 0
print(add_digits(test2))
assert test2_out == add_digits(test2)

test3 = 10
test3_out = 1
print(add_digits(test3))
assert test3_out == add_digits(test3)
