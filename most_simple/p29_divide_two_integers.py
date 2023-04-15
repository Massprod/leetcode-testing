# Given two integers dividend and divisor, divide two integers without using multiplication,
# division, and mod operator.
#
# The integer division should truncate toward zero, which means losing its fractional part.
# For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
#
# Return the quotient after dividing dividend by divisor.
#
# Note: Assume we are dealing with an environment that could only store integers
# within the 32-bit signed integer range: [−231, 231 − 1]. For this problem,
# if the quotient is strictly greater than 231 - 1, then return 231 - 1,
# and if the quotient is strictly less than -231, then return -231.
# -2 ** 31 < x < 2 ** 31 - 1:
import math


def divide_two_int(dividend: int, divisor: int) -> int:
    # working_sol (39.64%, 59%) time: O(log(a)) | space O(1)
    # lowest = -2 ** 31
    # highest = 2 ** 31 - 1
    # sign = 1
    # if dividend < 0 and divisor < 0:
    #     sign = 1
    #     # elif dividend < 0 or divisor < 0:
    #     sign = -1
    # quot = 0
    # limit = 0
    # dividend = abs(dividend)
    # divisor = abs(divisor)
    # for x in range(31, -1, -1):
    #     if limit + (divisor << x) <= dividend:
    #         limit += divisor << x
    #         quot += 1 << x  # 1 * 2 ** x
    # if sign < 0:
    #     quot = -quot
    # if quot < lowest:
    #     return lowest
    # elif quot > highest:
    #     return highest
    # return quot
    # ------------------------------------------
    # working_sol (71.78%, 59%) time: O(1) | space: O(1)
    if dividend == 0:
        return 0
    highest = 2 ** 31 - 1
    if divisor == 0:
        return highest
    lowest = -2 ** 31
    sign = 1
    if dividend < 0 and divisor < 0:
        sign = 1
    elif dividend < 0 or divisor < 0:
        sign = -1
    if dividend < 0 and divisor == 1:
        if dividend < lowest:
            return lowest
        return dividend
    elif dividend < 0 and divisor == -1:
        dividend = -dividend
        if dividend > highest:
            return highest
        return dividend
    elif dividend > 0 and divisor == 1:
        if dividend > highest:
            return highest
        return dividend
    elif dividend > 0 and divisor == -1:
        dividend = -dividend
        if dividend < lowest:
            return lowest
        return dividend
    # a / b = e ^ ln(a) / e ^ ln(b) = e ** (ln(a) – ln(b) )
    quot = int(math.exp(math.log(abs(dividend)) - math.log(abs(divisor))) + 0.0000000001)
    if sign < 0:
        quot = -quot
    if quot < lowest:
        return lowest
    elif quot > highest:
        return highest
    return quot


test1_div = 10
test1_sor = 3
test1_out = 3
print(divide_two_int(test1_div, test1_sor))
test2_div = -10
test2_sor = 3
test2_out = -3
print(divide_two_int(test2_div, test2_sor))
# test3 Failed because im just crawling with sums and I need some speed.
# Don't have any ideas how to speed up at this moment.
# At least we can skip divisor like 1 with max values, because it's going to be same max value.
# 100% sure it's not enough
test3_div = -2147483648546
test3_sor = -1
print(divide_two_int(test3_div, test3_sor))
# Yep. As expected. How ???
test4_div = -2147483647
test4_sor = 2
print(divide_two_int(test4_div, test4_sor))
# gret = test4_div << 10
# tt = 2 ** 10
# print(gret)
# print(test4_div * tt)
# x << y
# Returns x with the bits shifted to the left by y places
# (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.
#
# x >> y
# Returns x with the bits shifted to the right by y places.
# This is the same as dividing x by 2**y.
# ---------------------------------------
# another way to count dividing:
# a/b = e ^ ln(a) / e ^ ln(b) = e ** ( ln(a) – ln(b) )
test5_div = -231
test5_sor = 3
print(divide_two_int(test5_div, test5_sor))
# precision error 0.0000000001
test6_div = 1000000000
test6_sor = 1
print(divide_two_int(test6_div, test6_sor))
