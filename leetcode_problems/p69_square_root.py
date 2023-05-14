# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.
# 0 <= x <= 2 ** 31 - 1
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

def my_sqrt(x: int) -> int:
    # working_sol (10.14%, 12.86%) -> (2548ms, 16.3mb)  time: O(n) | space: O(1)
    if x == 0:
        return 0
    prev_num: int = 0
    for num in range(x + 1):  # +1 for case of x == 1
        result: int = num * num
        if result == x:
            return num
        if result > x:
            return prev_num
        prev_num = num

# Time complexity: O(n) -> one for_loop for values from 0 to input_int(x) => O(n).
# Space complexity: O(1) -> two constants: prev_num, result => O(1).

# I need to rebuild it, but I don't want to google solution, cuz there's built_in sqrt() in every language.
# So if I want to speed this up I need to search formulas to calc square_root and rebuild it.
# No reasons and time to do this now.
# ----------------------------------
# Welp. It worked, but obviously very slow, cuz we're just counting from 0 - n.
# Guess, it's one of the worst possible ways to solve it.
# ----------------------------------
# Most basic way to solve it, is brute force from 0 -> n, and find (value * value == x)
# until we hit something higher than x.
# I don't recall any formulas to count square root and don't want to google instantly,
# so try this solution and if I hit timelimit, rebuild with actual math_solution.


test1 = 4
test1_out = 2
print(my_sqrt(test1))
assert test1_out == my_sqrt(test1)

test2 = 8
test2_out = 2
print(my_sqrt(test2))
assert test2_out == my_sqrt(test2)

test3 = 2 ** 31 - 1
test3_out = 46340  # 46340.9500011
print(my_sqrt(test3))
assert test3_out == my_sqrt(test3)

test4 = 1
test4_out = 1
print(my_sqrt(test4))
assert test4_out == my_sqrt(test4)
