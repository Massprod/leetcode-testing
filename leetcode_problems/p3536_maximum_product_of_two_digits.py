# You are given a positive integer n.
# Return the maximum product of any two digits in n.
# Note: You may use the same digit twice if it appears more than once in n.
# ------------------------
# 10 <= n <= 10 ** 9


def max_product(n: int) -> int:
    # working_sol (48.82%, 40.05%) -> (1ms, 17.81mb)  time: O(n) | space: O(1)
    max1: int = 0
    max2: int = 0
    digit: int = 0
    # Take digits 1 by 1 and save max, pre_max.
    while n:
        digit = n % 10
        if digit >= max1:
            max1, max2 = max(max1, digit), max1
        else:
            max2 = max(max2, digit)
        n //= 10
    
    return max1 * max2


# Time complexity: O(n) <- n - number of digits of the input integer `n`
# Always using every digit of the `n`, once => O(n).
# ------------------------
# Auxiliary space: O(1)
# Only constant INT's are used, nothing depends on input => O(1).


test: int = 31
test_out: int = 3
assert test_out == max_product(test)

test = 22
test_out = 4
assert test_out == max_product(test)

test = 124
test_out = 8
assert test_out == max_product(test)
