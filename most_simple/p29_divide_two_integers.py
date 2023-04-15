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

def divide_two_int(dividend: int, divisor: int) -> int:
    limit = 0
    lowest = -2 ** 31
    highest = 2 ** 31 - 1
    summ = divisor
    if dividend <= lowest and divisor == 1:
        return lowest
    elif dividend >= highest and divisor == 1:
        return highest
    elif dividend <= lowest and divisor == -1:
        return 0 - (lowest + 1)
    elif dividend >= highest and divisor == -1:
        return 0 - (highest - 1)
    while abs(summ) <= abs(dividend):
        summ += divisor
        if dividend < 0 and divisor < 0:
            limit += 1
        elif dividend > 0 and divisor < 0:
            limit -= 1
        elif dividend < 0 and divisor > 0:
            limit -= 1
        elif dividend > 0 and divisor > 0:
            limit += 1
    if limit < lowest:
        return lowest
    elif limit > highest:
        return highest
    return limit


test1_div = 10
test1_sor = 3
test1_out = 3
# print(divide_two_int(test1_div, test1_sor))
test2_div = -10
test2_sor = 3
test2_out = -3
# print(divide_two_int(test2_div, test2_sor))
# test3 Failed because im just crawling with sums and I need some speed.
# Don't have any ideas how to speed up at this moment.
# At least we can skip divisor like 1 with max values, because it's going to be same max value.
# 100% sure it's not enough
test3_div = -2147483648
test3_sor = -1
print(divide_two_int(test3_div, test3_sor))
