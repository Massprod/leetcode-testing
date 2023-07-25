# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
# -------------
# -100.0 < x < 100.0
# -2 ** 31 <= n <= 2 ** 31-1
# n is an integer.
# Either x is not zero or n > 0.
# -10 ** 4 <= x ** n <= 10 ** 4


def my_power(x: float, n: int) -> float:
    # working_sol (92.49%, 77.84%) -> (39ms, 16.24mb)  time: O(log n) | space: O(log n)
    if n == 0:
        return 1
    if x == 1.0:
        return x

    def rec_pow(base: float, exp: int):
        if exp == 0:
            return 1
        if exp == 1.0:
            return base
        # x ** n == (x ** 2) ** n / 2   <- if n is even
        if exp % 2 == 0:
            return rec_pow(base * base, exp // 2)
        # x ** n == x * ((x ** 2) ** ((n - 1) / 2 ))  <- if n is odd
        else:
            return base * rec_pow(base * base, (exp - 1) // 2)

    if n < 0:
        return 1 / rec_pow(x, abs(n))
    return rec_pow(x, abs(n))


# Time complexity: O(log n) -> logarithmic scaling, instead of calculating every x ** n, we're culling most of it.
# n - exponent ^^|
# Space complexity: O(log n) -> storing all recursion calls, so it's only extra stack of recursion which equal
#                               to number of calls => O(log n).
# -------------
# Base method to improve:
#   x ** n == x * ((x ** 2) ** ((n - 1) / 2 ))  <- if n is odd
#   x ** n == (x ** 2) ** n / 2   <- if n is even


test1 = 2.00000
test1_pow = 10
test1_out = 1024.00000
assert test1_out == round(my_power(test1, test1_pow), 5)

test2 = 2.10000
test2_pow = 3
test2_out = 9.26100
assert test2_out == round(my_power(test2, test2_pow), 5)

test3 = 2.00000
test3_pow = -2
test3_out = 0.25000
assert test3_out == round(my_power(test3, test3_pow), 5)

test4 = 0.00001
test4_pow = 2147483647
test4_out = 0.0
assert test4_out == round(my_power(test4, test4_pow), 5)
