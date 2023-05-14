# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.
# 0 <= x <= 231 - 1
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

def my_sqrt(x: int) -> int:
    prev_num: int = 0
    for num in range(x):
        result: int = num * num
        if result == x:
            return num
        if result > x:
            return prev_num
        prev_num = num

# Most basic way to solve it, is brute force from 0 -> n, and find (value * value <= x)
# until we hit something higher than x.
# I don't recall any formulas to count square root and don't want to google instantly,
# so try this solution and if I hit timelimit, rebuild with actual math_solution.


test1 = 4
test1_out = 2
print(my_sqrt(test1))

test2 = 8
test2_out = 2
print(my_sqrt(test2))
