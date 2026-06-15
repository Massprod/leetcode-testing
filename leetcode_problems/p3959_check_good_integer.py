# You are given a positive integer n.
# Let digitSum be the sum of the digits of n,
#  and let squareSum be the sum of the squares of the digits of n.
# An integer is called good if squareSum - digitSum >= 50.
# Return true if n is good. Otherwise, return false.
# --- --- --- ---
# 1 <= n <= 10 ** 9


def check_good_integer(n: int) -> bool:
    # working_solution: (100%, 100%) -> (0ms, 19.28mb)  Time: O(n) Space: O(1)
    sum_square: int = 0
    sum_digit: int = 0
    while n:
        digit: int = n % 10
        sum_square += digit ** 2
        sum_digit += digit
        n //= 10

    return 50 <= (sum_square - sum_digit)


# Time complexity: O(n)
# --- --- --- ---
# Space complexity: O(1)


test: int = 1_000
test_out: bool = False
assert test_out == check_good_integer(test)

test = 19
test_out = True
assert test_out == check_good_integer(test)
